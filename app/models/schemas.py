from pydantic import BaseModel

class CVAnalyzeRequest(BaseModel):
    cv_text: str
