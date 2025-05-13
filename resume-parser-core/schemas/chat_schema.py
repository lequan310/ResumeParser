from schemas.base_schema import BaseRequestModel, BaseResponseModel
from pydantic import Field


class ChatMessageModel(BaseRequestModel):
    """
    Model for chat messages.
    """

    message: str = Field(..., description="The message content.")
    thread_id: str = Field(..., description="The ID of the chat thread.")


class ChatCleanupModel(BaseRequestModel):
    """
    Model for chat cleanup requests.
    """

    thread_id: str = Field(..., description="The ID of the chat thread.")
    message: str = Field(..., description="The message content.")
