import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import Roadmap, Stage, Topic, RoadmapCategory

def create_roadmap():
    # 1. Create/Get Category (Lookup by slug to avoid unique constraint error)
    category, _ = RoadmapCategory.objects.get_or_create(
        slug='backend-development',
        defaults={'name': 'Backend Development', 'color': '#ef4444', 'icon': 'fa-server'}
    )
    
    # 2. Create Roadmap
    title = "Python Backend Development"
    slug = "python-backend-mastery"
    
    description = """
    A complete, step-by-step Python Backend Development roadmap for BTech / CSE students.
    
    Starts from absolute basics and progresses to industry-ready backend skills.

    **Focus:**
    *   Real backend development, not just scripting
    *   Concept-first, not framework-first
    *   Why each concept is needed in backend
    *   Industry-standard practices
    """
    
    roadmap, created = Roadmap.objects.get_or_create(
        slug=slug,
        defaults={
            'title': title,
            'description': description,
            'short_description': "Master Python Backend Development. Build robust APIs, work with Databases, and learn Django/FastAPI.",
            'category': category,
            'difficulty': 'intermediate',
            'is_premium': True,
            'price': 699,
            'estimated_hours': 55,
            'is_featured': True
        }
    )
    
    if not created:
        print(f"Roadmap '{title}' already exists. Updating...")
        roadmap.description = description
        roadmap.save()
    else:
        print(f"Created Roadmap: {title}")

    # 3. Stages and Topics
    stages_data = [
        {
            "title": "Backend Foundations",
            "description": "Understand what backend development actually means.",
            "is_free": True,
            "topics": [
                "What backend development is",
                "Client–server architecture",
                "How HTTP request–response works",
                "Role of backend in real applications",
                "Where Python is used in backend systems"
            ]
        },
        {
            "title": "Core Python for Backend",
            "description": "Gain Python skills required for backend.",
            "is_free": False,
            "topics": [
                "Python data types & control flow (revision)",
                "Functions & modular coding",
                "OOPS concepts in Python",
                "Exception handling",
                "Writing clean, readable Python code"
            ]
        },
        {
            "title": "Python Backend Frameworks",
            "description": "Build real backend services.",
            "is_free": False,
            "topics": [
                "Why frameworks are needed in backend",
                "Django vs FastAPI (when to use which)",
                "Creating REST APIs",
                "URL routing & request handling",
                "Basic error handling"
            ]
        },
        {
            "title": "Database & API Integration",
            "description": "Connect backend to data.",
            "is_free": False,
            "topics": [
                "SQL basics",
                "Database integration with Python",
                "CRUD operations",
                "ORM concept (Django ORM / SQLAlchemy – concept level)",
                "Input validation & data integrity"
            ]
        },
        {
            "title": "Industry-Ready Python Backend Skills",
            "description": "Become job-ready.",
            "is_free": False,
            "topics": [
                "Authentication & authorization basics",
                "Backend security concepts",
                "API best practices",
                "Logging & error monitoring",
                "Basic deployment concepts",
                "Common mistakes Python backend beginners make"
            ]
        }
    ]
    
    for i, stage_data in enumerate(stages_data, 1):
        stage, _ = Stage.objects.get_or_create(
            roadmap=roadmap,
            order=i,
            defaults={
                'title': stage_data['title'],
                'description': stage_data['description'],
                'is_free': stage_data['is_free'],
                'color': '#3b82f6' # Blue for Python
            }
        )
        print(f"  Processed Stage {i}: {stage.title}")
        
        # Create topics
        for j, topic_title in enumerate(stage_data['topics'], 1):
            Topic.objects.get_or_create(
                stage=stage,
                title=topic_title,
                defaults={
                    'order': j,
                    'content': f"# {topic_title}\n\nContent coming soon...",
                    'content_type': 'text',
                    'duration_minutes': 20
                }
            )
            
    # Update Stats
    roadmap.update_stats()
    print("Roadmap creation complete!")

# Execute immediately without main check
create_roadmap()
