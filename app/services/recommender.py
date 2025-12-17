def recommend_courses(skill_gaps, course_map):
    return [course_map.get(skill) for skill in skill_gaps if skill in course_map]
