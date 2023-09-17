import re

# Define the regular expression pattern
pattern = r'\*\*\*(.*?)\*\*\*'

from typing import List, Any

import httpx
from decouple import config

from apps.chat.exceptions import ServiceCallError
from apps.chat.services.llm_service import LLMService


def replace_matches(match):
    return f'[{match.group(1)}]'

class CohereService(LLMService):
    url = config("COHERE_URL", "")
    api_key = config("COHERE_API_KEY", "")
    def init(self) -> None:
        self.message_primary = "Context: In this conversation, there are some parts that have been masked for user privacy, denoted by ___, so whenever you see ___, it belongs to something that has been masked.\
            These masked parts can be names, places, or any sensitive information provided by users. Please continue the conversation as naturally \
                as possible, and you can fill in the masked parts as needed. The main focus is on the flow and quality of the conversation. \
                    If you have any questions or need clarification, please feel free to ask. "

    def get_model(self):
        return "cohere_chat"

    def chat(self, messages: List[Any], temperature=0.3) -> str:
        url = self.url + "/chat"
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {self.api_key}"}
        print("messages old", messages)
        messages[-1]["content"] = re.sub('<.*?>', '___', messages[-1]["content"])

        result_messages = [self.message_primary + re.sub('<.*?>', '', message) for message in messages[:-1]]
        print("messages new", messages)
        result_messages = list(map(self.change_message_model, result_messages))

        data = {
            "prompt_truncation": "OFF",
            "temperature": temperature,
            "stream": False,
            "chat_history": result_messages,
            "message": messages[-1]["content"],
        }
        result = httpx.post(url, headers=headers, json=data, timeout=60)
        if result.status_code == 200:
            return result.json()["text"]
        raise ServiceCallError()

    def change_message_model(self, message):
        return {"message": message["content"], "user_name": message["role"]}