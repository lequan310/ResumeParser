from pydantic import Field

from schemas.base_schema import BaseRequestModel, BaseResponseModel


class ChatMessageModel(BaseRequestModel):
    """
    Model for chat messages.
    """

    message: str = Field(..., description="The message content.")
    thread_id: str = Field(..., description="The ID of the chat thread.")


class ChatCleanupResponseModel(BaseResponseModel):
    """
    Model for chat cleanup response.
    """

    thread_id: str = Field(..., description="The ID of the chat thread.")
    message: str = Field(..., description="The message content.")
