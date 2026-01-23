import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import Roadmap, Stage, Topic

def create_web_dev_roadmap():
    print("Creating Web Development Roadmap...")
    
    # Check if exists
    if Roadmap.objects.filter(slug='web-development').exists():
        print("Roadmap already exists!")
        return

    # Create Roadmap
    roadmap = Roadmap.objects.create(
        title="Web Development",
        slug="web-development",
        description="Master Full Stack Web Development from scratch. Learn HTML, CSS, JavaScript, React, and Django.",
        is_premium=False
    )
    
    # Stage 1: Fundamentals (HTML & CSS)
    stage1 = Stage.objects.create(
        roadmap=roadmap,
        title="Frontend Fundamentals",
        description="Build the skeleton and skin of websites using HTML and CSS.",
        order=1,
        is_free=True,
        required_xp=0,
        xp_reward=100
    )
    
    Topic.objects.create(
        stage=stage1,
        title="HTML Basics",
        content="""HTML (HyperText Markup Language) is the standard markup language for documents designed to be displayed in a web browser.
        
Key Concepts:
1. Tags and Elements: Content is wrapped in tags like <h1>, <p>, <div>.
2. Structure: Every page has <html>, <head>, and <body>.
3. Attributes: Tags can have attributes like 'class', 'id', 'src', 'href'.
""",
        order=1,
        duration_minutes=30,
        xp_reward=20
    )

    Topic.objects.create(
        stage=stage1,
        title="CSS Styling",
        content="""CSS (Cascading Style Sheets) describes how HTML elements are to be displayed.
        
Key Concepts:
1. Selectors: Target elements by tag, class (.), or id (#).
2. Box Model: Content, Padding, Border, Margin.
3. Flexbox & Grid: Modern layout techniques for responsive design.
""",
        order=2,
        duration_minutes=45,
        xp_reward=30
    )
    
    Topic.objects.create(
        stage=stage1,
        title="Responsive Design",
        content="""Responsive design ensures your web pages look good on all devices.
        
Key Concepts:
1. Viewport Meta Tag: Controls layout on mobile browsers.
2. Media Queries: Apply CSS based on device width (@media).
3. Fluid Layouts: Using percentages instead of fixed pixels.
""",
        order=3,
        duration_minutes=40,
        xp_reward=30
    )

    # Stage 2: JavaScript Mastery
    stage2 = Stage.objects.create(
        roadmap=roadmap,
        title="JavaScript Mastery",
        description="Add interactivity and logic to your web pages.",
        order=2,
        is_free=False,
        required_xp=100,
        xp_reward=200
    )
    
    Topic.objects.create(
        stage=stage2,
        title="Variables and Data Types",
        content="""JavaScript is the programming language of the web.
        
Key Concepts:
1. Variables: let, const, var.
2. Data Types: String, Number, Boolean, Array, Object.
3. Operators: Arithmetic (+, -), Comparison (===, !==), Logical (&&, ||).
""",
        order=1,
        duration_minutes=45,
        xp_reward=40
    )
    
    Topic.objects.create(
        stage=stage2,
        title="DOM Manipulation",
        content="""The DOM (Document Object Model) represents the page so code can change structure, style, and content.
        
Key Concepts:
1. Selecting Elements: document.querySelector(), document.getElementById().
2. Events: click, submit, change, hover.
3. Manipulation: element.innerHTML, element.style, element.classList.
""",
        order=2,
        duration_minutes=60,
        xp_reward=50
    )

    Topic.objects.create(
        stage=stage2,
        title="Fetch API & Async/Await",
        content="""Modern websites need to fetch data from servers without reloading.
        
Key Concepts:
1. Promises: Handling asynchronous operations.
2. Async/Await: Syntactic sugar for cleaner async code.
3. Fetch API: Making HTTP requests to APIs.
""",
        order=3,
        duration_minutes=60,
        xp_reward=60
    )

    # Stage 3: Backend with Python
    stage3 = Stage.objects.create(
        roadmap=roadmap,
        title="Backend Development",
        description="Server-side programming, databases, and APIs using Python.",
        order=3,
        is_free=False,
        required_xp=300,
        xp_reward=300
    )
    
    Topic.objects.create(
        stage=stage3,
        title="Introduction to HTTP",
        content="""Understanding how the web works is crucial for backend development.
        
Key Concepts:
1. Request/Response Cycle: Client sends request, Server sends response.
2. HTTP Methods: GET, POST, PUT, DELETE.
3. Status Codes: 200 (OK), 404 (Not Found), 500 (Server Error).
""",
        order=1,
        duration_minutes=30,
        xp_reward=50
    )
    
    Topic.objects.create(
        stage=stage3,
        title="Databases & SQL",
        content="""Databases store application data persistently.
        
Key Concepts:
1. Relational vs NoSQL: Tables vs Documents.
2. SQL: Structured Query Language for managing data.
3. ORM: Object-Relational Mapping (interacting with DB using code).
""",
        order=2,
        duration_minutes=60,
        xp_reward=60
    )

    print("Web Development Roadmap Created Successfully!")

if __name__ == "__main__":
    create_web_dev_roadmap()
