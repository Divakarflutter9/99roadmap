import os
import django
from django.template import Template, Context

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import Roadmap, Stage

try:
    roadmap = Roadmap.objects.get(slug='verilog-rtl-mastery')
    stage = Stage.objects.get(roadmap=roadmap, order=2)
    topics = stage.topics.all()
    
    print(f"--- Debugging Stage: {stage.title} ---")
    for t in topics:
        print(f"Topic '{t.title}':")
        print(f"  Repr: {repr(t.title)}")
    
    template_string = """
    {% for topic in topics %}
    T{{ topic.id }}("{{ topic.title|addslashes|safe }}")
    {% endfor %}
    """
    
    t = Template(template_string)
    c = Context({"topics": topics})
    rendered = t.render(c)
    
    print("\n--- Rendered Mermaid Output (HTML Source) ---")
    print(rendered)
    
except Exception as e:
    print(f"Error: {e}")
