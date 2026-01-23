"""
Script to add Stages 2, 3, 4, 5 to Control Systems Learning Roadmap
Run this script: python manage.py shell < import_control_systems_part2.py
"""

from core.models import Roadmap, Stage, Topic

# Get the existing roadmap
try:
    roadmap = Roadmap.objects.get(title="Control Systems Learning")
    print(f"✅ Found Roadmap: {roadmap.title}")
except Roadmap.DoesNotExist:
    print("❌ Roadmap not found! Please run import_control_systems_roadmap.py first.")
    exit()

# ==================== STAGE 2: Mathematical Modeling ====================
stage2, created = Stage.objects.get_or_create(
    roadmap=roadmap,
    title="Mathematical Modeling",
    defaults={
        "description": "Convert real physical systems into simple mathematical form. Understand behavior, not just equations.",
        "order": 2,
        "is_free": False
    }
)
if not created:
    print(f"ℹ️  Stage 2 already exists, adding missing topics...")

topics_stage2 = [
    {
        "title": "Why modeling is needed",
        "content": """# Why Modeling is Needed

## The Journey
Real System → Math Model → Analysis → Improvement

## Not About Accuracy
Mathematical modeling is NOT about creating perfect equations.

**It's about understanding HOW the system behaves.**

## Why Create Models?

### 1. Predict Behavior
- How will motor speed change if we increase voltage?
- Will the system be stable or unstable?

### 2. Design Before Building
- Test different designs on paper causing zero cost
- Avoid building bad designs

**Key Mindset**: A simple model that explains behavior is better than a complex one that confuses.""",
        "order": 1
    },
    {
        "title": "Modeling of electrical systems",
        "content": """# Modeling of Electrical Systems

## R, L, C Circuits as Systems

### Components
- **Resistor (R)**: Resists current (like friction)
- **Inductor (L)**: Opposes change in current (inertia)
- **Capacitor (C)**: Opposes change in voltage (spring)

## Voltage In → Current Out Concept

### RC Circuit Example
- Apply voltage suddenly
- Capacitor charges gradually (exponentially)
- **Current decreases over time**

**Focus**: We need to understand the pattern of change (exponential rise/decay), not just derivation.""",
        "order": 2
    },
    {
        "title": "Modeling of mechanical systems",
        "content": """# Modeling of Mechanical Systems

## Mass–Spring–Damper System

### Three Components
1. **Mass (M)**: Inertia (resists acceleration)
2. **Spring (K)**: Elasticity (stores energy)
3. **Damper (B)**: Friction (dissipates energy)

## Force In → Motion Out

### Example: Car Suspension
1. Hit a bump (Force Input)
2. Spring compresses
3. Damper reduces oscillation
4. Car settles smoothly

**Analogy**:
- Force = Voltage
- Velocity = Current
- Mass = Inductance
- Spring = Capacitance
- Damper = Resistance""",
        "order": 3
    },
    {
        "title": "Differential equations basics",
        "content": """# Differential Equations Basics

## Dynamic Systems
A differential equation describes **how something changes with time**.

### Meaning of Order
- **First Order**: One energy storage (e.g., RC circuit). Smooth response.
- **Second Order**: Two energy storages (e.g., Mass-Spring). Can oscillate.

**Don't Fear Math**: Computers solve the equations. We just need to understand what "Order" means for system behavior.""",
        "order": 4
    },
    {
        "title": "Transfer function concept",
        "content": """# Transfer Function Concept

## The Idea
Transfer Function = Output / Input (in s-domain)

It effectively tells you **how the system transforms any input into output**.

## Poles and Zeros (Simple View)
- **Poles**: Natural frequencies (resonance)
- **Zeros**: Frequencies that get blocked

**Power**: One simple equation (like `1/(s+1)`) describes the entire system's behavior for ANY input!""",
        "order": 5
    },
    {
        "title": "Block diagram algebra",
        "content": """# Block Diagram Algebra

## Visual Simplification

Block diagrams let you **see** system structure without intense math.

### Connections
1. **Series**: Multiply blocks (G1 × G2)
2. **Parallel**: Add blocks (G1 + G2)
3. **Feedback**: Loop formula (G / 1+GH)

**Usage**: Engineers use these to sketch complex systems and identify feedback loops quickly.""",
        "order": 6
    },
    {
        "title": "Signal flow graph basics",
        "content": """# Signal Flow Graph Basics

## Road Maps for Signals
Like block diagrams but cleaner for very complex systems with multiple overlapping loops.

### Mason's Gain Formula
A systematic "recipe" to find the total transfer function by tracing paths and loops.

**When to use**: For complex multi-loop systems where block diagram reduction gets messy.""",
        "order": 7
    }
]

for topic_data in topics_stage2:
    Topic.objects.get_or_create(
        stage=stage2,
        title=topic_data["title"],
        defaults={
            "content": topic_data["content"],
            "order": topic_data["order"]
        }
    )
    print(f"  ✅ Added topic: {topic_data['title']}")


# ==================== STAGE 3: Time Domain Analysis ====================
stage3, created = Stage.objects.get_or_create(
    roadmap=roadmap,
    title="Time Domain Analysis",
    defaults={
        "description": "Understand how systems behave with time. Predict real-life system responses.",
        "order": 3,
        "is_free": False
    }
)
if not created:
    print(f"ℹ️  Stage 3 already exists, adding missing topics...")

topics_stage3 = [
    {
        "title": "Standard test signals",
        "content": """# Standard Test Signals

## Three Main Signals
1. **Step Input**: Sudden change (Switch ON). Tests basic response.
2. **Ramp Input**: Constant increase (Gas pedal). Tests tracking.
3. **Impulse Input**: Sudden shock (Hammer hit). Tests natural behavior.

**Insight**: If we obtain the Step Response, we can predict the response to any other signal!""",
        "order": 1
    },
    {
        "title": "Time response characteristics",
        "content": """# Time Response Characteristics

## Transient vs Steady State
- **Transient**: Temporary behavior right after input (overshoot, oscillation).
- **Steady State**: Final behavior (constant value).

**Goal**: Fast transient response with minimal overshoot, and accurate steady state.""",
        "order": 2
    },
    {
        "title": "First order systems",
        "content": """# First Order Systems

## Behavior
- **Exponential Rise**: Starts fast, slows down.
- **No Overshoot**: Smoothly approaches target.
- **Time Constant (τ)**: Time to reach 63% of final value.

**Examples**: Room heating, RC circuit.""",
        "order": 3
    },
    {
        "title": "Second order systems",
        "content": """# Second Order Systems

## Behavior
Can oscillate because energy swaps between two storage elements (like Mass & Spring).

### Three Types
1. **Underdamped**: Overshoots and oscillates (Bouncy).
2. **Critically Damped**: Fastest rise with NO overshoot (Ideal).
3. **Overdamped**: Slow and sluggish (Heavy).

**Trade-off**: Speed vs Smoothness.""",
        "order": 4
    },
    {
        "title": "Stability interpretation",
        "content": """# Stability Interpretation

## Simple Definitions
- **Stable**: Returns to equilibrium after disturbance (Ball in bowl).
- **Unstable**: Runs away or explodes (Ball on hill).
- **Marginally Stable**: Oscillates forever (Pendulum in vacuum).

**Rule**: Stability is the #1 requirement. An unstable system is dangerous and useless.""",
        "order": 5
    },
    {
        "title": "Overshoot, rise time, settling time",
        "content": """# Performance Metrics

## Definitions
1. **Rise Time**: How fast it gets to target (Speed).
2. **Overshoot**: How much it goes past target (Bounciness).
3. **Settling Time**: How long until it stops moving (Total time).

**Constraint**: You can't have it all. Fast rise usually means more overshoot!""",
        "order": 6
    }
]

for topic_data in topics_stage3:
    Topic.objects.get_or_create(
        stage=stage3,
        title=topic_data["title"],
        defaults={
            "content": topic_data["content"],
            "order": topic_data["order"]
        }
    )
    print(f"  ✅ Added topic: {topic_data['title']}")


# ==================== STAGE 4: Frequency Domain Analysis ====================
stage4, created = Stage.objects.get_or_create(
    roadmap=roadmap,
    title="Frequency Domain Analysis",
    defaults={
        "description": "Analyze system behavior using frequency. Judge robustness and filters.",
        "order": 4,
        "is_free": False
    }
)
if not created:
    print(f"ℹ️  Stage 4 already exists, adding missing topics...")

topics_stage4 = [
    {
        "title": "Why frequency analysis is needed",
        "content": """# Why Frequency Analysis?

## Seeing Vibrations and Noise
Time domain shows *when* things happen. Frequency domain shows *how fast* things happen (oscillations).

**Usage**:
- Design filters to block noise (high freq).
- Avoid resonance (system shaking itself apart).
- Analyze stability margins easily.""",
        "order": 1
    },
    {
        "title": "Frequency response concept",
        "content": """# Frequency Response Concept

## How System Reacts to Frequencies
- **Low Freq**: System follows input well (Gain ≈ 1).
- **High Freq**: System can't keep up (Gain decreases).

**Bandwidth**: The range of frequencies a system can follow accurately. Higher bandwidth = Faster system.""",
        "order": 2
    },
    {
        "title": "Bode plots",
        "content": """# Bode Plots

## The Engineer's X-Ray
Two graphs that describe the system completely:
1. **Magnitude Plot**: Amplification vs Frequency.
2. **Phase Plot**: Delay vs Frequency.

**Slope**: Tells you the system order (-20dB/dec = 1st order, -40dB/dec = 2nd order).""",
        "order": 3
    },
    {
        "title": "Nyquist plot",
        "content": """# Nyquist Plot

## Stability Radar
Plots the loop response on a complex plane.

### The Rule
- Avoid the point **(-1, 0)**.
- If the curve encircles (-1, 0), the system is **Unstable**.
- Distance from (-1, 0) tells you how stable (robust) the system is.""",
        "order": 4
    },
    {
        "title": "Gain margin & phase margin",
        "content": """# Gain & Phase Margin

## Safety Buffers
- **Gain Margin**: How much gain we can add before instability.
- **Phase Margin**: How much delay we can tolerate before instability.

**Design Goal**: We want healthy margins so the system works even if components age or conditions change.""",
        "order": 5
    }
]

for topic_data in topics_stage4:
    Topic.objects.get_or_create(
        stage=stage4,
        title=topic_data["title"],
        defaults={
            "content": topic_data["content"],
            "order": topic_data["order"]
        }
    )
    print(f"  ✅ Added topic: {topic_data['title']}")


# ==================== STAGE 5: Controllers & Applications ====================
stage5, created = Stage.objects.get_or_create(
    roadmap=roadmap,
    title="Controllers & Applications",
    defaults={
        "description": "Connect theory to reality. PID controllers, robotics, and automation.",
        "order": 5,
        "is_free": False
    }
)
if not created:
    print(f"ℹ️  Stage 5 already exists, adding missing topics...")

topics_stage5 = [
    {
        "title": "PID controller concept",
        "content": """# PID Controller

## The Universal Solution
- **P (Proportional)**: Reacts to current error. "Push harder if far away."
- **I (Integral)**: Reacts to past error accumulation. "Fix the tiny remaining gap."
- **D (Derivative)**: Reacts to rate of change. "Slow down, we're approaching fast!"

**Together**: Fast, accurate, and stable control.""",
        "order": 1
    },
    {
        "title": "Tuning basics",
        "content": """# PID Tuning

## Finding the Sweet Spot
Adjusting Kp, Ki, and Kd gains.

1. Increase **P** until it responds fast (but oscillates).
2. Add **D** to stop the oscillation (smooth it out).
3. Add **I** to remove the final small error.

**Art vs Science**: Real tuning often involves "feeling" the system response.""",
        "order": 2
    },
    {
        "title": "Control systems in robotics",
        "content": """# Control in Robotics

## Applications
- **Speed Control**: Maintain wheel speed uphill/downhill.
- **Position Control**: Move robot arm to exact XYZ coordinates.
- **Balance**: Keep Segway/Drone upright (Inverted Pendulum).

**Robots are basically multiple control loops working together!**""",
        "order": 3
    },
    {
        "title": "Control in automation & industries",
        "content": """# Industrial Automation

## Process Control
- **Temperature**: Ovens, chemical reactors.
- **Flow/Level**: Water treatment, oil pipelines.
- **Pressure**: Boilers, hydraulics.

**PLC (Programmable Logic Controller)**: The industrial computer that runs these PID loops 24/7.""",
        "order": 4
    },
    {
        "title": "Embedded & real-time control",
        "content": """# Embedded & Real-Time Control

## Microcontrollers
Implementing control logic on chips (Arduino, ESP32, STM32).

## The Loop
1. Read Sensors
2. Calculate Error
3. Compute PID Output
4. Write to Actuators (Motors/Heaters)
5. Repeat (1000 times per second!)

**Real-Time**: Completing this loop reliably within a strict time deadline.""",
        "order": 5
    }
]

for topic_data in topics_stage5:
    Topic.objects.get_or_create(
        stage=stage5,
        title=topic_data["title"],
        defaults={
            "content": topic_data["content"],
            "order": topic_data["order"]
        }
    )
    print(f"  ✅ Added topic: {topic_data['title']}")

# Update roadmap stats
roadmap.update_stats()

print(f"\n🎉 Successfully added all remaining stages (2-5)!")
print(f"📊 Roadmap '{roadmap.title}' is now complete with 5 stages.")
