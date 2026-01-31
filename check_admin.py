import os
import django
import sys

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from django.contrib import admin
from core.models import UserRoadmapEnrollment
from core.admin import UserRoadmapEnrollmentAdmin

print("--- DEBUGGING ADMIN CONFIGURATION ---")
print(f"Admin Class: {UserRoadmapEnrollmentAdmin}")
print(f"List Display: {UserRoadmapEnrollmentAdmin.list_display}")

if 'amount_paid' in UserRoadmapEnrollmentAdmin.list_display:
    print("✅ SUCCESS: 'amount_paid' is present in list_display.")
else:
    print("❌ FAILURE: 'amount_paid' is MISSING from list_display.")
    print("REASON: The server is running OLD CODE.")
    print("SOLUTION: You must run 'git pull' and restart Gunicorn.")
