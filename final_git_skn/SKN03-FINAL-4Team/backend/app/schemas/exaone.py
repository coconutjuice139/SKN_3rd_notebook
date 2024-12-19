from pydantic import BaseModel

class GenerateRequest(BaseModel):
    model: str = "exaone3.5"
    prompt: str