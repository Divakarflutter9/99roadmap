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
    title = "Git & GitHub For Beginners"
    slug = "git-github-mastery"
    
    description = """
    A clear, step-by-step Git & GitHub learning roadmap for BTech / CSE beginner students.

    The roadmap helps students manage, track, and collaborate on code, starting from absolute basics and progressing to real-world usage.

    **Focus:**
    *   Beginner-friendly (no prior Git knowledge assumed)
    *   Concept-first, not command-dumping
    *   Focus on why and when to use Git features
    *   Practical, student-relevant examples
    """
    
    roadmap, created = Roadmap.objects.get_or_create(
        slug=slug,
        defaults={
            'title': title,
            'description': description,
            'short_description': "Master version control and collaboration. Learn to track changes, work with teams, and contribute to open source.",
            'category': category,
            'difficulty': 'beginner',
            'is_premium': True,
            'price': 499,
            'estimated_hours': 25,
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
            "title": "Version Control Foundations",
            "description": "Understand why version control exists.",
            "is_free": True,
            "topics": [
                "What problem Git actually solves",
                "Local code history concept",
                "Repository meaning",
                "Commit as a save point",
                "Basic Git workflow (edit → save → commit)"
            ]
        },
        {
            "title": "Core Git Usage",
            "description": "Confidently use Git for personal projects.",
            "is_free": False,
            "topics": [
                "Initializing a repository",
                "Tracking file changes",
                "Understanding commit history",
                "Undoing mistakes safely",
                "Ignoring unnecessary files"
            ]
        },
        {
            "title": "GitHub Basics",
            "description": "Publish and manage projects online.",
            "is_free": False,
            "topics": [
                "What GitHub is and how it works with Git",
                "Creating repositories on GitHub",
                "Pushing local code to GitHub",
                "Pulling updates",
                "README basics"
            ]
        },
        {
            "title": "Collaboration & Team Workflows",
            "description": "Work safely with others.",
            "is_free": False,
            "topics": [
                "Branching concept",
                "Merging changes",
                "Resolving conflicts (conceptual)",
                "Pull requests workflow",
                "Code review basics"
            ]
        },
        {
            "title": "Real-World & Open-Source Practices",
            "description": "Follow industry-standard workflows.",
            "is_free": False,
            "topics": [
                "GitHub issues & project boards",
                "Open-source contribution flow",
                "Commit message best practices",
                "Repository hygiene",
                "Common Git mistakes students make"
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
                'color': '#f0562e' # Git orange color
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
