"""
Script to fix duplicate phone numbers before applying unique constraint
"""

from core.models import User
from django.db.models import Count

def fix_duplicate_phones():
    """Clear phone numbers for duplicate entries, keeping only the first one"""
    
    # Find all phone numbers that appear more than once
    duplicates = User.objects.values('phone').annotate(
        count=Count('id')
    ).filter(count__gt=1, phone__isnull=False).exclude(phone='')
    
    print(f"Found {duplicates.count()} phone numbers with duplicates")
    
    for dup in duplicates:
        phone = dup['phone']
        users = User.objects.filter(phone=phone).order_by('date_joined')
        
        print(f"\nPhone {phone} has {users.count()} users:")
        
        # Keep the first user's phone, clear the rest
        for i, user in enumerate(users):
            if i == 0:
                print(f"  ✓ Keeping: {user.email} (joined {user.date_joined})")
            else:
                print(f"  ✗ Clearing: {user.email} (joined {user.date_joined})")
                user.phone = ''
                user.save()
    
    print("\n✅ Done! Duplicate phone numbers have been cleared.")
    print("   Users can update their phone numbers in their profile settings.")

if __name__ == '__main__':
    fix_duplicate_phones()
