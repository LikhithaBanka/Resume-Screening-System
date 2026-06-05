# Resume Screening System

A web-based Resume Screening System developed using Python and Flask.

## Features

* Extracts text from PDF resumes
* Analyzes resumes against multiple job roles
* Calculates match scores
* Identifies matched skills
* Identifies missing skills
* Displays results through a web interface

## Technologies Used

* Python
* Flask
* PDFPlumber
* HTML
* CSS

## Project Structure

Resume_Screening_System

├── app.py

├── templates

│   ├── index.html

│   └── results.html

├── static

│   └── style.css

├── resumes

└── README.md

## How to Run

1. Place a PDF resume inside the resumes folder.
2. Update the PDF filename in app.py.
3. Install required libraries:

pip install flask pdfplumber

4. Run:

python app.py

5. Open:

http://127.0.0.1:5000

## Output

* Match Score for each job role
* Matched Skills
* Missing Skills

## Author

Banka Likhitha

