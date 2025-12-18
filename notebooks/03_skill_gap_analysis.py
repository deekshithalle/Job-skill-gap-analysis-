import pandas as pd
import os

# Project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load extracted skills data
INPUT_CSV = os.path.join(BASE_DIR, "data", "processed", "extracted_skills.csv")
df = pd.read_csv(INPUT_CSV)

# -------------------------------
# USER PROFILE (Sample Input)
# -------------------------------
user_profile = {
    "name": "Sample User",
    "target_role": "AI Engineer",
    "current_skills": ["python", "sql"]
}

# Filter job of interest
job_row = df[df["job_title"] == user_profile["target_role"]]

if job_row.empty:
    raise ValueError("Target role not found in dataset")

# Extract required skills for the role
required_skills = eval(job_row.iloc[0]["extracted_skills"])

# Skill gap calculation
user_skills = set([s.lower() for s in user_profile["current_skills"]])
required_skills = set(required_skills)

skill_gap = list(required_skills - user_skills)

# Output
print("User Skills:", user_skills)
print("Required Skills:", required_skills)
print("Skill Gap (Missing Skills):", skill_gap)
