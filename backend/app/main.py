from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import pandas as pd
import os
import ast

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SKILLS_CSV = os.path.join(BASE_DIR, "data", "processed", "extracted_skills.csv")
COURSES_CSV = os.path.join(BASE_DIR, "data", "raw", "courses_dataset.csv")

@app.get("/ui", response_class=HTMLResponse)
def ui():
    return """
    <html>
    <head>
        <title>Skill Gap Analyzer</title>
        <style>
            body {
                font-family: 'Segoe UI', sans-serif;
                background: #f4f7fb;
                margin: 0;
                padding: 0;
            }
            header {
                background: linear-gradient(90deg, #2563eb, #1e40af);
                color: white;
                padding: 20px;
                text-align: center;
            }
            .container {
                display: flex;
                justify-content: center;
                gap: 30px;
                padding: 40px;
            }
            .card {
                background: white;
                width: 40%;
                padding: 25px;
                border-radius: 12px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.08);
            }
            h2 {
                color: #1e3a8a;
                margin-bottom: 15px;
            }
            label {
                font-weight: 600;
            }
            input, textarea {
                width: 100%;
                padding: 10px;
                margin-top: 8px;
                margin-bottom: 15px;
                border-radius: 6px;
                border: 1px solid #cbd5e1;
                font-size: 14px;
            }
            button {
                background: #22c55e;
                color: white;
                border: none;
                padding: 12px;
                width: 100%;
                border-radius: 8px;
                font-size: 16px;
                cursor: pointer;
                font-weight: bold;
            }
            button:hover {
                background: #16a34a;
            }
            footer {
                text-align: center;
                padding: 15px;
                color: #64748b;
                font-size: 14px;
            }
        </style>
    </head>

    <body>
        <header>
            <h1>🎓 Job Skill Gap Analyzer</h1>
            <p>Discover missing skills & get learning recommendations</p>
        </header>

        <form method="post" action="/analyze-ui">
            <div class="container">
                <div class="card">
                    <h2>🧑‍🎓 Student Input</h2>

                    <label>Target Job Role</label>
                    <input name="role" placeholder="AI Engineer" required>

                    <label>Your Current Skills</label>
                    <textarea name="skills" rows="5"
                        placeholder="Python, SQL, Excel"></textarea>

                    <button type="submit">Analyze My Skills 🚀</button>
                </div>
            </div>
        </form>

        <footer>
            Built for students • Skill-based learning guidance
        </footer>
    </body>
    </html>
    """

@app.post("/analyze-ui", response_class=HTMLResponse)
def analyze_ui(role: str = Form(...), skills: str = Form(...)):
    skills_df = pd.read_csv(SKILLS_CSV)
    courses_df = pd.read_csv(COURSES_CSV)

    row = skills_df[skills_df["job_title"] == role]

    if row.empty:
        return "<h3>Role not found in dataset</h3><a href='/ui'>Go Back</a>"

    required_skills = set(ast.literal_eval(row.iloc[0]["extracted_skills"]))
    user_skills = set(s.strip().lower() for s in skills.split(","))

    missing_skills = required_skills - user_skills

    recommended = courses_df[courses_df["skill"].isin(missing_skills)]

    course_html = "".join(
        f"<li><a href='{r.link}' target='_blank'>{r.course_name} ({r.platform})</a></li>"
        for r in recommended.itertuples()
    )

    return f"""
    <html>
<head>
    <title>Skill Gap Result</title>
    <style>
        body {{
            font-family: 'Segoe UI', sans-serif;
            background: #f4f7fb;
            padding: 30px;
        }}
        .container {{
            display: flex;
            gap: 30px;
            justify-content: center;
        }}
        .card {{
            background: white;
            width: 45%;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.08);
        }}
        h2 {{
            color: #1e3a8a;
        }}
        ul {{
            padding-left: 20px;
        }}
        li {{
            margin-bottom: 8px;
        }}
        a {{
            color: #2563eb;
            text-decoration: none;
            font-weight: 600;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        .badge {{
            display: inline-block;
            background: #dcfce7;
            color: #166534;
            padding: 6px 10px;
            border-radius: 20px;
            margin: 5px 5px 5px 0;
            font-size: 14px;
        }}
        .back {{
            margin-top: 30px;
            text-align: center;
        }}
    </style>
</head>

<body>
    <h1 style="text-align:center;">📊 Skill Gap Analysis Result</h1>

    <div class="container">
        <div class="card">
            <h2>🧾 Your Input</h2>
            <p><b>Target Role:</b> {role}</p>
            <p><b>Current Skills:</b></p>
            <p>{skills}</p>
        </div>

        <div class="card">
            <h2>🎯 Skill Gap</h2>
            {"".join(f"<span class='badge'>{s}</span>" for s in missing_skills)}

            <h2 style="margin-top:25px;">📚 Recommended Courses</h2>
            <ul>
                {course_html}
            </ul>
        </div>
    </div>

    <div class="back">
        <a href="/ui">⬅ Analyze Another Role</a>
    </div>
</body>
</html>
"""