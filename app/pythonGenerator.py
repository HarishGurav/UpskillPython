import json

# 50 realistic IT job titles
job_titles = [
    "Frontend Developer", "Backend Developer", "Full Stack Developer", "Data Scientist", "DevOps Engineer",
    "React Developer", "Angular Developer", "Node.js Developer", "Java Developer", "Python Developer",
    "Machine Learning Engineer", "Cloud Engineer", "Mobile App Developer", "UI/UX Designer", "QA Engineer",
    "Security Analyst", "Database Administrator", "Systems Analyst", "Software Architect", "Scrum Master",
    "AI Engineer", "Big Data Engineer", "Software Tester", "Product Manager", "Business Analyst",
    "Site Reliability Engineer", "Embedded Systems Developer", "Game Developer", "AR/VR Developer", "Software Consultant",
    "ERP Developer", "Salesforce Developer", "Blockchain Developer", "Cybersecurity Engineer", "IT Support Specialist",
    "Computer Vision Engineer", "NLP Engineer", "Data Engineer", "IoT Developer", "Software Trainer",
    "Frontend Lead", "Backend Lead", "Full Stack Lead", "Technical Lead", "Release Manager",
    "Cloud Solutions Architect", "Mobile Solutions Architect", "BI Developer", "Integration Specialist", "RPA Developer"
]

# Skills list patterns
skills_list = [
    ["HTML", "CSS", "JavaScript", "Angular", "Responsive Design"],
    ["Python", "Django", "REST APIs", "PostgreSQL"],
    ["JavaScript", "Python", "React", "Node.js", "SQL"],
    ["Python", "Machine Learning", "Pandas", "NumPy"],
    ["Docker", "Kubernetes", "AWS", "CI/CD"],
    ["JavaScript", "React", "HTML", "CSS"],
    ["JavaScript", "TypeScript", "Angular", "HTML", "CSS"],
    ["Node.js", "Express.js", "JavaScript", "MongoDB", "SQL"],
    ["Java", "Spring Boot", "SQL", "REST APIs"],
    ["Python", "Flask", "Django", "SQL", "REST APIs"]
]

# Course catalog mapping skills to courses
courses_catalog = {
    "HTML": [{"id": 1, "title": "Frontend with HTML & CSS", "platform": "Coursera", "link": "https://www.coursera.org/specializations/html-css-javascript"}],
    "CSS": [{"id": 2, "title": "CSS Essentials", "platform": "Udemy", "link": "https://www.udemy.com/course/css-essential-training/"}],
    "JavaScript": [{"id": 3, "title": "Modern JavaScript", "platform": "Udemy", "link": "https://www.udemy.com/course/modern-javascript/"}],
    "Angular": [{"id": 4, "title": "Angular Complete Guide", "platform": "Udemy", "link": "https://www.udemy.com/course/the-complete-guide-to-angular/"}],
    "Responsive Design": [{"id":5, "title":"Responsive Web Design","platform":"Coursera","link":"https://www.coursera.org/learn/responsive-web-design"}],
    "Python":[{"id":6,"title":"Python for Everybody","platform":"Coursera","link":"https://www.coursera.org/specializations/python"}],
    "Django":[{"id":7,"title":"Django for Beginners","platform":"Udemy","link":"https://www.udemy.com/course/django-for-beginners/"}],
    "REST APIs":[{"id":8,"title":"REST API Design","platform":"Pluralsight","link":"https://www.pluralsight.com/courses/restful-api-design"}],
    "PostgreSQL":[{"id":9,"title":"PostgreSQL Basics","platform":"Udemy","link":"https://www.udemy.com/course/postgresql-for-beginners/"}],
    "React":[{"id":10,"title":"React Complete Guide","platform":"Udemy","link":"https://www.udemy.com/course/react-the-complete-guide/"}],
    "Node.js":[{"id":11,"title":"Node.js Essentials","platform":"Pluralsight","link":"https://www.pluralsight.com/courses/nodejs"}],
    "SQL":[{"id":12,"title":"SQL Bootcamp","platform":"Udemy","link":"https://www.udemy.com/course/sql-bootcamp/"}],
    "Machine Learning":[{"id":13,"title":"Machine Learning by Andrew Ng","platform":"Coursera","link":"https://www.coursera.org/learn/machine-learning"}],
    "Pandas":[{"id":14,"title":"Data Analysis with Pandas","platform":"Udemy","link":"https://www.udemy.com/course/data-analysis-with-pandas-and-numpy/"}],
    "NumPy":[{"id":15,"title":"NumPy for Data Analysis","platform":"Udemy","link":"https://www.udemy.com/course/numpy-for-data-analysis/"}],
    "Docker":[{"id":16,"title":"Docker Mastery","platform":"Udemy","link":"https://www.udemy.com/course/docker-mastery/"}],
    "Kubernetes":[{"id":17,"title":"Kubernetes for Beginners","platform":"Udemy","link":"https://www.udemy.com/course/learn-kubernetes/"}],
    "AWS":[{"id":18,"title":"AWS Cloud Practitioner","platform":"Coursera","link":"https://www.coursera.org/learn/aws-cloud-practitioner-essentials"}],
    "TypeScript":[{"id":19,"title":"Understanding TypeScript","platform":"Udemy","link":"https://www.udemy.com/course/understanding-typescript/"}],
    "Express.js":[{"id":20,"title":"Express.js Fundamentals","platform":"Udemy","link":"https://www.udemy.com/course/expressjs/"}],
    "Java":[{"id":21,"title":"Java Masterclass","platform":"Udemy","link":"https://www.udemy.com/course/java-the-complete-java-developer-course/"}],
    "Spring Boot":[{"id":22,"title":"Spring Boot for Beginners","platform":"Udemy","link":"https://www.udemy.com/course/spring-boot-tutorial/"}],
    "Flask":[{"id":23,"title":"Flask Web Development","platform":"Udemy","link":"https://www.udemy.com/course/python-and-flask-bootcamp-create-websites/"}]
}

# Generate 50 jobs
jobs = []
for i in range(50):
    job_id = i+1
    title = job_titles[i]
    skills = skills_list[i % len(skills_list)]
    courses = []
    for skill in skills:
        if skill in courses_catalog:
            courses.extend(courses_catalog[skill])
    # Remove duplicate courses by id
    unique_courses = {c['id']: c for c in courses}
    jobs.append({
        "id": job_id,
        "title": title,
        "description": f"This is the description for {title} covering skills {', '.join(skills)}.",
        "skills": skills,
        "courses": list(unique_courses.values())
    })

# Save JSON locally
with open("jobProfilesWithCourses_realTitles.json", "w") as f:
    json.dump(jobs, f, indent=2)

print("✅ File saved locally as jobProfilesWithCourses_realTitles.json")
