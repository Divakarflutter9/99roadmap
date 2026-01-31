
"""
Add C Language Roadmap for ECE/Embedded Systems Students
Focuses on hardware interaction, memory control, and embedded firmware.
"""

import os
import django
import sys

# Setup Django
sys.path.append('/Users/saitejakaki/Divakar/devaproject')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import Roadmap, RoadmapCategory, Stage, Topic

def create_ece_c_roadmap():
    """Create C for Embedded Systems Roadmap"""
    
    # Get or create Embedded Systems category
    category, _ = RoadmapCategory.objects.get_or_create(
        slug='embedded-systems',
        defaults={
            'name': 'Embedded Systems & IoT',
            'icon': 'fas fa-microchip',
            'description': 'Master hardware-software interaction, firmware, and IoT'
        }
    )

    # Create roadmap
    roadmap, created = Roadmap.objects.get_or_create(
        slug='c-for-embedded-systems',
        defaults={
            'title': 'C for Electronics & Embedded Systems',
            'short_description': 'Master C for Hardware: From Blinking LEDs to Firmware Development.',
            'description': 'The definitive roadmap for ECE/EEE students. Learn how C controls microcontrollers, manages capabilities, and drives VLSI validation. Essential for careers in Qualcomm, Texas Instruments, Intel, and Bosch.',
            'category': category,
            'difficulty': 'intermediate',
            'estimated_hours': 140,
            'is_premium': True,
            'is_featured': True,
            'is_active': True
        }
    )
    
    if created:
        print(f"✅ Created roadmap: {roadmap.title}")
    else:
        print(f"ℹ️  Roadmap already exists: {roadmap.title}")
        # Proceeding to ensure content is added/updated in a real scenario, but standard logic applies.

    # ==========================================
    # STAGE 1: Programming Foundations
    # ==========================================
    stage1, _ = Stage.objects.get_or_create(
        roadmap=roadmap,
        title='Programming Foundations',
        defaults={
            'description': 'Understand how software controls hardware. The basics with an electronics perspective.',
            'order': 1,
            'is_free': True
        }
    )

    topics_stage1 = [
        {
            'title': 'What Programming Means in Electronics',
            'content': '''# Programming in Electronics

## Software: The Soul of the Machine
For an ECE engineer, programming is not about building websites. It is about **controlling electrons**.
*   **Web Dev**: "Show this button on screen."
*   **Embedded Dev**: "Send 3.3V to Pin 14 to turn on the relay."

### The Microcontroller (MCU)
Think of a microcontroller (Arduino, STM32, PIC) as a tiny brain.
*   **CPU**: The thinking part.
*   **GPIO**: The hands (Input/Output pins).
*   **Peripherals**: The senses (ADC, UART, I2C).
*   **Memory**: The short-term (RAM) and long-term (Flash) storage.

### Why C?
C is the **lingua franca** of hardware.
*   **Direct Hardware Access**: C lets you write to specific memory addresses (registers) to control hardware features.
*   **Efficiency**: Limited RAM (e.g., 2KB) and Flash requires highly optimized code.
*   **Speed**: Real-time systems (airbags, pacemakers) need microsecond reactions. Python is too slow/unpredictable here.

## The compilation flow for Hardware
1.  **Write C Code** on Laptop.
2.  **Cross-Compile**: Compile *for* the ARM/AVR architecture (not your laptop's Intel/M1 chip).
3.  **Link**: Combine with startup files (setting up stack pointer).
4.  **Flash**: Burn the `.bin` or `.hex` file into the MCU's Flash memory.

> **Key Mindset**: Your code doesn't float in the cloud. It burns into silicon and moves electricity.
''',
            'order': 1
        },
        {
            'title': 'Structure of a C Program',
            'content': '''# Structure of a C Program

## The Embedded Context
A standard C program ends. An embedded program **never** ends.

### The Infinite Loop
```c
#include <stdint.h> 

void main() {
    // 1. Initialization Code
    setup_gpio();
    init_uart();

    // 2. The Super Loop
    while (1) {
        read_sensor();
        process_data();
        control_motor();
    }
}
```
*   **`setup()`**: Runs once on power-up. Configure pins as Input/Output.
*   **`while(1)`**: The device runs forever until power is cut. There is no OS to return `0` to!

### Header Files
*   `#include <avr/io.h>` or `#include "stm32f4xx.h"`
*   These files map human names (like `PORTA`) to specific hex addresses (like `0x40020000`).

## Comments & Documentation
In hardware code, comments are critical.
*   Bad: `// Set bit 5`
*   Good: `// Set bit 5 to enable Temperature Sensor internal reference`
''',
            'order': 2
        },
        {
            'title': 'Data Types & Operators',
            'content': '''# Data Types & Operators

## Precision Matters
In desktop apps, an `int` is usually 32-bit. In embedded, it might be 16-bit. Ambiguity kills.

### stdint.h - The Embedded Standard
Always use fixed-width integer types from `<stdint.h>`.

| Type | Bits | Range | Usage |
| :--- | :--- | :--- | :--- |
| `uint8_t` | 8 | 0 to 255 | Flags, Pixel color, ASCII char |
| `int8_t` | 8 | -128 to 127 | Signed sensor data (Temperature) |
| `uint16_t`| 16 | 0 to 65,535 | ADC readings (0-1023), Counters |
| `uint32_t`| 32 | 0 to 4 Billion | Addresses, Timestamps |

### Why `unsigned`?
Hardware registers are usually unsigned.
*   A 10-bit ADC value is just "magnitude". It's not negative.
*   Bitwise operations can behave oddly with signed numbers (sign extension).

### The Size Constraint
*   **RAM**: Often only 2KB to 32KB.
*   Using `double` (8 bytes) instead of `float` (4 bytes) unnecessarily can waste 50% of your sensor buffer!
''',
            'order': 3
        },
        {
            'title': 'Compilation Process (High Level)',
            'content': '''# Compilation Process

## From C to Silicon
How does `PORTA |= 1;` become voltage?

### 1. Preprocessing
Expands defines.
`#define LED_PIN 5` -> code becomes `5`.

### 2. Compilation
Translates C to **Assembly** instructions for specific architecture (e.g., ARM Cortex-M4).
*   `LDR R0, [Address]` (Load Register)
*   `ORR R0, R0, #1` (Or Operation)
*   `STR R0, [Address]` (Store Register)

### 3. Assembly
Translates instructions to **Machine Code** (Hex codes like `E59F`).

### 4. Linking (Crucial for Embedded)
The Linker Script (`.ld` file) tells the code **where** to live.
*   **Code (.text)**: Goes to FLASH (Read-only, non-volatile).
*   **Variables (.data)**: Goes to RAM (Read-write, volatile).
*   **Map File**: The output file telling you exactly how much memory each function consumes.

> **Interview Q**: "What is the difference between `.text`, `.data`, and `.bss` sections?"
> *   `.text`: Code (Flash)
> *   `.data`: Initialized variables (RAM copy)
> *   `.bss`: Zero-initialized variables (RAM)
''',
            'order': 4
        }
    ]

    for topic in topics_stage1:
        Topic.objects.get_or_create(stage=stage1, title=topic['title'], defaults=topic)
        
    print(f"✅ Stage 1 complete: {len(topics_stage1)} topics")

    # ==========================================
    # STAGE 2: Core C for Hardware Control
    # ==========================================
    stage2, _ = Stage.objects.get_or_create(
        roadmap=roadmap,
        title='Core C for Hardware Control',
        defaults={
            'description': 'The toolkit for manipulating registers. Pointers and Bitwise math are your main tools.',
            'order': 2,
            'is_free': False
        }
    )

    topics_stage2 = [
        {
            'title': 'Pointers: The Hardware Interface',
            'content': '''# Pointers: The Hardware Interface

## Pointers are Addresses
In embedded C, a pointer is not just an abstract reference. It is a **physical wire address**.

### Accessing Registers via Pointers
A hardware register (like `GPIO_ODR` - Output Data Register) is just a memory address, say `0x40021014`.

How to write to it?
```c
#define GPIOA_ODR  ((volatile uint32_t *) 0x40021014)

void turn_on_led() {
    *GPIOA_ODR = 0x01; // Write 1 to address 0x40021014
}
```
*   `(uint32_t *)`: Cast the number to a pointer type.
*   `*`: Dereference to write to that destination.

### Arrays vs Pointers
*   **Buffer Handling**: Communication protocols (UART/SPI) send bytes. Pointers are efficient for iterating through these buffers.
*   `uart_send_string(char *str)`: Sends characters until `\0`.

### Null Pointers
In desktop, dereferencing `NULL` (0x0) crashes.
In embedded, `0x0` might be the **Reset Vector** or start of Flash! Writing there could brick the device (or do nothing if Flash is protected).
''',
            'order': 1
        },
        {
            'title': 'Bitwise Operations',
            'content': '''# Bitwise Operations

## The Surgical Knife of Embedded C
Registers are 32-bit blocks. You often need to change **just one bit** (e.g., Turn on simple LED) without affecting the others (e.g., Motor status).

### 1. Setting a Bit (OR `|`)
**Goal**: Set bit 5 to 1.
```c
// logic: x OR 1 = 1, x OR 0 = x
REGISTER = REGISTER | (1 << 5);
// Shorthand:
REGISTER |= (1 << 5);
```

### 2. Clearing a Bit (AND `&` NOT `~`)
**Goal**: Set bit 5 to 0.
```c
// logic: x AND 0 = 0, x AND 1 = x
REGISTER = REGISTER & ~(1 << 5);
// Shorthand:
REGISTER &= ~(1 << 5);
```

### 3. Toggling a Bit (XOR `^`)
**Goal**: Flip bit 5.
```c
REGISTER ^= (1 << 5);
```

### 4. Checking a Bit
**Goal**: Is bit 5 high?
```c
if (REGISTER & (1 << 5)) {
    // Bit is 1
}
```

### Real World Example
```c
// ADC Control Register
// Bit 0: Enable ADC
// Bit 1: Start Conversion
ADC_CR |= (1 << 0); // Enable
ADC_CR |= (1 << 1); // Start
```
''',
            'order': 2
        },
        {
            'title': 'Arrays & Structures in Hardware',
            'content': '''# Arrays & Structures in Hardware

## Memory Mapping with Structs
Instead of defining `#define` for every register, vendors use Structures to map memory.

### Struct Mapping
Imagine a timer peripheral has registers at offset 0x00, 0x04, 0x08.
```c
typedef struct {
    volatile uint32_t CTRL;  // Offset 0x00
    volatile uint32_t LOAD;  // Offset 0x04
    volatile uint32_t VAL;   // Offset 0x08
} Timer_Type;

#define TIMER1 ((Timer_Type *) 0x40000000)

void setup_timer() {
    TIMER1->LOAD = 1000; // Writes to 0x40000004
    TIMER1->CTRL = 1;    // Writes to 0x40000000
}
```
This is how STM32 HAL libraries are written. It's clean and readable.

### Struct Alignment & Padding
**Warning**: Hardware doesn't like unaligned access.
*   `struct { char c; int i; }` usually takes 8 bytes, not 5.
*   **Packed Structures**: `__attribute__((packed))` forces compiler to use 5 bytes. Useful for network packets (Zigbee/BLE) where every byte counts.
''',
            'order': 3
        }
    ]

    for topic in topics_stage2:
        Topic.objects.get_or_create(stage=stage2, title=topic['title'], defaults=topic)
    
    print(f"✅ Stage 2 complete: {len(topics_stage2)} topics")

    # ==========================================
    # STAGE 3: Embedded-Oriented C
    # ==========================================
    stage3, _ = Stage.objects.get_or_create(
        roadmap=roadmap,
        title='Embedded-Oriented C',
        defaults={
            'description': 'Concepts unique to the hardware world: Volatile, Interrupts, and Time.',
            'order': 3,
            'is_free': False
        }
    )

    topics_stage3 = [
        {
            'title': 'The Volatile Keyword',
            'content': '''# The Volatile Keyword

## The Most Important Interview Question
"What does `volatile` mean?"

### The Concept
It tells the compiler: **"Stop! Do not optimize this variable. Its value can change at any time, outside your control."**

### Why?
The compiler assumes it is the only one changing memory.
```c
int flag = 0;
// Wait for hardware button to set flag to 1
while (flag == 0) {
    // Do nothing
}
```
**Compiler Think**: "flag is 0. Loop body doesn't touch flag. Flag will always be 0. I will replace this with `while(true)`."
**Result**: Code hangs forever, even if button is pressed.

### The Fix
```c
volatile int flag = 0;
```
**Compiler Think**: "The user said `volatile`. I must re-read `flag` from memory every single time I check the condition."

### Where to use?
1.  **Memory-Mapped Registers**: Hardware changes values (e.g., Status Register).
2.  **Global Variables shared with ISRs**: Interrupt changes the variable.
3.  **Multi-threaded apps**: Another thread changes the variable.
''',
            'order': 1
        },
        {
            'title': 'Interrupt Concept using C',
            'content': '''# Interrupts in C

## Async World
Programs don't just run line-by-line. Hardware events **interrupt** the CPU.

### Interrupt Service Routine (ISR)
A special C function that runs when an event (Timer finished, Pin change, UART byte received) occurs.

```c
// Example ISR for Button Press
void EXTI0_IRQHandler(void) {
    if (check_pending_bit()) {
        toggle_led();
        clear_pending_bit(); // CRITICAL!
    }
}
```

### Rules for ISRs
1.  **Keep it Short**: Do the minimal work (set a flag) and exit. Long ISRs block other important tasks.
2.  **No Return/Args**: ISRs are called by hardware, not your code. They take no arguments and return nothing.
3.  **Reentrancy**: Be careful using functions like `printf` or `malloc` inside ISRs. They are often not interrupt-safe.

### Vector Table
How does CPU know which function to call?
A pointer array (Vector Table) at address 0x0000 holds addresses of all ISR functions.
''',
            'order': 2
        },
        {
            'title': 'Timing & Delay',
            'content': '''# Timing & Delay

## Controlling Time
Hardware often needs precise timing (Bit-banging protocols, LED blinking).

### 1. Blocking Delay (Naive)
```c
void delay(int count) {
    while(count--) {
        __asm("nop"); // Do nothing instruction
    }
}
```
*   **Pros**: Simple.
*   **Cons**: Wastes CPU cycles. Battery drain. Unpredictable if compiler optimizes loop.

### 2. Hardware Timer Delay
Use a hardware timer peripheral.
1.  Set Timer to tick every 1 microsecond.
2.  Load value 1000.
3.  Wait for "Update Flag".
*   **Pros**: Accurate, independent of CPU speed.

### 3. Non-Blocking (State Machine)
Instead of waiting, check time validity.
```c
if (current_time - last_time > 1000) {
    toggle_led();
    last_time = current_time;
}
```
Allows performing other tasks while waiting.
''',
            'order': 3
        }
    ]

    for topic in topics_stage3:
        Topic.objects.get_or_create(stage=stage3, title=topic['title'], defaults=topic)
    
    print(f"✅ Stage 3 complete: {len(topics_stage3)} topics")

    # ==========================================
    # STAGE 4: C in Embedded & VLSI Ecosystem
    # ==========================================
    stage4, _ = Stage.objects.get_or_create(
        roadmap=roadmap,
        title='C in Embedded & VLSI Ecosystem',
        defaults={
            'description': 'Moving beyond bare metal. Firmware, SDKs, and Chip Validation.',
            'order': 4,
            'is_free': False
        }
    )

    topics_stage4 = [
        {
            'title': 'C in Microcontroller SDKs',
            'content': '''# C in Microcontroller SDKs

## HAL and Drivers
You rarely write raw register code in production. You use **Vendor SDKs** (Software Development Kits).

### Low Level vs High Level
*   **Bare Metal**: `GPIOA->ODR = 1;` (Fast, Hard to read, Non-portable)
*   **HAL (Hardware Abstraction Layer)**: `HAL_GPIO_WritePin(GPIOA, PIN_5, SET);`

### How HAL works
It's just a giant wrapper of C structures and functions.
```c
void HAL_GPIO_WritePin(GPIO_TypeDef* GPIOx, uint16_t GPIO_Pin, GPIO_PinState PinState) {
    if (PinState == SET) {
        GPIOx->BSRR = GPIO_Pin;
    } else {
        GPIOx->BSRR = (uint32_t)GPIO_Pin << 16;
    }
}
```
*   **Understand the Underlayer**: If HAL has a bug (it happens), you need to be able to read the source code and fix the register logic.
''',
            'order': 1
        },
        {
            'title': 'C in VLSI Validation',
            'content': '''# C in VLSI Validation

## Testing the Chip Before/After Manufacture
VLSI engineers use C to verify that the silicon works as designed.

### Pre-Silicon Verification
*   Simulators/Emulators run C tests aginst the Verilog/VHDL design.
*   **Test**: Write C code to assert correct behavior.
    *   "Write 0xAA to Register X."
    *   "Read Register X. Is it 0xAA?"
    *   "If No -> FAIL."

### Post-Silicon Validation
*   The actual chip arrives.
*   Run C firmware to stress-test peripherals.
*   **Exercise**: "Run USB at max speed while writing to Flash at 85°C."
*   This C code is often closer to bare-metal than application firmware.

### Firmware vs Validation
*   **Firmware**: "Make product work reliably."
*   **Validation**: "Try to break the chip/Find hardware bugs."
''',
            'order': 2
        }
    ]

    for topic in topics_stage4:
        Topic.objects.get_or_create(stage=stage4, title=topic['title'], defaults=topic)
    
    print(f"✅ Stage 4 complete: {len(topics_stage4)} topics")

    # ==========================================
    # STAGE 5: Industry Readiness
    # ==========================================
    stage5, _ = Stage.objects.get_or_create(
        roadmap=roadmap,
        title='Industry Readiness',
        defaults={
            'description': 'Writing professional, optimized, and bug-free embedded code.',
            'order': 5,
            'is_free': False
        }
    )

    topics_stage5 = [
        {
            'title': 'Writing Optimized Embedded C',
            'content': '''# Writing Optimized Embedded C

## Squeezing Performance
Resources are scarce.

### 1. Size Optimization
*   **Use `const`**: `const int table[] = {1, 2, 3};` -> Stored in Flash (cheap). Without `const`, it might be copied to RAM (expensive).
*   **Small Types**: Use `uint8_t` for loops `0-10`.

### 2. Speed Optimization
*   **Inline Functions**: Use `static inline` for small, frequent functions to avoid function call overhead.
*   **Bit Shifting**: `x >> 1` is often faster than `x / 2` (though modern compilers are smart).
*   **Lookup Tables**: Instead of `sin(x)` (slow math), use a pre-calculated array `sin_table[x]`.

### 3. Power Optimization
*   **Sleep Modes**: If C code has nothing to do, don't `while(1)`. execute `__WFI()` (Wait For Interrupt) to put CPU to sleep.
''',
            'order': 1
        },
        {
            'title': 'Embedded Interview Questions',
            'content': '''# Embedded Interview Questions

## Top C Questions for Firmware Roles
1.  **"What affects the size of a structure?"**
    *   Answer: Variables and **padding** (alignment).
2.  **"Explain `static` in 3 contexts."**
    *   Global: File scope.
    *   Function: File scope.
    *   Local Variable: Persists value.
    *   *Embedded Context*: Static locals are not on stack!
3.  **"How to detect Endianness of a system?"**
    ```c
    int i = 1; 
    char *c = (char*)&i;
    // if *c is 1 -> Little Endian (LSB first)
    ```
4.  **"What is a Reentrant function?"**
    *   A function safely callable from multiple tasks/ISRs. Uses no global static variables.
5.  **"Set bit 3 of address 0x2000."**
    ```c
    *(volatile uint8_t *)0x2000 |= (1<<3);
    ```

## Career Paths
*   **Embedded Software Engineer**: Writing firmware for products (Fitbit, Tesla).
*   **Validation Engineer**: Testing chips (Intel, Qualcomm).
*   **Drivers Developer**: Unix/Linux Kernel (NVIDIA, AMD).
''',
            'order': 2
        }
    ]

    for topic in topics_stage5:
        Topic.objects.get_or_create(stage=stage5, title=topic['title'], defaults=topic)
    
    print(f"✅ Stage 5 complete: {len(topics_stage5)} topics")
    print("\n🎉 ECE C Roadmap creation complete!")

if __name__ == '__main__':
    create_ece_c_roadmap()
