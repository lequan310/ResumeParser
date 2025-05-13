from contextlib import asynccontextmanager
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from services.chat_service import ChatService
from schemas.chat_schema import ChatMessageModel, ChatCleanupModel
from core.db import get_connection_pool

chat_service = ChatService()


@asynccontextmanager
async def lifespan(app):
    # Application setup
    pool = get_connection_pool()
    await pool.open()
    await chat_service.setup()

    yield

    # Application teardown
    await pool.close()
    pool = None


router = APIRouter(prefix="/chat", tags=["Chat"], lifespan=lifespan)


@router.post("")
async def chat(message: ChatMessageModel):
    return StreamingResponse(
        content=chat_service.send_message(
            message=message.message, thread_id=message.thread_id
        ),
        media_type="text/plain",
    )


@router.delete("/disconnect/{thread_id}", response_model=ChatCleanupModel)
async def disconnect(thread_id: str):
    """Disconnect the chat session"""
    await chat_service.clear_history(thread_id=thread_id)

    response = ChatCleanupModel(
        thread_id=thread_id,
        message=f"Disconnected the chat session with thread id {thread_id}.",
    )

    return response
