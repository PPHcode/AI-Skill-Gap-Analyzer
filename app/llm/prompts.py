CV_EXTRACTION_PROMPT = """
Extract the following from the CV text:
- experience_field
- years_experience
- programming_languages
- skills_databases
- skills_cloud
- education_level
- certifications
- projects
- internships

Return JSON only.

CV:
{cv_text}
"""
