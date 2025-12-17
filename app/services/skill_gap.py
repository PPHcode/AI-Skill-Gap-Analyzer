import json

def identify_skill_gaps(candidate, jd_skills):
    gaps = []

    for skill in jd_skills["core"]:
        if skill not in candidate["programming_languages"]:
            gaps.append(skill)

    return gaps
