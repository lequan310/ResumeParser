from contextlib import asynccontextmanager
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from core.chat.graph import ChatGraph
from api.models.chat_message import ChatMessage
from db.pool import get_connection_pool, reset_db

chat_graph = ChatGraph()


@asynccontextmanager
async def lifespan(app):
    # Application setup
    pool = get_connection_pool()
    await pool.open()
    await reset_db()
    await chat_graph.setup()

    yield

    # Application teardown
    await pool.close()
    pool = None


router = APIRouter(prefix="/chat", tags=["Chat"], lifespan=lifespan)


@router.post("")
async def chat(message: ChatMessage):
    return StreamingResponse(
        chat_graph.astream(
            input=message.message,
            config={"configurable": {"thread_id": message.thread_id}},
        ),
        media_type="text/plain",
    )
