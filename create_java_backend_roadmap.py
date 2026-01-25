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
    title = "Java Backend Development"
    slug = "java-backend-mastery"
    
    description = """
    A complete, step-by-step Java Backend Development roadmap for BTech / CSE students.
    
    Starts from absolute basics and progresses to industry-ready backend skills.

    **Focus:**
    *   Real backend development, not just syntax
    *   Concept-first, not framework-first
    *   Why each concept is needed in backend
    *   Industry-standard practices
    """
    
    roadmap, created = Roadmap.objects.get_or_create(
        slug=slug,
        defaults={
            'title': title,
            'description': description,
            'short_description': "Become an industry-ready Java Backend Engineer. Master Spring Boot, APIs, Databases, and System Design.",
            'category': category,
            'difficulty': 'intermediate',
            'is_premium': True,
            'price': 699,
            'estimated_hours': 60,
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
                "How requests and responses work",
                "Role of backend in real applications",
                "Java role in backend systems"
            ]
        },
        {
            "title": "Core Java for Backend",
            "description": "Gain Java skills needed for backend.",
            "is_free": False,
            "topics": [
                "Core Java revision (classes, objects, OOPS)",
                "Exception handling",
                "Collections framework",
                "Java I/O basics",
                "Writing clean and readable Java code"
            ]
        },
        {
            "title": "Spring & Spring Boot Basics",
            "description": "Build real backend services.",
            "is_free": False,
            "topics": [
                "Why Spring framework exists",
                "Dependency injection concept",
                "Spring Boot basics",
                "Creating REST APIs",
                "Handling HTTP requests",
                "Basic error handling"
            ]
        },
        {
            "title": "Database & API Integration",
            "description": "Connect backend to data.",
            "is_free": False,
            "topics": [
                "SQL basics",
                "Connecting Java backend to database",
                "CRUD operations",
                "ORM concept (JPA/Hibernate – concept level)",
                "Data validation"
            ]
        },
        {
            "title": "Industry-Ready Backend Skills",
            "description": "Become job-ready.",
            "is_free": False,
            "topics": [
                "Authentication & authorization basics",
                "Backend security concepts",
                "API best practices",
                "Logging & exception handling",
                "Basic deployment concept",
                "Common mistakes Java backend beginners make"
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
                'color': '#ef4444' # Red for Java/Backend
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
