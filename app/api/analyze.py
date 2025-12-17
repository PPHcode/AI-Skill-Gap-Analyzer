from fastapi import APIRouter
from app.services.feature_extractor import extract_features
from app.services.skill_gap import identify_skill_gaps
from app.services.eligibility import calculate_eligibility

router = APIRouter()

@router.post("/")
def analyze(cv_text: str):
    features = extract_features(cv_text)
    skill_gaps = identify_skill_gaps(features, {})
    eligibility = calculate_eligibility(features)

    return {
        "features": features,
        "skill_gaps": skill_gaps,
        "eligibility": eligibility
    }
