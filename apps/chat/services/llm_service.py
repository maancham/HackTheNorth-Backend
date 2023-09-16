from typing import List, Any


class LLMService:
    def chat(self, messages: List[Any], temperature=0.3):
        raise NotImplementedError()

    def get_model(self) -> str:
        raise NotImplementedError()

    def change_message_model(self, message):
        return {"content": message["content"], "role": message["role"]}
