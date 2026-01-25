import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import Roadmap, Stage, Topic, RoadmapCategory

def create_roadmap():
    # 1. Create/Get Category (Reuse Computer Science)
    category, _ = RoadmapCategory.objects.get_or_create(
        name="Computer Science",
        defaults={'slug': 'computer-science', 'color': '#10b981', 'icon': 'fa-laptop-code'}
    )
    
    # 2. Create Roadmap
    title = "Problem Solving & Logical Thinking"
    slug = "problem-solving-logic"
    
    description = """
    A clear, step-by-step Problem Solving & Logical Thinking roadmap for BTech / CSE beginner students.

    This roadmap helps students think logically before coding, starting from absolute basics and moving to an advanced problem-solving mindset.

    **Focus:**
    *   Beginner-friendly, zero coding assumption
    *   Thinking process over syntax
    *   Simple, relatable examples
    *   Clear upgrade of thinking ability
    """
    
    roadmap, created = Roadmap.objects.get_or_create(
        slug=slug,
        defaults={
            'title': title,
            'description': description,
            'short_description': "Master the art of solving problems. Learn to break down complex issues, recognize patterns, and build efficient solutions.",
            'category': category,
            'difficulty': 'beginner',
            'is_premium': True,
            'price': 499,
            'estimated_hours': 30,
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
            "title": "Problem Understanding",
            "description": "Learn how to understand a problem clearly.",
            "is_free": True,
            "topics": [
                "Reading a problem correctly",
                "Identifying inputs and outputs",
                "Understanding constraints",
                "Common mistakes while reading questions",
                "Real-life problem examples"
            ]
        },
        {
            "title": "Logical Breakdown",
            "description": "Learn to convert problems into steps.",
            "is_free": False,
            "topics": [
                "Breaking problems into smaller parts",
                "Step-by-step thinking",
                "Flowchart-based logic",
                "Writing logic in simple words"
            ]
        },
        {
            "title": "Pattern Recognition",
            "description": "Start recognizing repeated logic patterns.",
            "is_free": False,
            "topics": [
                "Identifying similar problems",
                "Reusing logic ideas",
                "Common problem-solving patterns",
                "Avoiding overthinking"
            ]
        },
        {
            "title": "Solution Building",
            "description": "Build correct and efficient solutions.",
            "is_free": False,
            "topics": [
                "Trying multiple solution approaches",
                "Tracing logic manually",
                "Handling edge cases",
                "Debugging logic errors"
            ]
        },
        {
            "title": "Thinking Like a Problem Solver",
            "description": "Develop confidence and speed.",
            "is_free": False,
            "topics": [
                "Choosing the best approach",
                "Logical optimization (no math)",
                "Time-aware thinking",
                "Applying logic across subjects and languages"
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
                'color': '#8b5cf6' # Violet color for logic
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
