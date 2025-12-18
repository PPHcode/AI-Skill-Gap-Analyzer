from fastapi import APIRouter
from app.models.schemas import CVAnalyzeRequest
from app.services.feature_extractor import extract_features
from app.services.skill_gap import identify_skill_gaps
from app.services.eligibility import calculate_eligibility
import json
from pathlib import Path

router = APIRouter()

@router.post("/")
def analyze(request: CVAnalyzeRequest):
    features_raw = extract_features(request.cv_text)
    features = json.loads(features_raw)

    jd_path = Path("app/data/jd_skills.json")
    with open(jd_path, "r") as f:
        jd_skills = json.load(f)

    skill_gaps = identify_skill_gaps(features, jd_skills)
    eligibility = calculate_eligibility(features)

    return {
        "features": features,
        "skill_gaps": skill_gaps,
        "eligibility": eligibility
    }
