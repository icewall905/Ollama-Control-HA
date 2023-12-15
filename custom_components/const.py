"""Constants for ollama_control."""
from logging import Logger, getLogger

LOGGER: Logger = getLogger(__package__)

NAME = "Ollama Control"
DOMAIN = "ollama_control"
TIMEOUT = 60

MENU_OPTIONS = ["model_config", "prompt_system"]

"""Options"""

CONF_PROMPT = "prompt"
DEFAULT_PROMPT = """This smart home is controlled by Home Assistant."""

CONF_CHAT_MODEL = "chat_model"
DEFAULT_CHAT_MODEL = "orca"

CONF_MAX_TOKENS = "max_tokens"
DEFAULT_MAX_TOKENS = 250

CONF_TOP_P = "top_p"
DEFAULT_TOP_P = 1

CONF_TEMPERATURE = "temperature"
DEFAULT_TEMPERATURE = 0.5

LITELLM_ENDPOINT = "http://10.0.2.22:8000/v1"

CONF_API_KEY = "null"