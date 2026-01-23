"""
Script to add Control Systems Learning Roadmap to the database (CORRECTED VERSION)
Run this script: python manage.py shell < import_control_systems_roadmap.py
"""

from core.models import Roadmap, Stage, Topic, RoadmapCategory
from django.utils.text import slugify

# Get or create category
category, _ = RoadmapCategory.objects.get_or_create(
    name="Engineering",
    defaults={'slug': 'engineering', 'description': 'Engineering and technical courses'}
)

# Create the Roadmap with correct fields
roadmap = Roadmap.objects.create(
    title="Control Systems Learning",
    slug=slugify("Control Systems Learning"),
    description="Master control systems from basic concepts to advanced applications. Learn through real-world examples - from ceiling fans to robotics. Beginner-friendly, concept-first approach with practical focus. Perfect for engineering students and professionals looking to understand control theory and its applications in robotics, automation, and embedded systems.",
    short_description="Master control systems from basics to advanced with real-world examples and practical focus.",
    category=category,
    difficulty='beginner',  # Starts at beginner level
    is_premium=True,  # Will update based on stages
    estimated_hours=80,  # Approximately 12 weeks × 6-7 hours/week
    is_active=True,
    is_featured=False
)

print(f"✅ Created Roadmap: {roadmap.title}")

# ==================== STAGE 1: Foundations (FREE) ====================
stage1 = Stage.objects.create(
    roadmap=roadmap,
    title="Foundations",
    description="Understand what a system is and why control is needed. Learn through daily-life examples.",
    order=1,
    is_free=True  # First stage FREE
)

# Stage 1 Topics (6 topics)
topics_stage1 = [
    {
        "title": "What is a system",
        "content": """# What is a System

## Simple Meaning
A system is anything that takes an input, processes it, and gives an output.

## Real-Life Examples
- **Ceiling Fan**: Input = Regulator position, Output = Fan speed
- **Air Conditioner**: Input = Temperature setting, Output = Cool air
- **Water Tank**: Input = Water supply, Output = Water level
- **DC Motor**: Input = Voltage, Output = Rotation speed

## Key Takeaway
Systems are everywhere around us! Understanding systems helps us control and improve them.""",
        "order": 1
    },
    {
        "title": "Why systems need control",
        "content": """# Why Systems Need Control

## Input and Output
- **Input**: What we give to the system (the command)
- **Output**: What we want from the system (the result)

### Example: Fan Control
- Input: Regulator position (1, 2, 3, 4, 5)
- Output: Fan speed (slow to fast)

## Why Control Matters
Without control:
- Fan might run too fast or too slow
- AC might make room too cold or not cold enough
- Motor might spin unpredictably

**With control, we get the exact output we want!**""",
        "order": 2
    },
    {
        "title": "Feedback concept",
        "content": """# Feedback Concept

## What is Feedback?
Feedback means **checking the output** and **adjusting the input** based on what we see.

## Example: Thermostat in AC
1. You set temperature to 24°C (desired output)
2. AC cools the room
3. Thermostat **checks actual temperature** (feedback)
4. If room is 26°C → AC works harder
5. If room is 23°C → AC reduces cooling  
6. Result: Room stays at exactly 24°C!

**Key Point**: Feedback = Self-correction""",
        "order": 3
    },
    {
        "title": "Open loop vs Closed loop systems",
        "content": """# Open Loop vs Closed Loop Systems

## Open Loop System
- **No feedback** - system doesn't check its output
- Works blindly based on input only

### Example: Washing Machine Timer
- You set 30 minutes, machine runs for exactly 30 minutes
- Doesn't check if clothes are actually clean

## Closed Loop System
- **Has feedback** - system continuously checks output
- Adjusts itself automatically

### Example: Car Cruise Control
- You set speed to 100 km/h
- Car checks actual speed continuously
- Adjusts throttle to maintain exact speed""",
        "order": 4
    },
    {
        "title": "Control system block diagram",
        "content": """# Control System Block Diagram

## Basic Structure
```
Input → [Controller] → [Plant/System] → Output
                ↑                         |
                |------ [Feedback] -------
```

## Components
- **Input**: What we want the system to do
- **Controller**: The "brain" that makes decisions
- **Plant**: The actual physical system
- **Output**: What the system produces
- **Feedback**: Measures output, sends info back

## Real Example: Driving a Car
- Input: Where you want to go
- Controller: You (the driver)
- Plant: Car
- Output: Where car actually goes
- Feedback: Your eyes seeing the road""",
        "order": 5
    },
    {
        "title": "Control systems around us",
        "content": """# Control Systems Around Us

## Everyday Examples

### 1. Lift/Elevator Control
- Input: Button press (floor number)
- Control: Lift motor speed and direction
- Feedback: Position sensors
- Result: Smooth stop at exact floor

### 2. Mobile Phone Brightness
- Input: Ambient light setting
- Control: Screen brightness level
- Feedback: Light sensor  
- Result: Screen always readable

### 3. Traffic Signal Timing
- Input: Time-of-day, traffic density
- Control: Signal duration
- Feedback: Vehicle sensors
- Result: Optimized traffic flow

**Progress:** You can now see control systems everywhere! ✅""",
        "order": 6
    }
]

for topic_data in topics_stage1:
    Topic.objects.create(
        stage=stage1,
        title=topic_data["title"],
        content=topic_data["content"],
        order=topic_data["order"]
    )
    print(f"  ✅ Added topic: {topic_data['title']}")

# Update roadmap stats
roadmap.update_stats()

print(f"\n🎉 Successfully created Control Systems Learning Roadmap!")
print(f"📊 Stage 1 (Foundations): 6 topics - FREE")
print(f"\nℹ️  To add remaining stages (2-5), run the other import scripts.")
print(f"✨ Roadmap is now visible at /roadmaps/ !")
