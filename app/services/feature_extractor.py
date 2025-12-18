import json
from app.llm.openai_client import client
from app.llm.prompts import CV_EXTRACTION_PROMPT

def extract_features(cv_text: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You extract structured resume data."},
            {"role": "user", "content": CV_EXTRACTION_PROMPT.format(cv_text=cv_text)}
        ],
        temperature=0,
        response_format={"type": "json_object"}  # 🔥 THIS FIXES EVERYTHING
    )

    return response.choices[0].message.content
