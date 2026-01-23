import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import Roadmap
from django.contrib.auth import get_user_model

User = get_user_model()
roadmaps = Roadmap.objects.all()
print(f"Total Roadmaps: {roadmaps.count()}")

found_pdf = False
for r in roadmaps:
    if r.pdf_file:
        found_pdf = True
        print(f"Roadmap '{r.title}' (ID: {r.id}) has PDF: {r.pdf_file.name}")
    else:
        # print(f"Roadmap '{r.title}' (ID: {r.id}) has NO PDF")
        pass

if not found_pdf:
    print("NO ROADMAPS HAVE A PDF UPLOADED!")
else:
    print("Found at least one roadmap with PDF.")
