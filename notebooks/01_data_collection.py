import pandas as pd
import os

# -------------------------------
# Get project root directory
# -------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create data/raw directory safely
RAW_DATA_DIR = os.path.join(BASE_DIR, "data", "raw")
os.makedirs(RAW_DATA_DIR, exist_ok=True)

# -------------------------------
# Sample Indian job descriptions
# -------------------------------
jobs = [
    {
        "job_title": "AI Engineer",
        "company": "TCS",
        "location": "Bangalore",
        "description": "Python, Machine Learning, Deep Learning, NLP, TensorFlow"
    },
    {
        "job_title": "Data Analyst",
        "company": "Infosys",
        "location": "Hyderabad",
        "description": "SQL, Python, Data Visualization, Statistics, Excel"
    },
    {
        "job_title": "Software Engineer",
        "company": "Wipro",
        "location": "Pune",
        "description": "Java, OOPs, Data Structures, REST APIs, Problem Solving"
    }
]

# Convert to DataFrame
df = pd.DataFrame(jobs)

# Display data
print(df)

# Save CSV
csv_path = os.path.join(RAW_DATA_DIR, "indian_jobs_sample.csv")
df.to_csv(csv_path, index=False)

print(f"\nCSV file saved successfully at:\n{csv_path}")
