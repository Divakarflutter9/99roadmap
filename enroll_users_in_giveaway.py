
import os
import django
import sys

# Setup Django Environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import User, UserRoadmapEnrollment, Giveaway, GiveawayParticipation

def enroll_users():
    # 1. Get the latest active giveaway
    giveaway = Giveaway.objects.filter(is_active=True).order_by('-created_at').first()
    
    if not giveaway:
        print("❌ No active giveaway found.")
        return

    print(f"🎯 Target Giveaway: {giveaway.title}")

    # 2. Get all users who are enrolled in at least one roadmap
    # We use distinct() to avoid duplicates if a user is enrolled in multiple roadmaps
    target_users = User.objects.filter(enrollments__isnull=False).distinct()
    
    print(f"👥 Found {target_users.count()} unique users with roadmap enrollments.")
    
    created_count = 0
    skipped_count = 0

    for user in target_users:
        # 3. Create Participation entry
        participation, created = GiveawayParticipation.objects.get_or_create(
            user=user,
            giveaway=giveaway,
            defaults={'status': 'INTERESTED'}
        )
        
        if created:
            created_count += 1
            # print(f"✅ Added {user.email}")
        else:
            skipped_count += 1
            # print(f"⚠️ Skipped {user.email} (Already registered)")

    print("-" * 30)
    print(f"🎉 Operation Complete!")
    print(f"✅ Successfully Added: {created_count}")
    print(f"⚠️ Skipped (Already in Giveaway): {skipped_count}")
    print(f"📊 Total Participants: {GiveawayParticipation.objects.filter(giveaway=giveaway).count()}")

if __name__ == '__main__':
    enroll_users()
