from agentic.models.resume import Resume
from agentic.parser.utils.parse_utils import (
    convert_markdown_to_resume,
    convert_to_markdown,
)
from agentic.parser.utils.state import InputState, State
from agentic.parser.utils.tools import get_position_duration


async def get_resume_markdown(state: InputState):
    filename = state["input"].filename
    markdown = await convert_to_markdown(state["input"])

    return {"filename": filename, "markdown": markdown}


async def get_resume_structured(state: State):
    resume: Resume = await convert_markdown_to_resume(state["markdown"])
    resume = resume.model_dump()

    return {"output": resume}


async def postprocess_resume_output(state: State):
    output = state["output"]
    output["yoe"] = {"year": 0, "month": 0}

    for exp in output.get("work_experiences", []):
        exp["duration"] = get_position_duration(exp["start_date"], exp["end_date"])
        output["yoe"]["year"] += exp["duration"]["year"]
        output["yoe"]["month"] += exp["duration"]["month"]

    output["yoe"]["year"] += output["yoe"]["month"] // 12
    output["yoe"]["month"] %= 12

    return {"output": output}
