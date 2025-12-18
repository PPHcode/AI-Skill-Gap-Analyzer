CV_EXTRACTION_PROMPT = """
You are a resume parser.

Extract the following fields from the CV text.

Return ONLY valid JSON.
DO NOT include explanations, markdown, or extra text.

Schema:
{{
  "experience_field": "",
  "years_experience": 0,
  "programming_languages": [],
  "skills_databases": [],
  "skills_cloud": [],
  "education_level": "",
  "certifications": [],
  "projects": [],
  "internships": []
}}

CV TEXT:
{cv_text}
"""
