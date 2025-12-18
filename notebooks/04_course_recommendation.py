import pandas as pd

# -------------------------------
# Missing skills (from Step 3)
# -------------------------------
missing_skills = [
    "nlp",
    "deep learning",
    "machine learning",
    "tensorflow"
]

# -------------------------------
# Course Catalog (Sample)
# -------------------------------
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

df_courses = pd.DataFrame(courses)

# -------------------------------
# Recommendation Logic
# -------------------------------
recommended_courses = df_courses[
    df_courses["skill"].isin(missing_skills)
]

# Display recommendations
print("Recommended Courses:\n")
print(recommended_courses)
