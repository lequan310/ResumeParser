from core.workflows.llm import deepseek_llm
from core.workflows.chat.utils.tools import tools

deepseek_agent = deepseek_llm.bind_tools(tools)
