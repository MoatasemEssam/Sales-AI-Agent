from fastapi import FastAPI
from pydantic import BaseModel
from .agent import agent_workflow

api = FastAPI(title="SAB Sales Automation Service")

class PitchRequest(BaseModel):
    company: str

@api.post("/generate-sales-lead")
async def generate_lead(request: PitchRequest):
    # Runs the LangGraph agent
    result = agent_workflow.invoke({"company": request.company})
    return {
        "company": request.company,
        "pitch": result["final_pitch"],
        "raw_research": result["research_notes"][:500] # Sending snippet for the UI
    }