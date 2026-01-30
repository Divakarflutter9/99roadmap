import os
import sys
import django

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import Roadmap, Stage, Topic, RoadmapCategory

def create_vlsi_roadmap():
    # 1. Create/Get Category
    category, _ = RoadmapCategory.objects.get_or_create(
        name='Electronics & Hardware',
        defaults={
            'slug': 'electronics-hardware',
            'description': 'Master hardware design, embedded systems, and VLSI.'
        }
    )

    # 2. Create Roadmap
    roadmap, created = Roadmap.objects.get_or_create(
        slug='vlsi-front-end',
        defaults={
            'title': 'VLSI Front-End (RTL) Design',
            'description': 'A complete, end-to-end VLSI Front-End roadmap for active engineers and ECE students. Master RTL design from basics to industry-ready skills.',
            'category': category,
            'difficulty': 'intermediate',
            'estimated_hours': 120,
            'is_active': True,
            'is_premium': True
        }
    )
    
    if not created:
        print("Roadmap already exists. Updating...")
        roadmap.title = 'VLSI Front-End (RTL) Design'
        roadmap.description = 'A complete, end-to-end VLSI Front-End roadmap for active engineers and ECE students. Master RTL design from basics to industry-ready skills.'
        roadmap.save()

    # 3. Create Stages & Topics
    stages_data = [
        {
            'title': 'Stage 1: Digital Design Foundations',
            'description': 'Build a strong base for RTL design.',
            'order': 1,
            'is_free': True,
            'topics': [
                {
                    'title': 'Number Systems & Boolean Algebra',
                    'content': '''# Number Systems & Boolean Algebra
- Binary, Octal, Hexadecimal conversions
- Signed vs Unsigned numbers (2's complement)
- Boolean logic operations (AND, OR, NOT, XOR, NAND, NOR)
- De Morgan's Laws and simplification techniques
''',
                    'order': 1,
                    'duration': 45
                },
                {
                    'title': 'Logic Gates & Combinational Circuits',
                    'content': '''# Logic Gates & Combinational Circuits
- Truth tables and gate-level implementation
- Multiplexers (MUX), Demultiplexers (DEMUX)
- Encoders and Decoders
- Adders (Half, Full, Carry Lookahead)
- Designing combinational logic blocks
''',
                    'order': 2,
                    'duration': 60
                },
                {
                    'title': 'Sequential Circuits (Flip-Flops & Latches)',
                    'content': '''# Sequential Circuits
- Difference between Latches and Flip-Flops
- SR, JK, D, and T Flip-Flops
- Setup and Hold time concepts (Intuition)
- Registers and Counters (Synchronous vs Asynchronous)
- Finite State Machines (Mealy vs Moore) intro
''',
                    'order': 3,
                    'duration': 75
                },
                {
                    'title': 'Hardware vs Software Thinking',
                    'content': '''# Hardware vs Software Thinking
- Parallelism in hardware vs Sequential execution in software
- Concurrency concepts
- Propagation delay and timing constraints
- Why "loops" don't exist in hardware the same way
''',
                    'order': 4,
                    'duration': 45
                }
            ]
        },
        {
            'title': 'Stage 2: HDL Programming (Verilog)',
            'description': 'Learn to describe hardware using code.',
            'order': 2,
            'is_free': False,
            'topics': [
                {
                    'title': 'HDL Basics & Verilog Structure',
                    'content': '''# HDL Basics
- What is HDL (Hardware Description Language)?
- Verilog vs VHDL (Industry preference)
- Verilog Module structure (Ports, Parameters)
- Data types (wire, reg, logic, bit)
- Simulation vs Synthesis flow
''',
                    'order': 1,
                    'duration': 60
                },
                {
                    'title': 'Modeling Styles & Assignments',
                    'content': '''# Modeling Styles
- Gate-level modeling
- Dataflow modeling (assign statements)
- Behavioral modeling (always blocks)
- Blocking (=) vs Non-Blocking (<=) assignments (CRITICAL)
''',
                    'order': 2,
                    'duration': 75
                },
                {
                    'title': 'Combinational & Sequential RTL',
                    'content': '''# RTL Coding
- Writing synthesizable Combinational logic
- Writing synthesizable Sequential logic (Flip-flops)
- Sensitivity lists and common pitfalls
- Reset logic (Synchronous vs Asynchronous)
''',
                    'order': 3,
                    'duration': 75
                },
                {
                    'title': 'SystemVerilog Basics',
                    'content': '''# SystemVerilog Basics
- Why SystemVerilog?
- Enhanced data types (logic, int, byte)
- Structs and Enums
- Interfaces (concept level)
- SV for Design vs Verification
''',
                    'order': 4,
                    'duration': 60
                }
            ]
        },
        {
            'title': 'Stage 3: RTL Design Methodology',
            'description': 'Design real hardware blocks.',
            'order': 3,
            'is_free': False,
            'topics': [
                {
                    'title': 'RTL Design Flow',
                    'content': '''# Design Flow
- Specification to Architecture
- Micro-architecture definition
- RTL Coding -> Linting -> Simulation -> Synthesis
- Design tradeoffs (Area vs Speed vs Power)
''',
                    'order': 1,
                    'duration': 60
                },
                {
                    'title': 'FSM Design',
                    'content': '''# Finite State Machines (FSM)
- Designing robust FSMs in Verilog
- State encoding (Binary, One-hot, Gray)
- 3-Process FSM coding style
- Handling unused states and glitches
''',
                    'order': 2,
                    'duration': 90
                },
                {
                    'title': 'Datapath & Control Logic',
                    'content': '''# Datapath & Control
- Separating Control Path and Data Path
- Designing ALUs and Register Files
- Pipelining concepts (High-level)
- Handshaking protocols (Ready/Valid)
''',
                    'order': 3,
                    'duration': 90
                },
                {
                    'title': 'Code Quality & Linting',
                    'content': '''# Code Quality
- Coding guidelines (Naming conventions, Comments)
- What is Linting?
- Common Lint errors (Combinational loops, Latch inference)
- CDC (Clock Domain Crossing) basics
''',
                    'order': 4,
                    'duration': 60
                }
            ]
        },
        {
            'title': 'Stage 4: Functional Verification Basics',
            'description': 'Ensure RTL works correctly.',
            'order': 4,
            'is_free': False,
            'topics': [
                {
                    'title': 'Verification Overview',
                    'content': '''# Verification Basics
- Why verification takes 70% of the cycle
- Verification vs Validation
- Directed Testing vs Random Testing
- Code Coverage vs Functional Coverage
''',
                    'order': 1,
                    'duration': 60
                },
                {
                    'title': 'Testbench Architecture',
                    'content': '''# Testbench Architecture
- Stimulus, Driver, Monitor, Scoreboard (Concepts)
- Writing a simple linear Testbench in Verilog
- Generating clocks and resets
- Self-checking testbenches (Assertions basics)
''',
                    'order': 2,
                    'duration': 90
                },
                {
                    'title': 'Simulation & Debugging',
                    'content': '''# Debugging
- Running Simulations
- Waveform analysis (Finding the root cause)
- Debugging X-propagation
- Using $display and $monitor
''',
                    'order': 3,
                    'duration': 75
                }
            ]
        },
        {
            'title': 'Stage 5: Front-End Tools & Industry Flow',
            'description': 'Understand real company workflow.',
            'order': 5,
            'is_free': False,
            'topics': [
                {
                    'title': 'From RTL to GDSII',
                    'content': '''# Industry Flow
- RTL Design
- Logic Synthesis (Gate-level Netlist)
- Static Timing Analysis (STA)
- Place & Route (Physical Design Handoff)
- Signoff checks
''',
                    'order': 1,
                    'duration': 60
                },
                {
                    'title': 'EDA Tools Overview',
                    'content': '''# Industry Tools
- Simulation: VCS (Synopsys), Xcelium (Cadence), Questasim (Siemens)
- Synthesis: Design Compiler (Synopsys), Genus (Cadence)
- Linting: SpyGlass
- Debug: Verdi
''',
                    'order': 2,
                    'duration': 45
                },
                {
                    'title': 'PPA & Constraints',
                    'content': '''# PPA & Constraints
- Power, Performance, Area (PPA) trade-offs
- Basics of SDC (Synopsys Design Constraints)
- Clock definition and IO delays
- Low power design concepts (Clock Gating)
''',
                    'order': 3,
                    'duration': 60
                }
            ]
        },
        {
            'title': 'Stage 6: Job Readiness & Exposure',
            'description': 'Prepare for interviews & real roles.',
            'order': 6,
            'is_free': False,
            'topics': [
                {
                    'title': 'Interview Prep',
                    'content': '''# Interview Preparation
- Top 20 RTL Design Questions
- Digital Logic puzzles
- Verilog coding tests on whiteboard
- Behaviorial questions for VLSI roles
''',
                    'order': 1,
                    'duration': 60
                },
                {
                    'title': 'Roles & Companies',
                    'content': '''# Industry Roles
- RTL Design Engineer vs Design Verification (DV) Engineer
- FPGA Engineer vs ASIC Engineer
- Top Service Companies vs Product Companies
- Startups in the semiconductor space
''',
                    'order': 2,
                    'duration': 45
                },
                {
                    'title': 'Growth Path',
                    'content': '''# Career Growth
- Junior -> Senior -> Staff -> Principal Engineer
- Technical Track vs Management Track
- Continuing Education (Masters, Protocols like PCIe/DDR)
''',
                    'order': 3,
                    'duration': 45
                }
            ]
        }
    ]

    # Delete existing stages to avoid duplicates (optional, safe for clear update)
    Stage.objects.filter(roadmap=roadmap).delete()

    for stage_data in stages_data:
        stage = Stage.objects.create(
            roadmap=roadmap,
            title=stage_data['title'],
            description=stage_data['description'],
            order=stage_data['order'],
            is_free=stage_data.get('is_free', False)
        )
        print(f"Created Stage: {stage.title}")
        
        for topic_data in stage_data['topics']:
            Topic.objects.create(
                stage=stage,
                title=topic_data['title'],
                content=topic_data['content'],
                order=topic_data['order'],
                duration_minutes=topic_data['duration']
            )
            print(f"  - Created Topic: {topic_data['title']}")

    print("Successfully created VLSI Front-End Roadmap!")

if __name__ == '__main__':
    create_vlsi_roadmap()
