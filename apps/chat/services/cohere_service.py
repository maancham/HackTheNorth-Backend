from typing import List, Any

import httpx
from decouple import config

from apps.chat.exceptions import ServiceCallError
from apps.chat.services.llm_service import LLMService


class CohereService(LLMService):
    url = config("COHERE_URL", "")
    api_key = config("COHERE_API_KEY", "")

    def get_model(self):
        return "cohere_chat"

    def chat(self, messages: List[Any], temperature=0.3) -> str:
        url = self.url + "/chat"
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {self.api_key}"}
        data = {
            "prompt_truncation": "OFF",
            "temperature": temperature,
            "stream": False,
            "chat_history": list(map(self.change_message_model, messages[:-1])),
            "message": messages[-1]["content"],
        }
        result = httpx.post(url, headers=headers, json=data, timeout=60)
        if result.status_code == 200:
            return result.json()["text"]
        raise ServiceCallError()

    def change_message_model(self, message):
        return {"message": message["content"], "user_name": message["role"]}
