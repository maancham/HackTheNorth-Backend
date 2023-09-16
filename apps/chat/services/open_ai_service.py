from typing import List, Any

import httpx
from decouple import config

from apps.chat.exceptions import ServiceCallError
from apps.chat.services.llm_service import LLMService


class OpenAIService(LLMService):
    url = config("OPENAI_URL", "")
    api_key = config("OPENAI_API_KEY", "")
    model = "gpt-3.5-turbo"

    def get_model(self):
        return self.model

    def chat(self, messages: List[Any], temperature=0.3) -> str:
        url = self.url + "/chat/completions"
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {self.api_key}"}
        data = {"model": self.model, "temperature": temperature, "messages": messages}
        result = httpx.post(url, headers=headers, json=data, timeout=60)
        if result.status_code == 200:
            return result.json()["choices"][0]["message"]["content"]
        raise ServiceCallError()
