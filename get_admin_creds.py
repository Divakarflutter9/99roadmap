import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import User

admins = User.objects.filter(is_superuser=True)

if not admins.exists():
    print("No admin users found.")
else:
    print("Admin Users:")
    for admin in admins:
        print(f"Email: {admin.email}, Name: {admin.full_name}, Phone: {admin.phone}")
