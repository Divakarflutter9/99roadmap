"""
Script to add Stages 4 and 5 to Control Systems Learning Roadmap (Final Part)
Run this AFTER add_control_systems_roadmap_part2.py
Command: python manage.py shell < add_control_systems_roadmap_part3.py
"""

from core.models import Roadmap, Stage, Topic

# Get the existing roadmap
roadmap = Roadmap.objects.get(title="Control Systems Learning")
print(f"✅ Found Roadmap: {roadmap.title}")

# ==================== STAGE 4: Frequency Domain Analysis ====================
stage4 = Stage.objects.create(
    roadmap=roadmap,
    title="Frequency Domain Analysis",
    description="Analyze system behavior using frequency thinking. Judge system robustness like an engineer.",
    order=4,
    is_free=False
)

topics_stage4 = [
    {
        "title": "Why frequency analysis is needed",
        "content": """
# Why Frequency Analysis is Needed

## Time View vs Frequency View

### Time Domain
- **Shows**: How system changes with time
- **Good for**: Transient response, step response
- **Example**: How fast motor reaches speed after switch ON

### Frequency Domain
- **Shows**: How system reacts to different frequencies
- **Good for**: Noise rejection, stability margins, filtering
- **Example**: How motor handles vibrations at different frequencies

**Both views are needed for complete understanding!**

## Real-World Analogy: Music Equalizer

**Time domain**: Waveform on oscilloscope
- Shows signal up/down over time
- Hard to see which frequencies are loud

**Frequency domain**: Bar graph on equalizer
- Shows bass, mid, treble separately
- Easy to see and adjust each frequency

## Noise and Disturbances Understanding

### Problem
Real systems face:
- Sensor noise
- External vibrations
- Power supply fluctuations
- Environmental disturbances

### Time Domain Challenge
Hard to separate:
- Useful signal from noise
- Slow changes from fast changes

### Frequency Domain Solution
Easy to see:
- **Low frequencies**: Useful signals, slow changes
- **High frequencies**: Noise, vibrations, fast disturbances

## Why Engineers Use Frequency Analysis

### 1. Noise Rejection Design
- Identify noise frequencies
- Design filters to block them
- Keep useful signals

### 2. Stability Analysis
- More intuitive than time domain poles
- Visual tools (Bode, Nyquist)
- Safety margins clearly visible

### 3. System Specifications
Industries specify:
- Bandwidth (how fast system can track)
- Resonant frequency (where oscillations occur)
- Phase margin (safety from instability)

### 4. Frequency-Based Disturbances
Many disturbances are periodic:
- 50 Hz power line noise
- Engine vibrations at specific RPM
- Structural resonances

## Real Application Example: Car Suspension

**Time domain question**:
"How much does car bounce after hitting bump?"

**Frequency domain question**:
"Which road frequencies does suspension filter out best?"

**Both questions matter!**

### Frequency Insights
- Low frequency bumps (< 1 Hz): Large, slow - suspend smoothly
- High frequency vibrations (> 10 Hz): Small, fast - dampen quickly
- Resonant frequency (~2 Hz): Avoid amplification, tune dampers

## Key Benefit
**Frequency domain makes some problems much easier to solve!**

Some things obvious in frequency domain are hidden in time domain.
        """,
        "order": 1
    },
    {
        "title": "Frequency response concept",
        "content": """
# Frequency Response Concept

## How System Reacts to Different Frequencies

Imagine singing into a microphone at different pitches (frequencies):
- Low bass notes might sound quieter
- Mid-range clear and loud
- High-pitched squeals might sound different

**This is frequency response!**

## Definition (Simple)
Frequency response = How system output changes for inputs at different frequencies

## Low vs High Frequency Meaning

### Low Frequency Input
- **Physical meaning**: Slow changes
- **Example**: Temperature changing throughout the day
- **System behavior**: Usually follows well

### High Frequency Input
- **Physical meaning**: Fast changes, vibrations
- **Example**: High-pitch sound, mechanical vibration
- **System behavior**: Often filtered out, can't follow

## Frequency Response Graph

```
Magnitude
   ↑
   |  ███████╗           Low frequencies pass
   |         ╚═══╗       (System follows well)
   |             ╚═══════ High frequencies attenuated  
   |                     (System can't keep up)
   └────────────────────→ Frequency (Hz)
     Low        High
```

## Real-World Examples

### 1. Speakers
- **Low freq (bass)**: Large woofer needed
- **Mid freq**: All speakers can handle
- **High freq (treble)**: Small tweeter enough

### 2. Car Suspension
- **Low freq (large bumps)**: Absorbs well
- **High freq (road texture)**: Doesn't react (good!)

### 3. Human Hearing
- **Low freq**: 20 Hz (deep rumble)
- **Mid freq**: 1000 Hz (normal speech)
- **High freq**: 20,000 Hz (very high pitch)

## Bandwidth Concept

**Bandwidth** = Range of frequencies system can handle well

### Wide Bandwidth
- Can track fast changes
- Responds quickly
- Example: High-performance servo

### Narrow Bandwidth
- Only tracks slow changes
- Slower response
- Example: Temperature controller

## Practical Understanding

### Low Frequency Behavior
- System has time to adjust
- Follows input accurately
- Output magnitude ≈ Input magnitude

### High Frequency Behavior
- System can't keep up
- Output gets weaker
- Acts like a filter

## Why This Matters

### Design Decisions
- **Need fast tracking?** → Wide bandwidth
- **Want to filter noise?** → Narrow bandwidth at noise frequency
- **Trade-off**: Can't have both perfectly

### Example: Camera Stabilization
- **Low freq**: Intentional movement (panning) - allow through
- **High freq**: Hand shake - filter out aggressively

## Phase Shift
Along with magnitude change, frequency affects **timing** too.

Higher frequencies often get delayed more (phase lag).

### Example: Sound Delay
- Bass frequencies travel differently than treble
- This is why distant thunder sounds different

## Key Insight
Different frequencies = Different treatment by system

Understanding this helps design better filters, controllers, and systems!
        """,
        "order": 2
    },
    {
        "title": "Bode plots",
        "content": """
# Bode Plots

## Visual Tool for Frequency Response

Bode plots are **graphs** that show how a system behaves across all frequencies.

Think of it like an **X-ray of the system's frequency behavior**.

## Two Plots Together

### 1. Magnitude Plot
- **Y-axis**: Gain (in dB - decibels)
- **Shows**: How much input is amplified or attenuated

### 2. Phase Plot  
- **Y-axis**: Phase angle (in degrees)
- **Shows**: How much output is delayed from input

Both use:
- **X-axis**: Frequency (logarithmic scale)

## Magnitude Plot Intuition

```
Gain (dB)
   ↑
 20|  ──────╗                Flat region (good)
   |        ╚═════╗          
  0|              ╚════╗     Rolloff region
   |                  ╚══╗  
-20|                     ╚══ High freq attenuated
   └──────────────────────→ log(freq)
      Low freq    High freq
```

### What Different Regions Mean

**Flat region (Low freq)**:
- System passes signal unchanged
- Gain ≈ 1 (0 dB)
- Good tracking

**Rolloff region**:
- System starts filtering
- Gain decreasing
- Transition zone

**High attenuation region**:
- System blocks these frequencies
- Gain << 1 (negative  dB)
- Noise rejection zone

## Phase Plot Intuition

```
Phase (°)
    0°|  ──────╗
      |        ╚═════╗        
  -45°|              ╚════    Phase lag increases
      |                  ╗
  -90°|                  ╚══  More delay at high freq
      └──────────────────────→ log(freq)
```

### What Phase Means

- **0° phase**: Output in sync with input
- **-45° phase**: Output lags input by 1/8 cycle
- **-90° phase**: Output lags input by 1/4 cycle
- **-180° phase**: Output opposite to input (danger!)

## Slope Changes Indicate System Order

### Slope = -20 dB/decade
- **Meaning**: First-order system (one pole)
- **Example**: RC circuit, simple filter

### Slope = -40 dB/decade
- **Meaning**: Second-order system (two poles)
- **Example**: Mass-spring system, LC circuit

### Slope = -60 dB/decade
- **Meaning**: Third-order system
- More complex dynamics

**The slope tells you system complexity!**

## Reading Bode Plots

### Important Points

**Cutoff Frequency (ωc)**:
- Where gain drops to -3 dB
- Bandwidth of system
- System starts significant attenuation

**Gain Margin**:
- How far from 0 dB at phase -180°
- Safety margin for stability
- Bigger is safer

**Phase Margin**:
- How far from -180° when gain is 0 dB
- Another stability measure
- Typical target: > 45°

## Real Example: Audio Filter

### Low-Pass Filter Bode Plot
- Bass frequencies (20-200 Hz): Pass through (0 dB)
- Mid frequencies (200-2000 Hz): Gradual rolloff
- High frequencies (> 2000 Hz): Blocked (-40 dB)

**Use**: Remove high-frequency hiss from recording

## What Bode Plots Tell Engineers

✅ **Bandwidth**: How fast system can respond  
✅ **Filtering**: Which frequencies get blocked  
✅ **Stability**: Safety margins  
✅ **Resonance**: Where system amplifies (peaks)  
✅ **Order**: System complexity  

## Practical Design

### Want Fast Response?
- Push cutoff frequency higher
- Wider bandwidth

### Want Noise Rejection?
- Make rolloff steeper
- More aggressive filtering

### Want Stability?
- Check phase at gain crossover
- Maintain good phase margin

## Key Takeaway
Bode plots are the **engineer's dashboard** for frequency analysis.

One glance tells you:
- System speed
- Filtering characteristics
- Stability margins
- Problem frequencies
        """,
        "order": 3
    },
    {
        "title": "Nyquist plot",
        "content": """
# Nyquist Plot

## Stability Using Loop Behavior

Nyquist plot is a **clever graphical tool** to check stability by looking at how feedback loops behave across frequencies.

## What is Nyquist Plot?

It plots the **frequency response of the open-loop system** on complex plane (real + imaginary axes).

### Instead of Two Separate Plots (Bode)
- Magnitude on one axis
- Phase on another axis

### Nyquist Combines Both
- Real part (horizontal)
- Imaginary part (vertical)
- Creates a **curve** as frequency varies

## The Critical Point: (-1, 0)

This one point tells everything about stability!

```
  Imaginary
      ↑
      |     Curve path
      |   ╱───────╲
      | ╱     ●    ╲  
  ────┼────(-1,0)───╲─→ Real
      |               ╲─╯
      |
      ↓
```

### Stability Criterion (Simple)
- **Curve does NOT encircle (-1,0)** → System is **stable**
- **Curve encircles (-1,0)** → System is **unstable**

## Why Engineers Use Nyquist

### 1. Visual Stability Check
- One look at the plot
- Is (-1,0) inside or outside curve?
- Instant stability verdict!

### 2. Robust for Complex Systems
- Works even when Bode plots are tricky
- Handles multiple loops
- More general

### 3. Shows Stability Margins
- **Distance from (-1,0)** = Stability margin
- **Closer to (-1,0)** = Less stable (dangerous)
- **Far from (-1,0)** = Very stable (safe)

## Gain Margin & Phase Margin on Nyquist

### Gain Margin (GM)
- Distance from origin to where curve crosses negative real axis
- How much gain increase can system tolerate before instability

### Phase Margin (PM)
- Angular difference from (-1,0) direction
- How much phase lag can system tolerate

## Real-World Interpretation

### Example: Microphone Feedback

**Stable system**:
- Nyquist curve away from (-1,0)
- No howling screech

**Approaching instability**:
- Curve getting close to (-1,0)
- Slight echo, resonance

**Unstable**:
- Curve encircles (-1,0)
- Screaming feedback!

### Example: Car Steering

**Stable**:
- Smooth steering response
- Curve away from (-1,0)

**Marginally stable**:
- Steering feels "touchy"
- Curve near (-1,0)

**Unstable**:
- Steering oscillates
- Curve encircles (-1,0)
- Dangerous!

## Practical Nyquist Use

### Design Process
1. Plot Nyquist curve for your controller design
2. Check if curve encircles (-1,0)
3. If yes → Redesign (reduce gain, add damping)
4. If no → Check margins
5. Ensure sufficient distance from (-1,0)

### Tuning
- **Increase gain** → Curve expands outward
- **Too much gain** → Curve reaches (-1,0) → Unstable!
- **Decrease gain** → Curve shrinks inward → Safer but slower

## Comparison: Bode vs Nyquist

| Feature | Bode Plot | Nyquist Plot |
|---------|-----------|--------------|
| Plots | 2 separate (mag + phase) | 1 combined |
| Stability check | Read margins numerically | Visual encirclement |
| Complexity | Easier for beginners | More powerful |
| Industry use | Very common | Advanced analysis |

## Key Insight
Nyquist plot is like a **stability radar**.

- (-1,0) is the danger zone
- Keep your curve away from it
- Distance = Safety margin

**One plot, complete stability picture!**
        """,
        "order": 4
    },
    {
        "title": "Gain margin & phase margin",
        "content": """
# Gain Margin & Phase Margin

## What "Margin" Really Means

**Margin** = Safety buffer before system becomes unstable

Like:
- Safety margin in bridge design
- Margin of error in measurements
- Buffer stock in warehouse

**In control systems**: How much can things change before instability?

## Gain Margin (GM)

### Simple Definition
**How much can we increase gain before system goes unstable?**

### Physical Interpretation
Imagine you have a volume knob for your control system:
- Current volume: System is stable
- Turn up too much → Feedback screech (unstable)
- **Gain margin**: How many dB you can turn up safely

### Typical Values
- **GM = 20 dB**: Very safe, can double gain
- **GM = 10 dB**: Good margin, comfortable
- **GM = 6 dB**: Minimum acceptable
- **GM = 0 dB**: System at edge of instability!

### Real Example: Microphone System
- **High GM**: Turn up volume a lot before feedback
- **Low GM**: Barely touch volume knob → screech!

## Phase Margin (PM)

### Simple Definition
**How much extra delay can system tolerate before instability?**

### Physical Interpretation
Every system has delays:
- Sensor measurement delay
- Computation delay
- Actuator response delay

**Phase margin**: How much MORE delay before things go bad

### Typical Values
- **PM = 60°**: Excellent, very robust
- **PM = 45°**: Good, industry standard
- **PM = 30°**: Minimum safe
- **PM = 0°**: Unstable!

### Real Example: Robot Arm Control
- **High PM**: System tolerates cable delays, sensor delays
- **Low PM**: Any small delay → oscillations

## Why Both Margins Matter

### Can't Rely on Just One
- System might have good GM but poor PM → Still risky
- Or good PM but poor PM → Also risky

**Need BOTH to be comfortable!**

## How Much Safety a System Has

### Conservative Design (Safe Applications)
- **GM** > 12 dB
- **PM** > 45°
- **Use when**: Medical devices, aircraft, life safety

### Standard Design (Normal Applications)
- **GM** > 6 dB
- **PM** > 30°
- **Use when**: Consumer products, industrial machines

### Aggressive Design (Performance Priority)
- **GM** ≈ 4-6 dB
- **PM** ≈ 25-30°
- **Use when**: Racing, high-performance systems, can accept occasional instability

## Where Margins Come From

### Gain Margin from Bode Plot
1. Find frequency where phase = -180°
2. Read magnitude at that frequency
3. GM = Distance from 0 dB

### Phase Margin from Bode Plot
1. Find frequency where gain = 0 dB (crossover frequency)
2. Read phase at that frequency
3. PM = Distance from -180°

## Trade-offs with Margins

### Large Margins (Conservative)
**Pros**:
- Very stable
- Robust to variations
- Safe
**Cons**:
- Slower response
- More sluggish
- May not perform well

### Small Margins (Aggressive)
**Pros**:
- Fast response
- High performance
- Sensitive tracking
**Cons**:
- Fragile
- Might oscillate
- Risky

## Real Engineering Decisions

### Example: Drone Stabilization

**Conservative tuning** (GM = 15 dB, PM = 60°):
- Very stable flight
- Beginner-friendly
- Slow to respond to stick inputs
- Boring for racing

**Aggressive tuning** (GM = 5 dB, PM = 25°):
- Snappy, responsive
- Exciting flight
- Might oscillate in wind
- Expert pilots only

## Practical Guidelines

### Testing
1. Design system with good margins
2. Test in real environment
3. If too sluggish → Reduce margins (increase gain)
4. If unstable/oscillating → Increase margins (decrease gain)
5. Find sweet spot!

### Rule of Thumb
**Start conservative, tune for performance later**

Better to have:
- Slow but stable system for launch
  
Than:
- Fast but crashy system

## Key Insight
Margins are **insurance against the unknown**:
- Temperature changes
- Component aging
- Manufacturing variations
- External disturbances

**Good margins = System works reliably in real world!**

## Progress Checkpoint 🎯
**"I can judge system robustness like an engineer!"**

You've completed Frequency Domain Analysis. You now understand:
✅ Why frequency analysis matters
✅ Frequency response concepts
✅ Bode plots (magnitude & phase)
✅ Nyquist plot for stability
✅ Gain and phase margins

**Ready for Stage 5: Controllers & Applications!**
        """,
        "order": 5
    }
]

for topic_data in topics_stage4:
    Topic.objects.create(
        stage=stage4,
        title=topic_data["title"],
        content=topic_data["content"],
        order=topic_data["order"]
    )
    print(f"  ✅ Added topic: {topic_data['title']}")

# ==================== STAGE 5: Controllers & Applications ====================
stage5 = Stage.objects.create(
    roadmap=roadmap,
    title="Controllers & Applications",
    description="Connect control theory to actual engineering applications. Apply control systems to real products.",
    order=5,
    is_free=False
)

topics_stage5 = [
    {
        "title": "PID controller concept",
        "content": """
# PID Controller - The Universal Controller

## Why PID is Everywhere

**95% of industrial controllers use PID!**

Why? Because it's:
- ✅ Simple to understand
- ✅ Easy to implement
- ✅ Works for most applications
- ✅ Proven over decades

## Three Components: P, I, D

### P = Proportional
**"Push harder when error is big"**

#### Simple Meaning
- Error large → Corrective action large
- Error small → Corrective action small

#### Real Example: Driving
- Far from lane center → Turn wheel sharply
- Close to lane center → Gentle steering

#### Math (Simple)
`P control = Kp × Error`

**Problem**: Never reaches target perfectly (steady-state error)

---

### I = Integral
**"Remember past mistakes and correct them"**

#### Simple Meaning
- Accumulates error over time
- Eliminates steady-state error
- Ensures target is reached exactly

#### Real Example: Filling Water Bucket
- P alone: Stops slightly before full
- PI: Remembers "still not full", keeps filling until exactly full

#### Math (Simple)
`I control = Ki × (Sum of all past errors)`

**Problem**: Can cause overshoot and oscillation

---

### D = Derivative
**"Predict future and slow down early"**

#### Simple Meaning
- Looks at rate of change
- Brakes before overshooting
- Smoothens response

#### Real Example: Parking Car
- Approaching parking spot fast → Start braking early
- Avoids slamming into wall

#### Math (Simple)
`D control = Kd × (Rate of change of error)`

**Problem**: Sensitive to noise, can amplify rapid fluctuations

## PID Together

**Total Control Signal = P + I + D**

```
 Error ──┬──[P: Kp × error]──────────┐
         │                            ├──(+)── Control Output
         ├──[I: Ki × ∫ error dt]────┤
         │                            │
         └──[D: Kd × d(error)/dt]────┘
```

## What Each Does

| Component | Purpose | Effect |
|-----------|---------|--------|
| **P** | Main correction | Fast response |
| **I** | Zero steady error | Eliminates offset |
| **D** | Reduce overshoot | Smoothens response |

## Why PID is Powerful

### Flexibility
- Only P → Simple but has error
- PI → More accurate, slight overshoot
- PD → Fast and smooth, but drifts
- **PID → Best of all three!**

### Tuning
Adjust three knobs (Kp, Ki, Kd) to get:
- Speed you want
- Accuracy you need
- Smoothness you prefer

## Real-World PID Example: Cruise Control

### Without PID:
- Set speed 100 km/h
- Uphill → slows down (no compensation)
- Downhill → speeds up

### With PID:
**P**: Going 90 km/h (error = -10) → Increase throttle proportionally
**I**: Been slow for a while → Increase throttle more (eliminate error completely)
**D**: Speed increasing fast → Reduce throttle rate (prevent overshoot)

**Result**: Maintains exactly 100 km/h on all terrains!

## Another Example: Temperature Control

### Heating Room from 15°C to 25°C

**P alone**:
- Big temperature difference → heater full blast
- Gets close to 25°C → heater reduces
- **Problem**: Settles at 24°C (not quite 25°C)

**PI together**:
- P brings it close fast
- I notices "still 1°C short"
- I keeps adding heat until exactly 25°C reached
- **Problem**: Might overshoot to 26°C

**PID together**:
- P brings it close fast
- D predicts it's approaching fast → starts reducing heat early
- I fine-tunes to exactly 25°C
- **Result**: Fast, accurate, minimal overshoot!

## Key Insight
**PID is like a skilled human operator**:
- **P**: Main control action (your immediate reaction)
- **I**: Learning from repeat errors (your experience)
- **D**: Anticipating trouble (your intuition)

Together, they make an intelligent, adaptive controller!
        """,
        "order": 1
    },
    {
        "title": "Tuning basics",
        "content": """
# PID Tuning - Finding the Sweet Spot

## The Challenge

You have three knobs: Kp, Ki, Kd

How to set them for good performance?

## What Happens If...

### Kp Too High
- **Good**: Fast response
- **Bad**: Oscillations, overshoot
- **Very high**: Instability!

### Kp Too Low
- **Good**: Stable, smooth
- **Bad**: Sluggish, slow
- **Very low**: Barely responds

---

### Ki Too High
- **Good**: Eliminates error quickly
- **Bad**: Big overshoot, oscillations
- **Very high**: Unstable oscillations

### Ki Too Low
- **Good**: Stable
- **Bad**: Never reaches target exactly
- **Very low**: Persistent error

---

### Kd Too High
- **Good**: Very smooth response
- **Bad**: Amplifies noise, jittery
- **Very high**: System fights itself

### Kd Too Low
- **Good**: Ignores noise
- **Bad**: More overshoot
- **Very low**: No damping benefit

## Trial-and-Error Intuition

**This is an art, not exact science!**

### Step-by-Step Method

#### 1. Start with All Zeros
`Kp = 0, Ki = 0, Kd = 0`

#### 2. Add P First
- Increase Kp slowly
- Stop when system responds reasonably
- Accept some steady-state error for now
- **Goal**: Get 50-70% of desired response speed

#### 3. Add I Next
- Start with small Ki
- Increase until steady-state error eliminated
- Watch for overshoot
- **Goal**: Eliminate error without big oscillations

#### 4. Add D Last
- Start with small Kd
- Increase to reduce overshoot from I
- Stop if noise becomes a problem
- **Goal**: Smooth out response

#### 5. Fine-Tune All Three
- Go back to Kp, adjust for speed
- Tweak Ki for accuracy
- Tweak Kd for smoothness
- **Iterate until satisfied!**

## Ziegler-Nichols Method (Popular)

### Simplified Steps

1. **Set Ki = 0 and Kd = 0** (P controller only)
2. **Increase Kp until system oscillates**
3. **Note the Kp value (call it Ku)** and oscillation period (call it Tu)
4. **Calculate**:
   - Kp = 0.6 × Ku
   - Ki = 1.2 × Ku / Tu
   - Kd = 0.075 × Ku × Tu

5. **Test and fine-tune from here**

**This gives you a starting point, not final values!**

## Visual Effects of Each Parameter

### Increasing Kp
```
Response:  Gets faster and higher overshoot
     ↑         ╱──╲         ╱────╲
     │       ╱      ╲     ╱        ╲
     │    ╱─          ╲─╱
     └──────────────────────→ time
   Small Kp    Medium Kp   Large Kp
```

### Increasing Ki
```
Response: Eliminates error but causes overshoot
     ↑       ╱───╲           ╱─────╲
     │     ╱─     ╲         ╱─       ╲
     │   ╱─        ╲───  ╱─          ──
     │ ╱─                             
     └──────────────────────→ time
  Small Ki        Large Ki
   (has error)   (oscillates)
```

### Increasing Kd
```
Response: Smoothens and reduces overshoot
     ↑         ╱──╲
     │       ╱─    ╲      ╱───
     │     ╱─       ╲───╱
     │   ╱─
     └──────────────────────→ time
  Small Kd      Large Kd
  (oscillates)   (smooth)
```

## Common Tuning Mistakes

### 1. Tuning Too Aggressively
- Making huge changes to parameters
- **Better**: Small incremental changes

### 2. Not Testing Edge Cases
- Testing only one condition
- **Better**: Test with different loads, speeds, disturbances

### 3. Ignoring Noise
- Setting Kd too high
- **Better**: Watch for jitter, reduce Kd if needed

### 4. Over-Optimizing
- Spending days for 1% improvement
- **Better**: Good enough is often good enough!

## Real-World Tuning Example: Quadcopter

### Step 1: P Only
- Set Kp until quad responds to stick
- It's wobbly but flies
- Has steady-state tilt error

### Step 2: Add I
- Quad now levels perfectly
- But oscillates a bit

### Step 3: Add D
- Oscillations damped
- Smooth flight!

### Step 4: Fine-Tune
- Increase Kp for sharper response
- Reduce Ki slightly to avoid I-windup
- Tweak Kd for perfect smoothness

**Result**: Locked-in hover, responsive flight!

## Software Tools

Most modern systems have **auto-tuning**:
- System tests itself
- Discovers optimal values
- Saves you time!

**But**: Understanding manual tuning helps you:
- Fix when auto-tune fails
- Optimize further
- Troubleshoot problems

## Key Takeaway
**Tuning is iterative**:
1. Start conservative
2. Test real system
3. Adjust based on behavior
4. Repeat until satisfied

**No perfect formula - experience matters!**

Like:
- Cooking: Recipe is a start, taste and adjust!
- Sports: Learn basics, practice makes perfect

**Most important**: Understand what each knob does, then tune by feel!
        """,
        "order": 2
    },
    {
        "title": "Control systems in robotics",
        "content": """
# Control Systems in Robotics

Robots are **control systems on wheels (or legs)!**

## Speed Control

### Example: Mobile Robot
**Goal**: Robot moves at exact 1 m/s

**Challenge**:
- Battery voltage drops over time
- Floor friction varies
- Going uphill/downhill

**Solution**: PID speed controller
- **P**: Speed error → adjust motor power
- **I**: Maintain exact speed despite voltage drop
- **D**: Smooth acceleration/deceleration

**Real application**: Mars rovers, delivery robots

---

## Position Control

### Example: Robot Arm Picking Object
**Goal**: Move gripper to exact XYZ coordinates

**Challenge**:
- Arm has weight (gravity)
- Joints have friction
- Load varies (empty vs holding object)

**Solution**: PID position controller for each joint
- **P**: Distance from target → move proportionally
- **I**: Eliminate final positioning error
- **D**: Prevent overshoot (don't slam into object!)

**Real application**: Factory automation, surgical robots

---

## Line Following Robots

### How It Works

**Sensors**: Detect line position (left/center/right)

**Control Goal**: Keep line centered under robot

**Simple P Controller**:
```
Error = Line Position - Center
Motor Speed (Left) = Base Speed + Kp × Error  
Motor Speed (Right) = Base Speed - Kp × Error
```

**Behavior**:
- Line to left → Turn left (left motor slower)
- Line to right → Turn right (right motor faster)
- Line centered → Go straight

### Improvement with PID

**P** alone makes robot **oscillate** around line (wiggles)

**Adding D**: Predicts when approaching center → smoothens path

**Adding I**: Compensates for sensor bias, motor differences

### Real Application
- Warehouse robots following magnetic tape
- Automated guided vehicles (AGVs)
- Farming robots following crop rows

---

## Practical Robot Control Examples

### 1. Drone Altitude Hold

**Sensors**: Barometer, sonar, camera

**Controller**: PID altitude control

**How it works**:
- Measure current altitude
- Compare with desired altitude
- Adjust throttle to maintain height

**Challenges**:
- Wind gusts (disturbance)
- Battery voltage drop
- Sensor noise

**Solution**: Well-tuned PID handles all!

---

### 2. Self-Balancing Robot

**Example**: Segway, hoverboard

**Physics**: Inverted pendulum (naturally unstable!)

**Control Strategy**:
- Measure tilt angle (IMU sensor)
- If tilting forward → Drive forward to catch up
- If tilting backward → Drive backward

**Controller**: Very fast PID loop (100-1000 Hz)

**Why it's hard**:
- Must react FAST (milliseconds)
- Any delay → falls over
- Requires good sensor fusion

---

### 3. Robotic Vacuum Cleaner

**Multiple Control Loops**:

**Navigation**: Follow planned path
- PID steering control
- Sensor: Wheels odometry, gyroscope

**Wall Following**: Stay close to wall
- PID distance control
- Sensor: IR distance sensor

**Obstacle Avoidance**: Don't crash
- Bang-bang control (on/off)
- Sensor: Bumper, ultrasonic

---

## Cascaded Control in Robots

Often robots use **multiple PID loops nested**:

### Example: Drone

```
Position Controller (outer loop, slow)
    ↓
Velocity Controller (middle loop, medium)
    ↓
Attitude Controller (inner loop, fast)
    ↓
Motor PWM
```

**Why cascade?**
- Position control needs velocity control to work
- Velocity control needs attitude control to work
- Attitude control drives motors

Each loop runs at different speeds:
- Position: 10 Hz (slow, long-term goal)
- Velocity: 50 Hz (medium, immediate motion)
- Attitude: 500 Hz (fast, stabilization)

---

## Real-World Robot Control Challenges

### 1. Sensor Noise
- Encoders have jitter
- IMUs drift over time
- **Solution**: Filtering, sensor fusion

### 2. Delays
- Computation time
- Communication latency
- **Solution**: Fast microcontroller, low-latency protocols

### 3. Nonlinearities
- Friction not constant
- Motors have dead zones
- **Solution**: Calibration, adaptive control

### 4. Multiple Objectives
- Go fast AND avoid obstacles AND save battery
- **Solution**: Priority-based control, optimization

---

## From Theory to Practice

**Control theory gives you tools**:
- PID algorithm
- Stability analysis
- Tuning methods

**Robotics adds reality**:
- Noisy sensors
- Limited computation
- Real-world disturbances
- Safety constraints

**Success** = Theory + Practice + Testing!

---

## Key Insight

**Every robot movement is a control problem**:
- Want it to go somewhere? → Position control
- Want it at certain speed? → Velocity control
- Want it balanced? → Attitude control
- Want it to follow line? → Steering control

**Master control systems → Build amazing robots!**
        """,
        "order": 3
    },
    {
        "title": "Control in automation & industries",
        "content": """
# Control Systems in Automation & Industries

## Process Control

### What is a Process?
Any industrial operation that transforms inputs into outputs:
- Chemical reactions
- Food production
- Material processing
- Energy generation

### Common Process Variables
- **Temperature** (ovens, reactors, furnaces)
- **Pressure** (boilers, pipes, vessels)
- **Flow rate** (liquids, gases)
- **Level** (tanks, silos)
- **pH** (chemical processes)
- **Composition** (mixing, separation)

### Example: Chemical Reactor Temperature Control

**Setup**:
- Reactor vessel
- Heating element (input)
- Temperature sensor (feedback)
- PID controller

**How it works**:
1. Set desired temperature (e.g., 150°C)
2. Measure actual temperature
3. PID calculates heater power needed
4. Maintain exactly 150°C ± 1°C

**Why precise control matters**:
- Wrong temp → Bad product quality
- Too hot → Safety hazard, explosion risk
- Too cold → Reaction doesn't complete

**Industries using this**:
- Pharmaceutical (drug synthesis)
- Petrochemical (refining)
- Food (pasteurization, cooking)

---

## Motor Drives & Control

### What are Motor Drives?
Electronic systems that control motor speed, torque, position

### Types of Motor Control

#### 1. Speed Control
**Application**: Conveyor belts, fans, pumps

**Control Goal**: Constant RPM regardless of load

**Controller**: PI controller
- **P**: Speed error → Adjust voltage/current
- **I**: Eliminate steady-state error

**Example**: Paper mill
- Paper web must move at exact speed
- Any variation → Wrinkles,tears
- PI controller maintains ±0.1% speed accuracy

#### 2. Torque Control
**Application**: Cranes, elevators, hoists

**Control Goal**: Precise force application

**Example**: Elevator
- Accelerate smoothly (comfort)
- Constant torque during motion
- Gentle stop at floor

#### 3. Position Control
**Application**: CNC machines, robotic arms

**Control Goal**: Exact positioning

**Example**: CNC milling machine
- Must position tool to 0.01mm accuracy
- PID loops for X, Y, Z axes
- Cuts exactly to CAD design

---

## Manufacturing Systems

### Assembly Line Control

**Example**: Automobile Assembly

**Multiple synchronized controls**:
- Conveyor speed control (constant 0.5 m/min)
- Robot arm position control (welding points)
- Paint spray flow control (even coating)
- Oven temperature control (curing)

**Challenge**: All must work together perfectly!

**Solution**: Master PLCProgrammable Logic Controller) coordinates all

### Quality Control

**Example**: Bottle Filling

**Control loops**:
1. **Fill level control**: Exactly 500 ml per bottle
2. **Capping torque control**: Not too loose, not too tight
3. **Labeling position control**: Label straight

**Vision systems** + PID control → Reject bad bottles automatically

---

## Energy & Power Systems

### Power Plant Control

**Example**: Steam Power Plant

**Critical controls**:
- **Boiler pressure**: Must be stable (explosions if not!)
- **Temperature**: Superheated steam temperature
- **Generator frequency**: Exactly 50 or 60 Hz
- **Load sharing**: Multiple generators in sync

**Complexity**: Thousands of PID loops working together

### Building HVAC

**Heating, Ventilation, Air Conditioning**

**Control objectives**:
- Temperature zones (different rooms, different temps)
- Humidity control (comfort)
- Air quality (CO₂ levels)
- Energy efficiency (minimize cost)

**Example**: Office building
- 50+ temperature sensors
- 20+ zone controllers  
- Master controller optimizes energy
- Saves 30-40% energy vs uncontrolled

---

## Food & Beverage Industry

### Pasteurization Control

**Example**: Milk Processing

**Critical**: Temperature & time
- Too low → Bacteria survive
- Too high → Nutrients destroyed

**Controller**: PID temperature control
- Must maintain exact temp profile
- Timing synchronized with flow rate
- Safety-critical application!

### Brewing Control

**Example**: Beer Fermentation

**Multiple variables**:
- Temperature (different stages)
- Pressure (carbonation)
- pH level
- Sugar content (measured indirectly)

**Automated control** → Consistent taste batch after batch

---

## Water & Wastewater Treatment

### Water Treatment Plant

**Control loops**:
1. **pH control**: Add chemicals to neutralize
2. **Chlorine dosing**: Disinfection level
3. **Flow control**: Even distribution
4. **Level control**: Tank levels

**Why automation**:
- 24/7 operation needed
- Consistent water quality
- Regulatory compliance
- Reduced labor cost

---

## Safety & Protection Systems

### Industrial Safety

**Example**: Pressure Safety

**Normal control**: PID maintains 10 bar pressure

**Safety layer**: If pressure > 12 bar
- Emergency valve opens
- System shuts down
- Alarm triggers

**Layers of protection**:
1. Normal PID control
2. High/low alarms
3. Emergency shutdown
4. Physical relief valves

**Why critical**: Prevent:
- Explosions
- Chemical leaks
- Equipment damage
- Human injury

---

## Real-World Control Complexity

### Modern Factory

**Example**: Semiconductor Fabrication

- 1000+ control loops
- Temperature accuracy: ±0.01°C
- Pressure accuracy: ±0.001 mbar
- Vibration isolation control
- Clean room air flow control

**All controlled by**:
- PLCs (Programmable Logic Controllers)
- SCADA (Supervisory Control And Data Acquisition)
- DCS (Distributed Control System)

---

## Industry 4.0 - Smart Factories

**Modern trends**:
- IoT sensors everywhere
- Cloud-based monitoring
- AI/ML for optimization
- Predictive maintenance

**But foundation is still**:
Classic control theory!
- PID controllers
- Cascade control
- Feedforward control

**Advanced techniques** built on top of solid control fundamentals.

---

## Key Takeaway

**Control systems are invisible heroes of industry**:
- Make products consistently
- Ensure safety
- Save energy
- Reduce waste
- Enable automation

**Every industrial process = Multiple control loops!**

Understanding control → Understand modern manufacturing!
        """,
        "order": 4
    },
    {
        "title": "Embedded & real-time control",
        "content": """
# Embedded & Real-Time Control

## What is Embedded Control?

**Embedded system**: Computer built into a product (not a general-purpose PC)

**Examples**:
- Microwave controller
- Car engine control unit (ECU)
- Washing machine logic
- Drone flight controller
- 3D printer controller

**Why "embedded"?**
- Dedicated to specific task
- Built into the device
- Runs one program forever

---

## Microcontroller + Sensor + Actuator

### The Control Loop Components

```
     ┌──────────────────┐
     │  Microcontroller │
     │   (Brain/Logic)  │
     └─────┬─────▲──────┘
           │     │
           ▼     │
        Actuator │ Sensor
        (Action) │ (Measurement)
           │     │
           ▼     │
     ┌─────────────────┐
     │   Real World    │
     │    (System)     │
     └─────────────────┘
```

### Example: Thermostat

**Microcontroller**: Arduino, ESP32, PIC
- Runs PID algorithm
- Makes decisions

**Sensor**: Temperature sensor (DHT22, DS18B20)
- Measures room temperature
- Sends to microcontroller

**Actuator**: Relay controlling heater
- Microcontroller turns ON/OFF
- Heats the room

**Loop**:
1. Read temperature (sensor)
2. Compare with setpoint
3. Calculate PID output
4. Turn heater ON/OFF (actuator)
5. Wait 1 second
6. Repeat forever!

---

## Control Loop Execution

### Typical Code Structure

```c
void loop() {
    // 1. Read sensor
    float actual_temp = read_temperature_sensor();
    
    // 2. Calculate error
    float error = setpoint - actual_temp;
    
    // 3. PID calculation
    float P = Kp * error;
    float I += Ki * error * dt;
    float D = Kd * (error - previous_error) / dt;
    float output = P + I + D;
    
    // 4. Apply control (actuator)
    set_heater_power(output);
    
    // 5. Wait for next cycle
    delay(dt);  // e.g., 100ms
}
```

**This runs hundreds/thousands of times per second!**

---

## Real-Time Requirements

### What is "Real-Time"?

**Not** "very fast"

**Actual meaning**: "Predictable timing"

**Example**: Airbag deployment
- Must inflate within 20-30 milliseconds
- **Not**: As fast as possible
- **But**: Exactly when needed, reliably

### Hard Real-Time vs Soft Real-Time

#### Hard Real-Time
**Missing deadline = System failure**

**Examples**:
- Airbag controller (life/death)
- Anti-lock brakes (ABS)
- Flight control system
- Nuclear reactor control

**Characteristics**:
- Guaranteed response time
- No delays accepted
- Usually RTOS (Real-Time OS)

#### Soft Real-Time
**Missing deadline = Reduced performance**

**Examples**:
- Video streaming (skip a frame, no big deal)
- Sensor data logging
- Temperature control (1 second late is okay)

**Characteristics**:
- Best-effort timing
- Occasional delays acceptable
- Can use regular embedded OS

---

## Control Loop Timing

### Sample Rate (How Fast to Run Loop?)

**Too slow**:
- System can become unstable
- Misses fast changes
- Poor performance

**Too fast**:
- Wastes computation
- Sensor noise amplified (especially D term)
- Power consumption high

### Choosing Sample Rate

**Rule of thumb**: 10-100× faster than system response

**Examples**:

| System | Response Time | Sample Rate |
|--------|---------------|-------------|
| Temperature control | ~10 seconds | 1-10 Hz (0.1-1s) |
| Motor speed control | ~100 ms | 100-1000 Hz (1-10ms) |
| Drone attitude | ~10 ms | 500-2000 Hz (0.5-2ms) |
| Current control | ~1 ms | 10-100 kHz (10-100µs) |

---

## Real-World Embedded Control Example

### Quadcopter Flight Controller

**Hardware**:
- Microcontroller: STM32F4 (168 MHz)
- Sensors: IMU (gyro + accel), barometer, GPS
- Actuators: 4 brushless motor ESCs

**Control loops** (multiple frequencies!):

1. **Attitude loop** (500 Hz):
   - PID for roll, pitch, yaw
   - Stabilizes drone orientation
   - **Critical**: Must be fast!

2. **Altitude loop** (50 Hz):
   - PI for height control
   - Slower okay (altitude doesn't change fast)

3. **Position loop** (10 Hz):
   - PI for GPS lat/long
   - Even slower (GPS updates slowly)

**Why different rates?**
- Fast loops for fast-changing variables
- Slow loops for slow-changing variables
- Saves computation

---

## Common Embedded Platforms

### For Beginners
- **Arduino** (Atmega328, 16 MHz)
  - Simple, easy to learn
  - Good for slow control (temperature, LEDs)
  - Not for real-time critical

### For Serious Projects
- **ESP32** (Dual-core, 240 MHz)
  - WiFi/Bluetooth built-in
  - Fast enough for motor control
  - Popular for IoT + control

- **STM32** (ARM Cortex-M, 72-480 MHz)
  - Professional choice
  - Real-time capable
  - Drones, robots, industrial

- **Raspberry Pi** (Linux-based)
  - Full computer
  - Not hard real-time
  - Good for vision + control

---

## Challenges in Embedded Control

### 1. Limited Resources
- Limited RAM (few KB to MB)
- Limited flash (program storage)
- Slow CPU compared to PC

**Solution**: Efficient code, fixed-point math, optimize PID

### 2. Sensor Noise
- ADC noise
- Electromagnetic interference
- Vibrations

**Solution**: Filtering, sensor fusion, proper grounding

### 3. Integer Math vs Floating Point
- Many microcontrollers slow at floating-point
- Fixed-point math faster but trickier

**Example**: Instead of `float`, use `int16_t` with scaling

### 4. Timing Precision
- Interrupts can delay loop
- Need careful timing management

**Solution**: Hardware timers, RTOS, interrupt priorities

---

## Practical Implementation Tips

### 1. Start Simple
- Test with P controller first
- Add I and D only if needed
- Verify each step

### 2. Use Libraries
- Don't reinvent the wheel
- PID libraries available for Arduino, etc.
- Focus on tuning, not coding

### 3. Debugging
- Print sensor values to serial
- Plot in real-time (Arduino Serial Plotter)
- Use oscilloscope for fast signals

### 4. Safety First
- Limit actuator output (don't burn motors!)
- Watchdog timer (restart if code hangs)
- Emergency stop button

---

## Real Product Development

**Typical process**:

1. **Prototype**: Arduino/ESP32, breadboard
2. **Test**: Tune PID, verify performance
3. **PCB Design**: Custom board for product
4. **Production**: Mass manufacturing
5. **Certification**: Safety, EMI testing

**Control theory stays the same**, hardware evolves!

---

## Key Insight

**Modern products = Embedded control everywhere**:
- Your car: 50-100 microcontrollers!
- Smart home: Thermostats, lights, security
- Appliances: Washing machine, fridge, oven
- Toys: Drones, RC cars

**Learning embedded control** = **Building actual products!**

---

## Progress Checkpoint 🎯
**"I can apply control systems to real products!"**

You've completed the entire Control Systems Learning Roadmap! 🎉

### What You've Mastered:
✅ **Foundations**: Systems, feedback, open/closed loop
✅ **M.odeling**: Electrical, mechanical, transfer functions  
✅ **Time Domain**: Response, stability, performance metrics
✅ **Frequency Domain**: Bode, Nyquist, margins
✅ **Controllers**: PID design, tuning, applications
✅ **Real Systems**: Robotics, industry, embedded systems

### Next Steps:
1. **Build projects**: Start with Arduino + sensor + motor
2. **Practice tuning**: Try PID on real systems
3. **Explore advanced**: State-space, adaptive control, optimal control
4. **Specialize**: Robotics, process control, automotive, aerospace

**You now see control systems everywhere! Use this knowledge to build amazing things! 🚀**
        """,
        "order": 5
    }
]

for topic_data in topics_stage5:
    Topic.objects.create(
        stage=stage5,
        title=topic_data["title"],
        content=topic_data["content"],
        order=topic_data["order"]
    )
    print(f"  ✅ Added topic: {topic_data['title']}")

print(f"\n🎉🎉🎉 **COMPLETE!** Control Systems Learning Roadmap fully created!")
print(f"\n📊 Final Statistics:")
print(f"   - Total Stages: 5")
print(f"   - Stage 1 (Foundations): 6 topics")
print(f"   - Stage 2 (Mathematical Modeling): 7 topics")
print(f"   - Stage 3 (Time Domain Analysis): 6 topics")
print(f"   - Stage 4 (Frequency Domain Analysis): 5 topics")
print(f"   - Stage 5 (Controllers & Applications): 5 topics")
print(f"   - **Total Topics: 29 topics**")
print(f"\n✨ The roadmap is now live and accessible to your users!")
