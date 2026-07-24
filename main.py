import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import instructor
from openai import OpenAI

app = FastAPI(
    title="Async Agent API",
    description="A lightweight API for structured data extraction and triage using local LLMs.",
    version="1.0.0"
)

client = instructor.from_openai(
    OpenAI(
        base_url="http://127.0.0.1:1234/v1",
        api_key="not-needed"
    ),
    mode=instructor.Mode.JSON_SCHEMA
)

class RequestPayload(BaseModel):
    text: str = Field(description="The input text or ticket content to analyze")

class AnalysisResponse(BaseModel):
    category: str = Field(description="The primary category of the request (e.g., Billing, Technical, General)")
    urgency: str = Field(description="Urgency level: Low, Medium, High, or Urgent")
    summary: str = Field(description="A concise one-sentence summary of the user's issue based strictly on the input text")
    action_item: str = Field(description="Recommended next step or resolution for support staff based strictly on the input text")

@app.post("/analyze", response_model=AnalysisResponse)
async def analyze_content(payload: RequestPayload):
    try:
        response = client.chat.completions.create(
            model="local-model",
            response_model=AnalysisResponse,
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert AI operations assistant. Analyze the incoming text and extract structured triage metadata accurately. Rely ONLY on the clear facts directly mentioned in the input text. Do not assume, extrapolate, or hallucinate details not present in the text."
                },
                {
                    "role": "user",
                    "content": payload.text
                }
            ],
            temperature=0.0
        )
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "async-agent-pipeline"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
