from fastapi import FastAPI
from app.api import cv_upload, analyze

app = FastAPI(title="AI Skill Gap Analyzer")

app.include_router(cv_upload.router, prefix="/cv")
app.include_router(analyze.router, prefix="/analyze")
