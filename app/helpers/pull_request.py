import re
from datetime import datetime

from discord import Embed

from app.models.pull_request import PullRequest, User
from app.utils.datetime import pretty_date


def generate_embed_from(pull: PullRequest) -> Embed:
    embed = (
        Embed(title=__title(pull), color=__color(pull), url=pull.url)
        .set_author(
            name=pull.author.name, url=pull.author.url, icon_url=pull.author.icon_url
        )
        .add_field(name=f"\u200b", value=__description(pull), inline=False)
        .add_field(name="Assignees", value=__assignees(pull))
        .add_field(name="Reviewers", value=__reviewers(pull))
        .set_footer(
            text=f"{__footer_emoji(pull)} opened {pretty_date(pull.created_at)} (last updated {pull.updated_at})"
        )
    )
    return embed


def __title(pull: PullRequest):
    return f"[{pull.repo}] {pull.title} (#{pull.number})"


def __color(pull: PullRequest):
    if pull.draft:
        return 0xB3B3B3
    if pull.merging_state == "clean":
        return 0x33CC33
    if pull.merging_state == "dirty":
        return 0xFF9900
    if pull.merging_state == "blocked":
        return 0xFF3300
    if pull.merging_state == "unstable":
        return 0xBF8040
    if pull.merging_state == "unknown":
        return 0x4D4D4D


def __description(pull: PullRequest):
    body_lines = __sanitize_body(pull.body).splitlines()
    return "\n".join(body_lines[0:3])


def __assignees(pull: PullRequest):
    if not pull.assignees:
        return "undefined"

    assignee_handlers = map(__user_handler, pull.assignees)
    return ", ".join(assignee_handlers)


def __reviewers(pull: PullRequest):
    if not pull.reviewers:
        return "undefined"

    reviewer_handlers = map(__user_handler, pull.reviewers)
    return ", ".join(reviewer_handlers)


def __footer_emoji(pull: PullRequest):
    difftime = datetime.utcnow() - pull.created_at
    if difftime.days == 0 and difftime.seconds < 60 * 15:
        return "⚡"
    if difftime.days == 0 and difftime.seconds < 60 * 60:
        return "⏳"
    if difftime.days < 1:
        return "🕐"
    if difftime.days >= 1:
        return "🗓️"


def __sanitize_body(body: str):
    return re.sub(r"(<!--.*?-->)", "", body, flags=re.DOTALL)


def __user_handler(user: User):
    return f"@{user.name}"
