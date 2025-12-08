from fastapi import APIRouter, Form
from src.models.workflows import ApiWorkflow, IntakeWorkflow, LocalWorkflow
from src.services.workflow_runner import run_workflow

router = APIRouter(prefix="/txt2img")

@router.post("/api")
async def api_post(prompt: str = Form(...), model: str = Form(...)):
    return {"images": await run_workflow(ApiWorkflow(prompt=prompt, model=model))}

@router.post("/intake2moodboard")
async def intake_post(prompt: str = Form(...), category: str = Form(...), summary: str = Form(...)):
    return {"images": await run_workflow(IntakeWorkflow(prompt=prompt, category=category, summary=summary))}

@router.post("/localmodel")
async def local_post(pprompt: str = Form(...), nprompt: str = Form(""), seed: str = Form("randomize"), summary: str = Form(...)):
    return {"images": await run_workflow(LocalWorkflow(pprompt=pprompt, nprompt=nprompt, seed=seed, summary=summary))}