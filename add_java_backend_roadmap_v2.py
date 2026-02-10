
import os
import django
import sys

# Add project root to sys.path
sys.path.append('/Users/saitejakaki/Divakar/devaproject')

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import Roadmap, RoadmapCategory, Stage, Topic

def create_java_backend_roadmap():
    """Create Comprehensive Java Backend Career Roadmap"""
    
    print("🚀 Initializing Java Backend Roadmap v2 Creation...")
    
    # 1. Get or Create Category
    category, _ = RoadmapCategory.objects.get_or_create(
        slug='backend-development',
        defaults={'name': 'Backend Development'}
    )
    
    # 2. Create Roadmap
    roadmap_slug = 'java-backend-career'
    roadmap_title = 'Java Backend Development (Career Track)'
    
    roadmap, created = Roadmap.objects.get_or_create(
        slug=roadmap_slug,
        defaults={
            'title': roadmap_title,
            'short_description': 'The complete path to becoming a Senior Backend Engineer using Java & Spring Boot.',
            'description': 'Master the entire backend ecosystem: From Core Java and System Design to Microservices and Cloud Deployment. Built for aspiring product-based company engineers.',
            'category': category,
            'difficulty': 'intermediate',
            'estimated_hours': 120,
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
    # STAGE 1: BACKEND FOUNDATIONS (FREE)
    # ==========================================
    stage1 = Stage.objects.create(
        roadmap=roadmap,
        title='Backend Foundations',
        description='Understanding the hidden machinery of the web.',
        order=1,
        is_free=True
    )
    
    topics_s1 = [
        {
            'title': 'What is Backend?',
            'content': """# The Invisible Backbone

## 1. What IS it?
Frontend is the "Waiter" (Menu, ordering, serving).
Backend is the "Kitchen" (Cooking, inventory, recipes).

## 2. Why it matters
- **Data Persistence**: Frontend forgets data on refresh. Backend remembers forever (Database).
- **Security**: You can't trust the client. Logic validation happens here.
- **Heavy Lifting**: Processing payments, sending emails, AI inference.

## 3. The Tech Stack
- **Language**: Java, Python, Go
- **Server**: Tomcat, Netty
- **Database**: PostgreSQL, MongoDB
- **Cache**: Redis
- **Message Queue**: Kafka
""",
            'order': 1
        },
        {
            'title': 'Request – Response Lifecycle',
            'content': """# The Lifecycle of a Click

When you click "Buy Now", what happens?

1.  **DNS Resolution**: Browser finds the IP address of `amazon.in`.
2.  **TCP Handshake**: Browser connects to the server.
3.  **HTTP Request**:
    ```http
    POST /api/orders
    Header: Auth-Token: xyz
    Body: { "itemId": 55, "qty": 1 }
    ```
4.  **Server Processing (The Backend)**:
    - Validate User (Auth Middleware)
    - Check Stock (Database Query)
    - Process Payment (Payment Gateway API)
    - Save Order (Database Insert)
5.  **HTTP Response**:
    ```http
    200 OK
    Body: { "orderId": 999, "status": "Success" }
    ```
6.  **Browser Render**: Shows "Order Confirmed" screen.

**Interview Q**: "What happens when you type google.com?" (This is the answer).
""",
            'order': 2
        }
    ]
    
    for t in topics_s1:
        Topic.objects.create(stage=stage1, **t)
    print(f"   ✨ Added {len(topics_s1)} topics to Stage 1")


    # ==========================================
    # STAGE 2: JAVA FOR BACKEND
    # ==========================================
    stage2 = Stage.objects.create(
        roadmap=roadmap,
        title='Java for Backend',
        description='Core concepts used in production systems.',
        order=2,
        is_free=False
    )
    
    topics_s2 = [
        {
            'title': 'Collections Framework (Deep Dive)',
            'content': """# Collections in Real Apps

We don't just use `ArrayList` for everything.

## 1. ArrayList vs LinkedList
- **ArrayList**: Array-backed. Fast read (O(1)). Slow insert/delete (O(N)).
    - *Use Case*: Fetching a list of products to display.
- **LinkedList**: Node-backed. Fast insert/delete. Slow read.
    - *Use Case*: Implementing a Queue/Deque.

## 2. HashMap (The King)
- Use explicitly for **Caches** and **Lookups**.
- **Internal Working**:
    - `hashCode()` determines the bucket.
    - `equals()` handles collisions (Linked List / Red-Black Tree in Java 8+).
- *Interview Q*: "How does HashMap work internally?"

## 3. HashSet
- Unique items only.
- *Use Case*: Storing a list of "Online User IDs" (fast lookup, no duplicates).
""",
            'order': 1
        },
        {
            'title': 'Multithreading & Concurrency',
            'content': """# Concurrency in Backend

Servers handle 10,000 requests at once. We need threads.

## 1. The Old Way (Thread Class)
`new Thread(() -> ...).start()`
- **Problem**: Creating threads is expensive (OS resource).

## 2. The Right Way (ExecutorService)
Thread Pools! Reuse threads.

```java
// Create a pool of 10 fixed threads
ExecutorService executor = Executors.newFixedThreadPool(10);

executor.submit(() -> {
    sendEmail(user); // Async task
});
```
**Spring Boot** does this automatically for every HTTP request (Tomcat Thread Pool).

## 3. Thread Safety
- **Race Condition**: Two threads updating `balance` same time.
- **Solution**: `synchronized`, `stampedLock`, or `ConcurrentHashMap`.
""",
            'order': 2
        },
        {
            'title': 'Exceptions & Streams',
            'content': """# Modern Java Features

## 1. Exception Handling
- **Checked vs Unchecked**:
    - *Checked* (IOException): Force caller to handle. (e.g., File missing).
    - *Unchecked* (NullPointer): Programming error.
- **Best Practice**: Use Global Exception Handler in Spring (`@ControllerAdvice`). Don't scatter try-catch everywhere.

## 2. Stream API
Functional programming for data processing.

```java
// Filter active users and get emails
List<String> emails = users.stream()
    .filter(u -> u.isActive())
    .map(u -> u.getEmail())
    .collect(Collectors.toList());
```
Readable, concise, parallel-ready (`parallelStream()`).
""",
            'order': 3
        }
    ]
    
    for t in topics_s2:
        Topic.objects.create(stage=stage2, **t)
    print(f"   ✨ Added {len(topics_s2)} topics to Stage 2")


    # ==========================================
    # STAGE 3: BACKEND WITH FRAMEWORKS
    # ==========================================
    stage3 = Stage.objects.create(
        roadmap=roadmap,
        title='Backend with Frameworks',
        description='Building scalable APIs with Spring Boot.',
        order=3,
        is_free=False
    )
    
    topics_s3 = [
        {
            'title': 'Spring Boot Internals',
            'content': """# Spring Boot Magic Explained

## 1. Inversion of Control (IoC)
You don't create objects (`new Service()`). Spring creates them for you.
- **Why?** Decoupling. Easy testing.

## 2. Dependency Injection (DI)
```java
@Service
class UserService { ... }

@RestController
class UserController {
    @Autowired // Inject the instance here
    private UserService service;
}
```

## 3. Annotations
- `@SpringBootApplication`: The entry point.
- `@Component` / `@Service` / `@Repository`: "Hey Spring, manage this bean."
- `@Scope("singleton")`: Default. One instance per app.
""",
            'order': 1
        },
        {
            'title': 'REST API Design Standards',
            'content': """# Designing Professional APIs

## 1. Nouns, not Verbs
- ✅ `GET /users` (Get users)
- ❌ `GET /getUsers`

## 2. HTTP Methods
- `GET`: Read
- `POST`: Create
- `PUT`: Full Update
- `PATCH`: Partial Update (e.g., change just password)
- `DELETE`: Remove

## 3. Status Codes
- `200 OK`: Success
- `201 Created`: Resource made
- `400 Bad Request`: Validation failed
- `401 Unauthorized`: Who are you?
- `403 Forbidden`: You can't do that.
- `500 Server Error`: We crashed.

## 4. Response Structure
Always be consistent.
```json
{
  "success": true,
  "data": { ... },
  "error": null
}
```
""",
            'order': 2
        }
    ]
    
    for t in topics_s3:
        Topic.objects.create(stage=stage3, **t)
    print(f"   ✨ Added {len(topics_s3)} topics to Stage 3")


    # ==========================================
    # STAGE 4: INDUSTRY READINESS
    # ==========================================
    stage4 = Stage.objects.create(
        roadmap=roadmap,
        title='Industry Readiness',
        description='Production concerns: Security, Performance, Deployment.',
        order=4,
        is_free=False
    )
    
    topics_s4 = [
        {
            'title': 'Security Basics',
            'content': """# Securing Your Backend

## 1. Authentication vs Authorization
- **AuthN** (Authentication): "Who are you?" (Login)
- **AuthZ** (Authorization): "What can you do?" (Admin vs User)

## 2. JWT (JSON Web Tokens)
Stateless authentication.
1. User logs in.
2. Server signs a token (`HMACSHA256`) and sends it.
3. Client sends token in header (`Authorization: Bearer xyz`) for every request.
4. Server verifies signature. NO database lookup needed!

## 3. SQL Injection
- **Bad**: `query = "SELECT * FROM users WHERE name = '" + input + "'"`
- **Hack**: input = `' OR '1'='1` -> Dumps entire DB.
- **Fix**: Use JPA / PreparedStatement (inputs are treated as data, not code).
""",
            'order': 1
        },
        {
            'title': 'Backend Performance',
            'content': """# Making it Fast

## 1. Caching (Redis)
Don't hit the DB for "User Profile" every time.
- Read from Cache (1ms).
- If miss, read from DB (10ms) and save to Cache.

## 2. Database Indexing
(Covered in SQL roadmap, but apply it here with `@Index` annotations).

## 3. Pagination
Never `findAll()`.
Use `Pageable` in Spring Data Repository.

## 4. Connection Pooling (HikariCP)
Opening a DB connection is slow. Keep a pool of 10 connections open and reuse them. Spring Boot does this by default.
""",
            'order': 2
        }
    ]
    
    for t in topics_s4:
        Topic.objects.create(stage=stage4, **t)
    print(f"   ✨ Added {len(topics_s4)} topics to Stage 4")

    # Update stats
    roadmap.update_stats()
    print("✅ Java Backend Roadmap creation complete! Stats updated.")

if __name__ == '__main__':
    create_java_backend_roadmap()
