"""
Add Java Backend Development Roadmap
Complete roadmap for BTech/CSE students to become industry-ready Java backend developers
"""

import os
import django
import sys

# Setup Django
sys.path.append('/Users/saitejakaki/Divakar/devaproject')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import Roadmap, RoadmapCategory, Stage, Topic

def create_java_backend_roadmap():
    """Create comprehensive Java Backend Development roadmap"""
    
    # Get or create Backend category
    category, _ = RoadmapCategory.objects.get_or_create(
        slug='backend-development',
        defaults={
            'name': 'Backend Development',
            'icon': 'fas fa-server',
            'description': 'Server-side development and API creation'
        }
    )
    
    # Create roadmap
    roadmap, created = Roadmap.objects.get_or_create(
        slug='java-backend-development',
        defaults={
            'title': 'Java Backend Development',
            'short_description': 'Complete Java backend roadmap for BTech/CSE students - from basics to industry-ready skills',
            'description': 'Master Java backend development from scratch. Learn Spring Boot, REST APIs, databases, authentication, and deployment. Perfect for students aiming for backend engineer roles.',
            'category': category,
            'difficulty': 'intermediate',
            'estimated_hours': 200,
            'is_premium': True,
            'is_featured': True,
            'is_active': True
        }
    )
    
    if created:
        print(f"✅ Created roadmap: {roadmap.title}")
    else:
        print(f"ℹ️  Roadmap already exists: {roadmap.title}")
        return
    
    # Stage 1: Backend Foundations (FREE)
    stage1 = Stage.objects.create(
        roadmap=roadmap,
        title='Backend Foundations',
        description='Understand what backend development actually means and how it works in real applications',
        order=1,
        is_free=True
    )
    
    topics_stage1 = [
        {
            'title': 'What is Backend Development?',
            'content': '''# What is Backend Development?

## Introduction
Backend development is the **server-side** of web applications. While frontend handles what users see, backend manages data, business logic, and server operations.

## Real-World Example
When you use Instagram:
- **Frontend**: The app interface you see
- **Backend**: Stores photos, manages user data, handles likes/comments

## What Backend Does
- **Data Storage**: Saves user information, posts, messages
- **Business Logic**: Processes login, validates data
- **API Creation**: Connects frontend with database
- **Security**: Protects user data and authentication

## Backend Tech Stack
- **Programming Language**: Java, Python, Node.js
- **Database**: MySQL, PostgreSQL, MongoDB
- **Server**: Handles requests from millions of users

## Why Java for Backend?
- Used by Netflix, Amazon, LinkedIn
- Fast, secure, and scalable
- High-paying jobs in India and abroad
- Strong community support

## Key Takeaway
Backend is the **brain** of any application. It makes everything work behind the scenes!
''',
            'order': 1
        },
        {
            'title': 'Client-Server Architecture',
            'content': '''# Client-Server Architecture

## What is Client-Server Model?
The **client-server architecture** is how modern web applications work. Client requests, server responds.

## Real Example: WhatsApp
1. **Client** (Your phone): Sends "Hello" message
2. **Server** (WhatsApp backend): Receives message, stores it
3. **Server**: Sends message to friend's phone
4. **Client** (Friend's phone): Displays "Hello"

## Components

### Client (Frontend)
- Web browser (Chrome, Firefox)
- Mobile app (Android, iOS)
- **Job**: Send requests, display responses

### Server (Backend)
- Runs 24/7 on cloud (AWS, Google Cloud)
- Processes requests from millions of users
- **Job**: Handle logic, access database, send responses

## How They Communicate

```
Client → Request → Server
Client ← Response ← Server
```

### Example: Login Flow
1. User enters email/password (Client)
2. Client sends data to server
3. Server checks database
4. Server sends "Login Success" or "Invalid Password"
5. Client shows appropriate screen

## Request-Response Cycle
- **Request**: Client asks for something (data, login, etc.)
- **Response**: Server replies with data or status

## Why This Matters
- Separation of concerns (frontend vs backend)
- Scalability: One server handles millions of clients
- Security: Sensitive logic stays on server

## Key Takeaway
Client and server work together like a **restaurant**: Client orders (request), kitchen prepares (backend logic), waiter serves (response).
''',
            'order': 2
        },
        {
            'title': 'HTTP Requests and Responses',
            'content': '''# HTTP Requests and Responses

## What is HTTP?
**HTTP (HyperText Transfer Protocol)** is the language that clients and servers use to communicate.

## Real Example: Food Delivery App
- You search for "Pizza" → **HTTP Request**
- Server sends pizza list → **HTTP Response**

## HTTP Request Components

### 1. Method (Action Type)
- **GET**: Fetch data (e.g., get user profile)
- **POST**: Create data (e.g., register new user)
- **PUT**: Update data (e.g., edit profile)
- **DELETE**: Remove data (e.g., delete post)

### 2. URL (Endpoint)
```
https://api.instagram.com/users/123/posts
```
- **Domain**: api.instagram.com
- **Path**: /users/123/posts

### 3. Headers
Contains metadata:
```
Content-Type: application/json
Authorization: Bearer token123
```

### 4. Body (For POST, PUT)
```json
{
  "username": "john_doe",
  "email": "john@example.com"
}
```

## HTTP Response Components

### 1. Status Code
- **200**: Success (OK)
- **201**: Created (New resource created)
- **400**: Bad Request (Client error)
- **401**: Unauthorized (Login required)
- **404**: Not Found
- **500**: Internal Server Error (Backend crashed)

### 2. Response Body
```json
{
  "status": "success",
  "data": {
    "user_id": 123,
    "username": "john_doe"
  }
}
```

## Request-Response Example

**Request:**
```
GET https://api.example.com/products/5
Authorization: Bearer token123
```

**Response:**
```
Status: 200 OK
{
  "product_id": 5,
  "name": "Laptop",
  "price": 50000
}
```

## Why This Matters
- Every backend API you build uses HTTP
- Understanding requests/responses is **crucial** for backend
- Job interviews **always** ask about HTTP methods and status codes

## Key Takeaway
HTTP is the **postal system** of the internet: Request is the letter, Response is the reply!
''',
            'order': 3
        },
        {
            'title': 'Role of Backend in Real Applications',
            'content': '''# Role of Backend in Real Applications

## Introduction
Backend is the **invisible powerhouse** that makes applications work. Let's see what backend does in real companies.

## Real Application Examples

### 1. E-Commerce (Amazon, Flipkart)
**Backend handles:**
- User login and authentication
- Product search and filtering
- Shopping cart management
- Payment processing (Razorpay, Paytm)
- Order tracking
- Inventory management

**Example Flow:**
1. User searches "laptop"
2. Backend queries database for laptops
3. Applies filters (price, brand)
4. Sends sorted results to frontend

### 2. Social Media (Instagram, Twitter)
**Backend handles:**
- User registration and profiles
- Post creation and storage
- Like/comment functionality
- Follow/unfollow logic
- Feed generation (algorithm)
- Notifications

### 3. Banking Apps
**Backend handles:**
- Account balance checks
- Money transfers
- Transaction history
- Security and encryption
- OTP generation
- Fraud detection

## Core Backend Responsibilities

### 1. Data Management
- Store user data, posts, transactions
- Database operations (Create, Read, Update, Delete)
- Data validation and sanitization

### 2. Business Logic
- Registration rules (email format, password strength)
- Pricing calculations
- Discount application
- User permissions

### 3. API Development
- Create endpoints for frontend to use
- Define request/response formats
- Handle errors gracefully

### 4. Security
- Password hashing (never store plain passwords!)
- JWT tokens for authentication
- Input validation against SQL injection
- Rate limiting to prevent abuse

### 5. Integration
- Connect to payment gateways
- Send emails/SMS
- Integrate with third-party APIs

### 6. Performance & Scaling
- Handle millions of users simultaneously
- Database optimization
- Caching frequently accessed data

## Backend vs Frontend

| Backend | Frontend |
|---------|----------|
| Handles data | Displays data |
| Business logic | User interface |
| Database operations | Animations |
| Security | Look and feel |
| Server-side | Client-side |

## Backend Engineer in Companies

### Typical Day:
- Build new API endpoints
- Fix bugs in existing APIs
- Optimize database queries
- Review code from teammates
- Deploy updates to production

### Skills Expected:
- Java/Python/Node.js
- SQL and databases
- REST API design
- Git and version control
- Cloud platforms (AWS, Azure)

## Why Backend is Important
- **Apps cannot function without backend**
- High demand for backend engineers
- Better pay than many other roles
- Work on complex, challenging problems

## Key Takeaway
Backend is the **engine** of an application. Without it, apps are just pretty screens with no functionality!
''',
            'order': 4
        },
        {
            'title': 'Java\'s Role in Backend Systems',
            'content': '''# Java's Role in Backend Systems

## Why Java for Backend?

### 1. Industry Adoption
**Companies using Java backend:**
- Netflix (streaming service)
- LinkedIn (social network)
- Amazon (e-commerce)
- Uber (ride-sharing)
- Flipkart, Paytm (Indian unicorns)

### 2. Reasons Companies Choose Java

**a) Platform Independent**
```
Write once, run anywhere
- Develop on Windows
- Deploy on Linux servers
- Same code works everywhere
```

**b) Performance**
- Fast execution (JVM optimization)
- Handles millions of requests
- Low latency for real-time apps

**c) Scalability**
- Handles increasing users easily
- Multithreading support
- Load balancing capabilities

**d) Security**
- Built-in security features
- Strong type checking
- Memory management

**e) Rich Ecosystem**
- Spring Boot (backend framework)
- Hibernate (database ORM)
- Maven/Gradle (build tools)
- Huge community support

## Java Backend Tech Stack

### Core Components
1. **Java SE**: Core language features
2. **Spring Framework**: Dependency injection, MVC
3. **Spring Boot**: Build production-ready apps fast
4. **Maven/Gradle**: Dependency management
5. **JPA/Hibernate**: Database interaction
6. **MySQL/PostgreSQL**: Relational databases

### Modern Java Backend Stack
```
Frontend → REST API (Spring Boot) → Database
                ↓
        Business Logic (Java)
                ↓
    Third-party Services (Payments, Email)
```

## Java Backend Use Cases

### 1. E-Commerce Platforms
- Product catalog management
- Shopping cart APIs
- Payment integration
- Order processing

### 2. Banking Systems
- Core banking solutions
- Transaction processing
- Account management
- Security compliance

### 3. Enterprise Applications
- ERP systems (SAP)
- CRM platforms
- HR management systems

### 4. Microservices
- Small, independent services
- Easy to scale
- Used by Netflix, Amazon

## Java vs Other Backend Languages

| Feature | Java | Python | Node.js |
|---------|------|--------|---------|
| Speed | Fast | Medium | Fast |
| Typing | Static | Dynamic | Dynamic |
| Use Case | Enterprise | Data Science | Real-time |
| Jobs (India) | High | Medium | Medium |
| Learning Curve | Medium | Easy | Medium |

## Backend Job Market in India

### Entry Level (0-2 years)
- **Role**: Backend Developer, SDE-1
- **Salary**: ₹4-8 LPA
- **Companies**: Startups, service-based

### Mid Level (2-5 years)
- **Role**: Senior Backend Engineer, SDE-2
- **Salary**: ₹8-20 LPA
- **Companies**: Flipkart, Swiggy, PayTM

### Senior Level (5+ years)
- **Role**: Lead Engineer, Architect
- **Salary**: ₹20-50+ LPA
- **Companies**: FAANG, unicorns

## Skills You Need

### Must Have:
- Core Java (OOPS, Collections)
- Spring Boot
- REST APIs
- SQL and databases
- Git version control

### Good to Have:
- Microservices architecture
- Docker, Kubernetes
- Redis caching
- AWS/Azure cloud
- System design basics

## Why Learn Java Backend Now?

1. **High Demand**: Most companies need Java developers
2. **Career Growth**: Clear path from junior to architect
3. **Stability**: Java has been strong for 25+ years
4. **Remote Work**: Many opportunities for remote jobs
5. **Competitive Salary**: Backend roles pay well

## Key Takeaway
Java is the **backbone** of enterprise backend development. Learning it opens doors to high-paying, stable careers at top companies!
''',
            'order': 5
        }
    ]
    
    for topic_data in topics_stage1:
        Topic.objects.create(stage=stage1, **topic_data)
    
    print(f"✅ Stage 1: {stage1.title} - {len(topics_stage1)} topics")
    
    # Stage 2: Core Java for Backend
    stage2 = Stage.objects.create(
        roadmap=roadmap,
        title='Core Java for Backend',
        description='Master the Java skills essential for backend development - OOPS, Collections, Exception Handling',
        order=2,
        is_free=False
    )
    
    topics_stage2 = [
        {
            'title': 'Core Java Revision (OOPS)',
            'content': '''# Core Java Revision (OOPS)

## Why OOPS for Backend?
Object-Oriented Programming is the **foundation** of Java backend development. Every Spring Boot application uses OOPS concepts.

## 1. Classes and Objects

### Real Example: User Management System
```java
// Class: Blueprint for User
public class User {
    // Properties
    private Long id;
    private String username;
    private String email;
    private String password;
    
    // Constructor
    public User(Long id, String username, String email) {
        this.id = id;
        this.username = username;
        this.email = email;
    }
    
    // Methods
    public void sendWelcomeEmail() {
        System.out.println("Welcome email sent to " + email);
    }
}

// Object: Actual instance
User user1 = new User(1L, "john_doe", "john@example.com");
user1.sendWelcomeEmail();
```

**Backend Usage**: Every database entity (User, Product, Order) is a class!

## 2. Encapsulation

### Hiding Implementation Details
```java
public class BankAccount {
    private double balance;  // Private: Cannot access directly
    
    // Public methods to interact
    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
        }
    }
    
    public double getBalance() {
        return balance;
    }
    
    // Password is validated but not exposed
    private boolean validatePassword(String pwd) {
        return pwd.length() >= 8;
    }
}
```

**Backend Usage**: Hide sensitive logic (password hashing, payment processing) from external access.

## 3. Inheritance

### Code Reusability
```java
// Base class
public abstract class Employee {
    protected String name;
    protected double baseSalary;
    
    public abstract double calculateSalary();
}

// Derived classes
public class FullTimeEmployee extends Employee {
    private double bonus;
    
    @Override
    public double calculateSalary() {
        return baseSalary + bonus;
    }
}

public class ContractEmployee extends Employee {
    private int hoursWorked;
    private double hourlyRate;
    
    @Override
    public double calculateSalary() {
        return hoursWorked * hourlyRate;
    }
}
```

**Backend Usage**: Common functionality in base class, specific logic in subclasses.

## 4. Polymorphism

### Same Method, Different Behavior
```java
public interface PaymentProcessor {
    void processPayment(double amount);
}

public class CreditCardPayment implements PaymentProcessor {
    @Override
    public void processPayment(double amount) {
        // Credit card logic
        System.out.println("Processing credit card payment: ₹" + amount);
    }
}

public class UPIPayment implements PaymentProcessor {
    @Override
    public void processPayment(double amount) {
        // UPI logic
        System.out.println("Processing UPI payment: ₹" + amount);
    }
}

// Usage in backend
PaymentProcessor payment;
if (paymentType.equals("CARD")) {
    payment = new CreditCardPayment();
} else {
    payment = new UPIPayment();
}
payment.processPayment(500.0);
```

**Backend Usage**: Swap implementations without changing client code (Strategy Pattern).

## 5. Abstraction

### Focus on "What" Not "How"
```java
public interface NotificationService {
    void sendNotification(String message);
}

public class EmailService implements NotificationService {
    @Override
    public void sendNotification(String message) {
        // Complex email sending logic hidden
        System.out.println("Email sent: " + message);
    }
}

public class SMSService implements NotificationService {
    @Override
    public void sendNotification(String message) {
        // Complex SMS logic hidden
        System.out.println("SMS sent: " + message);
    }
}
```

**Backend Usage**: Services (Email, SMS, Push) expose simple interfaces, hide complex implementations.

## OOPS in Spring Boot Backend

### Entity Class (JPA)
```java
@Entity
@Table(name = "products")
public class Product {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(nullable = false)
    private String name;
    
    private double price;
    
    // Getters and Setters
}
```

### Service Class (Business Logic)
```java
@Service
public class ProductService {
    @Autowired
    private ProductRepository repository;
    
    public Product createProduct(Product product) {
        // Business logic here
        return repository.save(product);
    }
}
```

### Controller Class (REST API)
```java
@RestController
@RequestMapping("/api/products")
public class ProductController {
    @Autowired
    private ProductService service;
    
    @PostMapping
    public Product createProduct(@RequestBody Product product) {
        return service.createProduct(product);
    }
}
```

## Key Takeaways
- **Classes/Objects**: Foundation of backend entities
- **Encapsulation**: Protect sensitive data  
- **Inheritance**: Reuse common code
- **Polymorphism**: Flexible implementations
- **Abstraction**: Hide complexity

## Practice Exercise
Create a **Book Management System** with:
- Book class (id, title, author, price)
- BorrowableBook subclass (borrowDate, returnDate)
- BookService interface (addBook, removeBook, searchBook)
''',
            'order': 1
        },
        {
            'title': 'Exception Handling in Backend',
            'content': '''# Exception Handling in Backend

## Why Exception Handling Matters
In backend, **errors will happen**: database down, invalid input, network failure. Proper exception handling prevents app crashes and provides meaningful error messages.

## Types of Exceptions

### 1. Checked Exceptions (Compile-time)
Must be handled or declared.

```java
// File operations
public void readUserData(String filename) throws IOException {
    BufferedReader reader = new BufferedReader(new FileReader(filename));
    String line = reader.readLine();
    reader.close();
}
```

### 2. Unchecked Exceptions (Runtime)
Not mandatory to handle, but should for robustness.

```java
// Division by zero
int result = 10 / 0;  // ArithmeticException

// Null pointer
String name = null;
name.toUpperCase();  // NullPointerException

// Array index
int[] arr = new int[5];
arr[10] = 100;  // ArrayIndexOutOfBoundsException
```

## Try-Catch-Finally

### Basic Syntax
```java
try {
    // Code that might throw exception
    int result = 10 / 0;
} catch (ArithmeticException e) {
    System.out.println("Cannot divide by zero!");
} finally {
    System.out.println("This always executes");
}
```

### Multiple Catch Blocks
```java
public User getUserById(Long id) {
    try {
        // Database query
        return database.findById(id);
    } catch (SQLException e) {
        System.out.println("Database error: " + e.getMessage());
    } catch (NullPointerException e) {
        System.out.println("User not found");
    } catch (Exception e) {
        System.out.println("Unknown error: " + e.getMessage());
    }
    return null;
}
```

## Custom Exceptions

### Backend Example: User Not Found
```java
// Custom exception class
public class UserNotFoundException extends RuntimeException {
    public UserNotFoundException(String message) {
        super(message);
    }
}

// Usage in service
@Service
public class UserService {
    public User getUserById(Long id) {
        User user = repository.findById(id).orElse(null);
        if (user == null) {
            throw new UserNotFoundException("User with ID " + id + " not found");
        }
        return user;
    }
}
```

## Exception Handling in REST APIs

### Global Exception Handler (Spring Boot)
```java
@RestControllerAdvice
public class GlobalExceptionHandler {
    
    @ExceptionHandler(UserNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleUserNotFound(UserNotFoundException ex) {
        ErrorResponse error = new ErrorResponse(
            404,
            ex.getMessage(),
            System.currentTimeMillis()
        );
        return new ResponseEntity<>(error, HttpStatus.NOT_FOUND);
    }
    
    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorResponse> handleGenericException(Exception ex) {
        ErrorResponse error = new ErrorResponse(
            500,
            "Internal server error",
            System.currentTimeMillis()
        );
        return new ResponseEntity<>(error, HttpStatus.INTERNAL_SERVER_ERROR);
    }
}
```

### Error Response DTO
```java
public class ErrorResponse {
    private int statusCode;
    private String message;
    private long timestamp;
    
    // Constructor, getters, setters
}
```

## Real Backend Scenarios

### 1. User Registration
```java
public User registerUser(UserDTO userDTO) {
    try {
        // Validate email
        if (repository.existsByEmail(userDTO.getEmail())) {
            throw new EmailAlreadyExistsException("Email already registered");
        }
        
        // Hash password
        String hashedPassword = passwordEncoder.encode(userDTO.getPassword());
        
        // Save user
        User user = new User();
        user.setEmail(userDTO.getEmail());
        user.setPassword(hashedPassword);
        return repository.save(user);
        
    } catch (EmailAlreadyExistsException e) {
        throw e;  // Re-throw custom exception
    } catch (Exception e) {
        throw new RuntimeException("Registration failed: " + e.getMessage());
    }
}
```

### 2. Payment Processing
```java
public PaymentResponse processPayment(PaymentRequest request) {
    try {
        // Validate amount
        if (request.getAmount() <= 0) {
            throw new InvalidAmountException("Amount must be positive");
        }
        
        // Check account balance
        if (getBalance(request.getUserId()) < request.getAmount()) {
            throw new InsufficientBalanceException("Not enough balance");
        }
        
        // Process payment
        return paymentGateway.process(request);
        
    } catch (PaymentGatewayException e) {
        throw new PaymentFailedException("Payment gateway error: " + e.getMessage());
    }
}
```

## Best Practices

### 1. Don't Swallow Exceptions
```java
// ❌ Bad
try {
    riskyOperation();
} catch (Exception e) {
    // Empty catch block - error is lost!
}

// ✅ Good
try {
    riskyOperation();
} catch (Exception e) {
    logger.error("Operation failed", e);
    throw new CustomException("Operation failed", e);
}
```

### 2. Use Specific Exceptions
```java
// ❌ Bad
catch (Exception e) {
    // Too generic
}

// ✅ Good
catch (SQLException e) {
    // Handle database error
} catch (IOException e) {
    // Handle file error
}
```

### 3. Meaningful Error Messages
```java
// ❌ Bad
throw new RuntimeException("Error");

// ✅ Good
throw new UserNotFoundException("User with ID " + userId + " not found in database");
```

### 4. Clean Up Resources
```java
// Try-with-resources (Java 7+)
try (BufferedReader reader = new BufferedReader(new FileReader("file.txt"))) {
    String line = reader.readLine();
}  // Automatically closes reader
```

## Common Backend Exceptions

| Exception | When It Occurs | Example |
|-----------|----------------|---------|
| NullPointerException | Accessing null object | `user.getName()` when user is null |
| SQLException | Database error | Connection failed, query error |
| IOException | File/network error | File not found, network timeout |
| IllegalArgumentException | Invalid method argument | Negative age value |
| DateTimeParseException | Date parsing error | Invalid date format |

## Key Takeaways
- **Always handle exceptions** in backend to prevent crashes
- **Use custom exceptions** for business logic errors
- **Global exception handler** provides consistent error responses
- **Log exceptions** for debugging
- **Provide meaningful messages** to frontend

## Practice Exercise
Build a simple **Product Service** with exception handling:
- `ProductNotFoundException`: When product ID doesn't exist
- `InvalidPriceException`: When price is negative
- `DuplicateProductException`: When product name already exists
''',
            'order': 2
        },
        {
            'title': 'Collections Framework',
            'content': '''# Collections Framework

## Why Collections in Backend?
Backend applications deal with **large amounts of data**: user lists, product catalogs, order history. Collections Framework provides efficient data structures to manage this data.

## Collection Hierarchy
```
Collection (Interface)
├── List (Ordered, allows duplicates)
│   ├── ArrayList
│   ├── LinkedList
│   └── Vector
├── Set (Unordered, no duplicates)
│   ├── HashSet
│   ├── LinkedHashSet
│   └── TreeSet
└── Queue (FIFO)
    ├── PriorityQueue
    └── Deque
    
Map (Key-Value pairs)
├── HashMap
├── LinkedHashMap
└── TreeMap
```

## 1. ArrayList

### When to Use
- Need fast random access by index
- Read operations > Write operations
- Order matters

### Backend Example: Product List
```java
List<Product> products = new ArrayList<>();

// Add products
products.add(new Product(1L, "Laptop", 50000.0));
products.add(new Product(2L, "Mouse", 500.0));
products.add(new Product(3L, "Keyboard", 1500.0));

// Get product by index
Product firstProduct = products.get(0);

// Iterate
for (Product product : products) {
    System.out.println(product.getName());
}

// Filter products (Java 8+ Streams)
List<Product> expensive = products.stream()
    .filter(p -> p.getPrice() > 1000)
    .collect(Collectors.toList());
```

## 2. HashSet

### When to Use
- Need unique elements (no duplicates)
- Don't care about order
- Fast lookup (O(1))

### Backend Example: Unique Email Validation
```java
Set<String> registeredEmails = new HashSet<>();

public boolean isEmailRegistered(String email) {
    return registeredEmails.contains(email);
}

public void registerEmail(String email) {
    if (registeredEmails.add(email)) {
        System.out.println("Email registered successfully");
    } else {
        System.out.println("Email already exists");
    }
}
```

## 3. HashMap

### When to Use
- Store key-value pairs
- Fast lookup by key
- Most commonly used in backend

### Backend Example: User Cache
```java
Map<Long, User> userCache = new HashMap<>();

// Add user
userCache.put(1L, new User("john_doe", "john@example.com"));
userCache.put(2L, new User("jane_doe", "jane@example.com"));

// Get user by ID
User user = userCache.get(1L);

// Check if ID exists
if (userCache.containsKey(1L)) {
    System.out.println("User found");
}

// Iterate over entries
for (Map.Entry<Long, User> entry : userCache.entrySet()) {
    System.out.println("ID: " + entry.getKey() + ", User: " + entry.getValue());
}
```

## 4. LinkedList

### When to Use
- Frequent insertions/deletions at beginning/end
- Implement queue/stack

### Backend Example: Order Processing Queue
```java
Queue<Order> orderQueue = new LinkedList<>();

// Add orders to queue
orderQueue.offer(new Order(1L, "John", 1000.0));
orderQueue.offer(new Order(2L, "Jane", 2000.0));

// Process orders (FIFO)
while (!orderQueue.isEmpty()) {
    Order order = orderQueue.poll();
    processOrder(order);
}
```

## 5. TreeMap

### When to Use
- Need sorted keys
- Range queries

### Backend Example: Leaderboard (Sorted by Score)
```java
TreeMap<Integer, String> leaderboard = new TreeMap<>(Collections.reverseOrder());

// Add scores (score -> username)
leaderboard.put(95, "Alice");
leaderboard.put(100, "Bob");
leaderboard.put(88, "Charlie");

// Top 3 players (already sorted)
int count = 0;
for (Map.Entry<Integer, String> entry : leaderboard.entrySet()) {
    System.out.println(entry.getValue() + ": " + entry.getKey());
    if (++count == 3) break;
}
```

## Java 8 Streams (Modern Collections)

### Filter and Map
```java
List<Product> products = getProducts();

// Get names of products > ₹1000
List<String> expensiveProductNames = products.stream()
    .filter(p -> p.getPrice() > 1000)
    .map(Product::getName)
    .collect(Collectors.toList());

// Total price
double totalPrice = products.stream()
    .mapToDouble(Product::getPrice)
    .sum();

// Group by category
Map<String, List<Product>> byCategory = products.stream()
    .collect(Collectors.groupingBy(Product::getCategory));
```

### Sorting
```java
// Sort by price (ascending)
List<Product> sorted = products.stream()
    .sorted(Comparator.comparing(Product::getPrice))
    .collect(Collectors.toList());

// Sort by price (descending)
List<Product> sortedDesc = products.stream()
    .sorted(Comparator.comparing(Product::getPrice).reversed())
    .collect(Collectors.toList());
```

## Real Backend Use Cases

### 1. Shopping Cart (HashMap)
```java
@Service
public class CartService {
    // User ID -> (Product ID -> Quantity)
    private Map<Long, Map<Long, Integer>> userCarts = new HashMap<>();
    
    public void addToCart(Long userId, Long productId, int quantity) {
        userCarts.putIfAbsent(userId, new HashMap<>());
        Map<Long, Integer> cart = userCarts.get(userId);
        cart.put(productId, cart.getOrDefault(productId, 0) + quantity);
    }
    
    public int getTotalItems(Long userId) {
        return userCarts.getOrDefault(userId, new HashMap<>())
                        .values()
                        .stream()
                        .mapToInt(Integer::intValue)
                        .sum();
    }
}
```

### 2. Recent Activity (LinkedList - Limited Size)
```java
public class ActivityTracker {
    private static final int MAX_SIZE = 10;
    private LinkedList<String> recentActivities = new LinkedList<>();
    
    public void addActivity(String activity) {
        recentActivities.addFirst(activity);
        if (recentActivities.size() > MAX_SIZE) {
            recentActivities.removeLast();
        }
    }
    
    public List<String> getRecentActivities() {
        return new ArrayList<>(recentActivities);
    }
}
```

### 3. Unique Visitor Tracking (HashSet)
```java
@Service
public class AnalyticsService {
    private Set<String> uniqueVisitors = new HashSet<>();
    
    public void trackVisit(String ipAddress) {
        uniqueVisitors.add(ipAddress);
    }
    
    public int getUniqueVisitorCount() {
        return uniqueVisitors.size();
    }
}
```

## Performance Comparison

| Operation | ArrayList | LinkedList | HashSet | HashMap |
|-----------|-----------|------------|---------|---------|
| Add | O(1) | O(1) | O(1) | O(1) |
| Get (by index) | O(1) | O(n) | - | - |
| Contains | O(n) | O(n) | O(1) | O(1) |
| Remove | O(n) | O(1)* | O(1) | O(1) |

*Only if removing from beginning/end

## Best Practices

### 1. Use Interface Types
```java
// ✅ Good (flexible)
List<String> names = new ArrayList<>();

// ❌ Bad (tight coupling)
ArrayList<String> names = new ArrayList<>();
```

### 2. Initialize with Capacity
```java
// If you know size upfront
List<User> users = new ArrayList<>(1000);
Map<String, User> userMap = new HashMap<>(1000);
```

### 3. Use Immutable Collections
```java
List<String> immutable = List.of("A", "B", "C");  // Java 9+
// Cannot add/remove elements
```

## Key Takeaways
- **ArrayList**: Default choice for lists
- **HashMap**: Most used for key-value storage
- **HashSet**: When uniqueness is needed
- **Streams**: Modern way to process collections
- **Choose based on use case**: Performance matters!

## Practice Exercise
Build a **Student Management System** using:
- ArrayList for student list
- HashMap for student ID → Student mapping
- TreeMap for ranking by marks
- HashSet for unique student emails
''',
            'order': 3
        },
        {
            'title': 'Java I/O Basics',
            'content': '''# Java I/O Basics

## Why I/O in Backend?
Backend applications need to:
- Read configuration files
- Write logs
- Handle file uploads (images, PDFs)
- Export data (CSV, Excel)
- Read/write to network streams

## I/O Streams Hierarchy

### Byte Streams (Binary data: images, PDFs)
- **InputStream** → FileInputStream, BufferedInputStream
- **OutputStream** → FileOutputStream, BufferedOutputStream

### Character Streams (Text data: logs, config)
- **Reader** → FileReader, BufferedReader
- **Writer** → FileWriter, BufferedWriter

## 1. Reading Files

### Reading Text File (Line by Line)
```java
public List<String> readFile(String filename) {
    List<String> lines = new ArrayList<>();
    
    try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
        String line;
        while ((line = reader.readLine()) != null) {
            lines.add(line);
        }
    } catch (IOException e) {
        e.printStackTrace();
    }
    
    return lines;
}
```

### Modern Way (Java 8+)
```java
public List<String> readFileModern(String filename) throws IOException {
    return Files.readAllLines(Paths.get(filename));
}
```

## 2. Writing Files

### Writing to Text File
```java
public void writeFile(String filename, List<String> lines) {
    try (BufferedWriter writer = new BufferedWriter(new FileWriter(filename))) {
        for (String line : lines) {
            writer.write(line);
            writer.newLine();
        }
    } catch (IOException e) {
        e.printStackTrace();
    }
}
```

### Append to File
```java
try (FileWriter writer = new FileWriter("log.txt", true)) {  // true = append mode
    writer.write("New log entry\n");
}
```

## 3. File Operations (Java NIO)

### Check if File Exists
```java
Path path = Paths.get("data.txt");
if (Files.exists(path)) {
    System.out.println("File exists");
}
```

### Create Directory
```java
Path dir = Paths.get("uploads");
if (!Files.exists(dir)) {
    Files.createDirectories(dir);
}
```

### Copy File
```java
Path source = Paths.get("original.txt");
Path target = Paths.get("copy.txt");
Files.copy(source, target, StandardCopyOption.REPLACE_EXISTING);
```

### Delete File
```java
Files.deleteIfExists(Paths.get("temp.txt"));
```

## 4. Binary File Handling

### Writing Binary Data
```java
public void writeBytes(String filename, byte[] data) {
    try (FileOutputStream fos = new FileOutputStream(filename)) {
        fos.write(data);
    } catch (IOException e) {
        e.printStackTrace();
    }
}
```

### Reading Binary Data
```java
public byte[] readBytes(String filename) throws IOException {
    return Files.readAllBytes(Paths.get(filename));
}
```

## Real Backend Use Cases

### 1. Logging Service
```java
@Service
public class LoggingService {
    private static final String LOG_FILE = "application.log";
    
    public void log(String message) {
        String timestamp = LocalDateTime.now().toString();
        String logEntry = String.format("[%s] %s\n", timestamp, message);
        
        try (FileWriter writer = new FileWriter(LOG_FILE, true)) {
            writer.write(logEntry);
        } catch (IOException e) {
            System.err.println("Failed to write log: " + e.getMessage());
        }
    }
}
```

### 2. File Upload (Image/PDF)
```java
@RestController
@RequestMapping("/api/files")
public class FileUploadController {
    
    @PostMapping("/upload")
    public ResponseEntity<String> uploadFile(@RequestParam("file") MultipartFile file) {
        try {
            // Validate file
            if (file.isEmpty()) {
                return ResponseEntity.badRequest().body("File is empty");
            }
            
            // Create upload directory
            Path uploadDir = Paths.get("uploads");
            Files.createDirectories(uploadDir);
            
            // Save file
            String filename = System.currentTimeMillis() + "_" + file.getOriginalFilename();
            Path filePath = uploadDir.resolve(filename);
            Files.write(filePath, file.getBytes());
            
            return ResponseEntity.ok("File uploaded: " + filename);
            
        } catch (IOException e) {
            return ResponseEntity.status(500).body("Upload failed: " + e.getMessage());
        }
    }
}
```

### 3. CSV Export
```java
@Service
public class UserExportService {
    
    public void exportUsersToCSV(List<User> users, String filename) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(filename))) {
            // Header
            writer.write("ID,Username,Email,Created\n");
            
            // Data rows
            for (User user : users) {
                String row = String.format("%d,%s,%s,%s\n",
                    user.getId(),
                    user.getUsername(),
                    user.getEmail(),
                    user.getCreatedAt()
                );
                writer.write(row);
            }
            
        } catch (IOException e) {
            throw new RuntimeException("CSV export failed", e);
        }
    }
}
```

### 4. Configuration Reader
```java
@Component
public class ConfigReader {
    
    public Map<String, String> readConfig(String filename) {
        Map<String, String> config = new HashMap<>();
        
        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = reader.readLine()) != null) {
                if (line.contains("=")) {
                    String[] parts = line.split("=", 2);
                    config.put(parts[0].trim(), parts[1].trim());
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        
        return config;
    }
}
```

## 5. Properties File Handling

### Reading Properties
```java
Properties props = new Properties();
try (InputStream input = new FileInputStream("application.properties")) {
    props.load(input);
    String dbUrl = props.getProperty("database.url");
    String dbUser = props.getProperty("database.username");
}
```

### Writing Properties
```java
Properties props = new Properties();
props.setProperty("app.name", "99Roadmap");
props.setProperty("app.version", "1.0");

try (OutputStream output = new FileOutputStream("app.properties")) {
    props.store(output, "Application Settings");
}
```

## Best Practices

### 1. Always Close Resources
```java
// ❌ Bad (might not close if exception occurs)
FileReader reader = new FileReader("file.txt");
// ... use reader
reader.close();

// ✅ Good (try-with-resources - auto closes)
try (FileReader reader = new FileReader("file.txt")) {
    // ... use reader
}
```

### 2. Handle Large Files Efficiently
```java
// ❌ Bad (loads entire file into memory)
String content = new String(Files.readAllBytes(Paths.get("large.txt")));

// ✅ Good (reads line by line)
try (Stream<String> lines = Files.lines(Paths.get("large.txt"))) {
    lines.forEach(System.out::println);
}
```

### 3. Validate File Paths
```java
public boolean isValidUpload(String filename) {
    // Check for directory traversal attacks
    return !filename.contains("..") && !filename.contains("/") && !filename.contains("\\");
}
```

### 4. Use Buffered Streams
```java
// ❌ Slow (reads one byte at a time)
FileInputStream fis = new FileInputStream("file.txt");

// ✅ Fast (uses buffer)
BufferedInputStream bis = new BufferedInputStream(new FileInputStream("file.txt"));
```

## Common File Operations Summary

| Operation | Code |
|-----------|------|
| Read all lines | `Files.readAllLines(path)` |
| Write lines | `Files.write(path, lines)` |
| Check exists | `Files.exists(path)` |
| Create directory | `Files.createDirectories(path)` |
| Delete file | `Files.deleteIfExists(path)` |
| Copy file | `Files.copy(source, target)` |
| Move file | `Files.move(source, target)` |

## Security Considerations

### 1. Validate File Types
```java
public boolean isAllowedFileType(String filename) {
    String[] allowed = {".jpg", ".png", ".pdf"};
    return Arrays.stream(allowed).anyMatch(filename::endsWith);
}
```

### 2. Limit File Size
```java
private static final long MAX_FILE_SIZE = 5 * 1024 * 1024;  // 5MB

if (file.getSize() > MAX_FILE_SIZE) {
    throw new FileSizeExceededException("File too large");
}
```

## Key Takeaways
- **Use try-with-resources** to auto-close files
- **BufferedReader/Writer** for text files
- **Files class** for modern file operations
- **Validate and sanitize** file inputs in backend
- **Handle exceptions** properly

## Practice Exercise
Build a **Student Data Manager** that:
- Reads student data from CSV file
- Writes new students to CSV
- Creates backup files
- Logs all operations to a log file
''',
            'order': 4
        },
        {
            'title': 'Writing Clean and Readable Java Code',
            'content': '''# Writing Clean and Readable Java Code

## Why Clean Code Matters in Backend?
In companies:
- **Code is read 10x more than written**
- Multiple developers work on same codebase
- Code reviews happen before merging
- Clean code = fewer bugs + faster development

## 1. Naming Conventions

### Classes (PascalCase)
```java
// ✅ Good
public class UserService { }
public class ProductController { }
public class OrderRepository { }

// ❌ Bad
public class userservice { }
public class product_controller { }
```

### Methods and Variables (camelCase)
```java
// ✅ Good
public void sendEmailNotification() { }
private String userName;
int totalPrice;

// ❌ Bad
public void Send_Email_Notification() { }
private String UserName;
int TotalPrice;
```

### Constants (UPPER_SNAKE_CASE)
```java
// ✅ Good
public static final int MAX_LOGIN_ATTEMPTS = 3;
public static final String DEFAULT_ROLE = "USER";

// ❌ Bad
public static final int maxLoginAttempts = 3;
```

### Meaningful Names
```java
// ❌ Bad (unclear)
int d;  // days?
String s;  // what string?
List<User> list1;

// ✅ Good (self-explanatory)
int daysUntilExpiry;
String userEmail;
List<User> activeUsers;
```

## 2. Method Design

### Single Responsibility Principle
```java
// ❌ Bad (does too much)
public void processOrder(Order order) {
    // Validate order
    if (order.getAmount() <= 0) throw new Exception();
    
    // Update inventory
    inventory.reduce(order.getProductId(), order.getQuantity());
    
    // Process payment
    paymentGateway.charge(order.getAmount());
    
    // Send email
    emailService.send(order.getEmail(), "Order confirmed");
    
    // Save to database
    orderRepository.save(order);
}

// ✅ Good (separated concerns)
public void processOrder(Order order) {
    validateOrder(order);
    updateInventory(order);
    processPayment(order);
    sendConfirmationEmail(order);
    saveOrder(order);
}

private void validateOrder(Order order) {
    if (order.getAmount() <= 0) {
        throw new InvalidOrderException("Invalid amount");
    }
}

private void updateInventory(Order order) {
    inventory.reduce(order.getProductId(), order.getQuantity());
}
// ... other methods
```

### Small Methods (<20 lines)
```java
// ❌ Bad (100 lines method)
public User registerUser(UserDTO dto) {
    // 100 lines of validation, hashing, saving, emailing...
}

// ✅ Good (broken down)
public User registerUser(UserDTO dto) {
    validateUserData(dto);
    User user = createUserFromDTO(dto);
    hashPassword(user);
    saveUser(user);
    sendWelcomeEmail(user);
    return user;
}
```

## 3. Comments and Documentation

### Good Comments
```java
/**
 * Calculates the discounted price based on user membership level.
 * 
 * @param originalPrice The original product price
 * @param membershipType User's membership (SILVER, GOLD, PLATINUM)
 * @return Discounted price
 */
public double calculateDiscount(double originalPrice, MembershipType membershipType) {
    // Gold members get 15% discount, Platinum gets 25%
    return switch (membershipType) {
        case SILVER -> original Price * 0.95;
        case GOLD -> originalPrice * 0.85;
        case PLATINUM -> originalPrice * 0.75;
    };
}
```

### Avoid Redundant Comments
```java
// ❌ Bad (obvious comment)
// Get user by ID
public User getUserById(Long id) {
    return repository.findById(id);
}

// ✅ Good (self-documenting code)
public User getUserById(Long id) {
    return repository.findById(id);
}
```

## 4. Error Handling

### Don't Swallow Exceptions
```java
// ❌ Bad
try {
    processPayment(order);
} catch (Exception e) {
    // Silent failure - error is lost!
}

// ✅ Good
try {
    processPayment(order);
} catch (PaymentException e) {
    logger.error("Payment failed for order {}: {}", order.getId(), e.getMessage());
    throw new OrderProcessingException("Payment failed", e);
}
```

### Use Specific Exceptions
```java
// ❌ Bad
if (user == null) {
    throw new Exception("Error");
}

// ✅ Good
if (user == null) {
    throw new UserNotFoundException("User with ID " + userId + " not found");
}
```

## 5. Code Organization

### Package Structure
```
com.roadmap99.backend
├── controller  (REST endpoints)
├── service     (Business logic)
├── repository  (Database access)
├── model       (Entity classes)
├── dto         (Data Transfer Objects)
├── exception   (Custom exceptions)
└── config      (Configuration classes)
```

### Class Structure
```java
@Service
public class UserService {
    // 1. Constants
    private static final int MAX_LOGIN_ATTEMPTS = 3;
    
    // 2. Fields
    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;
    
    // 3. Constructor (Dependency Injection)
    @Autowired
    public UserService(UserRepository userRepository, PasswordEncoder passwordEncoder) {
        this.userRepository = userRepository;
        this.passwordEncoder = passwordEncoder;
    }
    
    // 4. Public methods
    public User registerUser(UserDTO dto) {
        // ...
    }
    
    public User login(String email, String password) {
        // ...
    }
    
    // 5. Private helper methods
    private void validateEmail(String email) {
        // ...
    }
}
```

## 6. DRY (Don't Repeat Yourself)

### Extract Common Logic
```java
// ❌ Bad (repeated code)
public void updateUserProfile(User user) {
    user.setUpdatedAt(LocalDateTime.now());
    user.setUpdatedBy("SYSTEM");
    userRepository.save(user);
}

public void updateUserEmail(User user, String newEmail) {
    user.setEmail(newEmail);
    user.setUpdatedAt(LocalDateTime.now());
    user.setUpdatedBy("SYSTEM");
    userRepository.save(user);
}

// ✅ Good (extracted common logic)
public void updateUserProfile(User user) {
    saveUser(user);
}

public void updateUserEmail(User user, String newEmail) {
    user.setEmail(newEmail);
    saveUser(user);
}

private void saveUser(User user) {
    user.setUpdatedAt(LocalDateTime.now());
    user.setUpdatedBy("SYSTEM");
    userRepository.save(user);
}
```

## 7. Use Enums for Constants

```java
// ❌ Bad (magic strings)
if (user.getRole().equals("ADMIN")) {
    // grant access
}

// ✅ Good (type-safe enum)
public enum UserRole {
    USER, ADMIN, MODERATOR
}

if (user.getRole() == UserRole.ADMIN) {
    // grant access
}
```

## 8. Builder Pattern for Complex Objects

```java
// ❌ Bad (constructor with many parameters)
User user = new User("John", "Doe", "john@example.com", "password123", 
                     "1234567890", "USA", "New York", "10001");

// ✅ Good (builder pattern)
User user = User.builder()
    .firstName("John")
    .lastName("Doe")
    .email("john@example.com")
    .password("password123")
    .phone("1234567890")
    .country("USA")
    .city("New York")
    .zipCode("10001")
    .build();
```

## 9. Logging

### Use Proper Log Levels
```java
@Service
public class OrderService {
    private static final Logger logger = LoggerFactory.getLogger(OrderService.class);
    
    public Order createOrder(OrderDTO dto) {
        logger.info("Creating order for user {}", dto.getUserId());
        
        try {
            Order order = processOrder(dto);
            logger.info("Order created successfully: {}", order.getId());
            return order;
        } catch (Exception e) {
            logger.error("Failed to create order for user {}: {}", dto.getUserId(), e.getMessage(), e);
            throw e;
        }
    }
}
```

## 10. Avoid Magic Numbers

```java
// ❌ Bad
if (user.getAge() < 18) {
    throw new Exception("Too young");
}

// ✅ Good
private static final int MINIMUM_AGE = 18;

if (user.getAge() < MINIMUM_AGE) {
    throw new InvalidAgeException("User must be at least " + MINIMUM_AGE + " years old");
}
```

## Real Backend Example (Before vs After)

### ❌ Bad Code
```java
public class UserController {
    @Autowired
    UserRepository ur;
    
    @PostMapping("/reg")
    public String reg(@RequestBody Map<String, String> data) {
        try {
            User u = new User();
            u.setName(data.get("n"));
            u.setEmail(data.get("e"));
            u.setPassword(data.get("p"));
            ur.save(u);
            return "OK";
        } catch (Exception ex) {
            return "Error";
        }
    }
}
```

### ✅ Good Code
```java
@RestController
@RequestMapping("/api/users")
public class UserController {
    
    private final UserService userService;
    
    @Autowired
    public UserController(UserService userService) {
        this.userService = userService;
    }
    
    @PostMapping("/register")
    public ResponseEntity<UserResponse> registerUser(@Valid @RequestBody UserRegistrationDTO dto) {
        try {
            User user = userService.registerUser(dto);
            UserResponse response = new UserResponse(user);
            return ResponseEntity.status(HttpStatus.CREATED).body(response);
            
        } catch (EmailAlreadyExistsException e) {
            throw e;  // Handled by global exception handler
        }
    }
}
```

## Code Review Checklist

- [ ] Meaningful variable/method names
- [ ] Methods < 20 lines
- [ ] No magic numbers/strings
- [ ] Proper exception handling
- [ ] Logging added for important operations
- [ ] No code duplication
- [ ] Comments only where necessary
- [ ] Followed company naming conventions
- [ ] Unit tests written

## Key Takeaways
- **Self-documenting code > Comments**
- **Small methods** with single responsibility
- **Consistent naming** across codebase
- **Handle exceptions** meaningfully
- **DRY principle** - avoid duplication
- **Code for humans**, not just machines

## Practice Exercise
Refactor this messy code:
```java
public String p(Map<String, String> d) {
    User u = new User();
    u.setN(d.get("name"));
    u.setE(d.get("email"));
    if(ur.findByEmail(u.getE()) != null) return "exists";
    ur.save(u);
    return "done";
}
```

**Goal**: Make it clean, readable, and production-ready!
''',
            'order': 5
        }
    ]
    
    for topic_data in topics_stage2:
        Topic.objects.create(stage=stage2, **topic_data)
    
    print(f"✅ Stage 2: {stage2.title} - {len(topics_stage2)} topics")
    
    print("\n" + "="*50)
    print(f"✅ Java Backend Development Roadmap Created!")
    print(f"   Stages: 2 (more to be added)")
    print(f"   Topics: {len(topics_stage1) + len(topics_stage2)}")
    print("="*50)

if __name__ == '__main__':
    create_java_backend_roadmap()
