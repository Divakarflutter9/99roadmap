import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from django.contrib.sites.models import Site

def fix_site():
    print("Fixing Site ID configuration...")
    
    # Check what sites exist
    sites = Site.objects.all()
    print(f"Current sites in DB: {[s for s in sites]}")
    
    # 1. Ensure Site(id=1) exists and is correct
    try:
        site = Site.objects.get(id=1)
        print("Site ID 1 exists. Updating...")
        site.domain = '99roadmap.droptechie.com'
        site.name = '99Roadmap'
        site.save()
        print("Updated Site ID 1.")
    except Site.DoesNotExist:
        print("Site ID 1 does NOT exist. Checking if we can rename another one or create new.")
        # If there's only one site and it's not ID 1, we might need to be careful if other foreign keys point to it.
        # But for a fresh deploy, we usually want ID 1.
        
        # If an existing site (like example.com) exists with another ID, we can force its ID to 1?
        # Only if no FK constraints block it.
        
        existing_site = Site.objects.first()
        if existing_site:
            print(f"Found existing site: {existing_site.id} - {existing_site.domain}")
            # Try to delete and recreate ID 1? Or update?
            # Creating ID 1 explicitly
            print("Creating Site ID 1...")
            Site.objects.create(id=1, domain='99roadmap.droptechie.com', name='99Roadmap')
        else:
            print("No sites found. Creating Site ID 1...")
            Site.objects.create(id=1, domain='99roadmap.droptechie.com', name='99Roadmap')
            
    print("Site configuration fixed.")
    print(f"Current Site: {Site.objects.get(id=1).domain}")

if __name__ == '__main__':
    fix_site()
