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

# Check Registry Loop to find the model
registered_admin = None
for model, admin_instance in admin.site._registry.items():
    if model.__name__ == 'UserRoadmapEnrollment':
        registered_admin = admin_instance
        break

if not registered_admin:
    print("❌ FAILURE: UserRoadmapEnrollment is NOT registered in Admin Site.")
    sys.exit(1)

print(f"Registered Admin Class: {type(registered_admin)}")
print(f"List Display (Runtime): {registered_admin.list_display}")

if 'amount_paid' in registered_admin.list_display:
    print("✅ SUCCESS: 'amount_paid' is present in the ACTIVE Admin Registry.")
    print("If you still don't see it, it is 100% a GUNICORN RESTART issue.")
else:
    print("❌ FAILURE: 'amount_paid' is MISSING from the ACTIVE Admin Registry.")
    print("This means Django loaded an old version of the class.")
