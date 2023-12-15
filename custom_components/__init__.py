import logging
import requests

from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.components.smarthome import SmartHomeDevice

DOMAIN = "ollama_control"

_LOGGER = logging.getLogger(__name__)

class OllamaConversationDevice(SmartHomeDevice):
    def __init__(self, hass, config):
        super().__init__(hass, config)
        self.api_key = config.get("api_key")

    def handle_conversation(self, message):
        # Send the user message to the LiteLLM proxy
        url = "http://10.0.2.22:8000/v1/completion"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        data = {"prompt": message}
        response = requests.post(url, headers=headers, json=data)

        # Parse the response and generate a response for the user
        if response.status_code == 200:
            response_data = response.json()
            response_text = response_data["choices"][0]["text"]
            _LOGGER.debug("Received response: %s", response_text)
            return response_text
        else:
            _LOGGER.error("Failed to get response from the LiteLLM proxy: %s", response.text)
            return None

def hass_service(call: ServiceCall):
    message = call.data.get("message")
    device = cast(OllamaConversationDevice, call.data["device"])

    response = device.handle_conversation(message)
    if response:
        call.data["conversation_id"] = response["conversation_id"]
        call.data["status"] = "success"
        call.data["data"] = response["data"]
    else:
        call.data["status"] = "error"
        call.data["error"] = "Failed to get response from the LiteLLM proxy"

@asyncio.coroutine
def async_setup_entry(hass: HomeAssistant, config_entry: config.ConfigEntry):
    return True

@asyncio.coroutine
def async_setup(hass: HomeAssistant, config: config.Config):
    for config_entry in config.get(DOMAIN, []):
        yield from async_setup_entry(hass, config_entry)

    return True

@asyncio.coroutine
def async_unload(hass: HomeAssistant):
    pass
