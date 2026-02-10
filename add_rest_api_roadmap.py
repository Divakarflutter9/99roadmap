
import os
import django
import sys

# Add project root to sys.path
sys.path.append('/Users/saitejakaki/Divakar/devaproject')

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import Roadmap, RoadmapCategory, Stage, Topic

def create_rest_api_roadmap():
    """Create Professional REST API Design Roadmap"""
    
    print("🚀 Initializing Professional REST API Roadmap Creation...")
    
    # 1. Get or Create Category
    # 'backend-development'
    category, _ = RoadmapCategory.objects.get_or_create(
        slug='backend-development',
        defaults={'name': 'Backend Development'}
    )
    
    # 2. Create Roadmap
    roadmap_slug = 'rest-api-mastery'
    roadmap_title = 'Professional REST API Design'
    
    roadmap, created = Roadmap.objects.get_or_create(
        slug=roadmap_slug,
        defaults={
            'title': roadmap_title,
            'short_description': 'Design scalable, intuitive, and secure APIs. Master HTTP verbs, status codes, JSON contracts, and versioning strategies.',
            'description': 'Stop building messy endpoints. Learn the industry standards for RESTful design, how to structure JSON responses, handle errors gracefully, and secure your APIs for production.',
            'category': category,
            'difficulty': 'intermediate',
            'estimated_hours': 35,
            'is_premium': True,
            'is_featured': True,
            'is_active': True,
            'price': 399
        }
    )
    
    if created:
        print(f"✅ Created Roadmap: {roadmap.title}")
    else:
        print(f"ℹ️  Roadmap '{roadmap.title}' already exists. Updating details...")
        roadmap.stages.all().delete()
        print("   ♻️  Cleared existing stages for fresh import.")
        
    # ==========================================
    # STAGE 1: API FUNDAMENTALS (FREE)
    # ==========================================
    stage1 = Stage.objects.create(
        roadmap=roadmap,
        title='API Fundamentals',
        description='Understand why APIs exist and the Client-Server model.',
        order=1,
        is_free=True
    )
    
    topics_s1 = [
        {
            'title': 'The Client-Server Contract',
            'content': """# The Interface of the Web

## What is an API?
- **Application Programming Interface**.
- It is a **Contract** between two pieces of software.
- "If you send me Request A, I promise to send you Response B."

## Client vs Server
- **Client**: The User (Mobile App, React Website, Smart Watch).
- **Server**: The Provider (AWS, Database, Logic).
- **The Gap**: They speak different languages (Swift/JS vs Python/Java).
- **The Bridge**: **HTTP** and **JSON**.

## Statelessness (The Golden Rule)
- The server does NOT remember the previous request.
- Every request must contain ALL information needed (Auth Token, Data).
- **Why?**: Allows scaling to millions of users across multiple servers.
""",
            'order': 1
        },
        {
            'title': 'What is REST?',
            'content': """# Representational State Transfer

## Practical Definition
- A set of architectural constraints for building Web APIs.
- **Resources**: Everything is a "noun" (User, Product, Order).
- **Uniform Interface**: We use standard HTTP methods to interact with resources.

## Not SOAP
- XML is heavy. JSON is light.
- REST uses the Web's existing machinery (HTTP Caching, URLs) instead of fighting it.
""",
            'order': 2
        }
    ]
    
    for t in topics_s1:
        Topic.objects.create(stage=stage1, **t)
    print(f"   ✨ Added {len(topics_s1)} topics to Stage 1")


    # ==========================================
    # STAGE 2: API DESIGN CONCEPTS
    # ==========================================
    stage2 = Stage.objects.create(
        roadmap=roadmap,
        title='API Design Concepts',
        description='Design clean, intuitive endpoints.',
        order=2,
        is_free=False
    )
    
    topics_s2 = [
        {
            'title': 'Resource Naming (The Noun Rule)',
            'content': """# URLs are for Resources

## The Good
- `GET /users` (Get all users)
- `GET /users/12` (Get user #12)
- `POST /users` (Create a user)
- `DELETE /users/12` (Delete user #12)

## The Bad (RPC Style)
- `POST /getAllUsers`
- `POST /createUser`
- `POST /deleteUser`

## Nested Resources
- **Relationship**: User has Orders.
- `GET /users/12/orders` (Get orders belonging to User 12).
""",
            'order': 1
        },
        {
            'title': 'HTTP Methods & Status Codes',
            'content': """# The Verbs of the Web

## Methods
- **GET**: Read data. Safe. Idempotent.
- **POST**: Create data. Not Idempotent.
- **PUT**: Replace/Update entire resource.
- **PATCH**: Partial update (e.g., just change email).
- **DELETE**: Remove resource.

## Status Codes (The Signal)
- **2xx Success**:
    - `200 OK`: General success.
    - `201 Created`: Successful POST creation.
- **3xx Redirection**:
    - `301 Moved Permanently`.
- **4xx Client Error** (You messed up):
    - `400 Bad Request`: Invalid JSON/Validation error.
    - `401 Unauthorized`: Who are you? (Missing Login).
    - `403 Forbidden`: I know you, but you can't touch this.
    - `404 Not Found`.
- **5xx Server Error** (I messed up):
    - `500 Internal Server Error`: Bug in code / DB down.
""",
            'order': 2
        }
    ]
    
    for t in topics_s2:
        Topic.objects.create(stage=stage2, **t)
    print(f"   ✨ Added {len(topics_s2)} topics to Stage 2")


    # ==========================================
    # STAGE 3: DATA HANDLING & INTEGRATION
    # ==========================================
    stage3 = Stage.objects.create(
        roadmap=roadmap,
        title='Data Handling & Integration',
        description='Structuring Requests and Responses.',
        order=3,
        is_free=False
    )
    
    topics_s3 = [
        {
            'title': 'JSON Structure',
            'content': """# The Universal Language

## Request Body (Input)
```json
{
  "email": "alice@example.com",
  "role": "admin"
}
```

## Response Body (Output)
Always wrap data or be consistent.
**Envelope Pattern**:
```json
{
  "data": [ ... ],
  "meta": {
    "page": 1,
    "total": 50
  }
}
```

## Date Handling
- Use **ISO 8601 Strings**.
- `2023-10-27T14:30:00Z` (UTC).
- Never send `10/05/2023` (Ambiguous: Can be May 10 or Oct 5).
""",
            'order': 1
        },
        {
            'title': 'Query Parameters vs Body',
            'content': """# How to send Input?

## 1. Path Parameters (`/users/12`)
- Use for **Identifying** a specific resource.
- Mandatory.

## 2. Query Parameters (`/users?role=admin&sort=desc`)
- Use for **Filtering, Sorting, Pagination**.
- Optional.
- Good because the URL can be bookmarked/shared.

## 3. Request Body (JSON)
- Use for **Complex/Large Data** (Creating/Updating).
- Secure (Not visible in URL logs).
- Only for POST/PUT/PATCH (GET should not have body).
""",
            'order': 2
        }
    ]
    
    for t in topics_s3:
        Topic.objects.create(stage=stage3, **t)
    print(f"   ✨ Added {len(topics_s3)} topics to Stage 3")


    # ==========================================
    # STAGE 4: INDUSTRY PRACTICES
    # ==========================================
    stage4 = Stage.objects.create(
        roadmap=roadmap,
        title='Industry Practices',
        description='Production-ready API standards.',
        order=4,
        is_free=False
    )
    
    topics_s4 = [
        {
            'title': 'Security (Auth & Rate Limiting)',
            'content': """# Locking the Door

## Authentication
- **Basic Auth** (User:Pass): Old, avoid.
- **API Keys**: Good for identifying *Machines*.
- **Bearer Tokens (JWT)**: Good for identifying *Users*.
    - Header: `Authorization: Bearer <token>`

## Rate Limiting
- Prevent spam/DDoS.
- Return `429 Too Many Requests`.
- Headers: `X-RateLimit-Remaining: 5`.

## HTTPS
- Mandatory. Never send JSON over HTTP (Cleartext).
""",
            'order': 1
        },
        {
            'title': 'Versioning & Documentation',
            'content': """# Managing Change

## Breaking Changes
- You cannot just rename a field. It breaks the Client App.
- **Solution**: Versioning.
    - URL: `/api/v1/users` -> `/api/v2/users`.
    - Header: `Accept-Version: v2`.

## Documentation
- If it's not documented, it doesn't exist.
- **Swagger / OpenAPI**: Standard for describing APIs.
- Generates interactive UI for devs to try endpoints.
""",
            'order': 2
        }
    ]
    
    for t in topics_s4:
        Topic.objects.create(stage=stage4, **t)
    print(f"   ✨ Added {len(topics_s4)} topics to Stage 4")

    # Update stats
    roadmap.update_stats()
    print("✅ Professional REST API Roadmap creation complete! Stats updated.")

if __name__ == '__main__':
    create_rest_api_roadmap()
