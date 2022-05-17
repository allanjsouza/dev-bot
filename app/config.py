import os
from dotenv import load_dotenv

load_dotenv()


class AppConfigError(Exception):
    pass


class AppConfig:
    AUTH_TOKEN: str
    COMMAND_PREFIX: str = "!"
    SCM_PROVIDER: str = "github"
    GITHUB_BASE_URL: str = "https://github.com"
    GITHUB_PAT: str
    GITHUB_ORG: str

    """
    Map environment variables to class fields according to these rules:
      - Field will be skipped if not in all caps
      - Class field and environment variable name are the same
    """

    def __init__(self, env):
        for field in self.__annotations__:
            if not field.isupper():
                continue

            # Raise AppConfigError if required field not supplied
            default_value = getattr(self, field, None)
            value = env.get(field, default_value)
            if value is None:
                raise AppConfigError(f"The {field} field is required")

            self.__setattr__(field, value)


# Expose Config object for app to import
Config = AppConfig(os.environ)
