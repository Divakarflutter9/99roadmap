"""
Add Python Backend Development Roadmap
Complete roadmap for BTech/CSE students to become industry-ready Python backend developers
"""

import os
import django
import sys

sys.path.append('/Users/saitejakaki/Divakar/devaproject')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import Roadmap, RoadmapCategory, Stage, Topic

def create_python_backend_roadmap():
    """Create comprehensive Python Backend Development roadmap"""
    
    # Get Backend category
    category = RoadmapCategory.objects.get(slug='backend-development')
    
    # Create roadmap
    roadmap, created = Roadmap.objects.get_or_create(
        slug='python-backend-development',
        defaults={
            'title': 'Python Backend Development',
            'short_description': 'Complete Python backend roadmap - from basics to building production-ready APIs with Django & FastAPI',
            'description': 'Master Python backend development from scratch. Learn Django, FastAPI, REST APIs, databases, authentication, and deployment. Perfect for students aiming for Python backend roles at startups and tech giants.',
            'category': category,
            'difficulty': 'intermediate',
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
        # Delete existing stages and topics to recreate
        roadmap.stages.all().delete()
        print("   Deleted existing stages to recreate with new content")
    
    # Stage 1: Backend Foundations (FREE)
    stage1 = Stage.objects.create(
        roadmap=roadmap,
        title='Backend Foundations',
        description='Understand what backend development means and how Python powers modern web applications',
        order=1,
        is_free=True
    )
    
    stage1_topics = [
        {
            'title': 'What is Backend Development?',
            'content': '''# What is Backend Development?

## Introduction
Backend development is the **server-side** of applications where all the logic, data processing, and business rules live. While users see the frontend, backend makes everything work.

## Real-World Example: Instagram
- **Frontend**: What you see (photos, stories, UI)
- **Backend**: 
  - Stores millions of photos in databases
  - Processes image uploads
  - Handles likes, comments, follows
  - Manages user authentication
  - Sends notifications

## What Backend Does

### 1. Data Management
- Store user data, posts, products
- Retrieve data when requested
- Update information (edit profile, update cart)
- Delete data when needed

### 2. Business Logic
- User registration validation
- Payment processing
- Recommendation algorithms
- Search and filtering

### 3. API Creation
Create endpoints frontend can call:
```
GET /api/users/123        → Get user data
POST /api/posts           → Create new post
PUT /api/profile          → Update profile
DELETE /api/posts/456     → Delete post
```

### 4. Security
- Password encryption
- User authentication (login/logout)
- Authorization (permissions)
- Protect against attacks (SQL injection, XSS)

## Why Backend is Critical
- **Apps are useless without backend**
- Backend handles millions of users simultaneously
- Stores and protects sensitive data
- Implements core business logic

## Key Takeaway
Backend is the **brain and memory** of any application. Without it, apps are just pretty interfaces with no functionality!
''',
            'order': 1
        },
        {
            'title': 'Client-Server Architecture',
            'content': '''# Client-Server Architecture

## How Web Applications Work

The **client-server model** is the foundation of modern web applications.

### Components

**Client (Frontend)**
- User's browser or mobile app
- Sends requests to server
- Displays data to user
- Examples: React app, Android app, iOS app

**Server (Backend)**
- Runs 24/7 on cloud (AWS, Google Cloud, Azure)
- Processes client requests
- Accesses database
- Sends responses back
- Examples: Django server, FastAPI server

**Database**
- Stores all data permanently
- MySQL, PostgreSQL, MongoDB
- Connected to backend server

## Request-Response Flow

```
User Types URL → Browser (Client) → Internet → Server (Backend) → Database
                                                      ↓
User Sees Page ← Browser ← Internet ← Response ← Backend
```

## Real Example: E-Commerce

**User Action**: Click "Add to Cart"

1. **Client**: Sends POST request
   ```
   POST /api/cart/add
   {
     "product_id": 123,
     "quantity": 2
   }
   ```

2. **Server (Python Backend)**: 
   - Receives request
   - Validates product exists
   - Checks stock availability
   - Updates cart in database
   - Returns success response

3. **Client**: Shows "Added to cart!" message

## Why This Architecture?

### Separation of Concerns
- Frontend focuses on UI/UX
- Backend handles logic and data
- Database manages storage

### Scalability
- One backend serves millions of clients
- Can add more servers when traffic increases
- Database can be scaled independently

### Security
- Sensitive logic stays on server
- Database not exposed to users
- Easier to protect and monitor

## Key Takeaway
Client and server work together like a **restaurant**: Client is the customer (orders food), Backend is the kitchen (prepares food), Database is the storage (ingredients).
''',
            'order': 2
        },
        {
            'title': 'HTTP Request-Response Cycle',
            'content': '''# HTTP Request-Response Cycle

## What is HTTP?

**HTTP (HyperText Transfer Protocol)** is the language browsers and servers use to communicate.

## HTTP Methods (CRUD Operations)

| Method | Purpose | Example |
|--------|---------|---------|
| **GET** | Retrieve data | Get user profile |
| **POST** | Create data | Register new user |
| **PUT** | Update data | Edit profile |
| **DELETE** | Remove data | Delete post |

## Anatomy of HTTP Request

### 1. Request Line
```
POST /api/users/login HTTP/1.1
```

### 2. Headers (Metadata)
```
Content-Type: application/json
Authorization: Bearer token123
User-Agent: Mozilla/5.0
```

### 3. Body (Data)
```json
{
  "email": "john@example.com",
  "password": "securepass123"
}
```

## Anatomy of HTTP Response

### 1. Status Code
```
HTTP/1.1 200 OK
```

### 2. Response Headers
```
Content-Type: application/json
Set-Cookie: session_id=abc123
```

### 3. Response Body
```json
{
  "success": true,
  "user": {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
  },
  "token": "jwt_token_here"
}
```

## HTTP Status Codes (Must Know!)

### Success (2xx)
- **200 OK**: Request successful
- **201 Created**: Resource created successfully
- **204 No Content**: Success but no data to return

### Client Errors (4xx)
- **400 Bad Request**: Invalid data sent
- **401 Unauthorized**: Login required
- **403 Forbidden**: No permission
- **404 Not Found**: Resource doesn't exist

### Server Errors (5xx)
- **500 Internal Server Error**: Backend crashed
- **503 Service Unavailable**: Server down

## Real Python Backend Example

```python
# FastAPI example
from fastapi import FastAPI

app = FastAPI()

@app.get("/api/users/{user_id}")  # GET request
def get_user(user_id: int):
    # Backend logic
    user = database.get_user(user_id)
    
    # Return response
    return {
        "status": 200,
        "data": {
            "id": user.id,
            "name": user.name
        }
    }
```

## Request-Response in Action

**Frontend Request:**
```javascript
// JavaScript (Frontend)
fetch('https://api.example.com/products', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    name: 'Laptop',
    price: 50000
  })
})
```

**Backend Response (Python):**
```python
# FastAPI
@app.post("/products")
def create_product(product: Product):
    saved = db.save(product)
    return {
        "status": "created",
        "product_id": saved.id
    }
```

## Key Takeaway
HTTP is the **postal system** of the internet. Requests are letters sent to server, responses are replies sent back. Status codes tell you if the delivery was successful!
''',
            'order': 3
        },
        {
            'title': 'Role of Backend in Real Applications',
            'content': '''# Backend in Real Applications

## Real Company Examples

### 1. Food Delivery (Swiggy, Zomato)

**Backend Responsibilities:**
- User registration and login
- Restaurant & menu management
- Real-time order tracking
- Payment processing (Razorpay, Paytm)
- Delivery partner assignment (algorithm)
- Rating and review system
- Discount & coupon validation

**Tech Stack (Python):**
- Django/FastAPI for APIs
- PostgreSQL for data storage
- Redis for caching
- Celery for background tasks

### 2. Social Media (Twitter, Instagram)

**Backend Handles:**
- User profiles and authentication
- Post creation and storage
- Like, comment, share functionality
- Follow/unfollow logic
- Feed generation (complex algorithm)
- Notifications (push, email, SMS)
- Content moderation

### 3. E-Learning (Coursera, Udemy)

**Backend Tasks:**
- User enrollment management
- Video streaming infrastructure
- Progress tracking
- Quiz and assignment grading
- Certificate generation
- Payment & subscription handling
- Discussion forum management

## Core Backend Responsibilities

### 1. Data Management
```python
# Example: User registration
def register_user(email, password):
    # Validate email format
    if not is_valid_email(email):
        raise ValidationError("Invalid email")
    
    # Check if email exists
    if User.objects.filter(email=email).exists():
        raise DuplicateError("Email already registered")
    
    # Hash password (never store plain!)
    hashed_password = hash_password(password)
    
    # Save to database
    user = User.objects.create(
        email=email,
        password=hashed_password
    )
    return user
```

### 2. Business Logic
```python
# Example: E-commerce cart total calculation
def calculate_cart_total(user_id):
    cart_items = CartItem.objects.filter(user_id=user_id)
    
    subtotal = sum(item.price * item.quantity for item in cart_items)
    
    # Apply discount if user has coupon
    discount = apply_coupon_discount(user_id, subtotal)
    
    # Calculate tax
    tax = subtotal * 0.18  # 18% GST
    
    # Shipping charges
    shipping = 0 if subtotal > 500 else 40
    
    total = subtotal - discount + tax + shipping
    return total
```

### 3. Third-Party Integrations
```python
# Payment gateway integration
def process_payment(order_id, amount):
    # Razorpay integration
    razorpay_order = razorpay_client.order.create({
        'amount': amount * 100,  # paisa
        'currency': 'INR',
        'receipt': f'order_{order_id}'
    })
    return razorpay_order

# Send email
def send_order_confirmation(user_email, order_id):
    # SendGrid/AWS SES integration
    send_email(
        to=user_email,
        subject="Order Confirmed",
        body=f"Your order #{order_id} is confirmed!"
    )
```

### 4. Security
```python
# Authentication middleware
def require_authentication(request):
    token = request.headers.get('Authorization')
    
    if not token:
        raise Unauthorized("Login required")
    
    user = verify_jwt_token(token)
    
    if not user:
        raise Unauthorized("Invalid token")
    
    return user

# Input sanitization
def sanitize_input(user_input):
    # Prevent SQL injection, XSS attacks
    return escape_html(user_input)
```

## Backend Engineer's Day

**Typical Tasks:**
- Build new API endpoints
- Fix bugs in existing APIs
- Optimize slow database queries
- Review teammate's code
- Write unit tests
- Deploy updates to production
- Monitor error logs

## Why Backend is High-Demand

- **Every app needs backend**: Mobile apps, websites, IoT devices
- **Scalability is critical**: Apps grow from 100 to 10 million users
- **Complex problems**: Algorithms, data structures, system design
- **High pay**: Backend engineers earn ₹8-30 LPA in India

## Key Takeaway
Backend is the **engine** that powers applications. Without it, apps are just beautiful shells with no brain or memory!
''',
            'order': 4
        },
        {
            'title': 'Python in Backend Systems',
            'content': '''# Python in Backend Systems

## Why Python for Backend?

### 1. Industry Adoption

**Companies Using Python Backend:**
- **Instagram**: Django (handles 1 billion+ users)
- **Spotify**: Flask, FastAPI (music streaming)
- **Netflix**: Microservices (recommendation engine)
- **Uber**: FastAPI (ride matching algorithms)
- **Dropbox**: Python (file synchronization)
- **Reddit**: Python backend
- **PayTM, Razorpay**: Payment processing

### 2. Why Companies Choose Python

**a) Easy to Learn & Read**
```python
# Python - Simple syntax
def get_user(user_id):
    user = User.objects.get(id=user_id)
    return user

# vs Java - More verbose
public User getUser(Long userId) {
    User user = userRepository.findById(userId)
        .orElseThrow(() -> new UserNotFoundException());
    return user;
}
```

**b) Fast Development**
- Build REST API in 30 minutes
- Prototype quickly
- Less code = faster shipping

**c) Rich Ecosystem**
- Django: Full-featured framework
- FastAPI: Modern, high-performance
- Flask: Lightweight, flexible
- 300,000+ packages on PyPI

**d) Data Science Integration**
- Machine Learning (scikit-learn, TensorFlow)
- Data Analysis (Pandas, NumPy)
- Perfect for AI-powered apps

**e) Excellent for Startups**
- Rapid MVP development
- Small teams can build big products
- Easy to hire Python developers

## Python Backend Tech Stack

### Web Frameworks
1. **Django**: Battery-included (ORM, admin panel, auth)
2. **FastAPI**: Modern, async, fast (best for APIs)
3. **Flask**: Minimal, flexible

### Databases
- **PostgreSQL**: Most popular with Django
- **MySQL**: Traditional choice
- **MongoDB**: NoSQL (flexible schema)
- **Redis**: Caching, session storage

### Tools
- **Celery**: Background tasks (emails, processing)
- **Gunicorn/Uvicorn**: Production servers
- **Docker**: Containerization
- **AWS/GCP**: Cloud deployment

## Python vs Other Backend Languages

| Feature | Python | Node.js | Java |
|---------|--------|---------|------|
| Learning Curve | Easy | Medium | Hard |
| Development Speed | Fast | Fast | Slow |
| Performance | Good | Excellent | Excellent |
| Use Case | Startups, AI apps | Real-time apps | Enterprise |
| Jobs (India) | High | High | Very High |
| Salary | ₹6-25 LPA | ₹6-20 LPA | ₹8-30 LPA |

## Python Backend Use Cases

### 1. REST APIs
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/api/products")
def get_products():
    products = Product.objects.all()
    return {"products": products}
```

### 2. Data-Heavy Applications
- Analytics dashboards
- Reporting systems
- ML-powered recommendations

### 3. Rapid Prototyping
- MVPs for startups
- Internal tools
- Admin dashboards

### 4. Microservices
- Small, independent services
- Easy to scale
- Used by Netflix, Uber

## Job Market in India

### Entry Level (0-2 years)
- **Role**: Python Backend Developer, SDE-1
- **Salary**: ₹4-8 LPA
- **Companies**: Startups, service companies

### Mid Level (2-5 years)
- **Role**: Senior Backend Engineer
- **Salary**: ₹8-20 LPA
- **Companies**: Swiggy, Zomato, PayTM, startups

### Senior Level (5+ years)
- **Role**: Lead Engineer, Architect
- **Salary**: ₹20-40+ LPA
- **Companies**: FAANG, unicorns

## Skills Needed

**Must Have:**
- Python (data structures, OOP)
- Django or FastAPI
- SQL and databases
- REST API design
- Git version control

**Good to Have:**
- Docker & Kubernetes
- Redis caching
- AWS/GCP cloud
- System design
- Testing (pytest)

## When to Choose Python Backend?

**Choose Python if:**
✅ Building MVP or startup product
✅ Need ML/AI integration
✅ Data-heavy applications
✅ Want rapid development
✅ Small to medium team

**Consider alternatives if:**
❌ Need extreme performance (use Go, Rust)
❌ Building real-time apps (consider Node.js)
❌ Enterprise Java shop (stick with Java)

## Key Takeaway
Python is **perfect for building backend systems quickly** without compromising quality. It powers billion-user apps like Instagram and is ideal for Indian startups and tech companies!
''',
            'order': 5
        }
    ]
    
    for topic_data in stage1_topics:
        Topic.objects.create(stage=stage1, **topic_data)
    print(f"✅ Stage 1: {stage1.title} - {len(stage1_topics)} topics")
    
    # Stage 2: Core Python for Backend
    stage2 = Stage.objects.create(
        roadmap=roadmap,
        title='Core Python for Backend',
        description='Master Python fundamentals essential for backend development - OOP, exceptions, file handling',
        order=2,
        is_free=False
    )
    
    stage2_topics = [
        {
            'title': 'Python Data Types & Control Flow',
            'content': '''# Python Revisions for Backend

## Data Types

```python
# Strings
username = "john_doe"
email = "john@example.com"

# Numbers
user_id = 123
price = 99.99

# Boolean
is_premium = True
is_verified = False

# Lists (mutable)
cart_items = ["laptop", "mouse", "keyboard"]

# Tuples (immutable)
coordinates = (28.6139, 77.2090)  # Lat, Long

# Dictionaries (key-value)
user = {
    "id": 1,
    "name": "John",
    "email": "john@example.com",
    "is_active": True
}

# Sets (unique elements)
tags = {"python", "backend", "api"}
```

## Control Flow

### If-Else
```python
def check_age(age):
    if age < 18:
        return "Not allowed"
    elif age >= 18 and age < 60:
        return "Eligible"
    else:
        return "Senior citizen discount"
```

### Loops
```python
# For loop
products = ["laptop", "phone", "tablet"]
for product in products:
    print(f"Product: {product}")

# While loop
attempts = 0
while attempts < 3:
    password = input("Enter password: ")
    if verify_password(password):
        break
    attempts += 1
```

## List Comprehension
```python
# Get user IDs from user list
user_ids = [user['id'] for user in users]

# Filter active users
active_users = [u for u in users if u['is_active']]

# Price with tax
prices_with_tax = [price * 1.18 for price in prices]
```

## Dictionary Operations
```python
# Access
user_email = user["email"]
user_name = user.get("name", "Guest")  # Default value

# Update
user["is_verified"] = True

# Loop
for key, value in user.items():
    print(f"{key}: {value}")

# Check existence
if "email" in user:
    print("Email exists")
```

## Backend Use Case
```python
def process_order(order_data):
    # Validate required fields
    required = ["user_id", "product_id", "quantity"]
    for field in required:
        if field not in order_data:
            raise ValueError(f"Missing field: {field}")
    
    # Calculate total
    quantity = order_data["quantity"]
    price = get_product_price(order_data["product_id"])
    total = quantity * price
    
    # Apply discount if quantity > 5
    if quantity > 5:
        total = total * 0.9  # 10% discount
    
    return {
        "order_id": generate_id(),
        "total_amount": total,
        "status": "confirmed"
    }
```
''',
            'order': 1
        },
        {
            'title': 'Functions & Modular Coding',
            'content': '''# Functions in Backend

## Basic Functions
```python
def greet_user(name):
    return f"Hello, {name}!"

# Call function
message = greet_user("John")
```

## Default Arguments
```python
def create_user(username, role="user"):
    return {
        "username": username,
        "role": role,
        "created_at": datetime.now()
    }

# Usage
admin = create_user("admin", "admin")
regular = create_user("john")  # role defaults to "user"
```

## *args and **kwargs
```python
def log_event(event_type, *args, **kwargs):
    print(f"Event: {event_type}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

# Usage
log_event("user_login", "john@example.com", ip="192.168.1.1", device="mobile")
```

## Lambda Functions
```python
# Sort users by registration date
users = sorted(users, key=lambda u: u['created_at'])

# Filter premium users
premium_users = list(filter(lambda u: u['is_premium'], users))
```

## Decorators (Important for Backend!)
```python
def require_auth(func):
    """Decorator to check if user is authenticated"""
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return {"error": "Authentication required"}, 401
        return func(request, *args, **kwargs)
    return wrapper

# Usage
@require_auth
def get_profile(request):
    return {"user": request.user.data}
```

## Modular Code Structure
```python
# utils.py
def validate_email(email):
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def hash_password(password):
    from hashlib import sha256
    return sha256(password.encode()).hexdigest()

# auth.py
from utils import validate_email, hash_password

def register_user(email, password):
    if not validate_email(email):
        raise ValueError("Invalid email")
    
    hashed = hash_password(password)
    # Save to database
    return create_user_in_db(email, hashed)
```

## Real Backend Example
```python
# services/user_service.py
class UserService:
    def __init__(self, db):
        self.db = db
    
    def create_user(self, user_data):
        # Validate
        self._validate_user_data(user_data)
        
        # Hash password
        user_data['password'] = self._hash_password(user_data['password'])
        
        # Save
        user_id = self.db.insert('users', user_data)
        
        # Send welcome email
        self._send_welcome_email(user_data['email'])
        
        return user_id
    
    def _validate_user_data(self, data):
        required = ['email', 'password', 'username']
        for field in required:
            if field not in data:
                raise ValueError(f"Missing {field}")
    
    def _hash_password(self, password):
        import bcrypt
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    
    def _send_welcome_email(self, email):
        # Email sending logic
        pass
```
''',
            'order': 2
        },
        {
            'title': 'OOPS in Python Backend',
            'content': '''# Object-Oriented Programming

## Classes and Objects
```python
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.is_active = True
    
    def deactivate(self):
        self.is_active = False
    
    def __str__(self):
        return f"User({self.username}, {self.email})"

# Create object
user = User("john_doe", "john@example.com")
print(user.username)  # john_doe
user.deactivate()
```

## Inheritance
```python
class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password
    
    def login(self):
        print(f"{self.email} logged in")

class PremiumUser(User):
    def __init__(self, email, password, subscription_type):
        super().__init__(email, password)
        self.subscription_type = subscription_type
    
    def access_premium_content(self):
        return f"{self.email} accessing premium content"

# Usage
premium = PremiumUser("john@ex.com", "pass123", "yearly")
premium.login()  # Inherited method
premium.access_premium_content()
```

## Encapsulation
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def get_balance(self):
        return self.__balance
    
    # Cannot directly access self.__balance from outside
```

## Backend Example: Models
```python
# models/user.py
from datetime import datetime

class User:
    def __init__(self, id, email, password_hash):
        self.id = id
        self.email = email
        self.password_hash = password_hash
        self.created_at = datetime.now()
    
    @classmethod
    def from_db_row(cls, row):
        return cls(
            id=row['id'],
            email=row['email'],
            password_hash=row['password']
        )
    
    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'created_at': self.created_at.isoformat()
        }

# models/product.py
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def is_available(self):
        return self.stock > 0
    
    def reduce_stock(self, quantity):
        if quantity > self.stock:
            raise ValueError("Insufficient stock")
        self.stock -= quantity
```

## Service Layer (OOP Pattern)
```python
class OrderService:
    def __init__(self, db, payment_gateway):
        self.db = db
        self.payment_gateway = payment_gateway
    
    def create_order(self, user_id, cart_items):
        # Calculate total
        total = self._calculate_total(cart_items)
        
        # Create order in DB
        order_id = self.db.create_order(user_id, cart_items, total)
        
        # Process payment
        payment_status = self.payment_gateway.charge(user_id, total)
        
        if payment_status == "success":
            self._send_confirmation_email(user_id, order_id)
            return order_id
        else:
            self.db.cancel_order(order_id)
            raise PaymentFailedException()
    
    def _calculate_total(self, items):
        return sum(item['price'] * item['quantity'] for item in items)
    
    def _send_confirmation_email(self, user_id, order_id):
        # Email logic
        pass
```
''',
            'order': 3
        },
        {
            'title': 'Exception Handling',
            'content': '''# Exception Handling in Backend

## Try-Except Basics
```python
def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    except TypeError:
        print("Invalid input types")
        return None
```

## Multiple Exceptions
```python
def get_user(user_id):
    try:
        user = database.query(f"SELECT * FROM users WHERE id = {user_id}")
        return user
    except ConnectionError:
        print("Database connection failed")
    except ValueError:
        print("Invalid user ID")
    except Exception as e:
        print(f"Unexpected error: {e}")
```

## Finally Block
```python
def read_file(filename):
    file = None
    try:
        file = open(filename, 'r')
        data = file.read()
        return data
    except FileNotFoundError:
        print(f"File {filename} not found")
    finally:
        if file:
            file.close()  # Always executes
```

## Custom Exceptions
```python
class UserNotFoundException(Exception):
    pass

class EmailAlreadyExistsException(Exception):
    pass

class InsufficientBalanceException(Exception):
    pass

# Usage
def register_user(email, password):
    if User.objects.filter(email=email).exists():
        raise EmailAlreadyExistsException(f"Email {email} already registered")
    
    # Registration logic
    return create_user(email, password)
```

## Backend API Error Handling
```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int):
    try:
        user = User.objects.get(id=user_id)
        return {"user": user.to_dict()}
    
    except User.DoesNotExist:
        raise HTTPException(status_code=404, detail="User not found")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
```

## Global Exception Handler
```python
# Django example
from rest_framework.views import exception_handler
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    
    if response is None:
        return Response({
            'error': 'Internal server error',
            'detail': str(exc)
        }, status=500)
    
    return response

# FastAPI example
from fastapi import Request
from fastapi.responses import JSONResponse

@app.exception_handler(UserNotFoundException)
def user_not_found_handler(request: Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"error": "User not found", "detail": str(exc)}
    )
```

## Real Use Case: Payment Processing
```python
class PaymentService:
    def process_payment(self, user_id, amount):
        try:
            # Check user balance
            balance = self.get_balance(user_id)
            if balance < amount:
                raise InsufficientBalanceException("Insufficient funds")
            
            # Deduct amount
            self.deduct_balance(user_id, amount)
            
            # Call payment gateway
            payment_result = self.payment_gateway.charge(amount)
            
            if payment_result['status'] != 'success':
                # Rollback balance deduction
                self.add_balance(user_id, amount)
                raise PaymentGatewayException("Payment failed")
            
            # Log transaction
            self.log_transaction(user_id, amount, 'success')
            
            return {
                'status': 'success',
                'transaction_id': payment_result['id']
            }
        
        except InsufficientBalanceException as e:
            self.log_transaction(user_id, amount, 'failed', str(e))
            raise
        
        except PaymentGatewayException as e:
            self.log_transaction(user_id, amount, 'failed', str(e))
            raise
        
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise ServerException("Payment processing failed")
```

## Logging with Exceptions
```python
import logging

logger = logging.getLogger(__name__)

def create_order(order_data):
    try:
        logger.info(f"Creating order for user {order_data['user_id']}")
        
        order = Order.create(order_data)
        
        logger.info(f"Order created: {order.id}")
        return order
    
    except ValidationError as e:
        logger.warning(f"Validation failed: {e}")
        raise
    
    except Exception as e:
        logger.error(f"Order creation failed: {e}", exc_info=True)
        raise
```
''',
            'order': 4
        },
        {
            'title': 'Writing Clean Python Code',
            'content': '''# Clean Python Code for Backend

## PEP 8 Style Guide

### Naming Conventions
```python
# Variables and functions: snake_case
user_name = "John"
def get_user_data():
    pass

# Classes: PascalCase
class UserService:
    pass

# Constants: UPPER_SNAKE_CASE
MAX_LOGIN_ATTEMPTS = 3
API_BASE_URL = "https://api.example.com"
```

### Meaningful Names
```python
# ❌ Bad
def f(x):
    return x * 2

# ✅ Good
def calculate_double(number):
    return number * 2

# ❌ Bad
u = db.get(1)

# ✅ Good
user = database.get_user_by_id(1)
```

## Function Design

### Single Responsibility
```python
# ❌ Bad (does too much)
def process_order(order_data):
    # Validate
    if not order_data.get('email'):
        raise ValueError()
    # Calculate price
    price = order_data['quantity'] * get_price()
    # Send email
    send_email(order_data['email'])
    # Save to DB
    db.save(order_data)

# ✅ Good (separated)
def process_order(order_data):
    validate_order(order_data)
    total_price = calculate_total_price(order_data)
    save_order_to_database(order_data, total_price)
    send_order_confirmation_email(order_data['email'])
```

### Keep Functions Small
```python
# ✅ Good (< 20 lines)
def register_user(email, password):
    validate_email(email)
    check_email_not_exists(email)
    hashed_password = hash_password(password)
    user = create_user_in_db(email, hashed_password)
    send_welcome_email(email)
    return user
```

## List Comprehensions
```python
# ❌ Verbose
active_users = []
for user in users:
    if user['is_active']:
        active_users.append(user)

# ✅ Pythonic
active_users = [u for u in users if u['is_active']]
```

## Context Managers
```python
# ✅ Good (auto-closes file)
with open('data.txt', 'r') as file:
    data = file.read()

# Database connection
with database.connection() as conn:
    result = conn.execute(query)
```

## Type Hints (Python 3.5+)
```python
from typing import List, Dict, Optional

def get_user_by_id(user_id: int) -> Optional[Dict]:
    user = database.query(user_id)
    return user

def filter_active_users(users: List[Dict]) -> List[Dict]:
    return [u for u in users if u['is_active']]
```

## Docstrings
```python
def calculate_discount(price: float, discount_percent: int) -> float:
    """
    Calculate discounted price.
    
    Args:
        price: Original price of product
        discount_percent: Discount percentage (0-100)
    
    Returns:
        Final price after discount
    
    Raises:
        ValueError: If discount_percent is invalid
    """
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100")
    
    discount_amount = price * (discount_percent / 100)
    return price - discount_amount
```

## Avoid Magic Numbers
```python
# ❌ Bad
if user.age < 18:
    return "Not allowed"

# ✅ Good
MINIMUM_AGE = 18

if user.age < MINIMUM_AGE:
    return f"Minimum age is {MINIMUM_AGE}"
```

## Backend Code Structure
```python
# project/
#   ├── api/
#   │   ├── routes.py
#   │   └── middleware.py
#   ├── services/
#   │   ├── user_service.py
#   │   └── order_service.py
#   ├── models/
#   │   ├── user.py
#   │   └── product.py
#   ├── utils/
#   │   ├── validators.py
#   │   └── helpers.py
#   └── config.py

# services/user_service.py
class UserService:
    """Handle all user-related business logic"""
    
    def __init__(self, db_connection):
        self.db = db_connection
    
    def create_user(self, user_data: Dict) -> int:
        """Create new user and return user ID"""
        self._validate_user_data(user_data)
        user_data['password'] = self._hash_password(user_data['password'])
        user_id = self.db.insert('users', user_data)
        self._send_welcome_email(user_data['email'])
        return user_id
    
    def _validate_user_data(self, data: Dict) -> None:
        """Validate user data (private method)"""
        required = ['email', 'password']
        for field in required:
            if field not in data:
                raise ValueError(f"Missing {field}")
```

## Error Handling
```python
# ✅ Be specific
try:
    user = get_user(user_id)
except UserNotFoundException:
    return {"error": "User not found"}, 404
except DatabaseError:
    return {"error": "Database unavailable"}, 500
```

## Code Review Checklist
- [ ] Meaningful variable names
- [ ] Functions < 20 lines
- [ ] No magic numbers
- [ ] Type hints added
- [ ] Docstrings for public functions
- [ ] Exception handling
- [ ] No code duplication
- [ ] Follows PEP 8
''',
            'order': 5
        }
    ]
    
    for topic_data in stage2_topics:
        Topic.objects.create(stage=stage2, **topic_data)
    print(f"✅ Stage 2: {stage2.title} - {len(stage2_topics)} topics")
    
    print("\n" + "="*60)
    print(f"✅ Part 1 Complete! Stages 1-2 created (10 topics)")
    print(f"   Creating remaining stages 3-5...")
    print("="*60 + "\n")
    
    roadmap.update_stats()
    return roadmap

if __name__ == '__main__':
    roadmap = create_python_backend_roadmap()
    print(f"\n✅ Python Backend Roadmap Part 1 Complete!")
