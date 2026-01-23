import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import Roadmap
from django.core.files.base import ContentFile
from reportlab.pdfgen import canvas
import io

def create_dummy_pdf():
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 100, "Hello world. This is a test PDF.")
    p.showPage()
    p.save()
    return buffer.getvalue()

roadmap = Roadmap.objects.first()
if roadmap:
    pdf_content = create_dummy_pdf()
    roadmap.pdf_file.save('test_roadmap.pdf', ContentFile(pdf_content), save=True)
    print(f"SUCCESS: Uploaded dummy PDF to roadmap '{roadmap.title}' (ID: {roadmap.id})")
else:
    print("ERROR: No roadmaps found.")
