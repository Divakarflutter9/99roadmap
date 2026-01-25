import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import Roadmap, Stage, Topic, RoadmapCategory

def create_roadmap():
    # 1. Create/Get Category
    category, _ = RoadmapCategory.objects.get_or_create(
        name="Computer Science",
        defaults={'slug': 'computer-science', 'color': '#10b981', 'icon': 'fa-laptop-code'}
    )
    
    # 2. Create Roadmap
    title = "Programming Fundamentals"
    slug = "programming-fundamentals"
    
    description = """
    A complete, step-by-step Programming Fundamentals roadmap for BTech students (all branches, especially CSE beginners).
    
    This roadmap starts from absolute zero and gradually moves to an advanced programming mindset.
    
    **Focus:**
    *   Beginner-friendly (no assumption of prior coding knowledge)
    *   Thinking, not memorizing syntax
    *   Real-life and logical examples
    *   Concept over Syntax
    """
    
    roadmap, created = Roadmap.objects.get_or_create(
        slug=slug,
        defaults={
            'title': title,
            'description': description,
            'short_description': "Master the art of thinking like a programmer. A beginner-friendly guide to logic, flow, and efficiency.",
            'category': category,
            'difficulty': 'beginner',
            'is_premium': True,
            'price': 499, # Setting a nominal price
            'estimated_hours': 40,
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
            "title": "Programming Foundations",
            "description": "Understand how a computer thinks and executes instructions.",
            "is_free": True,
            "topics": [
                "What programming actually means",
                "How a computer executes instructions step by step",
                "Variables and data types (real-life analogy)",
                "Input and output concepts",
                "Conditional thinking (if–else logic)",
                "Looping concept (repetition logic)",
                "Writing first logic-based programs"
            ]
        },
        {
            "title": "Logical Thinking & Flow",
            "description": "Learn how to convert thoughts into logical steps.",
            "is_free": False,
            "topics": [
                "Problem understanding before coding",
                "Breaking problems into smaller steps",
                "Flowcharts and decision making",
                "Pseudocode writing",
                "Common beginner logic mistakes"
            ]
        },
        {
            "title": "Structured Programming Concepts",
            "description": "Write clean, readable, and reusable logic.",
            "is_free": False,
            "topics": [
                "Functions and modular thinking",
                "Code reusability concepts",
                "Importance of naming and readability",
                "Avoiding duplicate logic",
                "Introduction to debugging mindset"
            ]
        },
        {
            "title": "Programming Mindset & Efficiency",
            "description": "Understand performance and problem-solving depth.",
            "is_free": False,
            "topics": [
                "How programs scale with input size",
                "Basic intuition of time complexity (no math)",
                "Choosing the right logic approach",
                "Debugging strategies",
                "Thinking like a programmer, not a learner"
            ]
        },
        {
            "title": "Language Readiness & Next Steps",
            "description": "Transition to learning any programming language.",
            "is_free": False,
            "topics": [
                "How programming concepts remain same across languages",
                "Mapping fundamentals to Python / C / Java",
                "How to approach a new programming language",
                "Common mistakes while switching languages",
                "Preparing for real projects"
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
                'color': '#6366f1'
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
                    'duration_minutes': 15
                }
            )
            
    # Update Stats
    roadmap.update_stats()
    print("Roadmap creation complete!")

create_roadmap()
