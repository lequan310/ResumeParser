import os
from tavily import AsyncTavilyClient
from langchain_core.tools import tool

tavily_client = AsyncTavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


@tool
async def search_tool(query: str) -> str:
    """Search for information using Google Search. Pass in a complete question to get a clear answer."""

    result = await tavily_client.qna_search(
        query=query, search_depth="advanced", max_results=1
    )
    return {"result": result}


tools = [search_tool]
tools_by_name = {tool.name: tool for tool in tools}
