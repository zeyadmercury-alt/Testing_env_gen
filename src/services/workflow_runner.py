import json, pathlib, typing as T
from src.services.comfy import ComfyClient
from pydantic import BaseModel

async def run_workflow(model: BaseModel, client: ComfyClient | None = None) -> list[str]:
    client = client or ComfyClient()
    wf = json.loads(pathlib.Path(f"static/workflows/{model.WORKFLOW_FILE}").read_text())

    # patch nodes
    for node_id, field in model.NODE_MAP.items():
        wf[node_id]["inputs"][field] = getattr(model, field)

    pid = await client.queue(wf)
    return await client.wait_images(pid)