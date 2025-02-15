from core.analysis.utils.state import State, InputState
from core.analysis.utils.analysis_utils import get_job_requirements, get_analysis_result


async def extract_job_requirements(state: InputState):
    job_requirements_dict = await get_job_requirements(state["job_desc"])
    basic_requirements_list = job_requirements_dict["basic_requirements"]
    preferred_requirements_list = job_requirements_dict["preferred_requirements"]
    basic_requirements = "\n".join(basic_requirements_list)
    preferred_requirements = "\n".join(preferred_requirements_list)
    requirements = f"Basic Requirements:\n{basic_requirements}\n\nPreferred Requirements:\n{preferred_requirements}"
    return {"requirements": requirements, "resume": state["resume"]}


async def compare_resume_jd(state: State):
    analysis_result_dict = await get_analysis_result(
        state["resume"], state["requirements"]
    )

    return {"result": analysis_result_dict}
