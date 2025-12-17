def calculate_eligibility(profile):
    score = 0
    score += min(profile["years_experience"] * 10, 30)
    score += len(profile["programming_languages"]) * 10

    if score >= 70:
        return "Eligible"
    elif score >= 40:
        return "Partially Eligible"
    return "Not Eligible"
