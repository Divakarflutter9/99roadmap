import os
import django
import sys

sys.path.append('/Users/saitejakaki/Divakar/devaproject')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import Roadmap, RoadmapCategory

def check_roadmaps():
    print("Checking Roadmaps in Database...")
    roadmaps = Roadmap.objects.all()
    count = roadmaps.count()
    print(f"Total Roadmaps found: {count}")
    
    if count == 0:
        print("❌ No roadmaps found in the database!")
        return

    print("\nList of Roadmaps:")
    print(f"{'ID':<5} {'Title':<40} {'Active':<10} {'Category':<20} {'Slug'}")
    print("-" * 100)
    
    for r in roadmaps:
        category_name = r.category.name if r.category else "No Category"
        print(f"{r.id:<5} {r.title[:38]:<40} {str(r.is_active):<10} {category_name[:18]:<20} {r.slug}")
    
    print("\nChecking Categories:")
    for c in RoadmapCategory.objects.all():
        print(f"- {c.name} (slug: {c.slug})")

if __name__ == '__main__':
    check_roadmaps()
