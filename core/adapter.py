from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.core.files.base import ContentFile
import requests

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def populate_user(self, request, sociallogin, data):
        """
        Populate user instance from social account data
        """
        user = super().populate_user(request, sociallogin, data)
        
        # Google specific handling
        if sociallogin.account.provider == 'google':
            extra_data = sociallogin.account.extra_data
            
            # 1. Full Name
            if not user.full_name:
                user.full_name = extra_data.get('name', '')
                if not user.full_name:
                    first = extra_data.get('given_name', '')
                    last = extra_data.get('family_name', '')
                    user.full_name = f"{first} {last}".strip()
            
            # 2. Email Verified
            if extra_data.get('email_verified', False):
                user.is_verified = True
                
        return user

    def save_user(self, request, sociallogin, form=None):
        """
        Called when the user is saved. Good place for profile image
        """
        user = super().save_user(request, sociallogin, form)
        
        if sociallogin.account.provider == 'google':
            extra_data = sociallogin.account.extra_data
            picture_url = extra_data.get('picture')
            
            if picture_url and not user.profile_image:
                try:
                    response = requests.get(picture_url)
                    if response.status_code == 200:
                        filename = f"google_{user.id}.jpg"
                        user.profile_image.save(filename, ContentFile(response.content), save=True)
                except Exception as e:
                    print(f"Error saving profile image: {e}")
                    
        return user
