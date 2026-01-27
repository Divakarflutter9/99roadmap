"""
Add Python Backend Roadmap - Stages 4 & 5 (Final)
"""

import os
import django
import sys

sys.path.append('/Users/saitejakaki/Divakar/devaproject')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import Roadmap, Stage, Topic

def add_final_stages():
    """Add stages 4 and 5 to complete Python Backend roadmap"""
    
    roadmap = Roadmap.objects.get(slug='python-backend-development')
    print(f"Completing: {roadmap.title}")
    
    # Stage 4: Database & API Integration
    stage4 = Stage.objects.create(
        roadmap=roadmap,
        title='Database & API Integration',
        description='Connect Python backend to databases, perform CRUD operations with SQLAlchemy and Django ORM',
        order=4,
        is_free=False
    )
    
    stage4_topics = [
        {
            'title': 'SQL Basics',
            'content': '''# SQL for Backend Development

## Essential SQL Commands

```sql
-- CREATE TABLE
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(50) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- INSERT
INSERT INTO users (email, username, password_hash)
VALUES ('john@example.com', 'john_doe', 'hashed_password_here');

-- SELECT (All)
SELECT * FROM users;

-- SELECT (Filtered)
SELECT id, username, email 
FROM users 
WHERE email = 'john@example.com';

-- UPDATE
UPDATE users 
SET username = 'john_updated' 
WHERE id = 1;

-- DELETE
DELETE FROM users WHERE id = 1;
```

## WHERE Clause
```sql
-- Comparison operators
SELECT * FROM products WHERE price > 1000;
SELECT * FROM users WHERE age >= 18 AND age <= 60;

-- String matching
SELECT * FROM products WHERE name LIKE '%laptop%';

-- IN operator
SELECT * FROM orders WHERE status IN ('pending', 'confirmed');
```

## JOINs (Relationships)
```sql
-- One-to-Many: Users and Posts
CREATE TABLE posts (
    id INTEGER PRIMARY KEY,
    title VARCHAR(200),
    content TEXT,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- INNER JOIN
SELECT users.username, posts.title
FROM users
INNER JOIN posts ON users.id = posts.user_id;

-- LEFT JOIN (all users, even without posts)
SELECT users.username, posts.title
FROM users
LEFT JOIN posts ON users.id = posts.user_id;
```

## Aggregation
```sql
-- COUNT
SELECT COUNT(*) FROM users;

-- SUM
SELECT SUM(price) FROM orders WHERE user_id = 1;

-- GROUP BY
SELECT status, COUNT(*) 
FROM orders 
GROUP BY status;

-- HAVING (filter groups)
SELECT user_id, COUNT(*) as order_count
FROM orders
GROUP BY user_id
HAVING order_count > 5;
```

## ORDER BY and LIMIT
```sql
-- Sort by price (descending)
SELECT * FROM products ORDER BY price DESC;

-- Top 10 products
SELECT * FROM products ORDER BY price DESC LIMIT 10;

-- Pagination
SELECT * FROM products LIMIT 10 OFFSET 20;  -- Page 3 (skip 20, show 10)
```
''',
            'order': 1
        },
        {
            'title': 'Database Integration with Python',
            'content': '''# Python Database Integration

## SQLite (Built-in)
```python
import sqlite3

# Connect
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        email TEXT UNIQUE,
        username TEXT
    )
''')

# Insert
cursor.execute(
    "INSERT INTO users (email, username) VALUES (?, ?)",
    ('john@ex.com', 'john_doe')
)
conn.commit()

# Select
cursor.execute("SELECT * FROM users WHERE email = ?", ('john@ex.com',))
user = cursor.fetchone()
print(user)  # (1, 'john@ex.com', 'john_doe')

# Close
conn.close()
```

## PostgreSQL/MySQL with psycopg2/mysql-connector

```python
import psycopg2

# PostgreSQL connection
conn = psycopg2.connect(
    host="localhost",
    database="mydb",
    user="postgres",
    password="password"
)

cursor = conn.cursor()

# Query
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
users = cursor.fetchall()

conn.close()
```

## FastAPI with Database

```python
from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Database setup
DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Model
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    username = Column(String)

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# FastAPI app
app = FastAPI()

@app.post("/users")
def create_user(email: str, username: str, db: Session = Depends(get_db)):
    user = User(email=email, username=username)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"id": user.id, "email": user.email}

@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(404, "User not found")
    return user
```

## Django ORM (Simpler!)

```python
# models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

# Usage (no SQL needed!)
# CREATE
product = Product.objects.create(
    name="Laptop",
    price=50000,
    stock=10
)

# READ
all_products = Product.objects.all()
laptop = Product.objects.get(id=1)
expensive = Product.objects.filter(price__gt=10000)

# UPDATE
product.price = 45000
product.save()

# DELETE
product.delete()
```
''',
            'order': 2
        },
        {
            'title': 'CRUD Operations',
            'content': '''# Complete CRUD Example

## FastAPI + SQLiteAlchemy

```python
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

# Pydantic models
class ProductCreate(BaseModel):
    name: str
    price: float
    stock: int

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    stock: int
    
    class Config:
        from_attributes = True

app = FastAPI()

# CREATE
@app.post("/products", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# READ (All)
@app.get("/products", response_model=List[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

# READ (One)
@app.get("/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(404, "Product not found")
    return product

# UPDATE
@app.put("/products/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int,
    product_update: ProductCreate,
    db: Session = Depends(get_db)
):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(404, "Product not found")
    
    for key, value in product_update.dict().items():
        setattr(product, key, value)
    
    db.commit()
    db.refresh(product)
    return product

# DELETE
@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(404, "Product not found")
    
    db.delete(product)
    db.commit()
    return {"message": "Product deleted"}
```

## Django REST Framework CRUD

```python
# serializers.py
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'stock']

# views.py
from rest_framework import viewsets

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# urls.py
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', ProductViewSet)

# Auto-creates: GET, POST, PUT, PATCH, DELETE
```
''',
            'order': 3
        },
        {
            'title': 'ORM Basics (Django & SQLAlchemy)',
            'content': '''# ORM (Object-Relational Mapping)

## What is ORM?

**ORM converts Python objects ↔ Database rows**

Without ORM (manual SQL):
```python
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
row = cursor.fetchone()
user = {"id": row[0], "name": row[1], "email": row[2]}
```

With ORM (Pythonic):
```python
user = User.objects.get(id=user_id)
# Direct object access: user.name, user.email
```

## Django ORM

### Models
```python
from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=  True)
```

### Queries
```python
# CREATE
user = User.objects.create(email="john@ex.com", username="john")

# READ
all_users = User.objects.all()
user = User.objects.get(id=1)
active_users = User.objects.filter(is_active=True)

# UPDATE
user.username = "john_updated"
user.save()

# DELETE
user.delete()

# Filtering
recent_posts = Post.objects.filter(published_at__gte=datetime(2024, 1, 1))
john_posts = Post.objects.filter(author__username="john")

# Ordering
posts = Post.objects.all().order_by('-published_at')  # DESC
```

## SQLAlchemy ORM

### Models
```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    username = Column(String)
    
    posts = relationship("Post", back_populates="author")

class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    author = relationship("User", back_populates="posts")
```

### Queries
```python
# CREATE
user = User(email="john@ex.com", username="john")
db.add(user)
db.commit()

# READ
all_users = db.query(User).all()
user = db.query(User).filter(User.id == 1).first()

# UPDATE
user.username = "john_updated"
db.commit()

# DELETE
db.delete(user)
db.commit()
```

## Relationships

```python
# Get user's posts (Django)
user = User.objects.get(id=1)
user_posts = user.post_set.all()

# Reverse (get post's author)
post = Post.objects.get(id=1)
author = post.author
```
''',
            'order': 4
        },
        {
            'title': 'Input Validation & Data Integrity',
            'content': '''# Input Validation

## Pydantic Validation (FastAPI)

```python
from pydantic import BaseModel, EmailStr, Field, validator

class UserCreate(BaseModel):
    email: EmailStr  # Auto-validates email format
    username: str = Field(..., min_length=3, max_length=50)
    age: int = Field(..., ge=18, le=100)  # 18-100
    password: str = Field(..., min_length=8)
    
    @validator('username')
    def username_alphanumeric(cls, v):
        if not v.isalnum():
            raise ValueError('Username must be alphanumeric')
        return v
    
    @validator('password')
    def password_strong(cls, v):
        if not any(c.isupper() for c in v):
            raise ValueError('Password must contain uppercase')
        return v

@app.post("/register")
def register(user: UserCreate):
    # Pydantic auto-validates!
    # Returns 422 if invalid
    return {"message": "User registered"}
```

## Django Validation

```python
from django.core.exceptions import ValidationError

def validate_positive(value):
    if value < 0:
        raise ValidationError('Value must be positive')

class Product(models.Model):
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[validate_positive]
    )
```

## Database Constraints

```python
# Django
class User(models.Model):
    email = models.EmailField(unique=True)  # No duplicates
    age = models.IntegerField(
        validators=[MinValueValidator(18)]
    )

# SQLAlchemy
class User(Base):
    email = Column(String, unique=True, nullable=False)
    age = Column(Integer, CheckConstraint('age >= 18'))
```

## Sanitize Input

```python
import html

def sanitize(user_input):
    return html.escape(user_input)

# Prevent XSS attacks
comment = sanitize(user_comment)
```
''',
            'order': 5
        }
    ]
    
    for topic_data in stage4_topics:
        Topic.objects.create(stage=stage4, **topic_data)
    print(f"✅ Stage 4: {stage4.title} - {len(stage4_topics)} topics")
    
    # Stage 5: Industry-Ready Skills
    stage5 = Stage.objects.create(
        roadmap=roadmap,
        title='Industry-Ready Python Backend Skills',
        description='Master authentication, security, deployment, and best practices to become job-ready',
        order=5,
        is_free=False
    )
    
    stage5_topics = [
        {
            'title': 'Authentication & Authorization',
            'content': '''# Authentication & Authorization

## Password Hashing

```python
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Register
hashed_password = pwd_context.hash(plain_password)
user = User(email=email, password=hashed_password)

# Login
def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

# Check
if verify_password(input_password, user.password):
    # Login successful
```

## JWT Tokens

```python
from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

def create_token(data: dict):
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode = data.copy()
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(401, "Invalid token")

# Usage
@app.post("/login")
def login(email: str, password: str):
    user = authenticate(email, password)
    token = create_token({"user_id": user.id})
    return {"access_token": token}

@app.get("/protected")
def protected(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    return {"user_id": payload['user_id']}
```

## AuthorizationRole-Based)

```python
from enum import Enum

class Role(Enum):
    USER = "user"
    ADMIN = "admin"

def require_role(required_role: Role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Get current user
            if user.role != required_role:
                raise HTTPException(403, "Forbidden")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@app.delete("/users/{user_id}")
@require_role(Role.ADMIN)
def delete_user(user_id: int):
    # Only admins can delete
    pass
```
''',
            'order': 1
        },
        {
            'title': 'Backend Security Concepts',
            'content': '''# Backend Security

## SQL Injection Prevention

```python
# ❌ NEVER do this (vulnerable)
query = f"SELECT * FROM users WHERE email = '{email}'"

# ✅ Always use parameterized queries
user = db.query(User).filter(User.email == email).first()
```

## XSS Prevention

```python
import html

# Escape user input
sanitized = html.escape(user_input)
```

## CORS Configuration

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Environment Variables

```python
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")
```

## Rate Limiting

```python
from slowapi import Limiter

limiter = Limiter(key_func=lambda: request.client.host)

@app.get("/api/data")
@limiter.limit("5/minute")  # Max 5 requests per minute
def get_data():
    return {"data": "value"}
```
''',
            'order': 2
        },
        {
            'title': 'API Best Practices',
            'content': '''# API Best Practices

## RESTful Naming

```
✅ Good:
GET    /api/users
POST   /api/users
GET    /api/users/123
PUT    /api/users/123
DELETE /api/users/123

❌ Bad:
/api/getAllUsers
/api/createUser
/api/deleteUserById?id=123
```

## Status Codes

```python
from fastapi import status

# 200 OK
return {"data": data}

# 201 Created
return Response(status_code=status.HTTP_201_CREATED)

# 400 Bad Request
raise HTTPException(400, "Invalid input")

# 401 Unauthorized
raise HTTPException(401, "Login required")

# 404 Not Found
raise HTTPException(404, "Resource not found")

# 500 Internal Server Error
raise HTTPException(500, "Server error")
```

## Pagination

```python
@app.get("/products")
def get_products(page: int = 1, limit: int = 10):
    skip = (page - 1) * limit
    products = db.query(Product).offset(skip).limit(limit).all()
    total = db.query(Product).count()
    
    return {
        "products": products,
        "page": page,
        "total_pages": (total + limit - 1) // limit,
        "total": total
    }
```

## API Versioning

```python
from fastapi import APIRouter

v1_router = APIRouter(prefix="/v1")
v2_router = APIRouter(prefix="/v2")

@v1_router.get("/users")
def get_users_v1():
    pass

@v2_router.get("/users")
def get_users_v2():
    # Improved version
    pass

app.include_router(v1_router)
app.include_router(v2_router)
```

## Response Format

```python
class APIResponse(BaseModel):
    success: bool
    data: Any = None
    error: str = None

@app.get("/users")
def get_users():
    return APIResponse(
        success=True,
        data={"users": users}
    )
```
''',
            'order': 3
        },
        {
            'title': 'Logging & Error Monitoring',
            'content': '''# Logging in Python Backend

## Basic Logging

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.post("/users")
def create_user(user: UserCreate):
    logger.info(f"Creating user: {user.email}")
    
    try:
        new_user = save_user(user)
        logger.info(f"User created: ID={new_user.id}")
        return new_user
    except Exception as e:
        logger.error(f"Failed to create user: {e}", exc_info=True)
        raise
```

## Log Levels

```python
logger.debug("Detailed debug info")
logger.info("General information")
logger.warning("Warning message")
logger.error("Error occurred")
logger.critical("Critical issue")
```

## File Logging

```python
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='app.log',
    filemode='a'
)
```

## Structured Logging

```python
import structlog

logger = structlog.get_logger()

logger.info("user_created", user_id=123, email="john@ex.com")
```

## Error Tracking (Sentry)

```python
import sentry_sdk

sentry_sdk.init(dsn="your-dsn-here")

# Auto-captures exceptions
@app.get("/test")
def test():
    1 / 0  # Sentry will capture this
```
''',
            'order': 4
        },
        {
            'title': 'Deployment & Common Mistakes',
            'content': '''# Python Backend Deployment

## Production Server

```bash
# Install Gunicorn (production server)
pip install gunicorn

# Run
gunicorn main:app --workers 4 --bind 0.0.0.0:8000
```

## Environment Variables

```python
# .env
DATABASE_URL=postgresql://localhost/mydb
SECRET_KEY=your-secret-key
DEBUG=False

# main.py
from dotenv import load_dotenv
import os

load_dotenv()
DEBUG = os.getenv("DEBUG") == "True"
```

## Docker Deployment

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "main:app", "--host", "0.0.0.0"]
```

## Common Mistakes

### 1. Not Using Environment Variables
```python
# ❌ Bad
SECRET_KEY = "hardcoded-secret"

# ✅ Good
SECRET_KEY = os.getenv("SECRET_KEY")
```

### 2. Not Hashing Passwords
```python
# ❌ NEVER
user.password = plain_password

# ✅ Always hash
user.password = hash_password(plain_password)
```

### 3. Not Validating Input
```python
# ❌ Bad
@app.post("/users")
def create(data: dict):
    return save(data)

# ✅ Good
@app.post("/users")
def create(user: UserCreate):  # Pydantic validates
    return save(user)
```

### 4. Not HandlingExceptions
```python
# ❌ Bad
def get_user(id):
    return db.query(User).filter(User.id == id).first()

# ✅ Good
def get_user(id):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(404, "User not found")
    return user
```

### 5. Not Using Database Transactions
```python
# ✅ Good
from sqlalchemy.orm import Session

def transfer(from_id, to_id, amount, db: Session):
    try:
        # Debit
        sender = db.query(Account).get(from_id)
        sender.balance -= amount
        
        # Credit
        receiver = db.query(Account).get(to_id)
        receiver.balance += amount
        
        db.commit()  # Both succeed or both fail
    except:
        db.rollback()
        raise
```

## Deployment Checklist

- [ ] Use environment variables
- [ ] Hash passwords
- [ ] Validate all inputs
- [ ] Handle exceptions
- [ ] Use HTTPS
- [ ] Enable CORS properly
- [ ] Set up logging
- [ ] Use production server (Gunicorn)
- [ ] Database migrations
- [ ] Monitor errors (Sentry)

## Skills Built

✅ REST API development
✅ Database integration (SQL, ORM)
✅ Authentication & security
✅ Error handling & logging
✅ Deployment basics
✅ Best practices

## Job Roles

- Python Backend Developer
- API Developer
- Full Stack Developer (Python)
- DevOps Engineer

## Next Steps

After mastering Python backend:
→ **System Design** (scalability, architecture)
→ **DevOps** (Docker, Kubernetes, CI/CD)
→ **Cloud** (AWS, GCP, Azure)
→ **Microservices** (advanced architecture)
''',
            'order': 5
        }
    ]
    
    for topic_data in stage5_topics:
        Topic.objects.create(stage=stage5, **topic_data)
    print(f"✅ Stage 5: {stage5.title} - {len(stage5_topics)} topics")
    
    # Update roadmap stats
    roadmap.update_stats()
    
    print("\n" + "="*60)
    print(f"✅ COMPLETE: Python Backend Development Roadmap!")
    print(f"   Total Stages: 5 (1 FREE, 4 PREMIUM)")
    print(f"   Total Topics: 25")
    print(f"   Estimated Hours: 180")
    print(f"   Status: Ready for students!")
    print("="*60)

if __name__ == '__main__':
    add_final_stages()
    print(f"\n🎉 Python Backend Roadmap is LIVE!")
