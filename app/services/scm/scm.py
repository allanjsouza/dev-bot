from app.config import Config
from app.services.scm.providers.github import GithubProvider
from app.services.scm.providers.provider import ScmProvider

PROVIDERS = {"github": GithubProvider}


def get_provider() -> ScmProvider:
    provider_class = PROVIDERS[Config.SCM_PROVIDER] or GithubProvider
    return provider_class()
