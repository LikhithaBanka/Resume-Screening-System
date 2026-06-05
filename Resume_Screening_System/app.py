from flask import Flask, render_template
import pdfplumber
import re

app = Flask(__name__)

@app.route("/")
def home():

    with pdfplumber.open("resumes/likhi.pdf") as pdf:
        resume = ""

        for page in pdf.pages:
            text = page.extract_text()

            if text:
                resume += text

    resume_lower = resume.lower()

    resume_words = set(
        re.findall(r'\b[a-zA-Z0-9+#]+\b', resume_lower)
    )

    jobs = {
        "Software Developer": "python java sql git github problem solving",
        "Frontend Developer": "html css javascript react bootstrap nodejs",
        "Backend Developer": "python java nodejs sql mysql api",
        "Full Stack Developer": "html css javascript react nodejs mongodb sql",
        "Python Developer": "python django flask sql mysql api",
        "Java Developer": "java spring sql mysql oops",
        "Data Analyst": "python sql excel power bi tableau data analysis",
        "Data Scientist": "python machine learning pandas numpy statistics",
        "Machine Learning Engineer": "python machine learning tensorflow pandas numpy",
        "AI Engineer": "python tensorflow pytorch machine learning deep learning",
        "Cloud Engineer": "aws azure docker kubernetes linux",
        "DevOps Engineer": "docker kubernetes aws linux git",
        "Cyber Security Analyst": "network security ethical hacking penetration testing",
        "Network Engineer": "networking routing switching tcp ip",
        "Database Administrator": "sql mysql postgresql database backup",
        "Android Developer": "java kotlin android studio firebase",
        "iOS Developer": "swift xcode ios ui ux",
        "UI UX Designer": "figma adobe xd wireframing prototyping",
        "QA Engineer": "testing selenium automation manual testing",
        "Business Analyst": "excel sql power bi communication",
        "Project Manager": "leadership communication planning agile scrum",
        "SAP Consultant": "sap excel business process",
        "Blockchain Developer": "solidity ethereum blockchain web3",
        "Game Developer": "unity c# unreal engine",
        "Embedded Engineer": "c c++ microcontroller arduino embedded systems"
    }

    results = []

    for job, job_skills in jobs.items():

        skills = job_skills.split()

        matched = []
        missing = []

        for skill in skills:

            if skill.lower() in resume_words:
                matched.append(skill)
            else:
                missing.append(skill)

        score = (len(matched) / len(skills)) * 100

        results.append({
            "job": job,
            "score": round(score, 2),
            "matched": matched,
            "missing": missing
        })

    results.sort(key=lambda x: x["score"], reverse=True)

    return render_template(
        "results.html",
        results=results
    )

if __name__ == "__main__":
    app.run(debug=True)