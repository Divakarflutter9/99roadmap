"""
Add Node.js Backend Development Roadmap
Complete roadmap for BTech/CSE students to become industry-ready Node.js backend developers
"""

import os
import django
import sys

sys.path.append('/Users/saitejakaki/Divakar/devaproject')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import Roadmap, RoadmapCategory, Stage, Topic

def create_nodejs_backend_roadmap():
    """Create comprehensive Node.js Backend Development roadmap"""
    
    # Get Backend category
    category = RoadmapCategory.objects.get(slug='backend-development')
    
    # Create roadmap
    roadmap, created = Roadmap.objects.get_or_create(
        slug='nodejs-backend-development',
        defaults={
            'title': 'Node.js Backend Development',
            'short_description': 'Complete Node.js backend roadmap - from basics to building production-ready APIs with Express.js',
            'description': 'Master Node.js backend development from scratch. Learn Express.js, REST APIs, databases, authentication, and deployment. Perfect for students aiming for JavaScript backend roles.',
            'category': category,
            'difficulty': 'intermediate',
            'estimated_hours': 160,
            'is_premium': True,
            'is_featured': True,
            'is_active': True
        }
    )
    
    if created:
        print(f"✅ Created roadmap: {roadmap.title}")
    else:
        print(f"ℹ️  Roadmap already exists: {roadmap.title}")
        roadmap.stages.all().delete()
        print("   Deleted existing stages to recreate")
    
    # Stage 1: Backend Foundations (FREE)
    stage1 = Stage.objects.create(
        roadmap=roadmap,
        title='Backend Foundations',
        description='Understand backend development and how Node.js powers modern JavaScript applications',
        order=1,
        is_free=True
    )
    
    stage1_topics = [
        {
            'title': 'What is Backend Development?',
            'content': """# What is Backend Development?

## Backend vs Frontend

**Frontend (Client-side)**
- What users see and interact with
- HTML, CSS, JavaScript in browser
- React, Angular, Vue frameworks
- Runs on user's device

**Backend (Server-side)**
- Business logic and data processing
- Database operations
- Authentication and security
- APIs that frontend consumes
- Runs on servers (cloud/data centers)

## Real-World Example: YouTube

### Frontend
- Video player interface
- Comment section UI
- Like/dislike buttons
- Recommendation sidebar

### Backend
- Video upload processing
- Video storage and streaming
- Comment storage in database
- Recommendation algorithm
- User authentication
- View count tracking

## What Backend Handles

### 1. Data Management
- Store user data, videos, comments
- Retrieve data when requested
- Update information (profile edits)
- Delete data when needed

### 2. Business Logic
```javascript
// Backend decides if user can upload video
function canUploadVideo(user) {
    if (!user.isVerified) {
        return {allowed: false, reason: "Email not verified"};
    }
    if (user.uploadedToday >= 10) {
        return {allowed: false, reason: "Daily limit reached"};
    }
    if (videoSize > user.maxUploadSize) {
        return {allowed: false, reason: "File too large"};
    }
    return {allowed: true};
}
```

### 3. API Creation
Backend exposes **endpoints** that frontend calls:

```
GET  /api/videos          → Get video list
POST /api/videos          → Upload new video
GET  /api/videos/123      → Get specific video
PUT  /api/videos/123      → Update video
DELETE /api/videos/123    → Delete video
```

### 4. Security
- Password hashing (never store plain text!)
- JWT tokens for authentication
- Data validation
- Rate limiting (prevent abuse)
- CORS configuration

## Backend Technologies Stack

**Language**: JavaScript (Node.js)
**Framework**: Express.js
**Database**: MongoDB, PostgreSQL, MySQL
**Authentication**: JWT, Passport.js
**Deployment**: AWS, Heroku, DigitalOcean

## Why Backend is Critical

- Apps are useless without data
- Backend handles millions of concurrent users
- Protects sensitive information
- Implements core business logic
- Scales to serve global audience

## Key Takeaway
Backend is the **engine** that powers applications. Frontend is the car body you see, backend is the engine that makes it work!
""",
            'order': 1
        },
        {
            'title': 'Client-Server Architecture',
            'content': """# Client-Server Architecture

## How Web Apps Work

The **client-server model** is fundamental to understanding backend development.

## Components

### Client (Frontend)
- User's browser or mobile app
- Sends HTTP requests
- Displays responses
- Examples: Chrome, Safari, React Native app

### Server (Backend)
- Always running on cloud servers
- Processes requests
- Interacts with database
- Sends responses
- Examples: Node.js + Express server

### Database
- Stores data permanently
- MySQL, PostgreSQL (SQL)
- MongoDB (NoSQL)
- Connected to backend server

## Request-Response Flow

```
User clicks "Login"
    ↓
Browser sends POST request
    ↓
Internet (HTTP)
    ↓
Node.js Server receives request
    ↓
Server validates credentials in database
    ↓
Server creates JWT token
    ↓
Response sent back to browser
    ↓
Browser stores token, shows dashboard
```

## Real Example: E-Commerce Checkout

**User Action**: Click "Place Order"

1. **Frontend (Client)**
   - Collects order data
   - Sends POST request:
   ```javascript
   fetch('/api/orders', {
       method: 'POST',
       headers: {'Content-Type': 'application/json'},
       body: JSON.stringify({
           items: cartItems,
           totalAmount: 5000,
           paymentMethod: 'card'
       })
   })
   ```

2. **Backend (Node.js Server)**
   ```javascript
   app.post('/api/orders', (req, res) => {
       // Validate items
       const {items, totalAmount} = req.body;
       
       // Check inventory
       if (!checkStock(items)) {
           return res.status(400).json({error: "Out of stock"});
       }
       
       // Process payment
       const payment = processPayment(totalAmount);
       
       // Save order to database
       const order = db.orders.create({
           userId: req.user.id,
           items,
           total: totalAmount,
           status: 'confirmed'
       });
       
       // Send email confirmation
       sendEmail(req.user.email, order);
       
       res.status(201).json({
           message: "Order placed successfully",
           orderId: order.id
       });
   });
   ```

3. **Database**
   - Stores order details
   - Updates inventory
   - Records transaction

## Why This Architecture?

### Separation of Concerns
- Frontend: UI/UX expertise
- Backend: Business logic and data
- Database: Data storage and retrieval

### Scalability
- One backend serves millions of clients
- Add more servers when traffic increases
- Database can scale independently

### Security
- Sensitive logic stays on server (hidden from users)
- Database not exposed to internet
- Easier to monitor and protect

## Multiple Clients, One Backend

Same Node.js backend can serve:
- Web app (React)
- Mobile app (React Native)
- Desktop app (Electron)
- Third-party integrations (APIs)

## Key Takeaway
Client-server is like a **restaurant**: 
- **Client** = Customer (orders food)
- **Backend** = Kitchen (prepares food)
- **Database** = Storage room (ingredients)
""",
            'order': 2
        },
        {
            'title': 'HTTP Request-Response Cycle',
            'content': """# HTTP Request-Response Cycle

## What is HTTP?

**HTTP (HyperText Transfer Protocol)** is how browsers and servers communicate.

## HTTP Methods (Verbs)

| Method | Purpose | Example |
|--------|---------|---------|
| **GET** | Retrieve data | Get user profile |
| **POST** | Create data | Register new user |
| **PUT/PATCH** | Update data | Edit profile |
| **DELETE** | Remove data | Delete post |

## HTTP Request Structure

### 1. Request Line
```
POST /api/users/login HTTP/1.1
```

### 2. Headers (Metadata)
```
Content-Type: application/json
Authorization: Bearer eyJhbGc...
User-Agent: Mozilla/5.0
```

### 3. Body (Data for POST/PUT)
```json
{
  "email": "john@example.com",
  "password": "securepass123"
}
```

## HTTP Response Structure

### 1. Status Line
```
HTTP/1.1 200 OK
```

### 2. Response Headers
```
Content-Type: application/json
Set-Cookie: token=abc123; HttpOnly
```

### 3. Response Body
```json
{
  "success": true,
  "user": {
    "id": 123,
    "name": "John Doe",
    "email": "john@example.com"
  },
  "token": "eyJhbGc..."
}
```

## HTTP Status Codes (Must Know!)

### Success (2xx)
- **200 OK**: Request successful
- **201 Created**: Resource created
- **204 No Content**: Success, no data to return

### Client Errors (4xx)
- **400 Bad Request**: Invalid data
- **401 Unauthorized**: Login required
- **403 Forbidden**: No permission
- **404 Not Found**: Resource doesn't exist
- **422 Unprocessable Entity**: Validation failed

### Server Errors (5xx)
- **500 Internal Server Error**: Backend crashed
- **503 Service Unavailable**: Server down

## Node.js Request-Response Example

```javascript
const express = require('express');
const app = express();

app.get('/api/users/:id', (req, res) => {
    // req = request object
    // res = response object
    
    const userId = req.params.id;  // Get URL parameter
    
    // Find user
    const user = database.findUser(userId);
    
    if (!user) {
        // Return 404
        return res.status(404).json({
            error: "User not found"
        });
    }
    
    // Return 200 with user data
    res.status(200).json({
        success: true,
        data: {
            id: user.id,
            name: user.name,
            email: user.email
        }
    });
});
```

## Request Types in Detail

### GET Request
```javascript
// Frontend
fetch('https://api.example.com/products?category=electronics')
    .then(res => res.json())
    .then(data => console.log(data));

// Backend (Node.js)
app.get('/products', (req, res) => {
    const category = req.query.category;  // 'electronics'
    const products = db.products.find({category});
    res.json({products});
});
```

### POST Request
```javascript
// Frontend
fetch('https://api.example.com/users', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
        name: 'John',
        email: 'john@example.com'
    })
});

// Backend (Node.js)
app.post('/users', (req, res) => {
    const {name, email} = req.body;
    const user = db.users.create({name, email});
    res.status(201).json({user});
});
```

## Common Patterns

### Handling Errors
```javascript
app.get('/users/:id', (req, res) => {
    try {
        const user = db.findUser(req.params.id);
        
        if (!user) {
            return res.status(404).json({error: "Not found"});
        }
        
        res.json({user});
    } catch (error) {
        res.status(500).json({error: "Server error"});
    }
});
```

### Setting Headers
```javascript
app.get('/data', (req, res) => {
    res.setHeader('X-Custom-Header', 'value');
    res.json({data: 'value'});
});
```

## Key Takeaway
HTTP is the **language** of the web. Requests are questions, responses are answers. Status codes tell you if the conversation was successful!
""",
            'order': 3
        },
        {
            'title': 'What is Node.js?',
            'content': """# What is Node.js?

## JavaScript Beyond the Browser

**Node.js is a JavaScript runtime** that lets you run JavaScript outside the browser - on servers!

Before Node.js (2009):
- ❌ JavaScript only ran in browsers
- ❌ Backend needed Java, Python, PHP, Ruby
- ❌ Developers needed to learn multiple languages

After Node.js:
- ✅ JavaScript runs on server
- ✅ Same language for frontend and backend
- ✅ Full-stack JavaScript development

## What is a "Runtime"?

A **runtime** is an environment to execute code.

- **Browser Runtime**: V8 engine (Chrome) runs JavaScript for webpages
- **Node.js Runtime**: V8 engine runs JavaScript for servers

```javascript
// This code works BOTH in browser and Node.js
const sum = (a, b) => a + b;
console.log(sum(5, 3));  // 8

// This ONLY works in Node.js (file system access)
const fs = require('fs');
fs.readFile('data.txt', 'utf8', (err, data) => {
    console.log(data);
});
```

## Why Node.js for Backend?

### 1. JavaScript Everywhere
```javascript
// Frontend (React)
function LoginButton() {
    fetch('/api/login', {
        method: 'POST',
        body: JSON.stringify({email, password})
    });
}

// Backend (Node.js) - Same language!
app.post('/api/login', (req, res) => {
    const {email, password} = req.body;
    // Authentication logic
});
```

### 2. Non-Blocking I/O (Super Fast!)

**Blocking (Traditional)**
```
Request 1 arrives → Process (wait for database) → Send response
⏳ Request 2 waits...
⏳ Request 3 waits...
```

**Non-Blocking (Node.js)**
```
Request 1 arrives → Start database query → Handle Request 2
Request 2 arrives → Start processing → Handle Request 3
Request 3 arrives → Start processing
Database returns → Send Reponse 1
```

### 3. NPM Ecosystem
- **1 million+ packages** on npm (Node Package Manager)
- Everything you need: databases, auth, testing, deployment
- Easy installation: `npm install express`

### 4. Real-Time Applications
Perfect for:
- Chat applications (WhatsApp Web)
- Live notifications
- Collaborative tools (Google Docs)
- Streaming services

## Node.js Architecture (Simple!)

```
JavaScript Code
      ↓
   V8 Engine (compiles JS to machine code)
      ↓
  Libuv (handles async operations)
      ↓
Operating System (file, network access)
```

## Real Company Examples

### Companies Using Node.js
- **Netflix**: Streams billions of hours
- **PayPal**: Payment processing
- **Uber**: Real-time ride matching
- **NASA**: Astronaut safety data
- **LinkedIn**: Backend services
- **Walmart**: E-commerce platform

## What Node.js is Good At

✅ **REST APIs**: Fast, scalable
✅ **Real-time apps**: Chat, notifications
✅ **Microservices**: Small, independent services
✅ **Data streaming**: Video, audio
✅ **I/O heavy apps**: File processing

## What Node.js is NOT Good At

❌ **CPU-intensive tasks**: Heavy calculations, video encoding
❌ **Blocking operations**: Use Python/Go for data science
❌ **When team doesn't know JavaScript**

## Installing Node.js

```bash
# Check if installed
node --version

# Run JavaScript file
node app.js

# Start interactive shell
node
> console.log("Hello from Node!")
Hello from Node!
```

## First Node.js Program

```javascript
// hello.js
console.log("Hello from Node.js!");

const greet = (name) => {
    return `Hello, ${name}!`;
};

console.log(greet("World"));
```

Run: `node hello.js`

Output:
```
Hello from Node.js!
Hello, World!
```

## Key Differences: Browser vs Node.js

| Feature | Browser | Node.js |
|---------|---------|---------|
| Purpose | Render webpages | Build servers |
| APIs | DOM, window, document | fs, http, path |
| Modules | ES6 import | require() or import |
| Use Case | User interfaces | Backend APIs |

## Key Takeaway
Node.js = **JavaScript superpowers** for backend development. Same language, different environment. Perfect for building fast, scalable APIs!
""",
            'order': 4
        },
        {
            'title': 'Where Node.js is Used in Real Applications',
            'content': """# Node.js in Production

## Real Company Use Cases

### 1. Netflix (Streaming Platform)

**Challenge**: Serve 200M+ users globally
**Node.js Solution**:
- Fast API responses
- Reduced startup time by 70%
- Handles millions of concurrent connections
- Real-time recommendations

**Tech Stack**:
- Node.js + Express for APIs
- React for frontend
- Microservices architecture

### 2. PayPal (Payment Processing)

**Before Node.js**:
- Java backend (slow development)
- Separate teams for frontend/backend
- 15+ developers, 6 months to build

**After Node.js**:
- Same team for full stack
- 5 developers, 3 months
- 35% faster page responses
- 2x faster development

### 3. Uber (Ride Sharing)

**Node.js Powers**:
- Real-time ride matching
- Driver location tracking
- Surge price calculations
- Push notifications
- Handles 20M+ rides daily

**Why Node.js**?
- Fast I/O for real-time updates
- Scales to millions of connections
- npm packages for maps, payments

### 4. LinkedIn (Professional Network)

**Migration to Node.js**:
- From Ruby on Rails to Node.js
- **20x faster** mobile API
- Traffic handled by 10 servers (was 30)
- Better resource utilization

### 5. Walmart (E-Commerce)

**Black Friday Traffic**:
- Handles 500M+ page views
- Node.js for backend APIs
- Real-time inventory updates
- Shopping cart management
- **Zero downtime** during sales

## Common Node.js Use Cases

### 1. REST APIs
```javascript
// Product API
app.get('/api/products', (req, res) => {
    const products = db.getProducts();
    res.json({products});
});

// Order API
app.post('/api/orders', (req, res) => {
    const order = createOrder(req.body);
    res.status(201).json({order});
});
```

**Companies**: Spotify, Twitter, Reddit

### 2. Real-Time Applications

**Chat Apps** (WhatsApp Web, Slack)
```javascript
const io = require('socket.io');

io.on('connection', (socket) => {
    socket.on('message', (msg) => {
        // Broadcast to all users
        io.emit('message', msg);
    });
});
```

**Live Dashboards** (Analytics, Stock Prices)
```javascript
setInterval(() => {
    const stockPrice = getLatestPrice();
    io.emit('price-update', stockPrice);
}, 1000);
```

### 3. Microservices

**Order Service**
```javascript
// orders-service.js
app.post('/orders', async (req, res) => {
    const order = await createOrder(req.body);
    
    // Call payment service
    await callService('http://payment-service/charge', orderData);
    
    // Call notification service
    await callService('http://notifications/send-email', emailData);
    
    res.json({order});
});
```

**Companies**: Netflix, Uber, Amazon

### 4. API Gateways

```javascript
// API Gateway routes requests to microservices
app.use('/users', proxy('http://user-service'));
app.use('/products', proxy('http://product-service'));
app.use('/orders', proxy('http://order-service'));
```

### 5. Server-Side Rendering

**Next.js (React SSR)**
```javascript
export async function getServerSideProps() {
    const products = await fetch('https://api.example.com/products');
    return {props: {products}};
}
```

**Benefits**:
- Better SEO (search engines see content)
- Faster initial page load
- Used by: Twitch, TikTok, Hulu

### 6. File Processing & Uploads

```javascript
const multer = require('multer');
const upload = multer({dest: 'uploads/'});

app.post('/upload', upload.single('file'), (req, res) => {
    // Process uploaded file
    const file = req.file;
    processImage(file.path);
    res.json({message: 'File uploaded'});
});
```

**Companies**: Dropbox, Google Drive clones

### 7. Authentication Services

```javascript
const jwt = require('jsonwebtoken');

app.post('/login', (req, res) => {
    const {email, password} = req.body;
    
    // Verify credentials
    const user = authenticateUser(email, password);
    
    // Generate token
    const token = jwt.sign({userId: user.id}, SECRET_KEY);
    
    res.json({token});
});
```

## Industry Adoption Statistics

- **85% of developers** use Node.js for backend
- **50M+ downloads** per week
- **Top choice for startups**: Fast development
- **Fortune 500 companies**: 43% use Node.js

## Job Market (India)

### Entry Level (0-2 years)
- **Role**: Node.js Developer, Full Stack Developer
- **Salary**: ₹4-8 LPA
- **Companies**: Startups, service companies

### Mid Level (2-5 years)
- **Role**: Senior Node.js Developer
- **Salary**: ₹8-20 LPA
- **Companies**: Flipkart, Zomato, PayTM, Swiggy

### Senior Level (5+ years)
- **Role**: Lead Engineer, Architect
- **Salary**: ₹20-40+ LPA
- **Companies**: FAANG, unicorns

## Skills Required

**Must Have**:
- JavaScript (ES6+)
- Node.js fundamentals
- Express.js framework
- MongoDB/PostgreSQL
- REST API design
- Git version control

**Good to Have**:
- TypeScript
- WebSockets
- Redis caching
- Docker containers
- AWS/GCP deployment
- Microservices

## When to Choose Node.js

**Choose Node.js if**:
✅ Building REST APIs
✅ Real-time applications
✅ I/O heavy tasks
✅ JavaScript team
✅ Fast development needed
✅ Microservices architecture

**Consider alternatives if**:
❌ CPU-intensive tasks (use Go, Rust)
❌ Existing Python/Java expertise
❌ Enterprise Java requirements

## Key Takeaway
Node.js powers **billion-user applications** like Netflix and Uber. It's fast, scalable, and perfect for modern backend development. JavaScript everywhere!
""",
            'order': 5
        }
    ]
    
    for topic_data in stage1_topics:
        Topic.objects.create(stage=stage1, **topic_data)
    print(f"✅ Stage 1: {stage1.title} - {len(stage1_topics)} topics")
    
    print("\n" + "="*60)
    print(f"✅ Stage 1 Complete! Creating remaining stages...")
    print("="*60 + "\n")
    
    roadmap.update_stats()
    return roadmap

if __name__ == '__main__':
    roadmap = create_nodejs_backend_roadmap()
    print(f"\n✅ Node.js Backend Roadmap Stage 1 Complete!")
