from django.shortcuts import render
from .models import SiteSetting
from django.conf import settings

class MaintenanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Allow static files and media
        if request.path.startswith(settings.STATIC_URL) or request.path.startswith(settings.MEDIA_URL):
            return self.get_response(request)
            
        # Allow admin interface
        if request.path.startswith('/admin/'):
            return self.get_response(request)
            
        # Allow staff users
        if request.user.is_staff:
            return self.get_response(request)
            
        # Check maintenance mode
        try:
            site_setting = SiteSetting.objects.first()
            if site_setting and site_setting.maintenance_mode:
                return render(request, 'maintenance.html', {
                    'message': site_setting.maintenance_message
                }, status=503)
        except Exception:
            # If DB error or table doesn't exist yet (during migration), pass through
            pass
            
        return self.get_response(request)
