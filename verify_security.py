
import os
import sys

sys.path.append('/Users/saitejakaki/Divakar/devaproject')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')

import django
django.setup()

from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponseRedirect
from django.conf import settings
from core.views import roadmap_list_view, roadmap_detail_view
from core.models import Roadmap

def check_login_required(view_func, *args, **kwargs):
    factory = RequestFactory()
    request = factory.get('/', HTTP_HOST='localhost:8000')
    request.user = AnonymousUser()
    
    try:
        response = view_func(request, *args, **kwargs)
        if response.status_code == 302:
            if settings.LOGIN_URL in response.url:
                print(f"✅ {view_func.__name__}: Redirects to Login (302)")
                return True
            else:
                print(f"⚠️ {view_func.__name__}: Redirects to {response.url} (302)")
                return False
        else:
            print(f"❌ {view_func.__name__}: Returned {response.status_code} (Expected 302)")
            return False
    except Exception as e:
        print(f"❌ {view_func.__name__}: Error - {e}")
        return False

print("--- Verifying Security ---")

# 1. Roadmap List
check_login_required(roadmap_list_view)

# 2. Roadmap Detail (Need a slug)
try:
    roadmap = Roadmap.objects.first()
    if roadmap:
        check_login_required(roadmap_detail_view, slug=roadmap.slug)
    else:
        print("⚠️ No roadmaps found to test detail view.")
except Exception as e:
    print(f"❌ Error getting roadmap: {e}")

print("--- Verification Complete ---")
