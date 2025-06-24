from typing import Annotated

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from core.container import Container
from schemas.chat_schema import ChatCleanupResponseModel, ChatMessageModel
from services.chat_service import ChatService

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("")
@inject
async def chat(
    message: ChatMessageModel,
    chat_service: Annotated[ChatService, Depends(Provide[Container.chat_service])],
):
    """
    Send a message to the chat service and get streamed response.

    Args:
        message: Chat message containing text and thread_id
        chat_service: Injected chat service dependency

    Returns:
        StreamingResponse: Streamed chat response
    """
    return StreamingResponse(
        content=chat_service.send_message(
            message=message.message, thread_id=message.thread_id
        ),
        media_type="text/plain",
    )


@router.delete("/disconnect/{thread_id}", response_model=ChatCleanupResponseModel)
@inject
async def disconnect(
    thread_id: str,
    chat_service: Annotated[ChatService, Depends(Provide[Container.chat_service])],
):
    """
    Disconnect the chat session and clear history.

    Args:
        thread_id: The ID of the chat thread to disconnect
        chat_service: Injected chat service dependency

    Returns:
        ChatCleanupResponseModel: Confirmation of disconnection
    """
    await chat_service.clear_history(thread_id=thread_id)

    response = ChatCleanupResponseModel(
        thread_id=thread_id,
        message=f"Disconnected the chat session with thread id {thread_id}.",
    )

    return response
