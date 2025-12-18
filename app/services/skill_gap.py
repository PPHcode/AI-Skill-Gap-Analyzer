import json

def identify_skill_gaps(candidate: dict, jd_skills: dict):
    gaps = {}

    candidate_all_skills = (
        candidate.get("programming_languages", []) +
        candidate.get("skills_databases", []) +
        candidate.get("skills_cloud", []) +
        candidate.get("projects", []) +
        [candidate.get("experience_field", "")]
    )

    candidate_all_skills = [s.lower() for s in candidate_all_skills]

    for category, required_skills in jd_skills.items():
        if category in ["role", "education"]:
            continue

        missing = []
        for skill in required_skills:
            if skill.lower() not in candidate_all_skills:
                missing.append(skill)

        if missing:
            gaps[category] = missing

    return gaps

