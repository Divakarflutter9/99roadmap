
import os
import django
import sys

# Add project root to sys.path
sys.path.append('/Users/saitejakaki/Divakar/devaproject')

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import Roadmap, RoadmapCategory, Stage, Topic

def create_python_backend_roadmap():
    """Create Comprehensive Python Backend Career Roadmap"""
    
    print("🚀 Initializing Python Backend Roadmap (Production Ready) Creation...")
    
    # 1. Get or Create Category
    category, _ = RoadmapCategory.objects.get_or_create(
        slug='backend-development',
        defaults={'name': 'Backend Development'}
    )
    
    # 2. Create Roadmap
    roadmap_slug = 'python-backend-career'
    roadmap_title = 'Python Backend Development (Production Ready)'
    
    roadmap, created = Roadmap.objects.get_or_create(
        slug=roadmap_slug,
        defaults={
            'title': roadmap_title,
            'short_description': 'Build scalable, production-grade backends with Django & FastAPI.',
            'description': 'Move beyond scripts. Learn how to structure large Flask/Django projects, handle authentication, manage databases, and deploy to the cloud.',
            'category': category,
            'difficulty': 'intermediate',
            'estimated_hours': 80,
            'is_premium': True,
            'is_featured': True,
            'is_active': True,
            'price': 499
        }
    )
    
    if created:
        print(f"✅ Created Roadmap: {roadmap.title}")
    else:
        print(f"ℹ️  Roadmap '{roadmap.title}' already exists. Updating details...")
        roadmap.stages.all().delete()
        print("   ♻️  Cleared existing stages for fresh import.")
        
    # ==========================================
    # STAGE 1: BACKEND BASICS (FREE)
    # ==========================================
    stage1 = Stage.objects.create(
        roadmap=roadmap,
        title='Backend Basics',
        description='The role of Python in the web ecosystem.',
        order=1,
        is_free=True
    )
    
    topics_s1 = [
        {
            'title': 'What Backend Actually Does',
            'content': """# The "Brain" of the App

## 1. Beyond the Script
You've written Python scripts to scrape data or solve math.
Backend is **Python that runs forever** (or until it crashes).

## 2. Responsibilities
- **Listen**: Wait for HTTP requests.
- **Think**: Execute Business Logic (e.g., "Is this password correct?").
- **Remember**: Read/Write to Database.
- **Reply**: Send JSON back to the user.

## 3. Why Python?
- **Speed of Development**: Write fewer lines than Java/C++.
- **AI Integration**: Easy to plug in ML models (PyTorch/TensorFlow).
- **Ecosystem**: Django (Batteries included) & FastAPI (Modern, async).
""",
            'order': 1
        },
        {
            'title': 'APIs & Servers Explained',
            'content': """# The Waiter Analogy

## 1. The Server (The Restaurant)
- A computer that runs your Python code 24/7.
- Examples: AWS EC2, DigitalOcean Droplet, Heroku.

## 2. The API (The Menu)
- Defines what you can ask for.
- `GET /menu`: Show food.
- `POST /order`: Buy food.
- **Interface**: The rules of communication.

## 3. JSON (The Language)
- Frontend and Backend speak different languages (JS vs Python).
- They talk in **JSON** (JavaScript Object Notation).
```json
{
  "user": "Alice",
  "balance": 500
}
```
""",
            'order': 2
        }
    ]
    
    for t in topics_s1:
        Topic.objects.create(stage=stage1, **t)
    print(f"   ✨ Added {len(topics_s1)} topics to Stage 1")


    # ==========================================
    # STAGE 2: PYTHON FOR BACKEND
    # ==========================================
    stage2 = Stage.objects.create(
        roadmap=roadmap,
        title='Python for Backend',
        description='Tools you need before touching Django.',
        order=2,
        is_free=False
    )
    
    topics_s2 = [
        {
            'title': 'Virtual Environments (Crucial)',
            'content': """# Dependency Hell & Solving It

## The Problem
Project A needs `Django 3.2`.
Project B needs `Django 4.0`.
If you install globally, one **breaks**.

## The Solution: venv
Create a isolated box for each project.

```bash
# Create
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate
```

## Modern Tools
- **Poetry**: dependency management on steroids.
- **Pipenv**: Combines pip and venv.
Use `requirements.txt` to freeze versions:
`pip freeze > requirements.txt`
""",
            'order': 1
        },
        {
            'title': 'Working with Packages',
            'content': """# The Python Ecosystem (PyPI)

## 1. pip (Python Package Installer)
- `pip install requests`
- Where do they go? -> `venv/lib/pythonX.X/site-packages/`

## 2. Essential Backend Packages
- **requests**: Making HTTP calls to other APIs.
- **python-dotenv**: Managing secrets (`.env` files).
- **pydantic**: Data validation (used heavily in FastAPI).
- **pytest**: Writing tests.

## 3. Structuring a Project
Don't put everything in `main.py`.
```
project/
├── core/
│   ├── auth.py
│   └── database.py
├── api/
│   └── routes.py
├── requirements.txt
└── .env
```
""",
            'order': 2
        }
    ]
    
    for t in topics_s2:
        Topic.objects.create(stage=stage2, **t)
    print(f"   ✨ Added {len(topics_s2)} topics to Stage 2")


    # ==========================================
    # STAGE 3: BACKEND FRAMEWORKS
    # ==========================================
    stage3 = Stage.objects.create(
        roadmap=roadmap,
        title='Backend Frameworks',
        description='Building APIs with Flask & Django.',
        order=3,
        is_free=False
    )
    
    topics_s3 = [
        {
            'title': 'Flask vs Django vs FastAPI',
            'content': """# Choosing Your Weapon

## 1. Flask (Microframework)
- **Philosophy**: "Here is the bare minimum. You add what you need."
- **Good For**: Small services, learning basics, flexibility.
- **Cons**: You have to manually setup DB, Auth, Admin.

## 2. Django (The Battery-Included Monolith)
- **Philosophy**: "We give you everything (ORM, Auth, Admin) out of the box."
- **Good For**: Speed of delivery, CMS, E-commerce, Standard Enterprise apps.
- **Cons**: Heavy, "Magic" can be confusing.

## 3. FastAPI (The Modern Speedster)
- **Philosophy**: "Async, fast, and type-safe."
- **Good For**: High-performance APIs, ML Model serving (uses Pydantic).
- **Cons**: Newer ecosystem than Django.

## Verdict
Start with **Flask** to learn *how* things work.
Use **Django** to build *products* fast.
Use **FastAPI** for *performance*.
""",
            'order': 1
        },
        {
            'title': 'The Concept of ORM',
            'content': """# Talking to Databases without SQL

## What is ORM?
**Object-Relational Mapping**.
It lets you interact with the DB using **Python Classes** instead of SQL queries.

## Example (Django ORM)
```python
# Instead of SQL: INSERT INTO users (name, age) VALUES ('Bob', 30);

# We do Python:
user = User(name="Bob", age=30)
user.save()
```

## Pros
- **Safety**: Automatically prevents SQL Injection.
- **Speed**: Write code faster.
- **Portability**: Switch from SQLite to PostgreSQL by changing 1 line in settings.

## Cons
- **N+1 Problem**: Easy to write inefficient queries if not careful.
- **Complexity**: Hard to optimize complex aggregations.
""",
            'order': 2
        }
    ]
    
    for t in topics_s3:
        Topic.objects.create(stage=stage3, **t)
    print(f"   ✨ Added {len(topics_s3)} topics to Stage 3")


    # ==========================================
    # STAGE 4: PRODUCTION READINESS
    # ==========================================
    stage4 = Stage.objects.create(
        roadmap=roadmap,
        title='Production Readiness',
        description='What separates a hobby project from a job-ready backend.',
        order=4,
        is_free=False
    )
    
    topics_s4 = [
        {
            'title': 'Authentication (JWT)',
            'content': """# Who goes there?

## 1. Session vs Token
- **Session**: Server remembers you (Requires server memory/DB). Hard to scale.
- **Token (JWT)**: You hold your own ID card. Server verifies signature. Easy to scale.

## 2. The Flow
1. User POST `login` with user/pass.
2. Server validates & generates `eyJ...` (JWT Token).
3. Client stores token (LocalStorage/Cookie).
4. Client sends token in `Authorization` header for next requests.

## 3. Libraries
- **Django**: `djangorestframework-simplejwt`
- **FastAPI**: `python-jose`
""",
            'order': 1
        },
        {
            'title': 'Deployment Basics (Gunicorn & Nginx)',
            'content': """# Going Live

You cannot run `python manage.py runserver` in production!

## 1. WSGI Server (Gunicorn)
- Django is just a Python app. It can't handle 1000 concurrent HTTP requests efficiently alone.
- **Gunicorn** (Green Unicorn) is a WSGI HTTP Server. It spawns multiple **Workers** to handle requests in parallel.
- `gunicorn myproject.wsgi:application`

## 2. Reverse Proxy (Nginx)
- Sits in front of Gunicorn.
- **Jobs**:
    - Serve Static Files (CSS/Images) EXTREMELY fast.
    - SSL Termination (HTTPS).
    - Load Balancing.
    - Buffer slow clients.

## The Architecture
`Client -> Nginx -> Gunicorn -> Django/Flask`
""",
            'order': 2
        },
        {
            'title': 'Interview Prep',
            'content': """# Cracking the Backend Interview

## Common Questions
1.  **"Explain the difference between List and Tuple."**
    - Mutability.
2.  **"How does a Dictionary work internally?"**
    - Hashing, Buckets.
3.  **"What is the GIL?"**
    - Global Interpreter Lock. Why Python threads aren't truly parallel on CPU.
4.  **"SQL vs NoSQL?"**
    - Structure, Scaling, CAP theorem.
5.  **"Design a URL Shortener."**
    - System Design basics.

## Code Tests
- **LeetCode**: Arrays, HashMaps, String manipulation.
- **Practical**: "Build a simple API with Flask that accepts a CSV and returns JSON."
""",
            'order': 3
        }
    ]
    
    for t in topics_s4:
        Topic.objects.create(stage=stage4, **t)
    print(f"   ✨ Added {len(topics_s4)} topics to Stage 4")

    # Update stats
    roadmap.update_stats()
    print("✅ Python Backend Roadmap creation complete! Stats updated.")

if __name__ == '__main__':
    create_python_backend_roadmap()
