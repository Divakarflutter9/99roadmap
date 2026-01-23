import os
import django
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import Roadmap, RoadmapBundle

def create_bundle_data():
    print("Setting up Bundles and Premium Roadmaps...")
    
    # 1. Update existing roadmaps
    try:
        py_roadmap = Roadmap.objects.get(title__icontains='Python')
        py_roadmap.is_premium = True
        py_roadmap.price = 299
        py_roadmap.save()
        print(f"Updated {py_roadmap.title}: Premium, Price 299")
    except Roadmap.DoesNotExist:
        print("Python Roadmap not found (Skipping)")
        py_roadmap = None

    try:
        web_roadmap = Roadmap.objects.get(title__icontains='Web')
        web_roadmap.is_premium = True
        web_roadmap.price = 399
        web_roadmap.save()
        print(f"Updated {web_roadmap.title}: Premium, Price 399")
    except Roadmap.DoesNotExist:
        print("Web Dev Roadmap not found (Skipping)")
        web_roadmap = None

    # 2. Create Bundle
    if py_roadmap and web_roadmap:
        bundle, created = RoadmapBundle.objects.get_or_create(
            title='Full Stack Python Bundle',
            defaults={
                'description': 'Master both Python and Web Development with this complete package.',
                'price': 499, # Discounted price
                'slug': 'full-stack-python-bundle'
            }
        )
        if created:
            bundle.roadmaps.add(py_roadmap, web_roadmap)
            print("Created Full Stack Python Bundle (Price 499)")
        else:
            print("Bundle already exists")

    print("Data setup complete!")

if __name__ == "__main__":
    create_bundle_data()
