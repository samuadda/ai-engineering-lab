from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ProcessRequest(BaseModel):
    text: str
    uppercase: bool


class ProcessResponse(BaseModel):
    original: str
    result: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/process", response_model=ProcessResponse)
def process(request: ProcessRequest):
    result_text = request.text.upper() if request.uppercase else request.text
    return {
        "original": request.text,
        "result": result_text,
    }
