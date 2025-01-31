from contextlib import asynccontextmanager
from fastapi import APIRouter, Body
from typing import Annotated
from core.chat.graph import ChatGraph

chat_graph = ChatGraph()


@asynccontextmanager
async def lifespan(app):
    # Application setup
    await chat_graph.setup()

    yield

    # Application teardown


router = APIRouter(prefix="/chat", tags=["Chat"], lifespan=lifespan)


@router.post("/chat")
async def chat(message: Annotated[str, Body()]):
    return {"message": message}
