import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import Roadmap, Stage

try:
    roadmap = Roadmap.objects.get(slug='verilog-rtl-mastery')
    # Stage 2 (order 2)
    stage = Stage.objects.get(roadmap=roadmap, order=2)
    
    print(f"Stage: {stage.title}")
    topics = stage.topics.all()
    print(f"Topic Count: {topics.count()}")
    
    for t in topics:
        print(f"ID: {t.id} | Title: {t.title}")
        
except Exception as e:
    print(f"Error: {e}")
