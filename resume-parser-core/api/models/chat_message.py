from pydantic import BaseModel


class ChatMessage(BaseModel):
    message: str
    thread_id: str
