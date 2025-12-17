from fastapi import APIRouter, UploadFile, File
from app.services.cv_parser import extract_text

router = APIRouter()

@router.post("/upload")
async def upload_cv(file: UploadFile = File(...)):
    text = extract_text(file)
    return {"cv_text": text}
