import os
import django
import sys

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import UserRoadmapEnrollment
from core.admin import UserRoadmapEnrollmentAdmin
from django.contrib.admin.sites import AdminSite

class MockUserRoadmapEnrollmentAdmin(UserRoadmapEnrollmentAdmin):
    """Mock to test methods without full registration"""
    def __init__(self):
        pass # Skip super init

print("--- TESTING RUNTIME EXECUTION ---")

# 1. Get an enrollment
enrollment = UserRoadmapEnrollment.objects.first()
if not enrollment:
    print("⚠️ No enrollments found in DB to test. Skipping runtime check.")
    sys.exit(0)

print(f"Testing with enrollment: {enrollment}")

# 2. Test the methods manually
admin_instance = MockUserRoadmapEnrollmentAdmin()

try:
    print("Attempting to run 'amount_paid'...")
    # We pass 'admin_instance' as self, and 'enrollment' as obj
    paid = UserRoadmapEnrollmentAdmin.amount_paid(admin_instance, enrollment)
    print(f"✅ amount_paid Result: {paid}")
except Exception as e:
    print(f"❌ CRASH in amount_paid: {e}")
    import traceback
    traceback.print_exc()

try:
    print("Attempting to run 'coupon_used'...")
    coupon = UserRoadmapEnrollmentAdmin.coupon_used(admin_instance, enrollment)
    print(f"✅ coupon_used Result: {coupon}")
except Exception as e:
    print(f"❌ CRASH in coupon_used: {e}")
    import traceback
    traceback.print_exc()

print("--- TEST COMPLETE ---")
