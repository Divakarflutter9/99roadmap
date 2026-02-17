
import os
import django
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from django.contrib.auth import get_user_model
from payments.models import UserSubscription

User = get_user_model()

print(f"Current Time: {timezone.now()}")
print("-" * 50)

for user in User.objects.all():
    print(f"User: {user.email} (ID: {user.id})")
    try:
        sub = user.subscription
        print(f"  Subscription: {sub.status}")
        print(f"  Plan: {sub.plan.name if sub.plan else 'None'}")
        if sub.plan:
            print(f"  Plan Duration Type: {sub.plan.duration_type}")
        print(f"  End Date: {sub.end_date}")
        print(f"  Is Active (Method): {sub.is_active()}")
    except UserSubscription.DoesNotExist:
        print("  Subscription: None")
    print("-" * 50)
