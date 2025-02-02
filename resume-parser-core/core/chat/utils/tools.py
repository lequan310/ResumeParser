from langchain_community.tools import TavilyAnswer
from langchain_core.tools import tool


@tool
async def search_tool(query: str) -> str:
    """Search for information using Google Search. Pass in a complete question to get a clear answer."""

    search = TavilyAnswer()
    result = await search.ainvoke(query)
    return {"result": result}


tools = [search_tool]
tools_by_name = {tool.name: tool for tool in tools}
