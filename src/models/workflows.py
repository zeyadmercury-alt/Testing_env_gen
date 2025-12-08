from pydantic import BaseModel, Field

class ApiWorkflow(BaseModel):
    prompt: str
    model: str = Field(description="OpenRouter model id")

    WORKFLOW_FILE: str = "api.json"
    NODE_MAP: dict = {"1": "STRING", "5": "image_generation_model"}

class IntakeWorkflow(BaseModel):
    prompt: str
    category: str
    summary: str

    WORKFLOW_FILE: str = "intake2moodboard.json"
    NODE_MAP: dict = {"23": "STRING", "21": "STRING", "22": "STRING"}

class LocalWorkflow(BaseModel):
    pprompt: str
    nprompt: str = ""
    seed: str = "randomize"
    summary: str

    WORKFLOW_FILE: str = "LoRA.json"
    NODE_MAP: dict = {"23": "STRING", "24": "STRING", "25": "STRING", "22": "STRING"}