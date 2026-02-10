
import os
import django
import sys

# Add project root to sys.path
sys.path.append('/Users/saitejakaki/Divakar/devaproject')

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import Roadmap, RoadmapCategory

def organize_categories():
    print("🚀 Starting Roadmap Category Reorganization...")

    # 1. Define Target Categories with Slugs and Names
    target_categories = {
        'frontend-development': 'Frontend Development',
        'backend-development': 'Backend Development',
        'cs-engineering': 'Computer Science & Engineering',
        'electronics-embedded': 'Electronics & Embedded Systems'
    }

    # Cache created category objects
    category_objs = {}
    for slug, name in target_categories.items():
        cat, created = RoadmapCategory.objects.get_or_create(slug=slug, defaults={'name': name})
        if created:
            print(f"✅ Created new category: {name} ({slug})")
        else:
            # Ensure name matches our standard
            if cat.name != name:
                cat.name = name
                cat.save()
                print(f"🔄 Updated category name: {name} ({slug})")
        category_objs[slug] = cat

    # 2. Define Roadmap Mapping (Slug -> Target Category Slug)
    # Using partial matching or explicit lists
    
    mapping = {
        # Frontend
        'html-professional-mastery': 'frontend-development',
        'css-professional-mastery': 'frontend-development',
        'javascript-core-mastery': 'frontend-development',
        'react-advanced': 'frontend-development',
        'frontend-basics': 'frontend-development',
        'web-performance-mastery': 'frontend-development',
        'web-development': 'frontend-development',

        # Backend
        'python-backend-career': 'backend-development',
        'java-backend-career': 'backend-development',
        'industry-sql-database': 'backend-development',
        'nodejs-backend-development': 'backend-development',
        'python-backend-development': 'backend-development',
        'java-backend-development': 'backend-development',
        'python-backend-mastery': 'backend-development',
        'java-backend-mastery': 'backend-development',
        'rest-api-mastery': 'backend-development',
        
        # CS & Engineering
        'industry-oop-concepts': 'cs-engineering',
        'dsa-through-c': 'cs-engineering',
        'c-programming-mastery': 'cs-engineering',
        'git-github-mastery': 'cs-engineering',
        'problem-solving-logic': 'cs-engineering',
        'programming-fundamentals': 'cs-engineering',
        'test-map': 'cs-engineering',
        'sdf': 'cs-engineering',

        # Electronics
        'embedded-systems-specialist': 'electronics-embedded',
        'c-for-embedded-systems': 'electronics-embedded',
        'vlsi-front-end': 'electronics-embedded',
        'control-systems-learning': 'electronics-embedded',
    }

    print("\n📦 Moving Roadmaps...")
    
    roadmaps = Roadmap.objects.all()
    moved_count = 0
    
    for roadmap in roadmaps:
        target_slug = mapping.get(roadmap.slug)
        
        # If no explicit match, try to guess or leave it (but we want to compress everything)
        # Check title keywords if not in mapping
        if not target_slug:
            title_lower = roadmap.title.lower()
            if 'python' in title_lower or 'java' in title_lower or 'backend' in title_lower or 'sql' in title_lower:
                target_slug = 'backend-development'
            elif 'react' in title_lower or 'frontend' in title_lower or 'html' in title_lower or 'css' in title_lower or 'web' in title_lower:
                target_slug = 'frontend-development'
            elif 'embedded' in title_lower or 'electronics' in title_lower or 'vlsi' in title_lower:
                target_slug = 'electronics-embedded'
            else:
                target_slug = 'cs-engineering' # Default bucket for generic CS stuff
        
        target_cat = category_objs[target_slug]
        
        if roadmap.category != target_cat:
            old_cat_name = roadmap.category.name if roadmap.category else "None"
            roadmap.category = target_cat
            roadmap.save()
            print(f"   Refiled '{roadmap.title}' from '{old_cat_name}' -> '{target_cat.name}'")
            moved_count += 1
    
    print(f"✅ Moved {moved_count} roadmaps.")

    # 3. Cleanup: Delete empty categories
    print("\n🧹 Cleaning up empty categories...")
    all_categories = RoadmapCategory.objects.all()
    deleted_count = 0
    
    for cat in all_categories:
        # Don't delete our 4 main targets
        if cat.slug in target_categories:
            continue
            
        if cat.roadmaps.count() == 0:
            print(f"   ❌ Deleting empty category: {cat.name} ({cat.slug})")
            cat.delete()
            deleted_count += 1
        else:
            print(f"   ⚠️  Category '{cat.name}' still has {cat.roadmaps.count()} roadmaps. Skipping.")
            
    print(f"✅ Deleted {deleted_count} empty categories.")
    print("\n🎉 Reorganization Complete.")

if __name__ == '__main__':
    organize_categories()
