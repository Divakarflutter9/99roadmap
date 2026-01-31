
"""
Add Data Structures & Algorithms (DSA) through C Roadmap
Focuses on manual memory management, pointer manipulation, and core algorithmic logic.
"""

import os
import django
import sys

# Setup Django
sys.path.append('/Users/saitejakaki/Divakar/devaproject')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import Roadmap, RoadmapCategory, Stage, Topic

def create_dsa_c_roadmap():
    """Create DSA through C Roadmap"""
    
    # Get or create DSA category
    category, _ = RoadmapCategory.objects.get_or_create(
        slug='data-structures-algorithms',
        defaults={
            'name': 'Data Structures & Algorithms',
            'icon': 'fas fa-project-diagram',
            'description': 'Master the core logic of computer science'
        }
    )

    # Create roadmap
    roadmap, created = Roadmap.objects.get_or_create(
        slug='dsa-through-c',
        defaults={
            'title': 'Data Structures & Algorithms in C',
            'short_description': 'Master DSA the Hard Way: build everything from scratch using Pointers and Memory Management.',
            'description': 'The deeper way to learn DSA. Unlike Python/Java, C forces you to understand memory, pointers, and linking. This roadmap covers standard layouts (Lists, Trees, Graphs) and algorithms (Sorting, Searching) with a focus on "How it works under the hood".',
            'category': category,
            'difficulty': 'advanced',
            'estimated_hours': 180,
            'is_premium': True,
            'is_featured': True,
            'is_active': True
        }
    )
    
    if created:
        print(f"✅ Created roadmap: {roadmap.title}")
    else:
        print(f"ℹ️  Roadmap already exists: {roadmap.title}")

    # ==========================================
    # STAGE 1: Foundations
    # ==========================================
    stage1, _ = Stage.objects.get_or_create(
        roadmap=roadmap,
        title='Foundations',
        defaults={
            'description': 'Before building structures, you must master the tools: Pointers, Structs, and Dynamic Memory.',
            'order': 1,
            'is_free': True
        }
    )

    topics_stage1 = [
        {
            'title': 'Memory Management & Pointers Refresher',
            'content': '''# Memory Management & Pointers

## Why C for DSA?
In Java/Python, you say `list.add(5)`. The language handles memory resizing.
In C, **you** act as the memory manager. You must ask the OS for bytes and give them back.

### 1. Dynamic Memory Allocation (`stdlib.h`)
*   **`malloc(size)`**: "Memory Allocation". Asks for a block of `size` bytes. Returns a `void*` pointer.
    ```c
    int *arr = (int*) malloc(5 * sizeof(int)); // Array of 5 ints
    ```
*   **`calloc(n, size)`**: "Contiguous Allocation". Like malloc, but initializes memory to Zero.
*   **`realloc(ptr, new_size)`**: Resizes an existing block. Crucial for Dynamic Arrays (Vectors).
*   **`free(ptr)`**: Releases memory. **If you forget this, you get Memory Leaks.**

### 2. Pointers to Pointers (`int **ptr`)
To modify a pointer itself (e.g., changing the Head of a Linked List), you need a pointer to it.
```c
void changeHead(Node **head_ref) {
    *head_ref = new_node;
}
```
This concept confuses 90% of beginners. Master it early.
''',
            'order': 1
        },
        {
            'title': 'Structs and Typedefs',
            'content': '''# Structs and Typedefs

## The Blueprint of Nodes
Every Data Structure consists of "Nodes" containing Data and Links.

### 1. Self-Referential Structures
A struct that points to itself.
```c
struct Node {
    int data;
    struct Node *next; // Pointer to another struct of same type
};
```
**Why?** Because a Linked List is just a chain of these structs.

### 2. Typedef for Clean Code
Nobody wants to write `struct Node*` every time.
```c
typedef struct Node {
    int data;
    struct Node *next;
} Node;

Node *head = NULL; // Cleaner syntax
```

### 3. Arrow Operator (`->`)
*   `(*ptr).data` is ugly.
*   `ptr->data` is beautiful.
*   It means: "Go to the address `ptr` points to, and access the member `data`."
''',
            'order': 2
        },
        {
            'title': 'Time & Space Complexity (Big O)',
            'content': '''# Time & Space Complexity

## Measuring Efficiency
We don't measure speed in seconds (hardware depends). We measure in **Operations given Input N**.

### 1. Big O Notation
*   **O(1)**: Jumping to an array index. `arr[5]`.
*   **O(n)**: Iterating a loop. Searching a Linked List.
*   **O(log n)**: Cutting problem in half. Binary Search.
*   **O(n²)**: Nested loops. Bubble Sort.

### 2. Space Complexity in C
*   **Stack**: Recursion uses stack space. Depth of N = O(N) space.
*   **Heap**: `malloc(N * sizeof(int))` = O(N) space.

### 3. Why it matters?
*   Constraints: "N <= 10^5".
*   If you write an O(n²) algorithm (10^10 ops), it will **Time Limit Exceed (TLE)**. You need O(n log n).
''',
            'order': 3
        }
    ]

    for topic in topics_stage1:
        Topic.objects.get_or_create(stage=stage1, title=topic['title'], defaults=topic)
        
    print(f"✅ Stage 1 complete: {len(topics_stage1)} topics")

    # ==========================================
    # STAGE 2: Core Skills (Linear DS)
    # ==========================================
    stage2, _ = Stage.objects.get_or_create(
        roadmap=roadmap,
        title='Core Skills (Linear DS)',
        defaults={
            'description': 'Building the bread and butter: Linked Lists, Stacks, and Queues.',
            'order': 2,
            'is_free': False
        }
    )

    topics_stage2 = [
        {
            'title': 'Linked Lists (Singly & Doubly)',
            'content': '''# Linked Lists

## The Chain of Pointers
Arrays are fixed size. Linked Lists grow dynamically.

### 1. Singly Linked List
*   **Structure**: `[Data | Next] -> [Data | Next] -> NULL`
*   **Insertion**: O(1) if at head. O(n) if at tail (without tail pointer).
*   **Deletion**: O(n) to find the node, O(1) to rewire pointers.

### 2. Implementation Logic
```c
void insertAtFront(Node **head, int val) {
    Node *newNode = (Node*)malloc(sizeof(Node));
    newNode->data = val;
    newNode->next = *head;
    *head = newNode;
}
```

### 3. Doubly Linked List
*   **Structure**: `NULL <- [Prev | Data | Next] -> [Prev | Data | Next] -> NULL`
*   **Pros**: Can traverse backward. Deletion is easier (you have access to prev).
*   **Cons**: Extra memory (8 bytes extra per node for prev pointer).

### Common Mistakes
*   Losing the reference to `head`.
*   Accessing `node->next` when node is `NULL` (Segfault).
''',
            'order': 1
        },
        {
            'title': 'Stacks using Arrays & Linked Lists',
            'content': '''# Stacks (LIFO)

## Last In, First Out
Think of a stack of plates. You can only add (Push) or remove (Pop) from the top.

### 1. Applications
*   Undo/Redo features.
*   Function Call Stack (Recursion).
*   Expression Evaluation (e.g., `(2 + 3) * 5`).

### 2. Implementation
#### Using Array
*   `int arr[MAX]; int top = -1;`
*   **Push**: `arr[++top] = val;`
*   **Pop**: `return arr[top--];`
*   **Issue**: Fixed size (Stack Overflow).

#### Using Linked List
*   **Push**: `insertAtFront(head, val)`
*   **Pop**: `deleteAtFront(head)`
*   **Pros**: Infinite size (heap limited).

### Complexity
All operations (Push, Pop, Peek) are **O(1)**.
''',
            'order': 2
        },
        {
            'title': 'Queues (FIFO)',
            'content': '''# Queues (FIFO)

## First In, First Out
Think of a ticket line. Enter at Rear/Tail, Leave from Front/Head.

### 1. Applications
*   Printer Job Scheduling.
*   BFS (Breadth-First Search) Algorithm.
*   CPU Task Scheduling.

### 2. Implementation Issues
*   **Linear Array**: If you increment Front, you waste space at the beginning.
*   **Circular Queue**: Connect Rear back to Front. `(rear + 1) % SIZE`.

### 3. Priority Queue
*   Not a normal FIFO. Elements obey "Priority".
*   Usually implemented using Heaps (Stage 4), NOT arrays or lists.
''',
            'order': 3
        }
    ]

    for topic in topics_stage2:
        Topic.objects.get_or_create(stage=stage2, title=topic['title'], defaults=topic)
    
    print(f"✅ Stage 2 complete: {len(topics_stage2)} topics")

    # ==========================================
    # STAGE 3: Applied Skills (Non-Linear DS)
    # ==========================================
    stage3, _ = Stage.objects.get_or_create(
        roadmap=roadmap,
        title='Applied Skills (Algo & Trees)',
        defaults={
            'description': 'Moving to hierarchical data and core algorithms.',
            'order': 3,
            'is_free': False
        }
    )

    topics_stage3 = [
        {
            'title': 'Recursion Visualized',
            'content': '''# Recursion Visualized

## Trusting the Leap of Faith
Recursion is defining a problem in terms of itself.

### 1. The Call Stack
Every recursive call pushes a new frame.
`fib(5)` -> `fib(4)` -> ... -> `fib(1)`.
When `fib(1)` returns, the stack **unwinds**.

### 2. Key components
*   **Base Case**: The stop condition. `if (n == 0) return;`
*   **Recursive Step**: Moving towards the base case.

### 3. Tail Recursion
If the recursive call is the *last* thing the function does, modern C compilers can optimize it into a Loop (Tail Call Optimization). This saves stack space.
''',
            'order': 1
        },
        {
            'title': 'Trees and BST',
            'content': '''# Trees and Binary Search Trees (BST)

## Hierarchical Data
Lists are linear. File systems, HTML DOM, and Organization charts are Trees.

### 1. Binary Tree Node
```c
struct Node {
    int data;
    struct Node *left;
    struct Node *right;
};
```

### 2. Binary Search Tree (BST)
*   **Rule**: `Left < Root < Right`.
*   **Search**: O(log n). Like binary search but dynamic.
*   **Worst Case**: Skewed Tree (Line). O(n).

### 3. Traversals
*   **Inorder** (Left, Root, Right): Returns sorted list for BST.
*   **Preorder** (Root, Left, Right): Useful for copying trees.
*   **Postorder** (Left, Right, Root): Useful for deleting trees (delete children first).

### 4. Implementation
Almost always recursive.
```c
void inorder(Node *root) {
    if (!root) return;
    inorder(root->left);
    printf("%d ", root->data);
    inorder(root->right);
}
```
''',
            'order': 2
        },
        {
            'title': 'Sorting & Searching',
            'content': '''# Sorting & Searching

## Organizing Data
Algorithms to order data for faster retrieval.

### 1. Quadratic Sorts O(n²)
*   **Bubble, Insertion, Selection**.
*   Good for small N (< 50). Simple to write.

### 2. Logarithmic Sorts O(n log n)
*   **Merge Sort**: Divide and Conquer. Stable. Good for Linked Lists.
*   **Quick Sort**: Partitioning logic. Fast in practice. Default in C `qsort()`.

### 3. Searching
*   **Linear Search**: O(n).
*   **Binary Search**: O(log n). Requires sorted array.
    *   `mid = low + (high - low) / 2;` (Avoids overflow)
''',
            'order': 3
        }
    ]

    for topic in topics_stage3:
        Topic.objects.get_or_create(stage=stage3, title=topic['title'], defaults=topic)
    
    print(f"✅ Stage 3 complete: {len(topics_stage3)} topics")

    # ==========================================
    # STAGE 4: Advanced & Industry Practices
    # ==========================================
    stage4, _ = Stage.objects.get_or_create(
        roadmap=roadmap,
        title='Advanced & Industry Practices',
        defaults={
            'description': 'Complex structures used in real-world systems: Graphs, Hashing, and Heaps.',
            'order': 4,
            'is_free': False
        }
    )

    topics_stage4 = [
        {
            'title': 'Graphs (BFS & DFS)',
            'content': '''# Graphs

## Connecting Everything
Maps, Social Networks, Internet - all are Graphs.

### 1. Representation
*   **Adjacency Matrix**: `int graph[N][N]`. O(1) lookup. O(N²) space. Good for dense graphs.
*   **Adjacency List**: Array of Linked Lists. O(V+E) space. Good for sparse graphs (Most real graphs).

### 2. Traversals
*   **BFS (Breadth-First)**: Uses Queue. Finds Shortest Path in unweighted graphs.
*   **DFS (Depth-First)**: Uses Stack (Recursion). Good for maze solving, cycle detection.

### 3. Real World
Google Maps uses Dijkstra/A* (Weighted Graph algorithms).
''',
            'order': 1
        },
        {
            'title': 'Hash Tables (Hashing)',
            'content': '''# Hash Tables

## The O(1) Magic
How do Python dictionaries or JSON objects work? Hashing.

### 1. Concept
Map a Key (String/Int) to an Index in an Array using a **Hash Function**.

### 2. Collisions
What if "Apple" and "Banana" hash to same index?
*   **Chaining**: Each array slot points to a Linked List.
*   **Open Addressing**: Find the next empty slot.

### 3. C Implementation
You need an array of struct pointers.
```c
struct Node *hashTable[SIZE];
```
This is pure pointer manipulation. Excellent for understanding memory lookups.
''',
            'order': 2
        },
        {
            'title': 'Heaps (Priority Queues)',
            'content': '''# Heaps (Priority Queues)

## Accessing the Max/Min O(1)
A Binary Tree stored in an Array.
*   **Max Heap**: Parent >= Children.
*   **Min Heap**: Parent <= Children.

### 1. Array Math
*   Parent at `i`.
*   Left Child: `2*i + 1`.
*   Right Child: `2*i + 2`.

### 2. Use Cases
*   Scheduling tasks by priority.
*   Dijkstra's Algorithm.
*   Heap Sort (O(n log n) space O(1)).
''',
            'order': 3
        }
    ]

    for topic in topics_stage4:
        Topic.objects.get_or_create(stage=stage4, title=topic['title'], defaults=topic)
    
    print(f"✅ Stage 4 complete: {len(topics_stage4)} topics")

    # ==========================================
    # STAGE 5: Career & Job Readiness
    # ==========================================
    stage5, _ = Stage.objects.get_or_create(
        roadmap=roadmap,
        title='Career & Job Readiness',
        defaults={
            'description': 'Applying DSA to clear interviews and solve real problems.',
            'order': 5,
            'is_free': False
        }
    )

    topics_stage5 = [
        {
            'title': 'Common Interview Patterns',
            'content': '''# Common Interview Patterns

## Don't memorize code, memorize patterns.

### 1. Two Pointers
*   **Use**: Sorted Arrays, Linked Lists.
*   **Example**: "Find pair with sum X". Left ptr at start, Right ptr at end.

### 2. Sliding Window
*   **Use**: Subarrays/Substrings.
*   **Example**: "Max sum subarray of size K".

### 3. Fast & Slow Pointers (Floyd's Cycle)
*   **Use**: Detect cycle in Linked List.
*   **Mantra**: If there is a loop, fast runner eventually catches slow runner.

### 4. Backtracking
*   **Use**: Generating all combinations (Sudoku, N-Queens).
*   **Concept**: Recursion with "Undo" step.
''',
            'order': 1
        },
        {
            'title': 'Standard Library vs Scratch',
            'content': '''# Standard Library vs Scratch

## In the Job
*   **Job**: Use `qsort` (C), `std::sort` (C++), `Collections.sort` (Java). Never implement Bubble Sort in production.
*   **Interview**: "Implement Quick Sort on the whiteboard."

### Using C's `qsort`
It uses `void*` and function pointers.
```c
int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}
qsort(arr, n, sizeof(int), compare);
```
Understanding this function pointer syntax proves you know C deep.

## Skills Gained
*   **Memory Mastery**: You no longer fear Segfaults.
*   **Optimization**: You "feel" the cost of O(n²).
*   **Language Agnostic**: Logic you learned here works in Python, JS, Go.

## Roles
*   **Backend Engineer**: High performance services.
*   **Systems Engineer**: Database internals, OS schedulers.
*   **Game Developer**: Physics engines, optimized rendering.
''',
            'order': 2
        }
    ]

    for topic in topics_stage5:
        Topic.objects.get_or_create(stage=stage5, title=topic['title'], defaults=topic)
    
    print(f"✅ Stage 5 complete: {len(topics_stage5)} topics")
    print("\n🎉 DSA in C Roadmap creation complete!")

if __name__ == '__main__':
    create_dsa_c_roadmap()
