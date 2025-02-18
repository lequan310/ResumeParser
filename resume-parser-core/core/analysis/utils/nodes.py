from fastapi import HTTPException
from core.analysis.utils.state import State, InputState
from core.analysis.utils.analysis_utils import get_job_requirements, get_analysis_result


async def extract_job_requirements(state: InputState):
    job_requirements_dict = await get_job_requirements(state["job_desc"])
    basic_requirements_list = job_requirements_dict.get("basic_requirements", [])
    preferred_requirements_list = job_requirements_dict.get(
        "preferred_requirements", []
    )

    # Get the requirements string
    sections = []

    if basic_requirements_list:
        sections.append("Basic Requirements:\n" + "\n".join(basic_requirements_list))

    if preferred_requirements_list:
        sections.append(
            "Preferred Requirements:\n" + "\n".join(preferred_requirements_list)
        )

    requirements = "\n\n".join(sections).strip()

    # Raise an error if no requirements are found
    if not requirements:
        raise HTTPException(
            status_code=400, detail="No requirements found in the job description"
        )

    return {"requirements": requirements, "resume": state["resume"]}


async def compare_resume_jd(state: State):
    analysis_result_dict = await get_analysis_result(
        state["resume"], state["requirements"]
    )

    return {"result": analysis_result_dict}
