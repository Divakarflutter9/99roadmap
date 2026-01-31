
"""
Add C Language Roadmap for CSE Students
Complete roadmap starting from absolute basics to industry-level usage.
"""

import os
import django
import sys

# Setup Django
sys.path.append('/Users/saitejakaki/Divakar/devaproject')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import Roadmap, RoadmapCategory, Stage, Topic

def create_c_roadmap():
    """Create comprehensive C Language roadmap"""
    
    # Get or create Computer Science category
    category, _ = RoadmapCategory.objects.get_or_create(
        slug='data-structures-and-algorithms', # Using an existing relevant category or creating a new specific one. 
        # Actually, let's create a "Programming Foundations" category if tailored for basics
        defaults={
            'name': 'Programming Foundations',
            'icon': 'fas fa-code',
            'description': 'Master the core languages of Computer Science'
        }
    )
    
    # If the slug above was 'data-structures-and-algorithms' but we want 'foundations', let's just make a specific category check
    # But adhering to the user's "CS Fundamentals" goal, let's try to ensure it fits well. 
    # Let's create a specific one for "Programming Languages" to be safe and clean.
    category, _ = RoadmapCategory.objects.get_or_create(
        slug='programming-languages',
        defaults={
            'name': 'Programming Languages',
            'icon': 'fas fa-laptop-code',
            'description': 'Master the foundational languages of software engineering'
        }
    )

    # Create roadmap
    roadmap, created = Roadmap.objects.get_or_create(
        slug='c-programming-mastery',
        defaults={
            'title': 'C Language Mastery',
            'short_description': 'The Definitive C Roadmap for CSE Students: From Zero to System-Level Engineer.',
            'description': 'A complete guide designed for CSE students to master C. Covers logic building, memory management, pointers, and system programming to prepare you for DSA and placements.',
            'category': category,
            'difficulty': 'beginner', # Starts beginner, goes to advanced
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
        # Note: In a real update scenario, we might want to update the existing one, 
        # but for this script we'll assume we are running it once or want to skip if exists.
        # To ensure we update content, let's continue but we won't recreate stages if they exist, 
        # or we could clear them. For safety, let's return if it exists to avoid duplicates or assume the user deletes it first.
        # However, if the user wants to "add data", let's assume we proceed.
        # For simplicity in this turn, I'll proceed only if created or if I implement safe upserts.
        # Let's just return to avoid complex logic conflicts for now unless requested.
        pass

    # ==========================================
    # STAGE 1: Programming Foundations
    # ==========================================
    stage1, _ = Stage.objects.get_or_create(
        roadmap=roadmap,
        title='Programming Foundations',
        defaults={
            'description': 'Understand how programs actually run and the structure of C.',
            'order': 1,
            'is_free': True 
        }
    )

    topics_stage1 = [
        {
            'title': 'What Programming Really Means',
            'content': '''# What Programming Really Means

## The Bridge Between You and the Hardware
At its core, **programming** is the act of giving instructions to a computer to perform specific tasks. But for a Computer Science Engineer (CSE), it means much more. It's about **control**.

### 1. The Hierarchy of Language
Computers only understand **Binary (0s and 1s)**.
*   **High-Level Languages (Python, Java)**: Close to human language. Easy to write, but hides the details.
*   **Low-Level Languages (C, Assembly)**: Close to hardware. Complex, but gives you power over memory and performance.
*   **Machine Code**: The raw 0s and 1s the CPU executes.

### 2. Why C? The "Mother" of Languages
C is not just "another language". It is the foundation of modern computing.
*   **Operating Systems**: Windows, Linux, macOS are written in C.
*   **Embed Systems**: Microwaves, Cars, Mars Rovers run on C.
*   **Other Languages**: Python, Java, and PHP implementations are written in C.

> **Key concept**: Learning C teaches you **how computers actually work**, not just how to use them.

## Changing Your Mindset
*   **Don't just memorize syntax** (semicolons and brackets).
*   **Focus on Logic**: How do I solve this problem?
*   **Focus on Flow**: How does data move through the CPU and Memory?

## Summary
Programming in C is about talking directly to the hardware. It is the most critical skill for a strong CS foundation.
''',
            'order': 1
        },
        {
            'title': 'Structure of a C Program',
            'content': '''# Structure of a C Program

## Anatomy of a C File
Every C program follows a specific structure. Let's dissect the classic "Hello World".

```c
#include <stdio.h>    // 1. Preprocessor Directive

int main() {          // 2. Main Function
    printf("Hello!"); // 3. Statement
    return 0;         // 4. Return Statement
}
```

### 1. Preprocessor Directives (`#include`)
*   Before compiling, the **Preprocessor** scans the code.
*   `#include <stdio.h>` tells the compiler: "Copy the contents of the Standard Input/Output library header file here."
*   Without this, the computer wouldn't know what `printf` means.

### 2. The `main()` Function
*   The **Entry Point**. Every C program must have exactly one `main` function.
*   Execution **always** starts here.
*   `int`: The return type. It promises to return an integer to the OS (0 usually means "Success").

### 3. Statements & Semicolons
*   `printf("Hello!");` is a command to print to the screen.
*   **; (Semicolon)**: The full stop of C. It tells the compiler "This instruction ends here".

### 4. `return 0;`
*   Sends a status code back to the Operating System.
*   `0`: "I finished correctly."
*   `Non-zero`: "Something went wrong."

## Compilation Process (How it Runs)
You write code → **Preprocessor** → **Compiler** (Source to Assembly) → **Assembler** (Assembly to Object Code) → **Linker** (Combines libraries) → **Executable (.exe / .out)**.

> **Interview Tip**: Never just say "compile and run". Understand these 4 steps!
''',
            'order': 2
        },
        {
            'title': 'Variables & Data Types',
            'content': '''# Variables & Data Types

## Memory: The Container Concept
A **Variable** is a named container in the computer's RAM (Random Access Memory) used to store data.

### 1. Data Types
C is a **Statically Typed** language. You must tell the compiler *exactly* what kind of data you are storing so it knows how much memory to reserve.

| Type | Size (Typical) | Usage | Example |
| :--- | :--- | :--- | :--- |
| `int` | 4 bytes | Whole numbers | `int age = 21;` |
| `float` | 4 bytes | Decimals (6 digit precision) | `float pi = 3.14;` |
| `double`| 8 bytes | High-precision decimals | `double salary = 95000.50;` |
| `char` | 1 byte | Single character | `char grade = 'A';` |

> **Note**: Sizes can vary by system (32-bit vs 64-bit), which is crucial for system-level programming.

### 2. Variable Declaration vs Definition
```c
int a;       // Declaration (Tells compiler 'a' exists)
a = 10;      // Initialization (Assigns value)
int b = 20;  // Definition (Allocates memory + Assigns)
```

### 3. The `sizeof` Operator
A vital tool for seeing memory usage.
```c
printf("%lu", sizeof(int)); // Prints 4 (bytes)
```

## Common Junior Mistakes
1.  **Uninitialized Variables**: `int x; printf("%d", x);` prints **Garbage Value** (random memory data), not 0.
2.  **Overflow**: Storing 300 in a `char` (Max 127/255) generally causes data warping/wrapping.

## Why this Matters for CSE?
Understanding data types is understanding **Memory Allocation**. In high-level languages like Python, this is hidden. In C, you control every byte.
''',
            'order': 3
        },
        {
            'title': 'Input / Output',
            'content': '''# Input / Output (I/O)

## Interacting with the User
Programs are useless if they can't take input or show output. In C, we use `stdio.h` functions.

### 1. Output: `printf()`
"Print Formatted". It uses **Format Specifiers** to display data.

```c
int age = 20;
printf("I am %d years old.", age);
```

*   `%d`: Integer (Decimal)
*   `%f`: Float
*   `%c`: Character
*   `%s`: String (Chain of characters)
*   `%p`: Pointer address (Advanced)

### 2. Input: `scanf()`
"Scan Formatted". Reads input from the keyboard (Standard Input).

```c
int num;
scanf("%d", &num); // Notice the & (Ampersand)
```

### The Role of `&` (Address-Of Operator)
*   `scanf` needs to know **where** in memory to store the input.
*   `num` is the value.
*   `&num` is the **Address** (Memory Location) of `num`.
*   **Crucial Rule**: `scanf` always needs the address.

### Common Pitfalls
*   **Buffer Issues**: `scanf` leaves a newline character (`\n`) in the buffer if you hit Enter. This can skip the next `scanf` character input. (Fix: add a space `scanf(" %c", &ch);` or use `getchar()`).

## CSE Relevance
I/O operations are extremely slow compared to CPU calculations. Efficient coding often means minimizing unnecessary I/O.
''',
            'order': 4
        },
        {
            'title': 'Control Statements: If & Loops',
            'content': '''# Control Statements

## Controlling the Flow
Code usually runs top-to-bottom. Control statements allow you to branch (make decisions) or loop (repeat tasks).

### 1. Conditional Logic (`if-else`)
The CPU checks the "Status Register" to make decisions based on flags like Zero (Z) or Negative (N).

```c
if (score > 90) {
    printf("Grade A");
} else if (score > 75) {
    printf("Grade B");
} else {
    printf("Grade C");
}
```

### 2. Loops (Iteration)
Essential for automating repetitive tasks.

#### `for` Loop
Best when we know **how many times** to repeat.
```c
for (int i = 0; i < 5; i++) {
    printf("%d ", i); // 0 1 2 3 4
}
```

#### `while` Loop
Best when we repeat **until a condition is met**.
```c
while (battery > 10) {
    play_game();
}
```

#### `do-while` Loop
Runs at least once.
```c
do {
    input = get_user_input();
} while (input != -1);
```

### 3. Break and Continue
*   `break`: Exits the loop immediately.
*   `continue`: Skips the current iteration and jumps to the next one.

## Logical Thinking Practice
**Task**: Write a program to print a Pyramid Pattern.
```c
   *
  ***
 *****
```
*   Reasoning: You need nested loops. Outer loop for rows, inner loops for spaces and stars. This builds your algorithmic thinking.
''',
            'order': 5
        }
    ]

    for topic in topics_stage1:
        Topic.objects.get_or_create(stage=stage1, title=topic['title'], defaults=topic)
    
    print(f"✅ Stage 1 complete: {len(topics_stage1)} topics")

    # ==========================================
    # STAGE 2: Core C Concepts
    # ==========================================
    stage2, _ = Stage.objects.get_or_create(
        roadmap=roadmap,
        title='Core C Concepts',
        defaults={
            'description': 'Build logical thinking with arrays, functions, and the most critical concept: Pointers.',
            'order': 2,
            'is_free': False
        }
    )

    topics_stage2 = [
        {
            'title': 'Functions & Modular Programming',
            'content': '''# Functions & Modular Programming

## The Art of Decomposition
In industry, you never write 10,000 lines inside `main()`. You break problems into small, reusable chunks called **Functions**.

### 1. Function Syntax
```c
// ReturnType Name(Parameters)
int add(int a, int b) {
    return a + b;
}
```

### 2. How the Stack Works
When you call a function:
1.  A **Stack Frame** is pushed onto the memory stack.
2.  Local variables are created there.
3.  When the function returns, the frame is **popped** (destroyed).
4.  Local variables act "Dead" (Scope).

### 3. Pass by Value (Default in C)
```c
void change(int x) { x = 100; }
int main() {
   int num = 5;
   change(num); 
   printf("%d", num); // Still 5!
}
```
*   C copies the **value** of `num` into `x`. They are different memory locations.
*   To change `num`, you need **Pointers** (Pass by Reference simulation).

## Why Modular?
*   **Debuggability**: Isolate errors easily.
*   **Reusability**: Write once, use everywhere.
*   **Readability**: Code reads like English.
''',
            'order': 1
        },
        {
            'title': 'Arrays & Strings',
            'content': '''# Arrays & Strings

## Dealing with Collections
What if you need to store marks for 100 students? `int m1, m2, ..., m100;` is impossible. Use Arrays.

### 1. Arrays: Contiguous Memory
```c
int marks[5] = {90, 85, 88, 70, 95};
```
*   **Contiguous**: Stored side-by-side in RAM. If `mark[0]` is at address 1000, `mark[1]` is at 1004 (since int is 4 bytes).
*   **Access**: `marks[2]` gives 88.
*   **No Bounds Checking**: C will let you access `marks[100]` even if it doesn't exist. This causes Crashes or Security Exploits (Buffer Overflow).

### 2. Strings: Arrays of Characters
C has no "String" type. It uses `char` arrays terminated by a **Null Character (`\0`)**.

```c
char name[] = "Alice";
// Memory: ['A', 'l', 'i', 'c', 'e', '\0']
```
*   The `\0` tells function like `printf` to stop reading memory. Without it, it prints garbage until it hits a random 0.

### Key Functions (`string.h`)
*   `strlen()`: Length (count until `\0`).
*   `strcpy()`: Copy strings.
*   `strcmp()`: Compare (returns 0 if equal).

## CSE Insight
Arrays are the basis of **Data Structures**. Lists, Stacks, Queues, HashMaps—they all essentially run on array logic or pointer logic underneath.
''',
            'order': 2
        },
        {
            'title': 'Pointers: The Heart of C',
            'content': '''# Pointers: The Heart of C

## Demystifying Pointers
A **Pointer** is simply a variable that stores a **Memory Address** instead of a value.

### 1. Syntax
```c
int x = 10;
int *ptr = &x; // ptr holds the address of x
```
*   `&` (Address-Of): "Give me the address of x".
*   `*` (Dereference): "Go to the address inside ptr and get the value".

### 2. Visualization
*   `x` lives at Address `1004`. Value: `10`.
*   `ptr` lives at Address `2000`. Value: `1004`.

### 3. Why are they so important?
*   **Pass by Reference**: Modify variables across functions.
*   **Dynamic Memory**: Create data structures that grow.
*   **Performance**: Passing a massive array? Don't copy it. Just pass its address (4 or 8 bytes). Rapid!

### Example: Swapping Numbers
```c
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}
// Call: swap(&val1, &val2);
```

> **Warning**: Pointers are powerful but dangerous. A "Dangling Pointer" or "Null Pointer Dereference" crashes your program instantly (Segmentation Fault).
''',
            'order': 3
        },
        {
            'title': 'Memory Basics: Stack vs Heap',
            'content': '''# Memory Basics: Stack vs Heap

## Where does your data live?
When you run a program, the OS gives it memory segments.

### 1. The Stack
*   **What**: Stores local variables and function calls.
*   **Management**: Automatic. Variables die when functions return.
*   **Speed**: Extremely fast allocation.
*   **Size**: Small (Few MBs). Recursion too deep = **Stack Overflow**.

### 2. The Heap
*   **What**: Free floating memory for user-controlled allocation.
*   **Management**: Manual. You allocate (`malloc`) and you MUST free (`free`).
*   **Size**: Huge (GBs, limited by RAM).
*   **Lifetime**: Persists until you free it or program ends.

### Comparison
| Feature | Stack | Heap |
| :--- | :--- | :--- |
| Allocation | Automatic | Manual |
| Size | Fixed/Small | Dynamic/Large |
| Access Speed | Very Fast | Slower |
| Usage | Local vars | Dynamic Arrays, Trees |

## The Golden Rule of C Memory
**"If you malloc() it, you must free() it."**
Failing to free memory leads to **Memory Leaks**. Over time, your server runs out of RAM and crashes.
''',
            'order': 4
        }
    ]

    for topic in topics_stage2:
        Topic.objects.get_or_create(stage=stage2, title=topic['title'], defaults=topic)

    print(f"✅ Stage 2 complete: {len(topics_stage2)} topics")

    # ==========================================
    # STAGE 3: C for DSA & Problem Solving
    # ==========================================
    stage3, _ = Stage.objects.get_or_create(
        roadmap=roadmap,
        title='C for DSA & Problem Solving',
        defaults={
            'description': 'Transition from syntax to building complex logic. Prepare for technical interviews.',
            'order': 3,
            'is_free': False
        }
    )

    topics_stage3 = [
        {
            'title': 'Structures & Unions',
            'content': '''# Structures & Unions

## Defining Custom Types
Arrays store items of the *same* type. What if you need to store a Student (Name: string, Age: int, GPA: float)? Enter **Structures**.

### 1. Struct Syntax
```c
struct Student {
    char name[50];
    int age;
    float gpa;
};

struct Student s1;
s1.age = 21;
strcpy(s1.name, "Riya");
```

### 2. Memory Layout (Padding)
C aligns memory for speed.
*   `char` (1 byte) + `int` (4 bytes) might take **8 bytes**, not 5, due to **Padding**. The CPU reads typical chunks (Standard word size).

### 3. Unions: Saving Space
In a `struct`, every member gets its own memory. In a `union`, all members **share** the same memory space. Size = Size of largest member.
```c
union Data {
    int i;
    float f;
} data;
```
*   Use `data.i`, then `data.f`, but not both at once. Used in low-level driver code or embedded systems to save RAM.

## DSA Connection
Structs are the building blocks of Linked List Nodes and Tree Nodes.
```c
struct Node {
    int data;
    struct Node* next; // Self-referential pointer
};
```
''',
            'order': 1
        },
        {
            'title': 'Data Structures in C',
            'content': '''# Data Structures in C

## Building Blocks of Efficiency
You know logical loops and memory management. Now, let's build structures to organize data efficiently.

### 1. Linked Lists
Unlike arrays, Linked Lists are not contiguous.
*   **Concept**: A chain of nodes. Each node holds Data and a Pointer to the next node.
*   **Pros**: Dynamic size (grow as needed). Efficient insertions/deletions.
*   **Cons**: No random access (can't do `list[5]`).

### 2. Implementing a Node
```c
struct Node {
    int data;
    struct Node* next;
};
```
**Creation:**
1.  `malloc` a new node from Heap.
2.  Set data.
3.  Set `next` to NULL or another node.

### 3. Stacks & Queues
*   **Stack (LIFO)**: Last In, First Out. Like a stack of plates. Use for Undo features, Recursion management.
*   **Queue (FIFO)**: First In, First Out. Like a ticket line. Use for Printer tasks, BFS Algorithms.

## Why C for DSA?
In Java/Python, lists handle themselves. In C, **you** write the logic to connect pointers. If your Linked List code works, your understanding of pointers is solid. This is why top product companies ask C-based DSA questions.
''',
            'order': 2
        },
        {
            'title': 'Recursion',
            'content': '''# Recursion

## The Function That Calls Itself
Recursion is a method of solving a problem where the solution depends on solutions to smaller instances of the same problem.

### 1. Base Case & Recursive Case
Every recursive function needs a **Stop Condition** (Base Case).
```c
int factorial(int n) {
    if (n == 0) return 1;      // Base Case
    return n * factorial(n-1); // Recursive Case
}
```

### 2. Memory Visualization
*   `factorial(3)` calls `factorial(2)` calls `factorial(1)` calls `factorial(0)`.
*   Stack frames pile up.
*   `factorial(0)` returns 1. Stack unwinds.

### 3. Recursion vs Iteration
*   **Recursion**: Cleaner code for Trees/Graphs. High memory overhead (stack space).
*   **Iteration (Loops)**: More complex code sometimes, but memory efficient.

## Common Interview Question
"Write a recursive C program to generate the Nth Fibonacci number."
*   Trick: Naive recursion is O(2^n) - very slow. Use Memoization (Advanced) or Iteration (O(n)).
''',
            'order': 3
        },
        {
            'title': 'Time & Space Complexity',
            'content': '''# Time & Space Complexity

## Measuring Efficiency
Does your code run in 1 second or 1 year? Complexity Analysis tells us.

### 1. Big O Notation
Describes the **Worst Case** scenario growth rate.
*   **O(1) - Constant**: Accessing an array index `arr[5]`. Instant.
*   **O(n) - Linear**: Searching an unsorted array. Loop runs `n` times.
*   **O(n²) - Quadratic**: Nested loops (Bubble Sort). Slow for large data.
*   **O(log n) - Logarithmic**: Binary Search. Very fast. Cuts problem in half each step.

### 2. Space Complexity
How much RAM does your algorithm eat?
*   Creating an array of size `n`: **O(n)**.
*   Recursion depth `n`: **O(n)** stack space.

### 3. Optimization in C
C is fast, but a bad algorithm in C is still slow.
*   **Task**: Sum of 1 to N.
*   **Bad**: Loop 1 to N (O(n)).
*   **Good**: Formula `N*(N+1)/2` (O(1)).

## The Engineer's Trade-off
Often, you trade Space for Time (use more memory to run faster) or vice-versa.
''',
            'order': 4
        }
    ]

    for topic in topics_stage3:
        Topic.objects.get_or_create(stage=stage3, title=topic['title'], defaults=topic)

    print(f"✅ Stage 3 complete: {len(topics_stage3)} topics")

    # ==========================================
    # STAGE 4: System-Level Programming
    # ==========================================
    stage4, _ = Stage.objects.get_or_create(
        roadmap=roadmap,
        title='System-Level Programming',
        defaults={
            'description': 'Go deeper. Files, Bitwise operations, and how Operating Systems interact with your code.',
            'order': 4,
            'is_free': False
        }
    )

    topics_stage4 = [
        {
            'title': 'File Handling',
            'content': '''# File Handling

## Persistence
Variables die when the program ends. Files live on the disk.

### 1. File Pointers (`FILE *`)
To work with a file, we need a stream pointer.
```c
FILE *fptr;
fptr = fopen("data.txt", "w"); // Modes: r(ead), w(rite), a(ppend)
```

### 2. Operations
*   `fprintf(fptr, "Text")`: Write to file.
*   `fscanf(fptr, ...)`: Read from file.
*   `fclose(fptr)`: **CRITICAL**. Saves changes and releases the file lock.

### 3. Binary Files
For efficiency, we don't always store text. We store raw bytes (structs).
*   `fwrite()` and `fread()`: direct RAM-to-Disk transfer. Much faster for large data.

### Real World Usage
Databases (like SQLite) are essentially complex C programs manipulating massive files on disk using these exact functions.
''',
            'order': 1
        },
        {
            'title': 'Command Line Arguments',
            'content': '''# Command Line Arguments

## Professional Execution
Real tools (ls, git, gcc) take arguments from the terminal.
`git c` -> `git` is the program, `c` is the argument.

### The Real `main`
```c
int main(int argc, char *argv[]) {
    // argc: Argument Count
    // argv: Argument Vector (Array of strings)
}
```

### Example
`./myprogram hello 10`
*   `argc` = 3
*   `argv[0]` = "./myprogram"
*   `argv[1]` = "hello"
*   `argv[2]` = "10"

## Utility
This allows you to create your own system tools.
**Project Idea**: Write a C program `mycp` that copies file A to file B. Usage: `./mycp source.txt dest.txt`.
''',
            'order': 2
        },
        {
            'title': 'Bit Manipulation',
            'content': '''# Bit Manipulation

## Thinking in Binary
System programmers work at the bit level. It's fast and memory efficient.

### Operators
*   `&` (AND): Both 1 -> 1.
*   `|` (OR): Any 1 -> 1.
*   `^` (XOR): Different -> 1.
*   `~` (NOT): Flip 0 to 1.
*   `<<` (Left Shift): Multiply by 2.
*   `>>` (Right Shift): Divide by 2.

### Use Cases
1.  **Flags/Permissions**: `read = 1`, `write = 2`, `exec = 4`.
    `read | write` (001 | 010) = 011 (3).  
    OS checks permissions using bitwise AND.
2.  **Compression**: Storing 8 booleans in 1 char byte instead of 8 ints (32 bytes).
3.  **Graphics**: Manipulating RGB color values.

### The "Twos Complement"
How negative numbers are stored in binary. Fundamental for understanding Integer Overflows.
''',
            'order': 3
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
            'description': 'Become Job-Ready. Clean code, Debugging, and Interview preparation.',
            'order': 5,
            'is_free': False
        }
    )

    topics_stage5 = [
        {
            'title': 'Writing Maintainable Code',
            'content': '''# Writing Maintainable Code

## Code is for Humans
Any fool can write code that a computer can understand. Good programmers write code that humans can understand.

### Best Practices
1.  **Naming Matters**: `int d;` (Bad) vs `int days_overdue;` (Good).
2.  **Macros**: Don't use "Magic Numbers".
    *   Bad: `if (status == 2)`
    *   Good: `#define STATUS_COMPLETED 2` ... `if (status == STATUS_COMPLETED)`
3.  **Comments**: Explain *Why*, not *What*.
    *   Bad: `i++; // Increment i`
    *   Good: `i++; // Move to next buffer slot`
4.  **Error Handling**: Always check `malloc` return (it can return NULL if RAM is full) and file opens.

### Linting
Using strict compiler flags: `gcc -Wall -Wextra`. Treat warnings as errors.
''',
            'order': 1
        },
        {
            'title': 'Debugging Techniques',
            'content': '''# Debugging Techniques

## When things go wrong
Debugging is the detective work of programming.

### 1. Printf Debugging
The classic. Adding `printf("Here 1\n");` ... `printf("Var x is %d\n", x);` to trace execution.

### 2. GDB (GNU Debugger)
The professional tool.
*   Run code line-by-line (`step`).
*   Check variable values at any moment (`print x`).
*   See where it crashed (`backtrace`).

### 3. Valgrind
The memory leak detector.
Running your program through Valgrind tells you exactly where you forgot to `free()` memory or accessed out-of-bounds arrays.
`valgrind ./myprogram`
''',
            'order': 2
        },
        {
            'title': 'Interview Focus: C Questions',
            'content': '''# Interview Focus: Top C Questions

## Preparing for the Grill
C is a favorite for testing fundamentals.

### Common Questions
1.  **Dangling Pointer vs Memory Leaks**: Explain the difference.
    *   *Dangling*: Pts to freed memory. *Leak*: Memory allocated but lost track of.
2.  **`static` keyword**: What does it do?
    *   *Variable*: Preserves value between function calls.
    *   *Global*: Restricts scope to this file (private).
3.  **`const int *p` vs `int * const p`**: CONSTant pointer vs pointer to CONSTant.
4.  **Little Endian vs Big Endian**: How bytes are ordered in memory.
5.  **Implement `memcpy`**: Write your own memory copy function handling overlaps.

## Final Advice
Start building.
*   Build a Text Editor (File I/O + Arrays).
*   Build a Snake Game (Logic + Console control).
*   Build a Web Server (Sockets + Threading).

**C is the martial arts of programming. It is hard, but it makes you a disciplined and powerful engineer.**
''',
            'order': 3
        }
    ]

    for topic in topics_stage5:
        Topic.objects.get_or_create(stage=stage5, title=topic['title'], defaults=topic)

    print(f"✅ Stage 5 complete: {len(topics_stage5)} topics")
    print("\n🎉 C Roadmap creation complete!")

if __name__ == '__main__':
    create_c_roadmap()
