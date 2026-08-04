"""
One-time script to populate the `roles` table with initial career roadmap data.
Run with: python seed_roles.py
Safe to re-run — it clears existing roles first, then re-inserts all 11.
"""

import json
from app.database import SessionLocal
from app.models import Role

roles_data = [
    {
        "title": "Software Engineer",
        "slug": "software-engineer",
        "job_description": "Designs, builds, and maintains software applications and systems. Works across the stack depending on the team, writing code, fixing bugs, and collaborating with product and design teams to ship features.",
        "skills_required": ["Data Structures & Algorithms", "Java/Python/C++", "Git", "SQL", "System Design Basics", "OOP"],
        "hiring_companies": ["Google", "Microsoft", "Amazon", "TCS", "Infosys", "Accenture"],
        "average_salary": "₹6-15 LPA",
        "learning_roadmap": [
            "Master one core language (Java, Python, or C++)",
            "Learn Data Structures & Algorithms deeply",
            "Understand OOP principles and design patterns",
            "Learn SQL and basic database design",
            "Build 2-3 solid projects with clean code",
            "Learn Git and collaborative workflows",
            "Practice DSA problems on LeetCode/GFG daily",
            "Learn basic System Design concepts",
        ],
        "interview_pattern": "Online Assessment (DSA + Aptitude) → Technical Round 1 (DSA + CS fundamentals) → Technical Round 2 (Project discussion + coding) → HR Round",
    },
    {
        "title": "Frontend Developer",
        "slug": "frontend-developer",
        "job_description": "Builds the user-facing part of web applications — layouts, interactivity, and performance. Works closely with designers to turn mockups into responsive, accessible interfaces.",
        "skills_required": ["HTML/CSS", "JavaScript", "React", "Responsive Design", "Git", "Browser DevTools"],
        "hiring_companies": ["Google", "Flipkart", "Swiggy", "Zomato", "Startups", "Accenture"],
        "average_salary": "₹5-12 LPA",
        "learning_roadmap": [
            "Master HTML, CSS, and JavaScript fundamentals",
            "Learn a modern framework (React recommended)",
            "Understand responsive design and CSS layout systems (Flexbox/Grid)",
            "Learn state management (Context API, Redux, or similar)",
            "Practice building real UI clones (Netflix, Instagram, etc.)",
            "Learn API integration and async JavaScript",
            "Understand performance optimization basics",
            "Build a portfolio with 3+ deployed projects",
        ],
        "interview_pattern": "Portfolio Review → JavaScript Fundamentals Round → Live Coding (build a small UI) → System Design (frontend architecture) → HR Round",
    },
    {
        "title": "Backend Developer",
        "slug": "backend-developer",
        "job_description": "Builds and maintains server-side logic, databases, and APIs that power applications. Focuses on scalability, security, and data integrity.",
        "skills_required": ["Python/Node.js/Java", "SQL & NoSQL Databases", "REST APIs", "System Design", "Authentication & Security", "Git"],
        "hiring_companies": ["Amazon", "Microsoft", "Razorpay", "PhonePe", "Infosys", "Wipro"],
        "average_salary": "₹6-14 LPA",
        "learning_roadmap": [
            "Master one backend language/framework (Node.js, Django, or Spring Boot)",
            "Learn relational databases deeply (PostgreSQL/MySQL)",
            "Understand REST API design principles",
            "Learn authentication (JWT, OAuth) and security basics",
            "Study system design fundamentals (caching, load balancing)",
            "Learn NoSQL basics (MongoDB or Redis)",
            "Build 2-3 APIs with proper documentation",
            "Practice DSA alongside backend concepts",
        ],
        "interview_pattern": "Online Assessment (DSA) → Technical Round 1 (DBMS + backend concepts) → Technical Round 2 (System Design + project deep-dive) → HR Round",
    },
    {
        "title": "Full Stack Developer",
        "slug": "full-stack-developer",
        "job_description": "Works across both frontend and backend, building complete features end-to-end. Highly valued at startups for versatility across the entire application stack.",
        "skills_required": ["JavaScript/TypeScript", "React", "Node.js/Django", "SQL", "REST APIs", "Git", "Deployment (Vercel/Render/AWS)"],
        "hiring_companies": ["Startups", "Flipkart", "Swiggy", "Paytm", "Accenture", "Cognizant"],
        "average_salary": "₹6-16 LPA",
        "learning_roadmap": [
            "Master JavaScript fundamentals deeply",
            "Learn a frontend framework (React)",
            "Learn a backend framework (Node.js/Express or Django)",
            "Understand databases (SQL fundamentals)",
            "Learn to connect frontend and backend via REST APIs",
            "Learn authentication and deployment basics",
            "Build 2-3 full end-to-end projects",
            "Practice DSA consistently alongside projects",
        ],
        "interview_pattern": "Online Assessment → Technical Round (full stack project walkthrough) → Live Coding Round → System Design → HR Round",
    },
    {
        "title": "Data Analyst",
        "slug": "data-analyst",
        "job_description": "Collects, cleans, and analyzes data to help businesses make decisions. Builds dashboards and reports, and communicates insights to non-technical stakeholders.",
        "skills_required": ["SQL", "Excel", "Python (Pandas)", "Power BI/Tableau", "Statistics Basics", "Data Visualization"],
        "hiring_companies": ["Deloitte", "Accenture", "Amazon", "Flipkart", "TCS", "Cognizant"],
        "average_salary": "₹4-10 LPA",
        "learning_roadmap": [
            "Master SQL for querying and joins",
            "Learn Excel deeply (pivot tables, formulas)",
            "Learn Python basics with Pandas and NumPy",
            "Learn a visualization tool (Power BI or Tableau)",
            "Understand basic statistics (mean, variance, correlation)",
            "Practice on real datasets (Kaggle)",
            "Build 2-3 dashboard projects",
            "Learn to present insights clearly",
        ],
        "interview_pattern": "Online Assessment (SQL + Aptitude) → Technical Round (SQL + Excel case study) → Case Study Presentation → HR Round",
    },
    {
        "title": "Data Scientist",
        "slug": "data-scientist",
        "job_description": "Builds predictive models and extracts insights from data using statistics and machine learning. Works on problems like forecasting, recommendation systems, and classification.",
        "skills_required": ["Python", "Statistics & Probability", "Machine Learning", "SQL", "Pandas/NumPy/Scikit-learn", "Data Visualization"],
        "hiring_companies": ["Amazon", "Microsoft", "Flipkart", "Myntra", "Deloitte", "Startups"],
        "average_salary": "₹8-18 LPA",
        "learning_roadmap": [
            "Master Python for data science",
            "Learn statistics and probability deeply",
            "Learn SQL for data extraction",
            "Study core ML algorithms (regression, classification, clustering)",
            "Learn Scikit-learn and model evaluation techniques",
            "Practice on Kaggle competitions",
            "Learn basic deep learning concepts",
            "Build 3+ end-to-end ML projects with clear documentation",
        ],
        "interview_pattern": "Online Assessment (Stats + Coding) → Technical Round 1 (ML concepts + coding) → Case Study/Project Discussion → HR Round",
    },
    {
        "title": "AI Engineer",
        "slug": "ai-engineer",
        "job_description": "Designs and deploys AI/ML systems into production, including LLM-based applications. Bridges research and engineering — building pipelines that make models usable at scale.",
        "skills_required": ["Python", "Machine Learning", "Deep Learning", "LLMs & Prompt Engineering", "APIs", "Cloud Basics (AWS/GCP)"],
        "hiring_companies": ["Google", "Microsoft", "OpenAI-adjacent startups", "Amazon", "AI startups"],
        "average_salary": "₹10-22 LPA",
        "learning_roadmap": [
            "Master Python and core ML fundamentals",
            "Learn deep learning (neural networks, CNNs, RNNs, Transformers)",
            "Understand how LLMs work and prompt engineering",
            "Learn to use ML frameworks (PyTorch or TensorFlow)",
            "Learn to deploy models via APIs (FastAPI + Docker basics)",
            "Explore vector databases and RAG systems",
            "Build 2-3 AI-powered applications",
            "Stay updated with recent AI research and tools",
        ],
        "interview_pattern": "Online Assessment (ML + Coding) → Technical Round 1 (Deep Learning concepts) → Technical Round 2 (System Design for AI systems) → HR Round",
    },
    {
        "title": "DevOps Engineer",
        "slug": "devops-engineer",
        "job_description": "Automates and manages infrastructure, deployment pipelines, and system reliability. Bridges development and operations to ship software faster and more reliably.",
        "skills_required": ["Linux", "Docker & Kubernetes", "CI/CD", "Cloud Platforms (AWS/Azure)", "Scripting (Bash/Python)", "Git"],
        "hiring_companies": ["Amazon", "Microsoft", "Infosys", "Wipro", "Startups", "Cognizant"],
        "average_salary": "₹6-16 LPA",
        "learning_roadmap": [
            "Master Linux fundamentals and shell scripting",
            "Learn Git deeply and version control workflows",
            "Learn Docker and containerization concepts",
            "Learn Kubernetes basics for orchestration",
            "Understand CI/CD pipelines (GitHub Actions/Jenkins)",
            "Learn a cloud platform (AWS recommended)",
            "Learn Infrastructure as Code (Terraform basics)",
            "Build a project with a full CI/CD deployment pipeline",
        ],
        "interview_pattern": "Online Assessment (Linux + Scripting) → Technical Round 1 (CI/CD + Docker/K8s) → Technical Round 2 (Cloud architecture scenario) → HR Round",
    },
    {
        "title": "Cloud Engineer",
        "slug": "cloud-engineer",
        "job_description": "Designs, deploys, and manages cloud infrastructure for scalability and reliability. Works with services across compute, storage, networking, and security on major cloud platforms.",
        "skills_required": ["AWS/Azure/GCP", "Networking Basics", "Linux", "IAM & Security", "Terraform", "Scripting"],
        "hiring_companies": ["Amazon", "Microsoft", "Google", "Accenture", "TCS", "Wipro"],
        "average_salary": "₹6-15 LPA",
        "learning_roadmap": [
            "Learn cloud fundamentals (start with AWS)",
            "Understand core services: compute, storage, networking",
            "Learn Linux administration basics",
            "Learn IAM, security groups, and cloud security basics",
            "Get an entry-level cloud certification (AWS CCP or similar)",
            "Learn Infrastructure as Code (Terraform)",
            "Practice deploying real applications to the cloud",
            "Learn cost optimization and monitoring basics",
        ],
        "interview_pattern": "Online Assessment (Networking + Cloud basics) → Technical Round 1 (Cloud services deep-dive) → Scenario-based Architecture Round → HR Round",
    },
    {
        "title": "Cybersecurity Analyst",
        "slug": "cybersecurity-analyst",
        "job_description": "Monitors, detects, and responds to security threats across systems and networks. Performs vulnerability assessments and helps organizations strengthen their security posture.",
        "skills_required": ["Networking Fundamentals", "Linux", "Security Tools (Wireshark, Nmap)", "OWASP Top 10", "Cryptography Basics", "Incident Response"],
        "hiring_companies": ["Deloitte", "Accenture", "TCS", "Wipro", "Cybersecurity firms", "Banks"],
        "average_salary": "₹5-14 LPA",
        "learning_roadmap": [
            "Master networking fundamentals (TCP/IP, DNS, firewalls)",
            "Learn Linux command line thoroughly",
            "Understand common vulnerabilities (OWASP Top 10)",
            "Learn security tools (Wireshark, Nmap, Burp Suite)",
            "Study cryptography basics",
            "Practice on platforms like TryHackMe/HackTheBox",
            "Learn about incident response and security frameworks",
            "Consider a certification (Security+, CEH) as you progress",
        ],
        "interview_pattern": "Online Assessment (Networking + Security basics) → Technical Round 1 (Scenario-based security questions) → Practical/Lab Round → HR Round",
    },
    {
        "title": "Mobile App Developer",
        "slug": "mobile-app-developer",
        "job_description": "Builds native or cross-platform mobile applications for Android and/or iOS. Focuses on performance, UI/UX, and smooth integration with backend services.",
        "skills_required": ["Kotlin/Swift or React Native/Flutter", "REST APIs", "UI/UX Basics", "Git", "App Store Deployment", "State Management"],
        "hiring_companies": ["Flipkart", "Swiggy", "Paytm", "Ola", "Startups", "Accenture"],
        "average_salary": "₹5-13 LPA",
        "learning_roadmap": [
            "Choose a path: native (Kotlin/Swift) or cross-platform (Flutter/React Native)",
            "Learn the fundamentals of your chosen framework",
            "Understand mobile UI/UX design principles",
            "Learn state management patterns",
            "Learn to integrate REST APIs into mobile apps",
            "Learn local storage and offline-first patterns",
            "Build and publish 2-3 apps (even to test tracks)",
            "Learn app performance optimization basics",
        ],
        "interview_pattern": "Online Assessment (DSA + Aptitude) → Technical Round 1 (Mobile framework concepts) → Live Coding/Project Walkthrough → HR Round",
    },
]


def seed():
    db = SessionLocal()
    try:
        deleted_count = db.query(Role).delete()
        print(f"Cleared {deleted_count} existing role(s).")

        for role_data in roles_data:
            role = Role(
                title=role_data["title"],
                slug=role_data["slug"],
                job_description=role_data["job_description"],
                skills_required=json.dumps(role_data["skills_required"]),
                hiring_companies=json.dumps(role_data["hiring_companies"]),
                average_salary=role_data["average_salary"],
                learning_roadmap=json.dumps(role_data["learning_roadmap"]),
                interview_pattern=role_data["interview_pattern"],
            )
            db.add(role)

        db.commit()
        print(f"Successfully seeded {len(roles_data)} roles.")
    finally:
        db.close()


if __name__ == "__main__":
    seed()