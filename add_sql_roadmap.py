
import os
import django
import sys

# Add project root to sys.path
sys.path.append('/Users/saitejakaki/Divakar/devaproject')

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import Roadmap, RoadmapCategory, Stage, Topic

def create_sql_roadmap():
    """Create Industry-Focused SQL & Database Roadmap"""
    
    print("🚀 Initializing SQL Roadmap Creation...")
    
    # 1. Get or Create Category
    # 'backend-development' is a good fit, or keep it under 'computer-science' if generic.
    # Let's use 'backend-development' as databases are core to backend.
    category, _ = RoadmapCategory.objects.get_or_create(
        slug='backend-development',
        defaults={'name': 'Backend Development'}
    )
    
    # 2. Create Roadmap
    roadmap_slug = 'industry-sql-database'
    roadmap_title = 'Industry-Focused SQL & Database Mastery'
    
    roadmap, created = Roadmap.objects.get_or_create(
        slug=roadmap_slug,
        defaults={
            'title': roadmap_title,
            'short_description': 'Master SQL, Database Design, and Performance Optimization for production systems.',
            'description': 'Go beyond `SELECT *`. Learn how to design scalable schemas, write efficient queries, understand indexing, and manage data in real-world applications.',
            'category': category,
            'difficulty': 'intermediate',
            'estimated_hours': 50,
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
    # STAGE 1: DATABASE BASICS (FREE)
    # ==========================================
    stage1 = Stage.objects.create(
        roadmap=roadmap,
        title='Database Basics',
        description='Understanding data persistence in modern software.',
        order=1,
        is_free=True
    )
    
    topics_s1 = [
        {
            'title': 'What Databases Solve',
            'content': """# Why We Need Databases

## The Problem with Files
Beginners often ask: *"Why not just save data in a JSON or Text file?"*

### ❌ File System Approach
```json
// users.json
[
  {"id": 1, "name": "John", "balance": 100},
  {"id": 2, "name": "Jane", "balance": 200}
]
```
**Issues in Production:**
1.  **Concurrency**: What if 2 users buy a ticket at the exact same millisecond? File writes will corrupt.
2.  **Scalability**: Reading a 5GB JSON file into RAM just to find one user is impossible.
3.  **Data Integrity**: You can accidentally save `"balance": "ten"` (string) instead of integer.

### ✅ The Database Solution
Databases (DBMS) are specialized software to manage data.
- **ACID Properties**: Guarantees transactions are processed reliably.
- **Indexing**: Find 1 record in 100 million in milliseconds.
- **Security**: Granular access control.

## Real World Analogy
- **Excel Sheet**: Good for 1 person, 1000 rows.
- **Database**: Good for 1 million people, 1 billion rows, accessed simultaneously.
""",
            'order': 1
        },
        {
            'title': 'Tables, Rows, Columns (Intuitive)',
            'content': """# The Spreadsheet Analogy

If you know Excel, you know 80% of Database basics.

## 1. Table (The Sheet)
A collection of related data.
- **Example**: `Users` Table, `Orders` Table.

## 2. Column (The Header)
Defines the **Data Type** and meaning.
- `email`: VARCHAR (Text)
- `age`: INTEGER
- `created_at`: TIMESTAMP

## 3. Row (The Record)
A single entry.
- `(1, "john@example.com", 25, "2023-01-01")`

## Primary Key (The ID)
Every row needs a unique identifier.
- usually `id` (Auto-incrementing Integer or UUID).
- **Analogy**: Your Student ID or Social Security Number. Names can be duplicates, IDs cannot.
""",
            'order': 2
        },
        {
            'title': 'SQL vs NoSQL Overview',
            'content': """# SQL vs NoSQL: Choosing the Right Tool

In interviews and system design, this is a critical decision.

## 1. SQL (Relational)
- **Structure**: Rigid, Pre-defined Tables.
- **Examples**: PostgreSQL, MySQL, SQLite, Oracle.
- **Use Case**:
    - Financial Systems (Banks).
    - E-commerce (Orders, Inventory).
    - User Management.
- **Why**: Strict consistency is required. You can't have an Order without a User.

## 2. NoSQL (Non-Relational)
- **Structure**: Flexible, Documents (JSON-like).
- **Examples**: MongoDB, Redis, Cassandra, DynamoDB.
- **Use Case**:
    - Real-time Analytics / Logs.
    - Content Management (Blogs with varying fields).
    - High-velocity IOT data.
    - Caching (Redis).

## Industry Reality
Most large companies use **BOTH**.
- **Uber**: Uses SQL (PostgreSQL) for Trips/Billing. Uses NoSQL (Cassandra) for storing location history.
- **Instagram**: Uses SQL for Users/Photos. Uses NoSQL (Redis) for feed generation.
""",
            'order': 3
        }
    ]
    
    for t in topics_s1:
        Topic.objects.create(stage=stage1, **t)
    print(f"   ✨ Added {len(topics_s1)} topics to Stage 1")


    # ==========================================
    # STAGE 2: CORE SQL
    # ==========================================
    stage2 = Stage.objects.create(
        roadmap=roadmap,
        title='Core SQL',
        description='Mastering the language of data.',
        order=2,
        is_free=False
    )
    
    topics_s2 = [
        {
            'title': 'CRUD Operations (Real Usage)',
            'content': """# CRUD: Create, Read, Update, Delete

The 4 operations that make up 90% of Backend interactions.

## 1. CREATE (INSERT)
```sql
-- User signs up
INSERT INTO users (email, password_hash, is_active) 
VALUES ('john@doe.com', 'x8df7s...', true);
```

## 2. READ (SELECT)
The most used command.
```sql
-- "Show me my profile"
SELECT * FROM users WHERE id = 1;

-- "Who are the admin users?"
SELECT email FROM users WHERE role = 'admin';
```

## 3. UPDATE
```sql
-- User changes password
UPDATE users 
SET password_hash = 'new_hash_123' 
WHERE id = 1;

-- ⚠️ DANGER ZONE:
-- If you forget the WHERE clause, you update EVERY user's password!
-- UPDATE users SET password = '...';  <-- FIRED
```

## 4. DELETE
```sql
-- Delete a spam comment
DELETE FROM comments WHERE id = 5521;
```
**Industry Tip**: We rarely actually `DELETE`. We use **Soft Deletes**.
Instead of removing the row, we set `is_deleted = true`.
- Allows data recovery.
- Maintains historical records.
""",
            'order': 1
        },
        {
            'title': 'Filtering & Sorting',
            'content': """# Filtering and Sorting Data

## WHERE Clause (The Filter)
Operators: `=`, `!=`, `>`, `<`, `IN`, `LIKE`.

```sql
-- Find active users over 18
SELECT * FROM users 
WHERE age > 18 AND status = 'active';

-- Search feature (Pattern Matching)
-- Finds emails ending in '@gmail.com'
SELECT * FROM users 
WHERE email LIKE '%@gmail.com';
```

## ORDER BY (The Sort)
Default is ASC (Ascending).

```sql
-- Leaderboard: Top scores first
SELECT username, score FROM gamification 
ORDER BY score DESC 
LIMIT 10;
```

## LIMIT & OFFSET (Pagination)
You never load 1 million rows on a webpage. You load pages of 20.

```sql
-- Page 2 (Items 21-40)
SELECT * FROM products 
LIMIT 20 OFFSET 20;
```
""",
            'order': 2
        },
        {
            'title': 'Joins (The Superpower)',
            'content': """# Joins: Connecting Tables

Relational databases shine here. We store data in separate tables to avoid duplication (Normalization) and `JOIN` them when needed.

## Scenario
- Table `Users` (id, name)
- Table `Orders` (id, user_id, amount)

## 1. INNER JOIN (The intersection)
"Show me users and their orders."
Only returns users who **have** orders.

```sql
SELECT users.name, orders.amount 
FROM users
INNER JOIN orders ON users.id = orders.user_id;
```

## 2. LEFT JOIN (Preserve the Left)
"Show me ALL users, and their orders if they have any."
Returns all users. If no order, returns `NULL`.

```sql
SELECT users.name, orders.amount 
FROM users
LEFT JOIN orders ON users.id = orders.user_id;
```
**Use Case**: Finding users who have *never* purchased anything (to send them a coupon).
`WHERE orders.id IS NULL`

## Visualizing it
Think of Venn Diagrams.
- Inner Join = A ∩ B
- Left Join = A (with parts of B matching)
""",
            'order': 3
        }
    ]
    
    for t in topics_s2:
        Topic.objects.create(stage=stage2, **t)
    print(f"   ✨ Added {len(topics_s2)} topics to Stage 2")


    # ==========================================
    # STAGE 3: DATABASE DESIGN
    # ==========================================
    stage3 = Stage.objects.create(
        roadmap=roadmap,
        title='Database Design',
        description='Structure your data for scalability and integrity.',
        order=3,
        is_free=False
    )
    
    topics_s3 = [
        {
            'title': 'Relationships (One-to-One, Many-to-Many)',
            'content': """# Defining Relationships

## 1. One-to-One (1:1)
**User <-> Profile**
- One User has one Profile.
- One Profile belongs to one User.
- **Design**: Put `user_id` (Unique) in the Profile table.

## 2. One-to-Many (1:N)
**User <-> Orders**
- One User can have Many Orders.
- One Order belongs to One User.
- **Design**: Put `user_id` (Foreign Key) in the **Orders** (Many side) table.

## 3. Many-to-Many (N:M)
**Students <-> Courses**
- One Student takes Many Courses.
- One Course has Many Students.
- **Design**: You need a **Junction Table** (e.g., `Enrollments`).
    - `student_id`
    - `course_id`

## Foreign Keys (Constraint)
Always use Foreign Key constraints!
It prevents "Orphaned Data".
- You cannot delete a User if they still have Orders (unless `ON DELETE CASCADE` is set).
""",
            'order': 1
        },
        {
            'title': 'Normalization Basics',
            'content': """# Normalization: Organizing Data

The goal: **Reduce Redundancy**.

## The Messy Way (Unnormalized)
Table `Orders`:
| OrderID | CustomerName | CustomerAddress | Product |
|---------|--------------|-----------------|---------|
| 1       | John         | 123 Main St     | iPhone  |
| 2       | John         | 123 Main St     | Case    |

**Problem**: If John moves to "456 Oak St", we have to update TWO rows. If we miss one, data is inconsistent.

## The Clean Way (Normalized)
Split into two tables.

Table `Customers`:
| ID | Name | Address |
|----|------|---------|
| 1  | John | 123 Main St |

Table `Orders`:
| OrderID | CustomerID | Product |
|---------|------------|---------|
| 1       | 1          | iPhone  |
| 2       | 1          | Case    |

**Benefit**: Update address in ONE place.
""",
            'order': 2
        }
    ]
    
    for t in topics_s3:
        Topic.objects.create(stage=stage3, **t)
    print(f"   ✨ Added {len(topics_s3)} topics to Stage 3")


    # ==========================================
    # STAGE 4: INDUSTRY USAGE
    # ==========================================
    stage4 = Stage.objects.create(
        roadmap=roadmap,
        title='Industry Usage',
        description='Performance, Indexing, and backend integration.',
        order=4,
        is_free=False
    )
    
    topics_s4 = [
        {
            'title': 'Indexing Basics',
            'content': """# Indexing: The Performance Key

## The Problem
Scanning 1 million rows to find `email = "test@gmail.com"` takes time (O(N)).

## The Solution: Index
An Index is a data structure (B-Tree) that points to the data. It's like the **Index at the back of a book**.
Instead of reading every page, you look up the word and go to the page number (O(log N)).

## Real Example
```sql
-- Slow (Full Table Scan)
SELECT * FROM users WHERE phone_number = '9876543210';

-- Add Index
CREATE INDEX idx_phone ON users(phone_number);

-- Fast (Index Scan)
SELECT * FROM users WHERE phone_number = '9876543210';
```

## The Trade-off
Indexes make **Reads FASTER** but **Writes SLOWER**.
(Because every time you `INSERT`, the database has to update the table AND the index).
**Rule**: Index columns you frequently SEARCH or JOIN on. Don't index everything.
""",
            'order': 1
        },
        {
            'title': 'Common Performance Mistakes',
            'content': """# N+1 Query Problem (The Backend Killer)

This happens in backend code (Django/Hibernate) more than raw SQL.

## Scenario
You want to display 10 orders and the user for each.

```python
# Bad Code
orders = Order.objects.all()[:10]  # 1 Query
for order in orders:
    print(order.user.name)         # 10 Queries! (One for each order)
```
Total Queries: 11.
If you load 1000 orders, you do 1001 queries. Server crashes.

## Solution: Eager Loading (JOIN)
Fetch everything in 1 query.

```python
# Django: select_related
orders = Order.objects.select_related('user').all()[:10]
```
Under the hood, this does a SQL `JOIN`.

## Other Mistakes
1.  `SELECT *`: Asking for all columns when you only need `name`. Wastes bandwidth.
2.  **Missing Indexes**: The #1 cause of slow apps.
3.  **Calculations in DB**: `SELECT * FROM orders WHERE Year(date) = 2023`. This prevents using the index on `date`. Be careful!
""",
            'order': 2
        }
    ]
    
    for t in topics_s4:
        Topic.objects.create(stage=stage4, **t)
    print(f"   ✨ Added {len(topics_s4)} topics to Stage 4")

    # Update stats
    roadmap.update_stats()
    print("✅ Roadmap creation complete! Stats updated.")

if __name__ == '__main__':
    create_sql_roadmap()
