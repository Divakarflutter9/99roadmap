
import os
import django
import sys

# Add project root to sys.path
sys.path.append('/Users/saitejakaki/Divakar/devaproject')

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import Roadmap, RoadmapCategory, Stage, Topic

def create_oop_roadmap():
    """Create Industry-Level OOP Concepts Roadmap"""
    
    print("🚀 Initializing OOP Roadmap Creation...")
    
    # 1. Get or Create Category
    # Using 'computer-science' as the most fitting category for Core CS concepts
    category, _ = RoadmapCategory.objects.get_or_create(
        slug='computer-science',
        defaults={'name': 'Computer Science'}
    )
    
    # 2. Create Roadmap
    roadmap_slug = 'industry-oop-concepts'
    roadmap_title = 'Industry-Level OOP Concepts'
    
    roadmap, created = Roadmap.objects.get_or_create(
        slug=roadmap_slug,
        defaults={
            'title': roadmap_title,
            'short_description': 'Master Object-Oriented Programming with real-world industry examples and design patterns.',
            'description': 'A professional roadmap for BTech students to move beyond textbook definitions. Learn how OOP is actually used in enterprise software, backend systems, and system design.',
            'category': category,
            'difficulty': 'intermediate',
            'estimated_hours': 40,
            'is_premium': True,
            'is_featured': True,
            'is_active': True,
            'price': 499  # localized pricing
        }
    )
    
    if created:
        print(f"✅ Created Roadmap: {roadmap.title}")
    else:
        print(f"ℹ️  Roadmap '{roadmap.title}' already exists. Updating details...")
        # Optional: Clear existing stages to rebuild
        roadmap.stages.all().delete()
        print("   ♻️  Cleared existing stages for fresh import.")
        
    # ==========================================
    # STAGE 1: OOP FOUNDATIONS (FREE)
    # ==========================================
    stage1 = Stage.objects.create(
        roadmap=roadmap,
        title='OOP Foundations',
        description='Why OOP exists and the problems it solves in modern software engineering.',
        order=1,
        is_free=True  # Explicitly FREE as requested
    )
    
    topics_s1 = [
        {
            'title': 'Why OOP Exists?',
            'content': """# Why We Need Object-Oriented Programming

## The Problem with "Spaghetti Code"
Before OOP, most programming was **Procedural** (functions calling functions). In small scripts, this is fine. But in large industry systems (like Amazon or Uber), it creates chaos.

### ❌ The Procedural Mess (Example)
Imagine building a Banking System using just functions and global variables:

```python
# Procedural Approach
balance_user1 = 1000
balance_user2 = 500

def transfer(amount, from_user, to_user):
    # We have to manually manage which variable to update
    # Global state is dangerous!
    global balance_user1, balance_user2
    if from_user == "user1":
        balance_user1 -= amount
    # ... logic gets complex and buggy fast
```

### ✅ The OOP Solution
OOP organizes code into **Objects** that hold their own data and behavior.

```python
# OOP Approach
class BankAccount:
    def __init__(self, user, balance):
        self.user = user
        self.balance = balance
    
    def transfer(self, amount, target_account):
        if self.balance >= amount:
            self.balance -= amount
            target_account.balance += amount

# Usage is clean and safe
alex = BankAccount("Alex", 1000)
sam = BankAccount("Sam", 500)
alex.transfer(200, sam)
```

## Problems OOP Solves in Industry
1.  **Complexity Management**: Breaks 10-million-line codebases into manageable chunks (Classes).
2.  **Data Security**: Prevents random functions from corrupting critical data (Encapsulation).
3.  **Reusability**: Don't rewrite code; extend existing well-tested code (Inheritance).
4.  **Scalability**: Easier to add new features without breaking old ones.

## Professional Insight
> "Code is read much more often than it is written."
OOP makes code **readable** and **maintainable**, which is the #1 priority in product companies.
""",
            'order': 1
        },
        {
            'title': 'Object vs Class (Real World)',
            'content': """# Objects vs Classes: The Real-World Analogy

Textbooks say: *"A class is a blueprint, an object is an instance."*
Let's look at this through the lens of a **Car Manufacturing Plant**.

## 🏭 The Blueprint (Class)
The **Class** is the CAD Drawing / Engineering Spec.
- It defines what a car *should* have (Engine, Wheels, Color).
- It defines what a car *can do* (Drive, Brake, Honk).
- **Physical existence?** NO. You cannot drive a blueprint.

```java
// The Blueprint
class Car {
    String color;
    Engine engine;
    
    void drive() { ... }
}
```

## 🚗 The Product (Object)
The **Object** is the actual car rolling off the assembly line.
- **Car #1**: Red, V8 Engine (Memory Address: 0x123)
- **Car #2**: Blue, Electric Motor (Memory Address: 0x456)
- **Physical existence?** YES. It consumes memory (RAM).

```java
// The Actual Cars
Car ferrari = new Car(); // Object 1
Car tesla = new Car();   // Object 2
```

## Why This Matters in Database Design
In Backend Development (Django/Spring/Node):
- **Class** = Database Table Schema (e.g., `User` Model)
- **Object** = A specific Row in that table (e.g., `User(id=1, name="John")`)

### Common Interview Q:
**"What is the difference between a Class and an Object in terms of memory?"**
*   **Class**: Logical definition, loaded once into method area/metadata.
*   **Object**: Dynamic instance, allocated on the **Heap** memory.
""",
            'order': 2
        }
    ]
    
    for t in topics_s1:
        Topic.objects.create(stage=stage1, **t)
    print(f"   ✨ Added {len(topics_s1)} topics to Stage 1")


    # ==========================================
    # STAGE 2: CORE OOP CONCEPTS
    # ==========================================
    stage2 = Stage.objects.create(
        roadmap=roadmap,
        title='Core OOP Concepts',
        description='Deep dive into the 4 pillars of OOP with a focus on how they are applied in production systems.',
        order=2,
        is_free=False
    )
    
    topics_s2 = [
        {
            'title': 'Encapsulation (Real Use Cases)',
            'content': """# Encapsulation: Protecting Your Data

## What it really means
It's not just "making variables private". It's about **Control** and **validity**.

## ❌ Bad Design (No Encapsulation)
```java
class Wallet {
    public int balance; // Anyone can change this directly!
}

Wallet myWallet = new Wallet();
myWallet.balance = -5000; // 😱 Invalid state! Logic broken.
```

## ✅ Good Design (Encapsulated)
```java
class Wallet {
    private int balance; // 🔒 Hidden
    
    public void withdraw(int amount) {
        // Validation Logic (The "Gatekeeper")
        if (amount <= 0) throw new Error("Invalid amount");
        if (amount > balance) throw new Error("Insufficient funds");
        
        balance -= amount;
        logTransaction(amount); // Side effect: Tracking
    }
}
```

## Industry Use Case: API Responses
When you fetch a User Profile from an API, the `User` class typically has a `password` field.
**Encapsulation safeguards this.**
- The `password` field is `private`.
- The `toJSON()` method (getter equivalent) explicitly **excludes** the password when sending data to the frontend.

## Key Benefit
**Refactoring Safety**: You can change the internal implementation (e.g., store balance as `BigDecimal` instead of `int`) without breaking the code that uses the `Wallet` class, because methods like `withdraw()` stay the same signature.
""",
            'order': 1
        },
        {
            'title': 'Abstraction (Why Companies Use It)',
            'content': """# Abstraction: Hiding Complexity

## The "Remote Control" Analogy
When you press the "Power" button on a TV remote:
- **Abstraction**: "Turn On" (Simple Interface)
- **Implementation**: Send IR signal -> Receiver decodes -> Capacitor charges -> Screen lights up (Complex Reality)

You don't need to be an electrical engineer to watch TV.

## Industry Example: Payment Gateways
Imagine building an E-commerce site. You want to accept payments.

Do you write code to talk directly to Visa/Mastercard servers? **NO.**
You use a **Payment Gateway** (Stripe/PayPal).

### Code without Abstraction (Bad)
```java
if (paymentType == "PayPal") {
    payPalConnection.login();
    payPalConnection.sendMoney();
} else if (paymentType == "Stripe") {
    stripeClient.createCharge();
}
```

### Code WITH Abstraction (Good)
We define an **Interface** (Contract).

```java
interface PaymentProcessor {
    void processPayment(double amount);
}

// Complexity hidden inside specific classes
class PayPalProcessor implements PaymentProcessor { ... }
class StripeProcessor implements PaymentProcessor { ... }

// Usage
currentProcessor.processPayment(100.0);
```

## Abstraction vs Encapsulation
- **Encapsulation**: Hiding *Data* (Information Hiding).
- **Abstraction**: Hiding *Implementation Details* (Complexity Hiding).

## Key Takeaway
Abstraction allows us to build **Loose Coupling**. We can swap Stripe for PayPal without rewriting our entire checkout logic.
""",
            'order': 2
        },
        {
            'title': 'Inheritance (When to Use/Avoid)',
            'content': """# Inheritance: The Double-Edged Sword

Inheritance (`extends`) allows a class to derive properties from another.
**Junior Devs use it everywhere. Senior Devs use it sparingly.**

## ✅ When to Use It ("Is-A" Relationship)
Use it when there is a clear, permanent hierarchy.
- **Animal** -> **Dog** (A Dog *is an* Animal)
- **HTMLElement** -> **Button** (A Button *is an* Element)

## ❌ When NOT to Use It
Do not use inheritance just to share code. This is a common beginner mistake.

### The "God Class" Anti-Pattern
Imagine you have a `BaseController` in a web app.
You put `logging`, `auth`, `database`, `email` logic all in `BaseController`.
Then every other controller extends it.

**Problem:**
- `ProfileController` inherits `BaseController` but maybe it doesn't need email logic.
- You change `BaseController` for one feature, and **break 50 other controllers**.
- This is called the **Fragile Base Class Problem**.

## Better Alternative: Composition ("Has-A")
Instead of inheriting, **compose** objects.

```java
// Bad: Inheritance
class User extends Logger { ... }

// Good: Composition
class User {
    private Logger logger = new Logger(); // Has-a Logger
}
```

## Industry Rule of Thumb
> **"Favor Composition over Inheritance."**
Only use Inheritance for true polymorphism, not just for code reuse.
""",
            'order': 3
        },
        {
            'title': 'Polymorphism (Runtime Behavior)',
            'content': """# Polymorphism: Evolution of Code

**Polymorphism** = "Many Forms".
It allows a single function or method to handle different types of objects essentially the same way.

## 1. Compile-time Polymorphism (Overloading)
Same method name, different parameters.
```java
print(String s)
print(int i)
print(List<String> items)
```
*Common in Java/C++, less common in Python (which uses dynamic typing).*

## 2. Runtime Polymorphism (Overriding)
The most powerful form. A subclass changes the behavior of a parent method.

### Real-World Scenario: Notification System
You have to send notifications: Email, SMS, Push.

```python
class Notification:
    def send(self, message):
        pass # Abstract

class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending Email: {message}")

class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS: {message}")

# The Power of Polymorphism
def notify_users(users, notification_service):
    for user in users:
        # We don't care IF it's SMS or Email.
        # We just know it can 'send'.
        notification_service.send(f"Hello {user.name}")
```

## Why this is huge for maintainability
If you want to add **WhatsApp Notifications** later:
1. Create `WhatsAppNotification` class.
2. Implement `send()`.
3. **You DO NOT touch the `notify_users` function!**

This adheres to the **Open/Closed Principle** (Open for extension, closed for modification).
""",
            'order': 4
        }
    ]
    
    for t in topics_s2:
        Topic.objects.create(stage=stage2, **t)
    print(f"   ✨ Added {len(topics_s2)} topics to Stage 2")


    # ==========================================
    # STAGE 3: OOP IN REAL CODE
    # ==========================================
    stage3 = Stage.objects.create(
        roadmap=roadmap,
        title='OOP in Real Code',
        description='Practical design patterns and structuring classes for scalability.',
        order=3,
        is_free=False
    )
    
    topics_s3 = [
        {
            'title': 'Designing Classes',
            'content': """# Designing Robust Classes

Writing a class syntax is easy. Designing a **good** class is hard.

## S.R.P. (Single Responsibility Principle)
**Rule**: A class should have only **one reason to change**.

### ❌ Bad Design (The "God Object")
```java
class UserManager {
    void createUser() { ... }
    void loginUser() { ... }
    void sendWelcomeEmail() { ... } // ⚠️ Logic mixed!
    void logActivity() { ... }      // ⚠️ Logic mixed!
    void saveToDatabase() { ... }   // ⚠️ Logic mixed!
}
```
If you change the Email provider, you have to touch `UserManager`.
If you change the Database, you have to touch `UserManager`.
Risk of breaking things is high.

### ✅ Good Design (Separation of Concerns)
Break it down:
1.  `User` (Data Model)
2.  `UserRepository` (Database interactions)
3.  `EmailService` (Sending emails)
4.  `AuthService` (Login logic)

## State vs Behavior
- **DTOs (Data Transfer Objects)**: Classes that hold only data (Getters/Setters). Used to move data between layers.
- **Service Classes**: Classes that hold logic/behavior but no state (they process the DTOs).

**Industry Standard**: Keep your "Entity" classes (Data) separate from your "Service" classes (Logic).
""",
            'order': 1
        },
        {
            'title': 'Relationships between Objects',
            'content': """# Relationships: Connecting the Dots

Objects rarely exist in isolation. They interact.

## 1. Association ("Uses-A")
Loose connection. Teacher and Student.
- A Teacher *uses* a Student object (to grade them) but they exist independently.
- If Teacher is deleted, Student still exists.

## 2. Aggregation ("Has-A" - Weak)
Department and Teacher.
- A Department *has* Teachers.
- But a Teacher can belong to multiple departments or exist without one.
- **Code**: Passed into constructor, not created inside.

## 3. Composition ("Part-Of" - Strong)
House and Room.
- A Room is *part of* a House.
- If you destroy the House, the Room is destroyed too.
- **Code**: Created *inside* the constructor.

```java
class House {
    private Room kitchen;
    
    public House() {
        // Strong lifecycle dependency
        this.kitchen = new Room("Kitchen"); 
    }
}
```

## Why distinguish?
**Memory Management & Cascading Deletes.**
- In a database (ORM), if you delete a User (Composition), you delete their Profile.
- But you generally DON'T delete their Forum Posts (Aggregation/Association), because those add value to the community.
""",
            'order': 2
        }
    ]
    
    for t in topics_s3:
        Topic.objects.create(stage=stage3, **t)
    print(f"   ✨ Added {len(topics_s3)} topics to Stage 3")


    # ==========================================
    # STAGE 4: OOP IN INDUSTRY
    # ==========================================
    stage4 = Stage.objects.create(
        roadmap=roadmap,
        title='OOP in Industry',
        description='How top tech companies use OOP in Backend Systems and Interviews.',
        order=4,
        is_free=False
    )
    
    topics_s4 = [
        {
            'title': 'OOP in Backend Systems',
            'content': """# OOP in Backend Architecture

How does OOP fit into a Django, Spring Boot, or NestJS application?

## The 3-Layer Architecture
Almost every professional backend follows this application of OOP:

### 1. Controller Layer (Interface)
- Handles HTTP Requests.
- Low abstraction.
- Example: `checkout()` method in `CartController`.

### 2. Service Layer (Business Logic)
- **Where OOP shines.**
- Contains the rules.
- Example: `PaymentService` class handles exact logic of validations, charging, and retries.

### 3. Data Access Layer (Persistence)
- **ORM (Object-Relational Mapping)**.
- Maps your Python/Java **Classes** to SQL **Tables**.
- You treat Database rows as Objects.

```python
# Django ORM Example
# We work with Objects, Django handles SQL
active_users = User.objects.filter(is_active=True) 
for user in active_users:
    user.send_email()
```

## Dependency Injection (DI)
The ultimate OOP pattern in industry.
Instead of creating objects manually (`new Service()`), the framework gives them to you.
This makes testing easy because you can inject "Mock" objects during tests.
""",
            'order': 1
        },
        {
            'title': 'Interview Focus: LLD',
            'content': """# Low-Level Design (LLD) Interviews

For Junior/Mid-level roles, companies (Amazon, Uber, Swiggy) ask **Machine Coding Rounds**.
You are asked to design a system using OOP in 60-90 minutes.

## Common Scenarios
1.  **Design a Parking Lot**
    - Classes: `ParkingLot`, `Floor`, `Spot`, `Vehicle`, `Ticket`.
    - Inheritance: `Vehicle` -> `Car`, `Bike`, `Truck`.
    - Enum: `SpotType` (Compact, Large).
    
2.  **Design an Elevator System**
    - Classes: `Elevator`, `Button`, `Door`, `Dispatcher`.
    - Logic: Scheduling algorithm.

3.  **Design StackOverflow**
    - Classes: `User`, `Question`, `Answer`, `Tag`, `Badge`.
    - Association: User *posts* Question.

## What Interviewers Look For
1.  **Modularity**: Is code split into logical classes?
2.  **Extensibility**: Can I add a new vehicle type without breaking the code? (Polymorphism)
3.  **Naming**: Are variable/method names clear?
4.  **Edge Cases**: Handling invalid inputs.

## Skills Gained from this Roadmap
By mastering these concepts, you are ready for:
- **SDE-1 Roles** (Backend/Fullstack)
- **Machine Coding Rounds**
- **Code Reviews** (Writing clean, maintainable code)

## Next Steps
- **Backend Development**: Learn High-Level Design (System Design).
- **Design Patterns**: Learn Singleton, Factory, Observer, Strategy patterns.
""",
            'order': 2
        }
    ]
    
    for t in topics_s4:
        Topic.objects.create(stage=stage4, **t)
    print(f"   ✨ Added {len(topics_s4)} topics to Stage 4")

    # Update summary stats
    roadmap.update_stats()
    print("✅ Roadmap creation complete! Stats updated.")

if __name__ == '__main__':
    create_oop_roadmap()
