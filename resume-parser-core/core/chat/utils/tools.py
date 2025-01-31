from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from core.llm import gemini_llm
from core.chat.utils.prompts import GEMINI_SYSTEM_MESSAGE


@tool
async def search_tool(query: str) -> str:
    """Search for information using Google Search. Pass in a complete question to get a clear answer."""

    # The description of the tool is a lie, it's actually to ask gemini for help. If I have more money for API keys I would use another tool.
    prompt = ChatPromptTemplate(
        [
            ("system", GEMINI_SYSTEM_MESSAGE),
            ("user", "{query}"),
        ]
    )
    chain = prompt | gemini_llm
    result = await chain.ainvoke({"query": query})
    return {"result": result.content}


tools = [search_tool]
