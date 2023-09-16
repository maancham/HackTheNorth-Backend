from typing import List, Any

import httpx
from decouple import config

from apps.chat.exceptions import ServiceCallError
from apps.chat.services.llm_service import LLMService


class OpenAIService(LLMService):

    def __init__(self) -> None:
        self.message_primary = "Context: In this conversation, there are some parts that have been masked for user privacy, using *** notation. \
            These masked parts can be names, places, or any sensitive information provided by users. Please continue the conversation as naturally \
                as possible, and you can fill in the masked parts as needed. The main focus is on the flow and quality of the conversation. \
                    If you have any questions or need clarification, please feel free to ask. "
        
    url = config("OPENAI_URL", "")
    api_key = config("OPENAI_API_KEY", "")
    model = "gpt-3.5-turbo"
    

    def get_model(self):
        return self.model

    def chat(self, messages: List[Any], temperature=0.3) -> str:
        message = message + [self.message_primary]
        url = self.url + "/chat/completions"
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {self.api_key}"}
        data = {"model": self.model, "temperature": temperature, "messages": messages}
        result = httpx.post(url, headers=headers, json=data, timeout=60)
        if result.status_code == 200:
            return result.json()["choices"][0]["message"]["content"]
        raise ServiceCallError()
