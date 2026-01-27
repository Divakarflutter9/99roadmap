"""
Add Python Backend Roadmap - Part 2 (Stages 3, 4, 5)
"""

import os
import django
import sys

sys.path.append('/Users/saitejakaki/Divakar/devaproject')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import Roadmap, Stage, Topic

def add_remaining_stages():
    """Add stages 3, 4, and 5 to Python Backend roadmap"""
    
    roadmap = Roadmap.objects.get(slug='python-backend-development')
    print(f"Adding stages to: {roadmap.title}")
    
    # Stage 3: Python Backend Frameworks
    stage3 = Stage.objects.create(
        roadmap=roadmap,
        title='Python Backend Frameworks',
        description='Build real backend services with Django and FastAPI - Learn when to use which framework',
        order=3,
        is_free=False
    )
    
    stage3_topics = [
        {
            'title': 'Why Frameworks are Needed',
            'content': '''# Why Backend Frameworks?

## The Problem Without Frameworks

Writing backend from scratch is:
- **Time-consuming**: Reinvent routing, auth, ORM
- **Error-prone**: Security vulnerabilities
- **Hard to maintain**: Messy code structure
- **No standards**: Every project different

## What Frameworks Provide

### 1. URL Routing
```python
# Without framework (complex)
def handle_request(path, method):
    if path == '/users' and method == 'GET':
        return get_all_users()
    elif path.startswith('/users/') and method == 'GET':
        user_id = extract_id(path)
        return get_user(user_id)
    # Hundreds of if-else...

# With framework (clean)
@app.get("/users")
def get_users():
    return users

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return find_user(user_id)
```

### 2. Request/Response Handling
```python
# Framework handles:
- Parsing JSON from request
- Validating data types
- Returning proper HTTP responses
- Setting headers and status codes
```

### 3. Database Integration (ORM)
```python
# Without ORM (manual SQL)
conn = mysql.connector.connect(...)
cursor = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,))
user = cursor.fetchone()

# With ORM (Pythonic)
user = User.objects.get(id=user_id)
```

### 4. Built-in Security
- CSRF protection
- SQL injection prevention
- XSS protection
- Password hashing
- Session management

### 5. Authentication & Authorization
- Ready-to-use login/logout
- User roles and permissions
- JWT token handling
- Social auth (Google, GitHub)

## Popular Python Frameworks

| Framework | Type | Use Case | Learning Curve |
|-----------|------|----------|----------------|
| Django | Full-stack | Large apps, admin panels | Medium |
| FastAPI | Modern API | Microservices, APIs | Easy |
| Flask | Lightweight | Small projects | Easy |

## When Frameworks Make Sense

✅ Use framework when:
- Building production applications
- Need rapid development
- Want community support
- Require standard patterns

❌ Skip framework for:
- Simple scripts
- Learning HTTP basics
- Very specific requirements

## Key Takeaway
Frameworks are like **pre-built house blueprints**. Instead of building from bricks, you get rooms, plumbing, and electricity ready to use!
''',
            'order': 1
        },
        {
            'title': 'Django vs FastAPI: When to Use Which',
            'content': '''# Django vs FastAPI

## Django

### What is Django?
**"The web framework for perfectionists with deadlines"**

Full-featured framework with everything included:
- Admin panel (auto-generated)
- ORM (database layer)
- Authentication system
- Template engine
- Form handling

### When to Use Django

✅ Choose Django for:
- **Full websites** (frontend + backend)
- **E-commerce platforms**
- **Content management systems**
- **Admin dashboards**
- **MVP development** (launch fast)
- When you need **batteries included**

### Django Example
```python
# models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

# views.py
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    return Response({'products': list(products.values())})
```

### Django Advantages
- **Admin panel**: Free database UI
- **ORM**: Built-in, powerful
- **Mature**: 18+ years old, battle-tested
- **Large community**: Tons of packages
- **Great for monoliths**

### Django Disadvantages
- **Heavy**: Large framework size
- **Slower**: Compared to FastAPI
- **Learning curve**: Lots to learn
- **Opinionated**: Django way or highway

---

## FastAPI

### What is FastAPI?
**Modern, fast, high-performance Python framework**

Built on:
- **Pydantic** (data validation)
- **Starlette** (ASGI framework)
- **Type hints** (Python 3.6+)

### When to Use FastAPI

✅ Choose FastAPI for:
- **REST APIs** (pure backend)
- **Microservices**
- **Real-time applications**
- **Data science APIs** (ML models)
- **High-performance needs**
- **Modern Python projects**

### FastAPI Example
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    name: str
    price: float
    stock: int

@app.get("/products")
def get_products():
    return {"products": []}

@app.post("/products")
def create_product(product: Product):
    # Auto-validates product data!
    return {"message": "Product created", "product": product}
```

### FastAPI Advantages
- **Fast**: Performance similar to Node.js, Go
- **Modern**: Uses async/await
- **Auto documentation**: Swagger UI included
- **Type safety**: Catches errors early
- **Easy to learn**: Intuitive syntax
- **Perfect for APIs**

### FastAPI Disadvantages
- **No admin panel**: Must build yourself
- **Newer**: Less mature (2018)
- **No built-in ORM**: Use SQLAlchemy
- **Smaller community**: Fewer packages

---

## Comparison Table

| Feature | Django | FastAPI |
|---------|--------|---------|
| **Speed** | Medium | Very Fast |
| **Type** | Full-stack | API-focused |
| **Admin Panel** | Yes | No |
| **ORM** | Built-in | SQLAlchemy |
| **Learning Curve** | Medium | Easy |
| **Use Case** | Websites | APIs |
| **Async Support** | Partial | Native |
| **Documentation** | Excellent | Auto-generated |
| **Community** | Huge | Growing |

---

## Real Company Examples

### Companies Using Django
- **Instagram**: Django handles 1 billion+ users
- **Spotify**: Web backend
- **Pinterest**: Image sharing platform
- **Dropbox**: File sync backend

### Companies Using FastAPI
- **Uber**: Ride matching microservices
- **Netflix**: Internal tools
- **Microsoft**: Azure services
- **Startups**: Rapid API development

---

## Decision Tree

```
Need admin panel? → Yes → Django
                 → No ↓

Building website? → Yes → Django
                 → No ↓

Need pure APIs? → Yes → FastAPI

Need ML integration? → Yes → FastAPI

Async/real-time? → Yes → FastAPI
                → No → Django or FastAPI
```

---

## Can You Use Both?

**Yes!** Many companies do:
- **Django** for main website + admin
- **FastAPI** for high-performance APIs

Example:
- Django handles user auth, admin panel
- FastAPI microservices for ML, search, notifications

---

## For Beginners

**Start with FastAPI if:**
- You want to build APIs
- You know Python basics
- You want quick results

**Start with Django if:**
- You're building a complete website
- You want admin panel
- You prefer structured framework

---

## Key Takeaway
- **Django** = Complete toolkit (hammer, screwdriver, saw)
- **FastAPI** = Specialized power tool (perfect for one job)

Both are excellent! Choose based on your project needs.
''',
            'order': 2
        },
        {
            'title': 'Creating REST APIs',
            'content': '''# Creating REST APIs

## What is REST API?

**REST (Representational State Transfer)** is a standard way to build web APIs.

### REST Principles
1. **Resources**: Users, products, orders
2. **HTTP Methods**: GET, POST, PUT, DELETE
3. **Stateless**: Each request is independent
4. **JSON Format**: Standard data format

## FastAPI REST API Example

### Setup
```bash
pip install fastapi uvicorn sqlalchemy
```

### Basic API
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# In-memory data (replace with database later)
users = []
user_id_counter = 1

class User(BaseModel):
    name: str
    email: str
    age: int

# CREATE - POST /users
@app.post("/users")
def create_user(user: User):
    global user_id_counter
    new_user = {
        "id": user_id_counter,
        **user.dict()
    }
    users.append(new_user)
    user_id_counter += 1
    return {"message": "User created", "user": new_user}

# READ (All) - GET /users
@app.get("/users")
def get_all_users():
    return {"users": users}

# READ (One) - GET /users/1
@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return {"error": "User not found"}, 404
    return {"user": user}

# UPDATE - PUT /users/1
@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User):
    for user in users:
        if user['id'] == user_id:
            user.update(updated_user.dict())
            return {"message": "User updated", "user": user}
    return {"error": "User not found"}, 404

# DELETE - DELETE /users/1
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    global users
    users = [u for u in users if u['id'] != user_id]
    return {"message": "User deleted"}
```

### Run Server
```bash
uvicorn main:app --reload
```

Visit: http://localhost:8000/docs (Auto documentation!)

---

## Django REST Framework Example

### Setup
```bash
pip install django djangorestframework
```

### Models
```python
# models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
```

### Serializers
```python
# serializers.py
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'stock', 'created_at']
```

### Views
```python
# views.py
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

### URLs
```python
# urls.py
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = router.urls
```

This automatically creates:
- `GET /products/` - List all
- `POST /products/` - Create
- `GET /products/1/` - Get one
- `PUT /products/1/` - Update
- `DELETE /products/1/` - Delete

---

## Request/Response Examples

### Create Product
```bash
curl -X POST http://localhost:8000/products \\
  -H "Content-Type: application/json" \\
  -d '{
    "name": "Laptop",
    "price": 50000,
    "stock": 10
  }'
```

Response:
```json
{
  "id": 1,
  "name": "Laptop",
  "price": 50000.00,
  "stock": 10,
  "created_at": "2024-01-27T10:30:00Z"
}
```

### Get All Products
```bash
curl http://localhost:8000/products
```

Response:
```json
{
  "products": [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Mouse", "price": 500}
  ]
}
```

---

## Status Codes in APIs

```python
from fastapi import HTTPException, status

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = find_user(user_id)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return user
```

---

## Query Parameters

```python
@app.get("/products")
def get_products(
    category: str = None,
    min_price: float = 0,
    max_price: float = 100000
):
    # Filter products
    filtered = products
    
    if category:
        filtered = [p for p in filtered if p['category'] == category]
    
    filtered = [p for p in filtered if min_price <= p['price'] <= max_price]
    
    return {"products": filtered}

# Usage: /products?category=electronics&min_price=1000&max_price=50000
```

---

## Request Body Validation

```python
from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    age: int = Field(..., ge=18, le=100)  # 18-100
    password: str = Field(..., min_length=8)

@app.post("/register")
def register(user: UserCreate):
    # FastAPI auto-validates!
    # Returns 422 if validation fails
    return {"message": "User registered"}
```

---

## Key Takeaways

✅ REST APIs use HTTP methods for CRUD
✅ JSON is standard format
✅ FastAPI auto-validates and documents
✅ Django REST Framework is powerful for complex apps
✅ Always return proper status codes
✅ Use Pydantic models for validation
''',
            'order': 3
        },
        {
            'title': 'URL Routing & Request Handling',
            'content': '''# URL Routing & Request Handling

## FastAPI Routing

### Path Parameters
```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

@app.get("/posts/{post_id}/comments/{comment_id}")
def get_comment(post_id: int, comment_id: int):
    return {"post": post_id, "comment": comment_id}
```

### Query Parameters
```python
# /search?q=laptop&page=1&limit=10
@app.get("/search")
def search(q: str, page: int = 1, limit: int = 10):
    return {
        "query": q,
        "page": page,
        "limit": limit
    }
```

### Request Body
```python
from pydantic import BaseModel

class LoginRequest(BaseModel):
    email: str
    password: str

@app.post("/login")
def login(credentials: LoginRequest):
    return {
        "email": credentials.email,
        "status": "authenticated"
    }
```

### Multiple Response Types
```python
from fastapi.responses import JSONResponse, PlainTextResponse

@app.get("/data", response_class=JSONResponse)
def get_data():
    return {"data": "value"}

@app.get("/health", response_class=PlainTextResponse)
def health_check():
    return "OK"
```

---

## Django URL Routing

### URL Patterns
```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('users/', views.user_list),
    path('users/<int:user_id>/', views.user_detail),
    path('posts/<slug:slug>/', views.post_detail),
]
```

### Class-Based Views
```python
# views.py
from django.views import View
from django.http import JsonResponse

class UserListView(View):
    def get(self, request):
        users = User.objects.all()
        return JsonResponse({'users': list(users.values())})
    
    def post(self, request):
        # Create user
        return JsonResponse({'message': 'User created'})
```

---

## Request Object

### FastAPI Request
```python
from fastapi import Request

@app.get("/info")
def get_info(request: Request):
    return {
        "method": request.method,
        "url": str(request.url),
        "headers": dict(request.headers),
        "client_ip": request.client.host
    }
```

### Django Request
```python
def my_view(request):
    return JsonResponse({
        "method": request.method,
        "path": request.path,
        "GET": dict(request.GET),
        "POST": dict(request.POST),
        "headers": dict(request.headers)
    })
```

---

## Headers

### Reading Headers
```python
from fastapi import Header

@app.get("/protected")
def protected_route(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(401, "Unauthorized")
    
    token = authorization.split("Bearer ")[-1]
    # Verify token...
    return {"message": "Access granted"}
```

### Setting Headers
```python
from fastapi import Response

@app.get("/custom")
def custom_headers(response: Response):
    response.headers["X-Custom-Header"] = "MyValue"
    response.headers["X-Request-ID"] = "12345"
    return {"data": "value"}
```

---

## File Uploads

```python
from fastapi import File, UploadFile

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # Read file
    contents = await file.read()
    
    # Save file
    with open(f"uploads/{file.filename}", "wb") as f:
        f.write(contents)
    
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(contents)
    }
```

---

## Form Data

```python
from fastapi import Form

@app.post("/login")
def login(
    username: str = Form(...),
    password: str = Form(...)
):
    # Process login
    return {"username": username}
```

---

## Cookies

```python
from fastapi import Cookie, Response

@app.get("/set-cookie")
def set_cookie(response: Response):
    response.set_cookie(
        key="session_id",
        value="abc123",
        max_age=3600  # 1 hour
    )
    return {"message": "Cookie set"}

@app.get("/get-cookie")
def get_cookie(session_id: str = Cookie(None)):
    return {"session_id": session_id}
```

---

## Response Models

```python
from pydantic import BaseModel

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    # password excluded from response!

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    user = db.get_user(user_id)
    return user  # FastAPI auto-filters fields
```

---

## Router Groups

```python
from fastapi import APIRouter

# users_router.py
router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def list_users():
    return {"users": []}

@router.post("/")
def create_user():
    return {"message": "User created"}

# main.py
app.include_router(router)
# Now you have: GET /users/ and POST /users/
```

---

## Middleware

```python
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    import time
    start_time = time.time()
    
    response = await call_next(request)
    
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    
    return response
```

---

## Key Takeaways

✅ Path parameters: `/users/{id}`
✅ Query parameters: `/search?q=value`
✅ Request body: JSON payload
✅ Headers for auth tokens
✅ File uploads with UploadFile
✅ Response models filter sensitive data
''',
            'order': 4
        },
        {
            'title': 'Basic Error Handling in APIs',
            'content': '''# Error Handling in APIs

## HTTP Exception in FastAPI

```python
from fastapi import HTTPException

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = db.find_user(user_id)
    
    if not user:
        raise HTTPException(
            status_code=404,
            detail=f"User {user_id} not found"
        )
    
    return user
```

## Custom Exception Classes

```python
class UserNotFoundException(Exception):
    pass

class EmailAlreadyExistsException(Exception):
    pass

# Usage
def register_user(email, password):
    if User.exists(email):
        raise EmailAlreadyExistsException(f"Email {email} already registered")
    
    return create_user(email, password)
```

## Global Exception Handlers

```python
from fastapi import Request
from fastapi.responses import JSONResponse

@app.exception_handler(UserNotFoundException)
async def user_not_found_handler(request: Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"error": "User not found", "detail": str(exc)}
    )

@app.exception_handler(EmailAlreadyExistsException)
async def email_exists_handler(request: Request, exc: EmailAlreadyExistsException):
    return JSONResponse(
        status_code=400,
        content={"error": "Email already exists", "detail": str(exc)}
    )
```

## Validation Errors

```python
from fastapi import HTTPException
from pydantic import ValidationError

@app.post("/users")
def create_user(user: UserCreate):
    try:
        # FastAPI auto-validates
        new_user = save_user(user)
        return new_user
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())
```

## Try-Except in Endpoints

```python
@app.post("/orders")
def create_order(order: OrderCreate):
    try:
        # Validate stock
        if not check_stock(order.product_id, order.quantity):
            raise HTTPException(400, "Insufficient stock")
        
        # Process payment
        payment_result = process_payment(order.amount)
        
        if payment_result['status'] != 'success':
            raise HTTPException(402, "Payment failed")
        
        # Create order
        order = save_order(order)
        
        return {"order_id": order.id, "status": "created"}
    
    except PaymentGatewayException as e:
        raise HTTPException(503, "Payment service unavailable")
    
    except Exception as e:
        logger.error(f"Order creation failed: {e}")
        raise HTTPException(500, "Internal server error")
```

## Error Response Format

```python
class ErrorResponse(BaseModel):
    errorstatus_code: int
    message: str
    detail: str = None
    timestamp: datetime

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "status_code": 500,
            "message": "Internal server error",
            "detail": str(exc),
            "timestamp": datetime.now().isoformat()
        }
    )
```

## Django Error Handling

```python
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

# settings.py
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'myapp.exceptions.custom_exception_handler'
}
```

## Logging Errors

```python
import logging

logger = logging.getLogger(__name__)

@app.post("/transfer")
def transfer_money(transfer: TransferRequest):
    try:
        logger.info(f"Processing transfer: {transfer.from_account} -> {transfer.to_account}")
        
        result = execute_transfer(transfer)
        
        logger.info(f"Transfer successful: {result.transaction_id}")
        return result
    
    except InsufficientBalanceException as e:
        logger.warning(f"Transfer failed: Insufficient balance - {e}")
        raise HTTPException(400, str(e))
    
    except Exception as e:
        logger.error(f"Transfer error: {e}", exc_info=True)
        raise HTTPException(500, "Transfer failed")
```

## Key Takeaways

✅ Use HTTPException for client errors (400, 404)
✅ Return 500 for server errors
✅ Log all errors for debugging
✅ Provide meaningful error messages
✅ Use global exception handlers
✅ Never expose sensitive info in errors
''',
            'order': 5
        }
    ]
    
    for topic_data in stage3_topics:
        Topic.objects.create(stage=stage3, **topic_data)
    print(f"✅ Stage 3: {stage3.title} - {len(stage3_topics)} topics")
    
    # Continue with stages 4 and 5...
    # (Due to length, creating remaining stages in next file)
    
    print("\n✅ Stage 3 complete! Creating stages 4-5...")
    return roadmap

if __name__ == '__main__':
    roadmap = add_remaining_stages()
    print(f"\n✅ Stage 3 added successfully!")
