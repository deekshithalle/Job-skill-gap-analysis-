import pandas as pd

# Course catalog (same as Step 4)
courses = [
    {
        "course_name": "Introduction to Machine Learning",
        "platform": "NPTEL",
        "skill": "machine learning",
        "duration_weeks": 8,
        "cost": 0
    },
    {
        "course_name": "Deep Learning Specialization",
        "platform": "Coursera",
        "skill": "deep learning",
        "duration_weeks": 16,
        "cost": 3000
    },
    {
        "course_name": "Natural Language Processing",
        "platform": "NPTEL",
        "skill": "nlp",
        "duration_weeks": 12,
        "cost": 0
    },
    {
        "course_name": "TensorFlow for Beginners",
        "platform": "Coursera",
        "skill": "tensorflow",
        "duration_weeks": 6,
        "cost": 2500
    }
]

df = pd.DataFrame(courses)

# -------------------------------
# Scoring Logic
# -------------------------------
# Lower cost and shorter duration → higher score

df["cost_score"] = df["cost"].apply(lambda x: 1 if x == 0 else 0.5)
df["duration_score"] = df["duration_weeks"].apply(lambda x: 1 / x)

# Final weighted score
df["final_score"] = (
    0.6 * df["cost_score"] +
    0.4 * df["duration_score"]
)

# Sort courses by score
ranked_courses = df.sort_values(by="final_score", ascending=False)

print("Ranked Course Recommendations:\n")
print(ranked_courses[[
    "course_name", "platform", "skill",
    "duration_weeks", "cost", "final_score"
]])
