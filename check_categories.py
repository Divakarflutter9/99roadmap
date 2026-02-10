
import os
import django
import sys

sys.path.append('/Users/saitejakaki/Divakar/devaproject')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import RoadmapCategory

categories = RoadmapCategory.objects.all()
for cat in categories:
    print(f"Slug: {cat.slug}, Name: {cat.name}")
