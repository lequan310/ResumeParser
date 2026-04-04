from agentic.chat.utils.tools import tools
from agentic.llm import deepseek_llm

deepseek_agent = deepseek_llm.bind_tools(tools)
