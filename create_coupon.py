import os
import django
from django.utils import timezone
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from payments.models import Coupon

def create_coupon():
    print("Creating Test Coupon...")
    
    if Coupon.objects.filter(code='WELCOME50').exists():
        print("Coupon WELCOME50 already exists.")
        return

    Coupon.objects.create(
        code='WELCOME50',
        discount_percent=50,
        valid_from=timezone.now(),
        valid_to=timezone.now() + timedelta(days=365),
        active=True,
        usage_limit=100
    )
    
    print("Coupon WELCOME50 Created! (50% Off)")

if __name__ == "__main__":
    create_coupon()
