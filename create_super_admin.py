import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import User

email = 'admin@gmail.com'
password = 'admin123'
phone = None

if User.objects.filter(email=email).exists():
    print(f"User {email} already exists. Updating password...")
    user = User.objects.get(email=email)
    user.set_password(password)
    user.is_staff = True
    user.is_superuser = True
    user.save()
    print(f"Updated {email} to Superuser with password: {password}")
else:
    print(f"Creating new superuser {email}...")
    User.objects.create_superuser(
        email=email,
        password=password,
        full_name='Admin User',
        phone=phone
    )
    print(f"Created Superuser: {email} / {password}")
