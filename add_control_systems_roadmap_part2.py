"""
Script to add Stages 3, 4, 5 to Control Systems Learning Roadmap
Run this AFTER add_control_systems_roadmap_part1.py
Command: python manage.py shell < add_control_systems_roadmap_part2.py
"""

from core.models import Roadmap, Stage, Topic

# Get the existing roadmap
roadmap = Roadmap.objects.get(title="Control Systems Learning")
print(f"✅ Found Roadmap: {roadmap.title}")

# ==================== STAGE 3: Time Domain Analysis ====================
stage3 = Stage.objects.create(
    roadmap=roadmap,
    title="Time Domain Analysis",
    description="Understand how systems behave with time. Predict real-life system responses.",
    order=3,
    is_free=False
)

topics_stage3 = [
    {
        "title": "Standard test signals",
        "content": """
# Standard Test Signals

## Why These Signals Are Used

In real life, systems face different types of inputs. We test with standard signals to understand how systems will behave.

## Three Main Test Signals

### 1. Step Input
**What it is**: Sudden change from 0 to constant value

**Real-life meaning**:
- Turning on a switch
- Pressing accelerator pedal
- Setting thermostat to new temperature

**Example**: Room heater
- OFF (0°C) → suddenly ON (target 25°C)
- Step input at t=0

**Why test with step**: Most common in real systems

### 2. Ramp Input
**What it is**: Constantly increasing value over time

**Real-life meaning**:
- Steadily pressing accelerator
- Gradually opening water tap
- Slowly moving joystick

**Example**: Car speed
- Speed increases linearly: 0 → 20 → 40 → 60 km/h

**Why test with ramp**: Tests tracking ability

### 3. Impulse Input
**What it is**: Very large input for very short time

**Real-life meaning**:
- Hammer strike
- Lightning strike
- Sudden shock

**Example**: Hitting a drum
- Large force for split second
- System rings afterward

**Why test with impulse**: Reveals natural behavior

## Which Signal for What?

| Signal | Tests | Real Example |
|--------|-------|--------------|
| Step | Basic response, overshoot | AC ON/OFF |
| Ramp | Tracking, steady-state error | Following moving object |
| Impulse | Natural frequency, damping | Testing suspension |

## Key Insight
These simple signals tell us EVERYTHING about system behavior!

If we know step response, we can predict response to ANY input.
        """,
        "order": 1
    },
    {
        "title": "Time response characteristics",
        "content": """
# Time Response Characteristics

## How Output Changes After Input

When you give an input to a system, the output doesn't change instantly (usually). Understanding this change pattern is crucial.

## Two Types of Response

### 1. Transient Response
- **What**: Temporary behavior right after input changes
- **Duration**: Short time
- **Example**: Car jerks when you suddenly brake, then settles

### 2. Steady-State Response  
- **What**: Final settled behavior
- **Duration**: Continues forever
- **Example**: Car maintains constant speed after settling

## Why Response Shape Matters

### Fast Response
- **Good**: Quick to use, efficient
- **Bad**: May overshoot, unstable
- **Example**: Sports car - fast but jerky

### Slow Response
- **Good**: Smooth, stable
- **Bad**: Sluggish, frustrating
- **Example**: Heavy truck - stable but slow

## Ideal Response
- Fast enough to be useful
- Stable enough to be safe
- Just right overshoot
- Quick settling time

## Visual Understanding

```
        Overshoot ↗
Input ─┐         ↗─ Final Value
       │    ↗─↗
       └──┬────────────→ Time
          ↑
      Rise Time
```

## Real-World Trade-offs

### Example: Camera Autofocus
- **Too fast**: Hunts back and forth, never settles (unstable)
- **Too slow**: Misses the moment (unusable)
- **Just right**: Quick focus, locks on target (perfect)

## Engineering Challenge
Design systems with:
- ✅ Fast response when needed
- ✅ Minimal overshoot
- ✅ Quick settling to steady state
- ✅ Stability under all conditions
        """,
        "order": 2
    },
    {
        "title": "First order systems",  
        "content": """
# First Order Systems

## Examples in Real Life

### 1. RC Circuit
- Capacitor charging/discharging
- Voltage changes exponentially
- No oscillation

### 2. Thermal System
- Room heating/cooling
- Temperature rises smoothly
- No overshoot

### 3. Liquid Level Tank
- Water filling tank
- Level increases exponentially
- Smooth rise

### 4. Simple Motor Speed Control
- Speed changes gradually
- Approaches final speed smoothly

## Characteristic Behavior

**One main feature**: **Exponential response**

```
Output          Final Value ──────────
   ↑                    ↗─────
   │              ↗──────
   │        ↗─────  (63% at time constant)
   │  ↗─────
   └──┴────────────────────→ Time
      τ (Time Constant)
```

## Time Constant (τ)

**Physical meaning**: How fast the system responds

- **Small τ**: Fast response
- **Large τ**: Slow response

### Rule of Thumb
- At time = τ → Output reaches 63% of final value
- At time = 3τ → Output reaches 95% of final value
- At time = 5τ → Output practically at final value

## Speed of Response

### Fast System Example: LED light
- τ = 0.001 seconds
- Instant ON perception

### Slow System Example: Room heater
- τ = 10 minutes  
- Takes 30-50 minutes to fully warm room

## Why First Order is Simple

✅ **No overshoot** - Always approaches final value smoothly  
✅ **No oscillation** - Just smooth exponential curve  
✅ **Predictable** - Always stable  
✅ **Easy to design** - One parameter to adjust (τ)  

## Real Applications

| System | Time Constant | Behavior |
|--------|---------------|----------|
| RC circuit | R×C | Voltage builds up |
| Heating system | Thermal mass | Temp rises slowly |
| Motor speed | Inertia/Damping | Speed increases |
| Water tank | Area/Flow | Level rises |

## Key Takeaway
First-order systems are the **simplest dynamic systems**.
- One energy storage element
- Exponential response always
- Always stable  
- Foundation for understanding complex systems
        """,
        "order": 3
    },
    {
        "title": "Second order systems",
        "content": """
# Second Order Systems

## Examples in Real Life

### 1. Car Suspension
- Mass (car body) + Spring + Damper
- Absorbs road bumps
- **Can oscillate** if poorly designed

### 2. Motor with Load
- Motor inertia + Spring coupling + Friction
- Position control
- May overshoot target position

### 3. Robotic Arm
- Mass of arm + Joint stiffness + Friction
- Precise positioning
- Trade-off between speed and accuracy

### 4. Pendulum
- Mass + Gravity (acts like spring) + AIr resistance (damping)
- Swings back and forth if undamped

## Why Second Order is More Complex

**Two energy storage elements**:
1. Can store energy (mass, capacitor)
2. Can store energy differently (spring, inductor)

Energy can **transfer between them** → Oscillation!

## Three Types of Response

### 1. Underdamped (Light Damping)
- **Behavior**: Overshoots and oscillates before settling
- **Example**: Cheap suspension - car bounces after bump
- **Use when**: Fast response needed, some overshoot acceptable

```
Output   ↗─╮
         ↗  ↘↗─╮
    ↗───    ↘ ↗─ Final Value
─────────────────→ Time
```

### 2. Critically Damped (Perfect Damping)
- **Behavior**: Reaches final value fastest without overshoot
- **Example**: Ideal door closer - closes smoothly, no slam
- **Use when**: Best balance of speed and stability

```
Output      ┌─── Final Value
         ↗──┘
    ↗───
─────────────────→ Time
```

### 3. Overdamped (Heavy Damping)
- **Behavior**: Slow rise, no overshoot, sluggish
- **Example**: Door in thick oil - very slow
- **Use when**: Stability critical, speed not important

```
Output          ┌─── Final Value
           ↗────┘
      ↗────
─────────────────→ Time
```

## Oscillation Meaning

**Physical interpretation**:
- Energy bounces between two storage forms
- Like a swing going back and forth
- Damping gradually removes energy (friction)

### Example: Mass-Spring
1. Compress spring (potential energy)
2. Release - mass moves up (kinetic energy)
3. Mass overshoots, compresses spring other way
4. Cycles repeat, getting smaller each time
5. Finally stops at equilibrium

## Real-World Design Choices

### Underdamped System
**Example**: Sports car suspension
- **Pros**: Fast response, sporty feel
- **Cons**: Bouncy ride, less comfortable

### Critically Damped System
**Example**: Premium car suspension
- **Pros**: Best compromise - fast and smooth
- **Cons**: Harder to achieve perfectly

### Overdamped System
**Example**: Heavy truck suspension
- **Pros**: Very stable, no bouncing
- **Cons**: Slow to respond, feels sluggish

## Key Parameters

### Natural Frequency (ωn)
- How fast system naturally wants to oscillate
- **Higher ωn** = Faster system

### Damping Ratio (ζ)
- How much damping vs oscillation
- **ζ < 1**: Underdamped (oscillates)
- **ζ = 1**: Critically damped (ideal)
- **ζ > 1**: Overdamped (slow)

## Engineering Trade-off

You CANNOT have:
- Fast response
- Zero overshoot
- Zero oscillation

**all at the same time!**

Pick two, sacrifice one.

## Progress Point
Understanding second-order systems means you understand 90% of control systems in real world!
        """,
        "order": 4
    },
    {
        "title": "Stability interpretation",
        "content": """
# Stability - Simple Interpretation

## What is Stability? (No Formulas)

**Stable system**: Eventually settles to a final value after disturbance

**Unstable system**: Keeps growing, oscillating wildly, or exploding

## Physical Understanding

### Stable Example: Ball in a Bowl
- Push ball → it rolls back to center
- May oscillate, but eventually settles at bottom
- **Energy dissipates**

### Unstable Example: Ball on Top of Hill
- Slight push → ball rolls away forever
- Never returns
- **Energy increases**

### Marginally Stable: Ball on Flat Surface
- Push ball → it rolls to new position and stays there
- Doesn't return but doesn't explode either
- **Energy constant**

## Three Types of Stability

### 1. Stable System
**Behavior**: 
- Output bounded (limited)
- Returns to equilibrium
- Damped response

**Real examples**:
- Room thermostat - maintains temperature
- Car cruise control - maintains speed
- Pendulum with friction - stops swinging

**Characteristic**: All disturbances eventually die out

### 2. Unstable System  
**Behavior**:
- Output grows without bound
- Never settles
- Explosive response

**Real examples**:
- Microphone feedback screech (audio feedback unstable)
- Inverted pendulum falling over
- Plane in a spin (without correction)

**Characteristic**: Small disturbance causes big problem

### 3. Marginally Stable System
**Behavior**:
- Output oscillates forever (constant amplitude)
- Doesn't grow but doesn't settle either

**Real examples**:
- Pendulum without friction (ideal)  
- LC circuit oscillating forever (ideal)
- Satellite in perfect orbit

**Characteristic**: Keeps going, never stops, never explodes

## How to Tell if System is Stable?

### Time Domain View
- **Plot output over time**
- Does it settle? → Stable
- Does it explode? → Unstable
- Does it oscillate forever? → Marginally stable

### Frequency Domain View (Advanced)  
- Check pole locations
- Left half plane → Stable
- Right half plane → Unstable
- On axis → Marginally stable

## Why Stability Matters

### Unstable = Dangerous!
- Plane crash
- Bridge collapse (resonance)
- Robot going wild
- Chemical plant explosion

### Stable = Safe and Usable
- Reliable operation
- Predictable behavior
- Safe for humans

## Real-World Stability Issues

### Famous Example: Tacoma Narrows Bridge (1940)
- Bridge oscillations grew due to wind
- Became unstable (resonance)
- Collapsed dramatically
- **Lesson**: Stability is life-or-death important!

### Example: Segway/Hoverboard
- Inverted pendulum (naturally unstable)
- Control system makes it stable
- Turn off controller → immediately falls

## Ensuring Stability in Design

### 1. Add Damping
- Friction reduces oscillations
- Energy dissipates
- System settles faster

### 2. Reduce Gain
- Lower amplification
- Less aggressive response
- More stable but slower

### 3. Use Feedback Properly
- Negative feedback stabilizes
- Positive feedback destabilizes
- Must be designed carefully

## Key Insight
**Stability is the MOST important requirement**

Better to have:
- Slow but stable system
  
Than:
- Fast but unstable system (useless and dangerous!)

**First make it stable. Then make it fast.**
        """,
        "order": 5
    },
    {
        "title": "Overshoot, rise time, settling time",
        "content": """
# Response Quality Metrics

## What They Tell About System Quality

These metrics describe HOW WELL a system performs its job.

## 1. Rise Time (tr)

### Definition
Time taken to reach from 10% to 90% of final value

### Physical Meaning
**How quickly system responds initially**

### Real Examples

**Fast rise time**: Sports car acceleration
- 0 to 60 mph in 3 seconds
- Quick response

**Slow rise time**: Heavy truck acceleration  
- 0 to 60 mph in 30 seconds
- Sluggish response

### Industry Perspective
- **Faster is better** BUT...
- Too fast can cause overshoot
- **Trade-off**: Speed vs stability

## 2. Overshoot (Mp)

### Definition
How much output exceeds final value (as percentage)

### Physical Meaning
**How much system overshoots the target**

### Real Examples

**Low overshoot (5%)**: Luxury car suspension
- Smooth, comfortable
- Barely noticeable bump response

**High overshoot (50%)**: Cheap toy car suspension
- Bouncy, uncomfortable
- Dramatic oscillations

### Industry Standards
- **Control systems**: Usually < 10-20% acceptable
- **Safety-critical**: < 5% required
- **High-performance**: < 2% needed

### Why Overshoot Matters
- **Manufacturing**: Product might get damaged
- **Robotics**: Might hit obstacles
- **Aircraft**: Passenger discomfort
- **Process control**: Waste, inefficiency

## 3. Settling Time (ts)

### Definition
Time for output to stay within ±2% or ±5% of final value permanently

### Physical Meaning
**How long before system is "done"**

### Real Examples

**Short settling time**: Automatic camera focus
- < 1 second
- Must be fast for photography

**Long settling time**: Large ship steering
- Several minutes
- Acceptable for slow operations

### Industry Perspective
Various tolerance bands:
- **2% band**: Tight spec, precision needed
- **5% band**: Normal industrial spec
- **10% band**: Loose spec, general use

## Visualizing All Three Together

```
Output
   ↑
   |        Overshoot (Mp)
   |          ↗─╮
   |       ↗─    ↘ ←── ±2% band
   |    ↗─        ╰──── Final Value
   | ↗─              ±2% band
   |┘
   └──┬──┬───┬─────────────→ Time
      tr  |   └─ ts (Settling time)
      Rise Time
```

## Why Industries Care

### Example: Robot Arm Picking Object

**Rise Time**: How fast arm moves to target
- **Too slow**: Productivity suffers
- **Too fast**: Might break things

**Overshoot**: How much it overshoots target
- **Too much**: Might knock things over
- **Zero overshoot**: Takes forever (overdamped)

**Settling Time**: How long before ready for next task
- **Too long**: Cycle time increases
- **Short**: Higher throughput

### Example: Temperature Control in Oven

**Rise Time**: How fast oven heats up
- Important for user convenience

**Overshoot**: How much over target temp
- **Too much**: Burns food, wastes energy
- **Acceptable**: ±5°C

**Settling Time**: How long to stabilize
- Important for consistent baking

## Design Trade-offs

**You cannot optimize all three simultaneously!**

### Fast Rise Time
- Usually causes overshoot
- May increase settling time

### Zero Overshoot
- Requires slow rise time
- Longer settling time

### Quick Settling
- Needs good damping
- May sacrifice rise time

## Industry Specifications

Different applications, different priorities:

| Application | Priority | Typical Specs |
|-------------|----------|---------------|
| Audio systems | Low overshoot | Mp < 5%, ts < 1s |
| Motor control | Fast rise | tr < 100ms, Mp < 20% |
| Temperature | Low overshoot | Mp < 2%, ts doesn't matter |
| Fighter jet | Fast everything | tr < 0.1s, tight control |

## Progress Checkpoint 🎯
**"I can predict how a system will respond in real life!"**

You've completed Time Domain Analysis. You now understand:
✅ Test signals and their meanings
✅ Response characteristics
✅ First and second-order systems
✅ Stability concepts
✅ Quality metrics (overshoot, rise time, settling time)

**Ready for Stage 4: Frequency Domain Analysis!**
        """,
        "order": 6
    }
]

for topic_data in topics_stage3:
    Topic.objects.create(
        stage=stage3,
        title=topic_data["title"],
        content=topic_data["content"],
        order=topic_data["order"]
    )
    print(f"  ✅ Added topic: {topic_data['title']}")

print(f"\n🎉 Stage 3 completed! Continuing with Stages 4 and 5...")
print("Note: This is Part 2 of the script. Stages 4 and 5 content will be added next.")
