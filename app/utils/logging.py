import logging
from logging.config import fileConfig

fileConfig("settings/logging.ini")
logger = logging.getLogger(__name__)
