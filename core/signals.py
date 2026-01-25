from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from allauth.socialaccount.models import SocialAccount
from django.core.files.base import ContentFile
import requests
from io import BytesIO

@receiver(user_signed_up)
def populate_profile(request, user, **kwargs):
    """
    Populate user profile from social account data on signup
    """
    # Check if this is a social signup
    if 'sociallogin' in kwargs:
        sociallogin = kwargs['sociallogin']
        
        # Only proceed for Google for now (or make generic)
        if sociallogin.account.provider == 'google':
            data = sociallogin.account.extra_data
            print(f"DEBUG: Google Data: {data}")
            
            # 1. Full Name
            if not user.full_name:
                user.full_name = data.get('name', '')
                if not user.full_name:
                    # Fallback to first/last name
                    first = data.get('given_name', '')
                    last = data.get('family_name', '')
                    user.full_name = f"{first} {last}".strip()
            
            # 2. Profile Image
            picture_url = data.get('picture')
            if picture_url and not user.profile_image:
                try:
                    response = requests.get(picture_url)
                    if response.status_code == 200:
                        # Create a filename
                        filename = f"google_{user.id}.jpg"
                        user.profile_image.save(filename, ContentFile(response.content), save=False)
                except Exception as e:
                    print(f"Error saving profile image: {e}")
            
            # 3. Email Verification (Google emails are verified)
            if data.get('email_verified', False):
                user.is_verified = True
                
            user.save()
