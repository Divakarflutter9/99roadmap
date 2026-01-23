import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from payments.models import SubscriptionPlan

def create_plan():
    print("Creating Subscription Plans...")
    
    if SubscriptionPlan.objects.filter(name='Pro Monthly').exists():
        print("Plan already exists.")
        return

    SubscriptionPlan.objects.create(
        name='Pro Monthly',
        price=499,
        duration_type='monthly',
        duration_days=30,
        description='Perfect for dedicated learners.',
        features=[
            'Access to All Premium Roadmaps',
            'Unlimited AI Tutor Support',
            'Certificate of Completion',
            'Priority Support'
        ],
        is_popular=True
    )
    
    SubscriptionPlan.objects.create(
        name='Pro Yearly',
        price=4999,
        duration_type='yearly',
        duration_days=365,
        description='Best value for long-term learning.',
        features=[
            'Everything in Monthly',
            '2 Months Free',
            'Resume Review Service',
            'Offline Access (Coming Soon)'
        ],
        is_popular=False
    )
    
    print("Subscription Plans Created!")

if __name__ == "__main__":
    create_plan()
