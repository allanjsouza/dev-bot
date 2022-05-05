#!/usr/bin/env bash

# It uses git-cliff (https://github.com/orhun/git-cliff) as changelog gen tool
# In order to install it (through asdf), run:
# $ asdf plugin-add rust
# $ asdf install rust stable
# $ cargo install git-cliff
# $ sudo ln -s $HOME/.asdf/installs/rust/stable/bin/git-cliff /bin/

NAT='0|[1-9][0-9]*'
ALPHANUM='[0-9]*[A-Za-z-][0-9A-Za-z-]*'
IDENT="$NAT|$ALPHANUM"
FIELD='[0-9A-Za-z-]+'

SEMVER_REGEX="\
^[vV]?\
($NAT)\\.($NAT)\\.($NAT)\
(\\-(${IDENT})(\\.(${IDENT}))*)?\
(\\+${FIELD}(\\.${FIELD})*)?$"

Cyan='\033[0;36m'   # Cyan
Green='\033[0;32m'  # Green
NC='\033[0m'        # No Color
Bold='\033[1m'      # Bold
NF='\033[0m'        # Regular

# ensure it's all up to date
echo -n "Checkout main..." && git checkout -q main && echo -e " Done!"
echo -n "Fetching main branch..." && git pull -q && echo -e " Done!"
echo -n "Fetching (remote) tags..." && git fetch --tags -q && echo -e " Done!\n"

# check unreleased changes
export CONFIG="properties.toml"
echo -e "${Cyan}These are the unreleased changes:"
echo -e "${Green}$(git cliff --unreleased --strip all)${NC}\n"

# check version being released (based on current one)
current_version=$(git describe --tags --abbrev=0)
[[ $current_version =~ $SEMVER_REGEX ]]
major=${BASH_REMATCH[1]}
minor=${BASH_REMATCH[2]}
patch=${BASH_REMATCH[3]}

PS3="> Which version is being released? "
select opt in major minor patch quit; do
  case $opt in
    major)
      version=(`echo v$(($major+1)).0.0`)
      break;;
    minor)
      version=(`echo v$major.$(($minor+1)).0`)
      break;;
    patch)
      version=(`echo v$major.$minor.$(($patch+1))`)
      break;;
    quit)
      echo "Abort." && exit 0;;
    *)
      echo "Invalid option $REPLY";;
  esac
done
echo -e "\n${Bold}Releasing $version (previous was $current_version)${NF}\n"

# update CHANGELOG.md
git cliff --unreleased --tag $version --prepend CHANGELOG.md
git add CHANGELOG.md && git commit -q -m "chore(release): prepare for $version" && git push -q
echo -e "${Cyan}Successfully created release commit ($(git log -1 --pretty=format:%h))${NC}"

# git tag message template
export TEMPLATE="\
{% for group, commits in commits | group_by(attribute=\"group\") %}
  {{ group | upper_first }}\
  {% for commit in commits %}
    - {% if commit.breaking %}BREAKING {% endif %}{% if commit.scope %}({{commit.scope}}) {% endif %}{{ commit.message | upper_first }} ({{ commit.id | truncate(length=7, end=\"\") }})\
  {% endfor %}
{% endfor %}"

# tag (annotated) version
echo && read -p "> Continue with version tag? [Y/n] " -r
if [[ $REPLY =~ ^[Nn]$ ]]
then
  echo "Then you should tag version mannually." && exit 1
fi
changes=$(git cliff --unreleased --strip all)
git tag -a $version -e -m "Release $version" -m "$changes"
echo -e "${Cyan}Successfully tagged $version${NC}"
git push --tags
remote_url=$(git config --get remote.origin.url)
echo -e "Create release by visting:\n\t${remote_url%.*}/releases/new?tag=$version"
