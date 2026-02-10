
import os
import django
import sys

# Add project root to sys.path
sys.path.append('/Users/saitejakaki/Divakar/devaproject')

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import Roadmap, RoadmapCategory, Stage, Topic

def create_verilog_rtl_roadmap():
    """Create Verilog RTL Roadmap"""
    
    print("🚀 Initializing Verilog RTL Roadmap Creation...")
    
    # 1. Get Category
    # 'electronics-embedded'
    category, _ = RoadmapCategory.objects.get_or_create(
        slug='electronics-embedded',
        defaults={'name': 'Electronics & Embedded Systems'}
    )
    
    # 2. Create Roadmap
    roadmap_slug = 'verilog-rtl-mastery'
    roadmap_title = 'Verilog RTL for VLSI Engineers'
    
    roadmap, created = Roadmap.objects.get_or_create(
        slug=roadmap_slug,
        defaults={
            'title': roadmap_title,
            'short_description': 'Stop thinking like a programmer. Start thinking like hardware. Master synthesizable Verilog, RTL design patterns, and the industry standard VLSI flow.',
            'description': 'A professional roadmap for Electronics/VLSI engineers. Learn to write clean, synthesizable Verilog RTL that maps perfectly to silicon. Covers Synchronous Design, FSMs, Pipelining, Static Timing concepts, and how to avoid costly silicon bugs.',
            'category': category,
            'difficulty': 'advanced',
            'estimated_hours': 80,
            'is_premium': True,
            'is_featured': True,
            'is_active': True,
            'price': 499
        }
    )
    
    if created:
        print(f"✅ Created Roadmap: {roadmap.title}")
    else:
        print(f"ℹ️  Roadmap '{roadmap.title}' already exists. Updating details...")
        # Clear stages for fresh import
        roadmap.stages.all().delete()
        print("   ♻️  Cleared existing stages for fresh import.")
        
    # ==========================================
    # STAGE 1: RTL THINKING FUNDAMENTALS (FREE)
    # ==========================================
    stage1 = Stage.objects.create(
        roadmap=roadmap,
        title='RTL Thinking Fundamentals',
        description='Grounding yourself in hardware-centric thinking.',
        order=1,
        is_free=True
    )
    
    topics_s1 = [
        {
            'title': 'The Parallel Hardware View (NOT C Code)',
            'content': """# Hardware Description, Not Software

## Concurrency
- In C/Python, code runs line-by-line.
- In Verilog, **everything happens at once**.
- Each `always` block represents a separate piece of hardware running in parallel.

## Clocked Behavior
- **Synchronous Design**: Changes only happen on the clock edge (posedge clk).
- **Registers (Flops)**: Provide memory and stability.
- **Combinational Logic**: Computes values *between* registers.

## Common Mistakes
- Thinking `always` blocks execute sequentially.
- Using `#10` delays (Simulation only! Ignored in silicon).
- Forgetting Resets (Hardware starts in random state).
""",
            'order': 1
        },
        {
            'title': 'Registers vs Combinational Logic',
            'content': """# The Physical Silicon

## 1:1 Mapping
- **RTL (Register Transfer Level)** maps directly to Flops and Gates.
- **Sequential Logic**: Lives in Flip-Flops. Updates on Clock.
- **Combinational Logic**: Lives in Gates (AND, OR, MUX). Updates instantly (propagation delay).

## The Flow
1. Clock rises -> Flops capture new values.
2. Signals race through Combinational Logic.
3. Signals arrive at next Flop setup input *before* next clock.
""",
            'order': 2
        },
        {
            'title': 'Simulation vs Synthesis',
            'content': """# It works in Sim, but fails in Chip?

## The Dangerous Gap
- You can write Verilog that simulates fine but creates garbage hardware.
- **Initial Blocks**: Used for testbenches only. Do NOT use in RTL.
- **File I/O**: Synthesizers cannot read files.
- **Inferred Latches**: If you forget an `else` in combinational logic, you get a Latch (Bad timing, glitches).

## Rule of Thumb
- If it doesn't map to a Flop or a Gate, it's not Synthesizable.
""",
            'order': 3
        }
    ]
    
    for t in topics_s1:
        Topic.objects.create(stage=stage1, **t)
    print(f"   ✨ Added {len(topics_s1)} topics to Stage 1")


    # ==========================================
    # STAGE 2: CORE VERILOG RTL CONCEPTS
    # ==========================================
    stage2 = Stage.objects.create(
        roadmap=roadmap,
        title='Core Verilog RTL Concepts',
        description='Building blocks of synthesizable code.',
        order=2,
        is_free=False
    )
    
    topics_s2 = [
        {
            'title': 'Reg vs Wire & Assignments',
            'content': """# Data Types & Flow

## Reg vs Wire
- **Wire**: A physical connection. Driven by `assign` or module output.
- **Reg**: Storage variable. Driven inside `always` blocks. (Note: In SystemVerilog, `logic` replaces both).

## Blocking (=) vs Non-blocking (<=)
- **Use `<=` (Non-blocking)** for **Sequential Logic** (Clocked).
    - Updates all registers in parallel at end of step.
    - `a <= b; b <= a;` swaps values correctly.
- **Use `=` (Blocking)** for **Combinational Logic**.
    - Executes order-dependent.

## The Deadly Mistake
- Using `=` inside `always @(posedge clk)` causes Race Conditions.
""",
            'order': 1
        },
        {
            'title': 'Always Blocks & Sensitivity',
            'content': """# Defining Processes

## Sequential Block
```verilog
always @(posedge clk or negedge rst_n) begin
  if (!rst_n) q <= 0;
  else        q <= d;
end
```
- Infers Flip-Flops.

## Combinational Block
```verilog
always @(*) begin
  y = a & b;
end
```
- Infers Gates.
- **`@(*)`**: Auto-senses all inputs. NEVER list signals manually (prone to errors).
- **Default Values**: Always assign a default to prevent **Inferred Latches**.
""",
            'order': 2
        },
        {
            'title': 'Reset Strategies',
            'content': """# Initializing the Chip

## Synchronous vs Asynchronous
- **Synchronous**: Reset only happens on clock edge. (Cleaner timing, used in FPGAs).
- **Asynchronous**: Reset happens instantly. (Used in ASICs).

## Active Low Convention (`rst_n`)
- Industry standard is Active Low.
- `if (!rst_n)`

## No Gate Clocks Manually
- **Bad**: `assign gated_clk = clk & en;` (Glitches!).
- **Good**: Use Clock Enables inside logic.
  ```verilog
  if (en) q <= d;
  ```
""",
            'order': 3
        }
    ]
    
    for t in topics_s2:
        Topic.objects.create(stage=stage2, **t)
    print(f"   ✨ Added {len(topics_s2)} topics to Stage 2")


    # ==========================================
    # STAGE 3: RTL DESIGN PATTERNS
    # ==========================================
    stage3 = Stage.objects.create(
        roadmap=roadmap,
        title='RTL Design Patterns',
        description='Designing Counters, FSMs, and Datapaths.',
        order=3,
        is_free=False
    )
    
    topics_s3 = [
        {
            'title': 'Counters & Pipelining',
            'content': """# Moving Data

## The Counter
- Just a register adding 1 to itself.
- Watch out for **Overflow**. Define widths clearly `reg [3:0] cnt`.

## Pipelining (For Speed)
- Breaking a long logic path into smaller steps with Flops in between.
- **Why**: Increases Max Frequency (Fmax).
- **Trade-off**: Increases Latency (Cycles to result) and Area (More flops).

## Thought Exercise
- Trace a signal cycle-by-cycle. "In cycle 1 it's here, Cycle 2 it's there."
""",
            'order': 1
        },
        {
            'title': 'Finite State Machines (FSMs)',
            'content': """# Control Logic

## Industry Standard: 2-Process FSM
1.  **Sequential Block**: Updates `state` register.
2.  **Combinational Block**: Calculates `next_state` based on inputs.

```verilog
// 1. State Reg
always @(posedge clk) state <= next_state;

// 2. Next State Logic
always @(*) begin
  next_state = state; // Default
  case (state)
    IDLE: if (start) next_state = RUN;
    RUN:  if (done)  next_state = IDLE;
  endcase
end
```
- **Clean**: Avoids mixing output logic with state logic.
- **Safe**: Always have a `default` case.
""",
            'order': 2
        },
        {
            'title': 'Simulation Mismatches',
            'content': """# Trust Issues

## X-Propagation
- In Sim, uninitialized regs are 'X'.
- In Silicon, they are 0 or 1 (Random).
- **Bug**: `if (val == 1)` might be false in sim (if X), but true in silicon.

## Race Conditions
- Caused by mixing blocking/non-blocking assignments.
- Simulation order might differ from synthesis reality.
""",
            'order': 3
        }
    ]
    
    for t in topics_s3:
        Topic.objects.create(stage=stage3, **t)
    print(f"   ✨ Added {len(topics_s3)} topics to Stage 3")


    # ==========================================
    # STAGE 4: RTL QUALITY & INDUSTRY EXPECTATIONS
    # ==========================================
    stage4 = Stage.objects.create(
        roadmap=roadmap,
        title='RTL Quality & Industry Expectations',
        description='Writing job-ready code.',
        order=4,
        is_free=False
    )
    
    topics_s4 = [
        {
            'title': 'Coding Style & Standards',
            'content': """# Professional Code

## Naming Conventions
- `clk`, `rst_n` (Active low).
- `_r` or `_q` for registered signals.
- `_nxt` for next-state signals.

## Parameterization
- **Never Hardcode Numbers**: Don't write `7:0`.
- Use `parameter WIDTH = 8;`. Makes code reusable.

## Linting
- Tools (SpyGlass, Verilator) check for code quality.
- **Zero Warnings** policy is common in top companies.
""",
            'order': 1
        },
        {
            'title': 'Interview Questions',
            'content': """# Testing Your Knowledge

## 1. "Blocking vs Non-Blocking?"
- Explanation of race conditions and sequential vs combinational.

## 2. "How to detect an Inferred Latch?"
- Missing `else` or incomplete `case`.

## 3. "Synchronous vs Asynchronous Reset?"
- Pros/Cons in timing and area.

## 4. "Coding a simple FSM"
- Be ready to write the 2-process FSM template on a whiteboard.
""",
            'order': 2
        }
    ]
    
    for t in topics_s4:
        Topic.objects.create(stage=stage4, **t)
    print(f"   ✨ Added {len(topics_s4)} topics to Stage 4")


    # ==========================================
    # STAGE 5: RTL IN THE VLSI FLOW
    # ==========================================
    stage5 = Stage.objects.create(
        roadmap=roadmap,
        title='RTL in the VLSI Flow',
        description='From Code to GDSII.',
        order=5,
        is_free=False
    )
    
    topics_s5 = [
        {
            'title': 'Synthesis & STA',
            'content': """# Mapping to Reality

## Synthesis
- Translating RTL into a **Netlist** of standard cells (NAND, D-FF) from a library.
- Optimization for Area, Power, and Speed.

## Static Timing Analysis (STA)
- Checking if signals meet **Setup** and **Hold** times.
- **Constraint**: `create_clock -period 10 [get_ports clk]`.
- Bad RTL (Combinational Loops, Deep Logic) causes Timing Violations.
""",
            'order': 1
        },
        {
            'title': 'The Cost of Bugs',
            'content': """# Why Verification matters

## The 10x Rule
- Finding a bug in RTL: $0 (Just fix code).
- Finding a bug in Netlist: $1,000s (Re-synthesis).
- Finding a bug in Silicon: $1,000,000s (Re-spin mask set).

## "Golden RTL"
- Once verified, RTL is "frozen".
- No changes allowed without rigorous re-testing.
""",
            'order': 2
        }
    ]
    
    for t in topics_s5:
        Topic.objects.create(stage=stage5, **t)
    print(f"   ✨ Added {len(topics_s5)} topics to Stage 5")

    # Update stats
    roadmap.update_stats()
    print("✅ Verilog RTL Roadmap creation complete! Stats updated.")

if __name__ == '__main__':
    create_verilog_rtl_roadmap()
