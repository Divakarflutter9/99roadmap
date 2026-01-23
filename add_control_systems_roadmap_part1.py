"""
Script to add Control Systems Learning Roadmap to the database
Run this script: python manage.py shell < add_control_systems_roadmap.py
"""

from core.models import Roadmap, Stage, Topic

# Create the Roadmap
roadmap = Roadmap.objects.create(
    title="Control Systems Learning",
    description="Master control systems from basic concepts to advanced applications. Learn through real-world examples - from ceiling fans to robotics. Beginner-friendly, concept-first approach with practical focus.",
    difficulty="Beginner",
    estimated_duration="12 weeks",
    is_free=False,
    created_by=None  # Set to admin user if needed
)

print(f"✅ Created Roadmap: {roadmap.title}")

# ==================== STAGE 1: Foundations ====================
stage1 = Stage.objects.create(
    roadmap=roadmap,
    title="Foundations",
    description="Understand what a system is and why control is needed. Learn through daily-life examples.",
    order=1,
    is_free=True
)

# Stage 1 Topics
topics_stage1 = [
    {
        "title": "What is a system",
        "content": """
# What is a System

## Simple Meaning
A system is anything that takes an input, processes it, and gives an output.

## Real-Life Examples
- **Ceiling Fan**: Input = Regulator position, Output = Fan speed
- **Air Conditioner**: Input = Temperature setting, Output = Cool air
- **Water Tank**: Input = Water supply, Output = Water level
- **DC Motor**: Input = Voltage, Output = Rotation speed

## Key Takeaway
Systems are everywhere around us! Understanding systems helps us control and improve them.
        """,
        "order": 1
    },
    {
        "title": "Why systems need control",
        "content": """
# Why Systems Need Control

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

**With control, we get the exact output we want!**
        """,
        "order": 2
    },
    {
        "title": "Feedback concept",
        "content": """
# Feedback Concept

## What is Feedback? (Simple Explanation)
Feedback means **checking the output** and **adjusting the input** based on what we see.

## Why Feedback Improves Accuracy

### Example: Thermostat in AC
1. You set temperature to 24°C (desired output)
2. AC cools the room
3. Thermostat **checks actual temperature** (feedback)
4. If room is 26°C → AC works harder
5. If room is 23°C → AC reduces cooling
6. Result: Room stays at exactly 24°C!

## Without Feedback
AC would just blow cold air continuously - room becomes too cold, wasting energy.

## With Feedback
AC adjusts automatically to maintain perfect temperature.

**Key Point**: Feedback = Self-correction
        """,
        "order": 3
    },
    {
        "title": "Open loop vs Closed loop systems",
        "content": """
# Open Loop vs Closed Loop Systems

## Open Loop System
- **No feedback** - system doesn't check its output
- Works blindly based on input only

### Example: Washing Machine Timer
- You set 30 minutes
- Machine runs for exactly 30 minutes
- Doesn't check if clothes are actually clean
- **Problem**: Might over-wash or under-wash

## Closed Loop System
- **Has feedback** - system continuously checks output
- Adjusts itself automatically

### Example: Car Cruise Control
- You set speed to 100 km/h
- Car checks actual speed continuously
- If speed drops (uphill) → increases throttle
- If speed increases (downhill) → reduces throttle
- **Result**: Maintains exact 100 km/h

## Comparison

| Feature | Open Loop | Closed Loop |
|---------|-----------|-------------|
| Feedback | ❌ No | ✅ Yes |
| Accuracy | Lower | Higher |
| Cost | Cheaper | More expensive |
| Complexity | Simple | Complex |
| Use When | Accuracy not critical | Accuracy essential |

## Where Open Loop Fails
- Traffic lights (fixed timing can't adapt to actual traffic)
- Electric kettle without auto-shutoff (can boil dry)
- Hand dryer (fixed time, may not dry completely)
        """,
        "order": 4
    },
    {
        "title": "Control system block diagram",
        "content": """
# Control System Block Diagram

## Basic Blocks

```
Input → [Controller] → [Plant/System] → Output
                ↑                         |
                |------ [Feedback] -------
```

## What Each Block Means

### 1. Input (Reference/Setpoint)
- What we **want** the system to do
- Example: Desired room temperature = 24°C

### 2. Controller
- The "brain" that makes decisions
- Compares what we want vs what we have
- Decides how to adjust

### 3. Plant/System
- The actual physical system we're controlling
- Example: AC unit, motor, robot arm

### 4. Output
- What the system **actually** produces
- Example: Actual room temperature = 25°C

### 5. Feedback
- Measures the output
- Sends information back to controller
- Example: Thermometer reading

## How Signal Flows
1. Set desired temperature (Input)
2. Controller compares with actual temperature
3. Sends signal to AC (Plant)
4. AC produces cooling
5. Thermometer measures room temp (Feedback)
6. Loop continues until desired temp is reached

## Real Example: Driving a Car
- Input: Where you want to go
- Controller: You (the driver)
- Plant: Car
- Output: Where car actually goes
- Feedback: Your eyes seeing the road
        """,
        "order": 5
    },
    {
        "title": "Control systems around us",
        "content": """
# Control Systems Around Us

You interact with control systems every single day!

## 1. Lift/Elevator Control
- **Input**: Button press (floor number)
- **Control**: Lift motor speed and direction
- **Feedback**: Position sensors
- **Result**: Smooth stop at exact floor

## 2. Traffic Signal Timing
- **Input**: Time-of-day, traffic density
- **Control**: Signal duration (red/green)
- **Feedback**: Vehicle sensors (advanced systems)
- **Result**: Optimized traffic flow

## 3. Mobile Phone Brightness Control
- **Input**: Ambient light setting
- **Control**: Screen brightness level
- **Feedback**: Light sensor
- **Result**: Screen always readable, saves battery

## 4. Washing Machine Cycles
- **Input**: Selected program (cotton, delicate)
- **Control**: Water level, spin speed, duration
- **Feedback**: Load sensors, water level sensors
- **Result**: Clothes washed perfectly

## 5. Refrigerator Temperature
- **Input**: Temperature dial setting
- **Control**: Compressor on/off
- **Feedback**: Internal thermometer
- **Result**: Food stays fresh

## 6. Automatic Doors
- **Input**: Presence detection
- **Control**: Door motor
- **Feedback**: Position sensors
- **Result**: Smooth opening/closing

## Progress Checkpoint 🎯
**"I can now see control systems everywhere!"**

You've completed the foundations. You now understand:
✅ What a system is
✅ Why control is needed
✅ How feedback works
✅ Difference between open and closed loop
✅ Real-world applications everywhere

**Ready for Stage 2: Mathematical Modeling!**
        """,
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

# ==================== STAGE 2: Mathematical Modeling ====================
stage2 = Stage.objects.create(
    roadmap=roadmap,
    title="Mathematical Modeling",
    description="Convert real physical systems into simple mathematical form. Understand behavior, not just equations.",
    order=2,
    is_free=False
)

topics_stage2 = [
    {
        "title": "Why modeling is needed",
        "content": """
# Why Modeling is Needed

## The Journey
Real System → Math Model → Analysis → Improvement

## Not About Accuracy
Mathematical modeling is NOT about creating perfect equations.

**It's about understanding HOW the system behaves.**

## Why Create Models?

### 1. Predict Behavior
- How will motor speed change if we increase voltage?
- Will the system be stable or unstable?
- How fast will it respond?

### 2. Design Before Building
- Test different designs on paper
- Save time and money
- Avoid building bad designs

### 3. Understand Relationships
- How does input affect output?
- What parameters matter most?
- Where are the limitations?

## Example: Designing a Drone
- Don't build 100 prototypes
- Create a mathematical model first
- Test virtually
- Build only the best design

## Key Mindset
**Simple model that explains behavior >> Complex model that confuses**

A model that helps you understand is better than a perfect model you can't use.
        """,
        "order": 1
    },
    {
        "title": "Modeling of electrical systems",
        "content": """
# Modeling of Electrical Systems

## R, L, C Circuits as Systems

### Resistor (R)
- **Input**: Voltage
- **Output**: Current
- **Relationship**: Current = Voltage / Resistance
- **Physical meaning**: Resists current flow (like friction)

### Inductor (L)
- **Input**: Voltage
- **Output**: Current (changes gradually)
- **Behavior**: Opposes sudden changes in current
- **Physical meaning**: Stores energy in magnetic field

### Capacitor (C)
- **Input**: Voltage
- **Output**: Charge storage
- **Behavior**: Opposes sudden changes in voltage
- **Physical meaning**: Stores energy in electric field

## Voltage In → Current Out Concept

### Simple Circuit Example
```
Voltage Source → Resistor → Current flows
V(t) → R →  I(t)
```

**Relationship**: I(t) = V(t) / R

### RC Circuit (Resistor + Capacitor)
- Apply voltage suddenly
- Capacitor charges gradually
- Current decreases over time
- **Behavior**: Exponential charging curve

### RL Circuit (Resistor + Inductor)
- Apply voltage suddenly
- Current increases gradually (inductor resists change)
- **Behavior**: Exponential rise

## Physical Meaning, Not Derivation
We care about:
- ✅ What happens to current when voltage changes
- ✅ How fast the system responds
- ✅ Steady-state vs transient behavior

We DON'T need:
- ❌ Complex differential equation derivations (yet)
- ❌ Every mathematical step
- ❌ Proofs and theorems

**Focus**: Understanding the behavior pattern
        """,
        "order": 2
    },
    {
        "title": "Modeling of mechanical systems",
        "content": """
# Modeling of Mechanical Systems

## Mass–Spring–Damper System

The fundamental model for understanding mechanical behavior.

### Three Components

#### 1. Mass (M)
- **Physical meaning**: Inertia, resistance to acceleration
- **Example**: Heavy object is hard to push
- **Effect**: Makes system respond slowly

#### 2. Spring (K)
- **Physical meaning**: Elasticity, stores potential energy
- **Example**: Compression/extension creates restoring force
- **Effect**: Makes system oscillate

#### 3. Damper (B)
- **Physical meaning**: Friction, dissipates energy
- **Example**: Shock absorber in car
- **Effect**: Reduces oscillations

## Force In → Motion Out

### Example: Car Suspension
- **Force Input**: Road bumps
- **Mass**: Car body weight
- **Spring**: Suspension springs
- **Damper**: Shock absorbers
- **Motion Output**: How much car body moves

### Behavior
1. Hit a bump (force applied)
2. Spring compresses
3. Car body moves up
4. Spring pushes back (restoring force)
5. Damper reduces oscillation
6. Car settles smoothly

## Electrical–Mechanical Analogy

Understanding one helps understand the other!

| Mechanical | Electrical | Physical Meaning |
|------------|------------|------------------|
| Force | Voltage | Driving agent |
| Velocity | Current | Flow |
| Mass | Inductance | Stores energy, resists change |
| Spring | Capacitance | Stores energy |
| Damper | Resistance | Dissipates energy |

### Why This Matters
- Same mathematical equations!
- Learn once, apply everywhere
- Electrical circuits behave like mechanical systems

## Real Applications
- **Earthquake-proof buildings**: Mass-spring-damper model
- **Vehicle suspension**: Comfort vs stability
- **Robot arms**: Precise positioning
- **Hard disk drives**: Smooth head movement
        """,
        "order": 3
    },
    {
        "title": "Differential equations basics",
        "content": """
# Differential Equations Basics

## Why Systems are Dynamic

Static system: Output = Input × Constant  
**Example**: Resistance, R = V/I (instant)

Dynamic system: Output depends on input **AND** its history  
**Example**: Capacitor charging (takes time)

## What Differential Equation Represents Physically

### Simple Explanation
A differential equation describes **how something changes with time**.

### Example: Water Tank Filling
- Rate of water level change = (Water in - Water out)
- dh/dt = (inflow - outflow)
- **Physical meaning**: How fast level rises or falls

### Example: RC Circuit
- Rate of voltage change = (Input - Current × Resistance) / Capacitance
- **Physical meaning**: How fast voltage builds up

## Order of System

### First Order System
- **Meaning**: One energy storage element
- **Examples**: 
  - RC circuit (one capacitor)
  - Water tank (one tank)
  - Room heating (one thermal mass)
- **Behavior**: Exponential response, no oscillation

### Second Order System
- **Meaning**: Two energy storage elements
- **Examples**:
  - Mass-spring system (mass + spring)
  - LC circuit (inductor + capacitor)
  - Pendulum (kinetic + potential energy)
- **Behavior**: Can oscillate, overshoot

### Higher Order
- More complex, multiple storage elements
- More complex behavior

## Key Insight
**Order tells you how complex the system's dynamics are**

- 1st order → Simple, smooth
- 2nd order → Can oscillate
- Higher order → More complex patterns

## Don't Fear the Math
You don't need to solve differential equations by hand!

**What matters**:
- ✅ Understanding what the equation represents
- ✅ Knowing what order means
- ✅ Predicting system behavior

**Computers solve the equations**, we understand the meaning.
        """,
        "order": 4
    },
    {
        "title": "Transfer function concept",
        "content": """
# Transfer Function Concept

## Why Laplace is Used (Simple Idea)

### The Problem with Time Domain
Differential equations in time domain are **hard to solve** and **hard to visualize**.

### The Solution
Transform to **s-domain** using Laplace transform:
- Differential equations → Algebraic equations
- Much easier to work with!

**Think of it like**: Converting rupees to dollars for easy international trade

## Input–Output Relationship

Transfer Function = Output / Input (in s-domain)

### What It Tells You
How the system **transforms** any input into output.

**Example**: H(s) = 1/(s+1)
- This tells you the system's complete input-output behavior
- One equation describes everything!

## Poles and Zeros (No Math Fear!)

### Poles
- **Simple meaning**: Values of 's' that make output infinite
- **Physical meaning**: Natural frequencies where system resonates
- **Importance**: Determine stability and response speed

### Zeros
- **Simple meaning**: Values of 's' that make output zero
- **Physical meaning**: Frequencies that get blocked/cancelled
- **Importance**: Shape the frequency response

### Visual Analogy
Think of transfer function as a filter:
- **Poles**: Amplify certain frequencies
- **Zeros**: Block certain frequencies

## Why Transfer Functions Are Powerful

### 1. System Characterization
- One function tells you everything about the system
- Easy to analyze different inputs

### 2. Design
- Easy to see how changing parameters affects behavior
- Compare different system designs quickly

### 3. Stability Analysis
- Just check pole locations!
- Left half s-plane = stable
- Right half s-plane = unstable

## Practical Example: Audio Equalizer
- Transfer function = how it modifies sound
- Poles and zeros = bass boost, treble cut, etc.
- You adjust these without knowing the math!

## Key Takeaway
Transfer function is a **compact representation** of system behavior.

**You're not solving equations manually** - you're understanding what they mean for real systems!
        """,
        "order": 5
    },
    {
        "title": "Block diagram algebra",
        "content": """
# Block Diagram Algebra

## Visual System Simplification

Block diagrams let you **see** how complex systems work without heavy math.

## Series Connection

```
Input → [G₁] → [G₂] → Output
```

**Combined**: G_total = G₁ × G₂

**Physical meaning**: Output of first block becomes input to second

**Example**: Amplifier → Speaker
- Amp gain = 10
- Speaker gain = 5
- Total gain = 10 × 5 = 50

## Parallel Connection

```
        ┌─ [G₁] ─┐
Input ──┤         ├──(+)── Output
        └─ [G₂] ─┘
```

**Combined**: G_total = G₁ + G₂

**Physical meaning**: Both paths contribute to output

**Example**: Two motors lifting same load
- Motor 1 force = 100N
- Motor 2 force = 150N
- Total force = 250N

## Feedback Connection

```
Input ──(+)── [G] ── Output
         ↑           |
         └── [H] ────┘
```

**Combined**: G_total = G / (1 + G×H)

**Physical meaning**: Output affects input through feedback path

### Negative Feedback (Most Common)
- Reduces overall gain
- Improves stability
- Reduces sensitivity to disturbances

### Positive Feedback (Rare)
- Increases overall gain
- Can cause instability
- Used in oscillators

## Simplifying Complex Systems Visually

### Example: Cruise Control Block Diagram
```
Desired Speed ──(-)── [Controller] ── [Engine] ── Actual Speed
                ↑                              |
                └────── [Sensor] ──────────────┘
```

**Step-by-step simplification**:
1. Identify feedback loops
2. Combine series blocks
3. Reduce feedback blocks
4. Final single transfer function!

## Moving Summing Points and Pickoff Points

### Rules to Remember
- You can move blocks around while preserving signal relationships
- Goal: Make diagram simpler
- Same input-output relationship = correct simplification

## Practical Benefits

### 1. System Understanding
- See signal flow at a glance
- Identify critical paths
- Spot feedback loops

### 2. Design
- Add/remove components visually
- Test "what if" scenarios
- Optimize system structure

### 3. Troubleshooting
- Identify where problems occur
- Trace signal through system
- Find weak links

## Key Insight
**Block diagrams are visual thinking tools** - they help you reason about systems without getting lost in equations.

Engineers use these daily to:
- Design control systems
- Debug problems
- Communicate with teammates
        """,
        "order": 6
    },
    {
        "title": "Signal flow graph basics",
        "content": """
# Signal Flow Graph Basics

## Another Way to See Systems

Signal Flow Graphs (SFG) are like **road maps** for signals traveling through a system.

## Nodes and Paths Meaning

### Nodes
- **Represent**: Variables (input, output, intermediate signals)
- **Think of**: Stations where signals exist

### Branches
- **Represent**: Transfer functions (how signal changes)
- **Think of**: Roads connecting stations with gain/loss

### Paths
- **Represent**: Route from input to output
- **Think of**: Journey a signal takes through the system

## Simple Example

```
X₁ ──(a)──→ X₂ ──(b)──→ X₃
```

- X₁, X₂, X₃ are nodes
- 'a' and 'b' are branch gains
- Path from X₁ to X₃ has gain = a × b

## Why Use Signal Flow Graphs?

### 1. Cleaner Than Block Diagrams
- Less cluttered
- Easier to see signal paths
- Better for complex systems

### 2. Mason's Gain Formula
- Systematic way to find overall transfer function
- Works even for very complex systems
- No tedious algebra needed!

### 3. Multiple Feedback Loops
- Block diagrams get messy with multiple loops
- SFG handles them elegantly

## Basic Components

### Forward Path
Path from input to output without repeating nodes

### Loop
Path that starts and ends at same node

### Non-touching Loops
Loops that don't share any nodes (independent)

## Real Example: Feedback System

```
       ┌────(G)────→
R ──→ ☉            Y
       ↑           │
       └──(-H)─────┘
```

- Forward path gain: G
- Feedback loop gain: -GH
- Overall gain: G / (1 + GH)

## Mason's Gain Formula (Concept Only)

**Don't memorize the formula!**

**Understand**: It's a systematic way to:
1. Identify all forward paths
2. Identify all feedback loops
3. Calculate overall transfer function
4. Handle complex systems methodically

## When to Use SFG vs Block Diagrams

### Use Block Diagrams When:
- Simple systems
- Need physical interpretation
- Teaching/learning basics

### Use Signal Flow Graphs When:
- Complex systems with multiple loops
- Need systematic analysis
- Want compact representation

## Progress Checkpoint 🎯
**"I can convert a real system into a model!"**

You've completed Mathematical Modeling. You now understand:
✅ Why modeling matters
✅ Electrical and mechanical systems
✅ Differential equations (physical meaning)
✅ Transfer functions
✅ Block diagram simplification
✅ Signal flow graphs

**Ready for Stage 3: Time Domain Analysis!**
        """,
        "order": 7
    }
]

for topic_data in topics_stage2:
    Topic.objects.create(
        stage=stage2,
        title=topic_data["title"],
        content=topic_data["content"],
        order=topic_data["order"]
    )
    print(f"  ✅ Added topic: {topic_data['title']}")

print(f"\n🎉 Successfully created Control Systems Learning Roadmap!")
print(f"📊 Total Stages: 2 (Stage 1 & 2 completed)")
print(f"📝 Total Topics: {len(topics_stage1) + len(topics_stage2)}")
print(f"\nNote: Stages 3, 4, and 5 will be added in the next script.")
