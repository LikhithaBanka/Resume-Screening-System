import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Read Resume PDF
with pdfplumber.open("resumes/sample resume name.pdf") as pdf:
    resume = ""

    for page in pdf.pages:
        text = page.extract_text()
        if text:
            resume += text

resume_lower = resume.lower()

# Job Roles Database
jobs = {
    "Software Developer":
        "python java sql git github problem solving",

    "Frontend Developer":
        "html css javascript react bootstrap nodejs",

    "Python Developer":
        "python django flask sql mysql api",

    "Data Analyst":
        "python sql excel power bi tableau data analysis",

    "Machine Learning Engineer":
        "python machine learning tensorflow pandas numpy",

    "Cloud Engineer":
        "aws azure docker kubernetes linux",

    "Full Stack Developer":
        "html css javascript react nodejs mongodb sql",

    "Cyber Security Analyst":
        "network security ethical hacking penetration testing",

    "DevOps Engineer":
        "docker kubernetes aws linux git",

    "Java Developer":
        "java spring sql mysql oops"
}

print("\n===== JOB MATCH ANALYSIS =====\n")

for job, job_skills in jobs.items():

    documents = [resume, job_skills]

    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(documents)

    score = cosine_similarity(
        matrix[0:1],
        matrix[1:2]
    )[0][0] * 100

    print(f"\n{job}")
    print("Match Score:", round(score, 2), "%")

    missing = []

    for skill in job_skills.split():
        if skill.lower() not in resume_lower:
            missing.append(skill)

    print("Missing Skills:")

    if len(missing) == 0:
        print("None")
    else:
        for skill in missing:
            print("-", skill)