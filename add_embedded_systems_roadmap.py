"""
Add Embedded Systems Roadmap
Complete roadmap for ECE/BTech students to become industry-ready Embedded Engineers
"""

import os
import django
import sys

sys.path.append('/Users/saitejakaki/Divakar/devaproject')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import Roadmap, RoadmapCategory, Stage, Topic

def create_embedded_roadmap():
    """Create comprehensive Embedded Systems roadmap"""
    
    # Get Category
    # Using 'embedded-systems' if available, else 'electronics-hardware'
    try:
        category = RoadmapCategory.objects.get(slug='embedded-systems')
    except RoadmapCategory.DoesNotExist:
        category = RoadmapCategory.objects.get(slug='electronics-hardware')
    
    # Create Roadmap
    roadmap, created = Roadmap.objects.get_or_create(
        slug='embedded-systems-specialist',
        defaults={
            'title': 'Embedded Systems Specialist',
            'short_description': 'From absolute basics to industry-ready Embedded Engineer. Master C, Microcontrollers, Protocols, and RTOS.',
            'description': 'A clear, step-by-step roadmap designed for ECE & BTech students to master Embedded Systems. Learn how software controls hardware, understand microcontrollers, debug real systems, and prepare for core industry jobs.',
            'category': category,
            'difficulty': 'intermediate',
            'estimated_hours': 120,
            'is_premium': True,
            'is_featured': True,
            'is_active': True
        }
    )
    
    if created:
        print(f"✅ Created roadmap: {roadmap.title}")
    else:
        print(f"ℹ️  Roadmap already exists: {roadmap.title}")
        # Clear existing structure to rebuild
        roadmap.stages.all().delete()
        print("   Rebuilding stages...")

    # 📍 Stage 1: Embedded Systems Basics
    stage1 = Stage.objects.create(
        roadmap=roadmap,
        title='Embedded Systems Basics',
        description='Build a clear understanding of what Embedded Systems are and how they differ from general software.',
        order=1,
        is_free=True
    )
    
    Topic.objects.create(
        stage=stage1,
        title='Introduction to Embedded Systems',
        content='''# What is an Embedded System?

*   **Definition**: An integrated system comprising hardware and software designed to perform a specific dedicated function within a larger system.
*   **Key Difference**: 
    *   **General Purpose Systems (e.g., Laptops)**: Can run games, browsers, editors simultaneously. Designed for versatility.
    *   **Embedded Systems (e.g., Washing Machine)**: Designed to do *one thing* strictly and efficiently (wash clothes).
*   **Hardware + Software**: 
    *   **Hardware (Body)**: Microcontroller, sensors, actuators.
    *   **Software (Soul)**: The code (Firmware) that tells the hardware what to do.
*   **Real-Life Examples**:
    *   **Consumer Electronics**: Microwave, Digital Camera, Smart Watch.
    *   **Automotive**: Airbag System, ABS (Anti-lock Braking System).
    *   **Medical**: Pacemaker, MRI Machine.
    *   **Industrial**: Robotic Arms, Assembly Line Controllers.

### Why this matters?
Understanding the "constrained" nature of embedded systems (limited memory, power, processing speed) is the first step to writing efficient code for them.
''',
        order=1
    )

    # 📍 Stage 2: Embedded Programming Basics
    stage2 = Stage.objects.create(
        roadmap=roadmap,
        title='Embedded Programming Basics',
        description='Learn how software communicates with and controls hardware using C.',
        order=2,
        is_free=True
    )

    Topic.objects.create(
        stage=stage2,
        title='C Programming for Embedded',
        content='''# C Programming for Embedded Systems

*   **Why C?**: It allows direct hardware manipulation and is highly efficient.
*   **Key Concepts**:
    *   **Pointers**: Essential for accessing specific memory addresses and registers.
    *   **Structures & Unions**: Used to map hardware registers and organize data.
    *   **Bitwise Operations**:
        *   AND (`&`): Clear bits (turn off).
        *   OR (`|`): Set bits (turn on).
        *   XOR (`^`): Toggle bits.
        *   Shift (`<<`, `>>`): Move bits to specific positions.
    *   **Volatile Keyword**: Tells compiler not to optimize a variable because it can change unexpectedly (by hardware).
    *   **Infinite Loops**: `while(1)` is standard because embedded software never "exits" until power is cut.

### Memory Basics (Intuition)
*   **Flash (ROM)**: where your code lives (like a book on a shelf). Read-only during execution.
*   **SRAM (RAM)**: where variables live (scratchpad). Data is lost when power goes.
*   **Registers**: Special switches inside the microcontroller that control peripherals (e.g., "Turn on LED at pin 5").
''',
        order=1
    )

    # 📍 Stage 3: Microcontrollers & Interfacing
    stage3 = Stage.objects.create(
        roadmap=roadmap,
        title='Microcontrollers & Interfacing',
        description='Work with real hardware. Understand the brain of the embedded system.',
        order=3,
        is_free=False
    )

    Topic.objects.create(
        stage=stage3,
        title='Microcontroller Fundamentals',
        content='''# working with Microcontrollers (MCU)

*   **What is an MCU?**: A small computer on a single chip containing a CPU, Memory, and IO peripherals.
*   **GPIO (General Purpose Input/Output)**:
    *   **Output**: Driving a pin High (3.3V/5V) or Low (0V). Used for LEDs, Relays, Buzzers.
    *   **Input**: Reading voltage state. Used for Buttons, Switches.
*   **Timers**:
    *   Internal clocks used to measure time intervals or generate delays without stopping the CPU.
*   **Interrupts**:
    *   A signal that stops the CPU's current task to handle a high-priority event (e.g., Emergency Stop button pressed).
    *   Better than "Polling" (constantly checking "is button pressed?").
*   **Reading Datasheets**:
    *   The "User Manual" for chips.
    *   Look for: Pin Diagram, Electrical Characteristics, Register Maps.

### Interfacing Examples
*   **LED**: Basics of current limiting resistors.
*   **Button**: Pull-up vs Pull-down resistors to avoid floating states.
*   **Sensors**: Reading analog data (Temperature, Light) using ADC (Analog to Digital Converter).
''',
        order=1
    )

    # 📍 Stage 4: Communication & Debugging
    stage4 = Stage.objects.create(
        roadmap=roadmap,
        title='Communication & Debugging',
        description='Build reliable systems by making components talk to each other.',
        order=4,
        is_free=False
    )

    Topic.objects.create(
        stage=stage4,
        title='Common Communication Protocols',
        content='''# Communication Protocols

*   **Why Protocols?**: To let the MCU talk to sensors, displays, or other MCUs.
*   **UART (Universal Asynchronous Receiver-Transmitter)**:
    *   Simple, 2 wires (TX, RX).
    *   Used for: Debugging (printing messages to PC), GPS modules, Bluetooth.
*   **I2C (Inter-Integrated Circuit)**:
    *   2 wires (SDA - Data, SCL - Clock).
    *   Supports multiple devices (Master-Slave).
    *   Used for: Sensors, EEPROMs, RTCs.
*   **SPI (Serial Peripheral Interface)**:
    *   4 wires (MISO, MOSI, SCK, CS).
    *   Faster than I2C.
    *   Used for: SD Cards, Displays (TFT/LCD), High-speed ADC.

### Debugging & Reliability
*   **Debugging Tools**:
    *   **Multimeter**: Checking voltages and connections.
    *   **Logic Analyzer**: Visualizing communication signals (I2C/SPI/UART).
    *   **Debugger (JTAG/SWD)**: Stepping through code line-by-line using hardware tools.
*   **Common Issues**:
    *   **Timing**: Code running too fast/slow.
    *   **Power**: Insufficient current causing resets (Brown-out).
    *   **Noise**: Electrical interference on long wires.
''',
        order=1
    )

    # 📍 Stage 5: Industry-Level Embedded Skills
    stage5 = Stage.objects.create(
        roadmap=roadmap,
        title='Industry-Level Embedded Skills',
        description='Become job-ready with advanced concepts and professional practices.',
        order=5,
        is_free=False
    )

    Topic.objects.create(
        stage=stage5,
        title='Professional Embedded Development',
        content='''# Moving to Industry Level

*   **Embedded Design Flow**: Requirements -> Component Selection -> Schematic/PCB -> Firmware -> Testing.
*   **RTOS (Real-Time Operating System)**:
    *   **Concept**: An OS designed to run applications with very precise timing and reliability (e.g., FreeRTOS).
    *   **Why**: Managing multiple complex tasks (WiFi + Sensor + Display) simultaneously.
*   **Code Quality**:
    *   Modular Code: Writing reusable drivers.
    *   Comments & Documentation.
    *   Version Control (Git).
*   **Optimization**:
    *   Writing code that uses less RAM/Flash.
    *   Using Deep Sleep modes to save battery.

### Career & Next Steps
*   **Skills Gained**: C programming, Hardware interfacing, Schematic reading, Protocol debugging.
*   **Job Roles**: Embedded Software Engineer, Firmware Engineer, IoT Developer.
*   **Next Steps**:
    *   **Embedded Linux**: Building systems on Raspberry Pi / i.MX boards.
    *   **IoT**: Connecting embedded systems to the Cloud (MQTT, AWS IoT).
    *   **VLSI**: Designing the chips themselves (Verilog/VHDL).
''',
        order=1
    )

    print("✅ Roadmap creation complete!")

if __name__ == '__main__':
    create_embedded_roadmap()
