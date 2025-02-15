from fastapi import APIRouter
from api.models.analysis_input import AnalysisInput
from core.analysis.graph import AnalysisGraph


analyis_graph = AnalysisGraph()
router = APIRouter(prefix="/analysis", tags=["Analysis"])


@router.post("")
async def get_analysis(input: AnalysisInput):
    result = await analyis_graph.ainvoke(
        {"resume": input.resume, "job_desc": input.job_desc}
    )

    return {"response": result["result"]}
