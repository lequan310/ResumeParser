from core.llm import deepseek_llm
from core.chat.utils.tools import tools

deepseek_agent = deepseek_llm.bind_tools(tools)
