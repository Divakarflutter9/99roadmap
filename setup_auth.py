import os
import django
import sys

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp

def setup_auth():
    print("=== 99Roadmap Auth Setup ===")
    
    # 1. Check for Credentials
    client_id = os.getenv('GOOGLE_CLIENT_ID')
    secret = os.getenv('GOOGLE_CLIENT_SECRET')
    
    if not client_id or not secret:
        print("\nERROR: Missing Google credentials in .env")
        print("Please add the following lines to your .env file:")
        print('GOOGLE_CLIENT_ID="your_client_id_here"')
        print('GOOGLE_CLIENT_SECRET="your_client_secret_here"')
        print("\nThen run this script again.")
        sys.exit(1)

    print("\n1. Configuring Site...")
    # Ensure Site(id=1) exists and is correct
    site, created = Site.objects.get_or_create(id=1)
    site.domain = '99roadmap.droptechie.com'
    site.name = '99Roadmap'
    site.save()
    print(f"   Success: Site configured as {site.domain}")

    print("\n2. Configuring Google Login...")
    app, created = SocialApp.objects.get_or_create(
        provider='google',
        defaults={
            'name': 'Google',
            'client_id': client_id,
            'secret': secret,
        }
    )
    
    if not created:
        app.client_id = client_id
        app.secret = secret
        app.save()
        print("   Success: Updated existing Google app.")
    else:
        print("   Success: Created new Google app.")

    # Link app to site
    app.sites.add(site)
    print("   Success: Linked Google app to Site.")
    
    print("\n=== Setup Complete! Restart Gunicorn now. ===")

if __name__ == '__main__':
    setup_auth()
