
import os
import django
import sys

sys.path.append('/Users/saitejakaki/Divakar/devaproject')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

try:
    from core.views import roadmap_detail_view
    print("✅ Successfully imported roadmap_detail_view. No SyntaxError or ImportError.")
    
    # Check if SubscriptionPlan is in the global scope of core.views (indirectly)
    import core.views
    if hasattr(core.views, 'SubscriptionPlan'):
        print("✅ SubscriptionPlan is available in core.views scope.")
    else:
        print("❌ SubscriptionPlan is NOT available in core.views scope.")

except Exception as e:
    print(f"❌ Error importing core.views: {e}")
