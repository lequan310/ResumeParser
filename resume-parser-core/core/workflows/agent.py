from core.workflows.chat.utils.tools import tools
from core.workflows.llm import deepseek_llm

deepseek_agent = deepseek_llm.bind_tools(tools)
