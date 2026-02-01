
import os
import django
import sys

# Setup settings
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import Roadmap, Stage, Topic, RoadmapCategory
from django.utils.text import slugify

def create_roadmap():
    print("🚀 Creating React Advanced Roadmap...")

    # 1. Get or Create Category
    category, _ = RoadmapCategory.objects.get_or_create(
        name="Development",
        defaults={
            'slug': 'development',
            'description': 'Software Development Roadmaps',
            'icon': 'fa-code',
            'color': '#3b82f6'
        }
    )

    # 2. Create Roadmap
    title = "Advanced Frontend (React.js)"
    slug = "react-advanced"
    
    # Check if exists
    if Roadmap.objects.filter(slug=slug).exists():
        print(f"⚠️ Roadmap '{title}' already exists. Skipping.")
        return

    roadmap = Roadmap.objects.create(
        title=title,
        slug=slug,
        description="A professional Advanced Frontend roadmap using React.js for CSE / BTech students who already know HTML, CSS, and JavaScript. Focuses on real industry skills.",
        short_description="Master React.js for real-world frontend engineering.",
        category=category,
        difficulty='intermediate',
        is_premium=False,
        price=699,
        estimated_hours=60,
        is_active=True,
        is_featured=True
    )

    # 3. Create Stages & Topics
    stages_data = [
        {
            "title": "React Foundations",
            "description": "Understand React mindset",
            "is_free": True,
            "order": 1,
            "topics": [
                {
                    "title": "Why React Exists?",
                    "content": """
**Goal:** Understand the problem React solves.

*   **The Old Way:** Updating DOM manually (`document.getElementById`) is slow and messy in big apps.
*   **The React Way:** Declarative UI. You tell React "What it should look like based on data", and React handles the DOM updates.
*   **SPA (Single Page Application):** No page reloads. Just data fetching and UI updates.
                    """,
                    "duration": 20
                },
                {
                    "title": "Component-Based Thinking",
                    "content": """
**Goal:** Breaking UI into Lego blocks.

*   **Atomic Design:** Button -> SearchBar -> Header -> Layout.
*   **Reusability:** Write once, use everywhere (e.g., a `<Button />` component).
*   **Isolation:** A bug in the Sidebar shouldn't crash the Activity Feed.
                    """,
                    "duration": 25
                },
                {
                    "title": "JSX Fundamentals",
                    "content": """
**Goal:** Writing HTML-like syntax in JavaScript.

*   **It's not HTML:** It's syntactic sugar for `React.createElement`.
*   **Differences:** `className` instead of `class`, `htmlFor` instead of `for`.
*   **Expressions:** Embedding JS logic inside `{}` curly braces.
                    """,
                    "duration": 30
                },
                {
                    "title": "Props vs State",
                    "content": """
**Goal:** Managing Data.

*   **Props (Properties):** Read-only data passed *down* from parent to child (like arguments to a function).
*   **State:** Memory of a component. Data that *changes* over time (like user input, open/close toggle).
*   **Rule of Thumb:** If a parent controls it, use Props. If the component controls it, use State.
                    """,
                    "duration": 35
                }
            ]
        },
        {
            "title": "Core React Development",
            "description": "Build real frontend applications",
            "is_free": False,
            "order": 2,
            "topics": [
                {
                    "title": "Functional Components",
                    "content": """
**Goal:** Modern React coding.

*   **Functions vs Classes:** Why the industry moved to Functions (Cleaner, Hooks support).
*   **The Render Cycle:** A function component runs every time its props or state change.
*   **Return Value:** A Component essentially returns a UI View (JSX).
                    """,
                    "duration": 30
                },
                {
                    "title": "Hooks Fundamentals (useState, useEffect)",
                    "content": """
**Goal:** Giving superpowers to functions.

*   **useState:** "Remember this value across renders". `const [count, setCount] = useState(0)`.
*   **useEffect:** "Do something *after* render". (Fetching data, Subscribing to events, Changing document title).
*   **Dependency Array:** Controlling *when* the effect runs (`[]` = mount only, `[prop]` = when prop changes).
                    """,
                    "duration": 60
                },
                {
                    "title": "Conditional Rendering & Lists",
                    "content": """
**Goal:** Dynamic UIs.

*   **Ternary Operators:** `isLoggedIn ? <Admin /> : <Login />` (Better than `if/else`).
*   **Short Circuit:** `isLoading && <Spinner />`.
*   **Lists:** Using `.map()` to turn data arrays into UI lists.
*   **Keys:** Why React needs a unique `key` prop for lists (Performance & State preservation).
                    """,
                    "duration": 45
                }
            ]
        },
        {
            "title": "State Management & Data Flow",
            "description": "Handle complex UI logic",
            "is_free": False,
            "order": 3,
            "topics": [
                {
                    "title": "Lifting State Up",
                    "content": """
**Goal:** Sharing data between siblings.

*   **The Problem:** Sibling A cannot talk to Sibling B directly.
*   **The Pattern:** Move state to the Common Component (Parent). Pass data down via Props.
*   **One-Way Data Flow:** Data always flows *down*. Events flow *up*.
                    """,
                    "duration": 40
                },
                {
                    "title": "Context API",
                    "content": """
**Goal:** avoiding Prop Drilling.

*   **Prop Drilling:** Passing specific data through 5 layers of components that don't need it.
*   **Context:** A "Teleportation" mechanism. Provide data at the top, Consume it anywhere below.
*   **Use Cases:** Themes (Dark Mode), User Auth status, Language settings.
                    """,
                    "duration": 50
                },
                {
                    "title": "Managing Side Effects",
                    "content": """
**Goal:** Keeping components pure.

*   **Pure Functions:** Input -> Output. No side effects.
*   **Side Effects:** API calls, DOM manipulation, Timers.
*   **Cleanup Function:** Returning a function from `useEffect` to clean up functionality (e.g., clearing intervals) to prevent memory leaks.
                    """,
                    "duration": 45
                }
            ]
        },
        {
            "title": "API Integration & Performance",
            "description": "Build production-ready apps",
            "is_free": False,
            "order": 4,
            "topics": [
                {
                    "title": "API Calls & Async Handling",
                    "content": """
**Goal:** Talking to the backend.

*   **Where to fetch?** Inside `useEffect`.
*   **Loading States:** Showing skeletons/spinners while waiting.
*   **Error Handling:** What if the server crashes? (Try/Catch + Error UI).
*   **Custom Hooks:** Extracting fetching logic into `useFetch` for reuse.
                    """,
                    "duration": 55
                },
                {
                    "title": "Performance Optimization Basics",
                    "content": """
**Goal:** Fast apps.

*   **Re-renders:** Understanding why a component updates.
*   **Memoization:** `React.memo` (Don't re-render if props didn't change).
*   **useMemo & useCallback:** Caching heavy calculations and function references.
*   **Code Splitting:** `React.lazy` (Don't load the Settings page code until user clicks Settings).
                    """,
                    "duration": 60
                }
            ]
        },
        {
            "title": "Industry-Ready Frontend Skills",
            "description": "Become job-ready",
            "is_free": False,
            "order": 5,
            "topics": [
                {
                    "title": "Folder Structure & Scalability",
                    "content": """
**Goal:** Organizing code like a pro.

*   **Grouping by Feature:** `/components`, `/hooks`, `/pages`, `/services`, `/utils`.
*   **Index Files:** Clean imports.
*   **Separation of Concerns:** Logic in hooks, UI in components.
                    """,
                    "duration": 30
                },
                {
                    "title": "Debugging & Quality",
                    "content": """
**Goal:** Professional workflow.

*   **React DevTools:** Inspecting Component hierarchy and State.
*   **Linting:** ESLint (Finding errors before running).
*   **Clean Code:** Meaningful variable names, small components, consistent formatting (Prettier).
                    """,
                    "duration": 40
                },
                {
                    "title": "Testing & Interview Prep",
                    "content": """
**Goal:** Hired.

*   **Unit Testing:** `Jest` + `React Testing Library` (Testing user interactions, not implementation details).
*   **Interview Topics:** Virtual DOM, Reconciliation, Lifecycle methods (Old vs New), Hook rules.
                    """,
                    "duration": 45
                }
            ]
        }
    ]

    for stage_data in stages_data:
        stage = Stage.objects.create(
            roadmap=roadmap,
            title=stage_data['title'],
            description=stage_data['description'],
            is_free=stage_data['is_free'],
            order=stage_data['order']
        )
        
        for i, topic_data in enumerate(stage_data['topics'], 1):
            Topic.objects.create(
                stage=stage,
                title=topic_data['title'],
                content=topic_data['content'],
                content_type='text',
                order=i,
                duration_minutes=topic_data['duration']
            )
            
    # Update Stats
    roadmap.update_stats()
    print(f"✅ Successfully created Roadmap: {roadmap.title}")

if __name__ == "__main__":
    create_roadmap()
