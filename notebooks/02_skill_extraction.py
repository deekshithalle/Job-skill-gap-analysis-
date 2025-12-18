import pandas as pd
import spacy
import os

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Get project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# File paths
INPUT_CSV = os.path.join(BASE_DIR, "data", "raw", "indian_jobs_sample.csv")
OUTPUT_CSV = os.path.join(BASE_DIR, "data", "processed", "extracted_skills.csv")

# Create processed directory if not exists
os.makedirs(os.path.dirname(OUTPUT_CSV), exist_ok=True)

# Load job data
df = pd.read_csv(INPUT_CSV)

# Predefined skill keywords (initial vocabulary)
SKILL_KEYWORDS = [
    "python", "machine learning", "deep learning", "nlp",
    "tensorflow", "sql", "data visualization", "statistics",
    "excel", "java", "oops", "data structures", "rest apis",
    "problem solving"
]

def extract_skills(text):
    text = text.lower()
    found_skills = []
    for skill in SKILL_KEYWORDS:
        if skill in text:
            found_skills.append(skill)
    return list(set(found_skills))

# Apply skill extraction
df["extracted_skills"] = df["description"].apply(extract_skills)

# Display result
print(df[["job_title", "extracted_skills"]])

# Save extracted skills
df.to_csv(OUTPUT_CSV, index=False)

print(f"\nExtracted skills saved at:\n{OUTPUT_CSV}")
