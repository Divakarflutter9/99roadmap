
import os
import django
import sys

# Add project root to sys.path
sys.path.append('/Users/saitejakaki/Divakar/devaproject')

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import Roadmap, RoadmapCategory, Stage, Topic

def create_js_pro_roadmap():
    """Create Professional Core JavaScript Roadmap"""
    
    print("🚀 Initializing Professional JS Roadmap Creation...")
    
    # 1. Get or Create Category
    # 'frontend-development', 'development'
    category, _ = RoadmapCategory.objects.get_or_create(
        slug='development',
        defaults={'name': 'Development'}
    )
    
    # 2. Create Roadmap
    roadmap_slug = 'javascript-core-mastery'
    roadmap_title = 'Professional Core JavaScript'
    
    roadmap, created = Roadmap.objects.get_or_create(
        slug=roadmap_slug,
        defaults={
            'title': roadmap_title,
            'short_description': 'Master the Runtime. Execution Contexts, Event Loop, Protoypal Inheritance, and Async patterns.',
            'description': 'Move beyond syntax. Understand how the V8 engine executes your code, how the Event Loop handles concurrency, and how to write production-grade asynchronous JavaScript.',
            'category': category,
            'difficulty': 'intermediate',
            'estimated_hours': 60,
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
        roadmap.stages.all().delete()
        print("   ♻️  Cleared existing stages for fresh import.")
        
    # ==========================================
    # STAGE 1: JAVASCRIPT FOUNDATIONS (FREE)
    # ==========================================
    stage1 = Stage.objects.create(
        roadmap=roadmap,
        title='JavaScript Foundations',
        description='Understanding what JavaScript controls in applications.',
        order=1,
        is_free=True
    )
    
    topics_s1 = [
        {
            'title': 'Role of JS in Modern Apps',
            'content': """# The Behavior Layer

## Data Handling
- **State**: JS remembers "Is the user logged in?" or "What is in the cart?".
- **Events**: JS listens for "Click", "Scroll", "Keypress".
- **Network**: JS fetches data from the backend (JSON) and updates the UI.

## JS vs HTML vs CSS
- **HTML**: Structure (Noun) -> "This is a Button."
- **CSS**: Appearance (Adjective) -> "The Button is Blue."
- **JS**: Behavior (Verb) -> "The Button submits the Form."

## Execution Environment
- JS does not run on your computer directly. It runs inside a **Host Environment** (Browser or Node.js).
- The Browser provides the **Window API** (DOM, Fetch, LocalStorage). JS just talks to it.
""",
            'order': 1
        },
        {
            'title': 'How JS Executes',
            'content': """# Single Threaded & JIT

## Single Threaded
- JS has **One Call Stack**. It can do only **one thing at a time**.
- If you run a `while(true)` loop, the entire browser tab freezes. (UI is blocked).

## JIT Compilation (V8 Engine)
- JS is not just "Interpreted". Modern engines (V8, SpiderMonkey) use **Just-In-Time Compilation**.
- Code is parsed -> turned to Bytecode -> Hot functions are compiled to Machine Code for speed.
""",
            'order': 2
        }
    ]
    
    for t in topics_s1:
        Topic.objects.create(stage=stage1, **t)
    print(f"   ✨ Added {len(topics_s1)} topics to Stage 1")


    # ==========================================
    # STAGE 2: CORE JAVASCRIPT BEHAVIOR
    # ==========================================
    stage2 = Stage.objects.create(
        roadmap=roadmap,
        title='Core JavaScript Behavior',
        description='Control logic and data flow.',
        order=2,
        is_free=False
    )
    
    topics_s2 = [
        {
            'title': 'Variables & Data Types',
            'content': """# Memory & References

## Primitive vs Reference Types
- **Primitives** (String, Number, Boolean, Null, Undefined, Symbol): Stored by **Value**.
    ```js
    let a = 10;
    let b = a;
    b = 20; // a is still 10.
    ```
- **References** (Object, Array, Function): Stored by **Reference** (Pointer).
    ```js
    let x = { val: 10 };
    let y = x;
    y.val = 20; // x.val is also 20! They point to the same memory.
    ```
- **Industry Impact**: Mutating objects passed as props can cause impossible-to-debug side effects in React/Angular.

## Const vs Let vs Var
- **var**: Function scoped. Hoisted. (Avoid in modern code).
- **let**: Block scoped. Reassignable.
- **const**: Block scoped. Reference is immutable (but the object inside CAN change).
""",
            'order': 1
        },
        {
            'title': 'Functions & Scope',
            'content': """# The Functional Core

## Scopes
1.  **Global Scope**: Accessible everywhere. (Bad practice to pollute).
2.  **Function Scope**: Variables defined inside `function`.
3.  **Block Scope**: Variables defined inside `{ }` (if/for).

## Closures (The Most Asked Interview Q)
- A function **remembers** the variables from its outer scope, even after the outer function has finished executing.
```js
function makeCounter() {
    let count = 0; // Private variable
    return function() {
        count++;
        return count;
    };
}
const count = makeCounter();
count(); // 1
count(); // 2
```
- **Use Case**: Data Encapsulation, Factory Functions, React Hooks (`useState`).
""",
            'order': 2
        }
    ]
    
    for t in topics_s2:
        Topic.objects.create(stage=stage2, **t)
    print(f"   ✨ Added {len(topics_s2)} topics to Stage 2")


    # ==========================================
    # STAGE 3: JAVASCRIPT RUNTIME CONCEPTS
    # ==========================================
    stage3 = Stage.objects.create(
        roadmap=roadmap,
        title='JavaScript Runtime Concepts',
        description='Understand the real execution model.',
        order=3,
        is_free=False
    )
    
    topics_s3 = [
        {
            'title': 'The Execution Context',
            'content': """# Where Code Lives

Every time a function runs, a new **Execution Context** is created.

## Components of a Context
1.  **Variable Environment**: Where `let a = 10` lives.
2.  **Scope Chain**: Link to parent scopes.
3.  **`this` Binding**: What `this` points to (depends on *how* the function was called).

## The `this` Keyword
- **Global**: `window` (or `global` in Node).
- **Method Call**: `obj.method()` -> `this` is `obj`.
- **Function Call**: `func()` -> `this` is `undefined` (in strict mode).
- **Arrow Function**: Inherits `this` from outer scope (Lexical scoping).
""",
            'order': 1
        },
        {
            'title': 'The Event Loop',
            'content': """# How JS Handles Concurrency

If JS is single-threaded, how can it wait for a Network Request without freezing?

## The Pieces
1.  **Call Stack**: Executes synchronous code.
2.  **Web APIs**: Browser threads handling functionality (Timer, Fetch, DOM).
3.  **Callback Queue**: Waiting line for async callbacks (`setTimeout`).
4.  **Microtask Queue**: Priority line for Promises.

## The Loop
1.  Check if Call Stack is empty.
2.  If empty, check Microtask Queue -> Push to Stack.
3.  If Microtask empty, check Callback Queue -> Push one to Stack.

**Rule**: Promises (Microtasks) run BEFORE `setTimeout` (Macrotasks).
""",
            'order': 2
        }
    ]
    
    for t in topics_s3:
        Topic.objects.create(stage=stage3, **t)
    print(f"   ✨ Added {len(topics_s3)} topics to Stage 3")


    # ==========================================
    # STAGE 4: ASYNCHRONOUS JAVASCRIPT
    # ==========================================
    stage4 = Stage.objects.create(
        roadmap=roadmap,
        title='Asynchronous JavaScript',
        description='Handling real-world async data.',
        order=4,
        is_free=False
    )
    
    topics_s4 = [
        {
            'title': 'Promises',
            'content': """# The Future Value

## The Problem: Callback Hell
Nesting callbacks (`fs.read(A, () => fs.read(B...))`) makes code unreadable and hard to handle errors.

## The Solution: Promise
An object representing eventual completion (or failure).
- **States**: Pending, Resolved (Fulfilled), Rejected.

```js
fetchUser()
    .then(user => fetchPosts(user.id))
    .then(posts => showPosts(posts))
    .catch(err => showError(err));
```
- **Data Flow**: Linear, easy to chain.
""",
            'order': 1
        },
        {
            'title': 'Async / Await',
            'content': """# Synchronous-Style Async

Syntactic sugar over Promises.

## Usage
```js
async function loadDashboard() {
    try {
        const user = await fetchUser(); // Pauses function here!
        const posts = await fetchPosts(user.id);
        return posts;
    } catch (err) {
        // Handles both fetchUser AND fetchPosts errors
        console.error(err);
    }
}
```

## Why Industry Prefers It
- Readable (looks like execution is top-to-bottom).
- Error handling is cleaner (standard `try/catch`).
- **Gotcha**: Don't use `await` inside a `forEach` loop. (It doesn't wait!). Use `for..of`.
""",
            'order': 2
        }
    ]
    
    for t in topics_s4:
        Topic.objects.create(stage=stage4, **t)
    print(f"   ✨ Added {len(topics_s4)} topics to Stage 4")


    # ==========================================
    # STAGE 5: JAVASCRIPT IN PRODUCTION
    # ==========================================
    stage5 = Stage.objects.create(
        roadmap=roadmap,
        title='JavaScript in Production',
        description='Writing reliable JS code.',
        order=5,
        is_free=False
    )
    
    topics_s5 = [
        {
            'title': 'Modules (ESM vs CommonJS)',
            'content': """# Organizing Code

## 1. ES Modules (The Standard)
- `import { func } from './utils.js'`
- `export const func = ...`
- Used in Browsers (React, Vue) and modern Node.js.
- **Static Analysis**: Imports are evaluated before code runs.

## 2. CommonJS (Legacy Node)
- `const utils = require('./utils')`
- `module.exports = ...`
- Dynamic (runtime) loading.

## Industry Standard
Always stick to **ES Modules** for frontend development. It allows "Tree Shaking" (removing unused code).
""",
            'order': 1
        },
        {
            'title': 'Interview Expectations',
            'content': """# What Senior Devs Ask

## 1. "Explain the Event Loop"
- Must mention Stack, Queue, and Microtasks.

## 2. "Fix this Reference bug"
- Given code where object mutation causes side effects. (Solution: Spread syntax `...obj` or `structuredClone`).

## 3. "Debounce vs Throttle"
- **Debounce**: Wait for pause in typing (Search bar).
- **Throttle**: Limit execution rate (Scroll listener).

## 4. "Output of this code?"
- Examining `this` context or Closure scope variables.
""",
            'order': 2
        }
    ]
    
    for t in topics_s5:
        Topic.objects.create(stage=stage5, **t)
    print(f"   ✨ Added {len(topics_s5)} topics to Stage 5")

    # Update stats
    roadmap.update_stats()
    print("✅ Professional JS Roadmap creation complete! Stats updated.")

if __name__ == '__main__':
    create_js_pro_roadmap()
