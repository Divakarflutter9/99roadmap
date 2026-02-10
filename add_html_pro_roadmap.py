
import os
import django
import sys

# Add project root to sys.path
sys.path.append('/Users/saitejakaki/Divakar/devaproject')

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import Roadmap, RoadmapCategory, Stage, Topic

def create_html_pro_roadmap():
    """Create Professional HTML & Semantics Roadmap"""
    
    print("🚀 Initializing Professional HTML Roadmap Creation...")
    
    # 1. Get or Create Category
    # 'frontend-development' or 'development' if specific one not exists.
    # checking categories... 'Development' exists.
    category, _ = RoadmapCategory.objects.get_or_create(
        slug='development',
        defaults={'name': 'Development'}
    )
    
    # 2. Create Roadmap
    roadmap_slug = 'html-professional-mastery'
    roadmap_title = 'Professional HTML & Semantics'
    
    roadmap, created = Roadmap.objects.get_or_create(
        slug=roadmap_slug,
        defaults={
            'title': roadmap_title,
            'short_description': 'Master industry-standard HTML. Semantic structure, SEO auditing, Accessibility (WCAG), and modern integration patterns.',
            'description': 'Stop writing `<div>` soup. Learn how senior engineers structure web applications for scalability, maximizing SEO, and ensuring accessibility compliance.',
            'category': category,
            'difficulty': 'intermediate',
            'estimated_hours': 40,
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
    # STAGE 1: HTML CORE FOUNDATIONS (FREE)
    # ==========================================
    stage1 = Stage.objects.create(
        roadmap=roadmap,
        title='HTML Core Foundations',
        description='Understanding HTML’s real role in professional systems.',
        order=1,
        is_free=True
    )
    
    topics_s1 = [
        {
            'title': 'Role of HTML in Web Applications',
            'content': """# HTML: The Content Backbone

## What Problem It Solves
- Defines **Meaning** and **Structure** of data, not just appearance.
- Provides hooks for CSS (styling) and JS (interactivity).

## Content Handled
- Text (Headings, Paragraphs)
- Media (Images, Videos)
- Interactive Controls (Buttons, Inputs)

## Industry Reality
- **Senior Dev**: Thinks in terms of "Document Outline" and "Component Hierarchy".
- **Junior Dev**: Thinks in terms of "putting things on screen".
- **Rule**: If you turn off CSS, the page should still be readable and logical.
""",
            'order': 1
        },
        {
            'title': 'Browser Rendering Basics',
            'content': """# From Code to Pixels

## The Process (Quick Overview)
1.  **Parse HTML**: Browser reads bytes -> Text -> Tokenization -> DOM Trees.
2.  **DOM Tree**: The "Object Model" that JS interacts with.
3.  **Render Tree**: Combined with CSSOM (CSS Object Model). Hidden elements (`display: none`) are removed here.
4.  **Layout**: Calculating geometry (width, height, position).
5.  **Paint**: Filling in pixels.

## Why It Matters
- **Performance**: Large HTML DOM trees slow down "Layout" and "Paint".
- **JS interaction**: If HTML is malformed, the DOM tree is unpredictable.
""",
            'order': 2
        }
    ]
    
    for t in topics_s1:
        Topic.objects.create(stage=stage1, **t)
    print(f"   ✨ Added {len(topics_s1)} topics to Stage 1")


    # ==========================================
    # STAGE 2: PROFESSIONAL HTML STRUCTURE
    # ==========================================
    stage2 = Stage.objects.create(
        roadmap=roadmap,
        title='Professional HTML Structure',
        description='Write clean, maintainable markup.',
        order=2,
        is_free=False
    )
    
    topics_s2 = [
        {
            'title': 'Semantic HTML Patterns',
            'content': """# Semantic Markup: Meaning over Appearance

## Why Semantics?
- **SEO**: Google bots understand `<article>` is content, `<nav>` is links.
- **Accessibility**: Screen readers jump to `<main>` or `<footer>`.
- **Maintainability**: `<header>` is clearer than `<div class="top-bar">`.

## Common Elements & Usage
- `<main>`: The primary unique content of the page. (Use once per page).
- `<article>`: Self-contained content (Blog post, Product card).
    - *Data*: Heading, Author, Date, Body.
- `<section>`: Thematic grouping of content.
    - *Data*: Usually has a Heading (`<h2>`).
- `<aside>`: Indirectly related content (Sidebar, Ad, "Read Also").
- `<nav>`: Major navigation blocks.

## Real World Example (Blog Page)
```html
<body>
  <header>Logo + Nav</header>
  <main>
    <article>
      <h1>Blog Title</h1>
      <p>Content...</p>
    </article>
    <aside>Author Bio</aside>
  </main>
  <footer>Copyright</footer>
</body>
```
""",
            'order': 1
        },
        {
            'title': 'Document Flow & Hierarchy',
            'content': """# Controlling the Flow

## Block vs Inline
- **Block**: Takes full width. Starts new line. (div, p, h1, section).
- **Inline**: Takes necessary width. Flows with text. (span, a, strong, em).
- **Implication**: Do NOT put Block elements inside Inline elements (e.g., `<a><div>...</div></a>` is invalid in older specs, though HTML5 allows it for whole-card links, it breaks text flow).

## Heading Hierarchy (h1-h6)
- **Problem Solved**: Creates a Table of Contents for bots/screen readers.
- **Rule 1**: Only ONE `<h1>` per page (The main title).
- **Rule 2**: Don't skip levels (h2 -> h4 is bad).
- **Rule 3**: Don't use headings just for font size. Use CSS.
""",
            'order': 2
        }
    ]
    
    for t in topics_s2:
        Topic.objects.create(stage=stage2, **t)
    print(f"   ✨ Added {len(topics_s2)} topics to Stage 2")


    # ==========================================
    # STAGE 3: FORMS & DATA HANDLING
    # ==========================================
    stage3 = Stage.objects.create(
        roadmap=roadmap,
        title='Forms & Data Handling',
        description='Handling user input professionally.',
        order=3,
        is_free=False
    )
    
    topics_s3 = [
        {
            'title': 'Forms & Input Types',
            'content': """# Capturing User Data

## The <form> Element
- **Data Handled**: User inputs to be sent to a server.
- **Key Attributes**:
    - `action`: URL to send data to.
    - `method`: `GET` (search) or `POST` (create/update).

## Input Types & Mobile UX
- `type="email"`: Triggers email keyboard on mobile.
- `type="tel"`: Triggers number pad.
- `type="date"`: Triggers native date picker.
- **Lesson**: Choosing the right type improves UX significantly without JS.

## Labels are Mandatory
- **Bad**: `<div>Name: <input type="text"></div>` (Screen reader sees "Input", doesn't know it's for Name).
- **Good**: `<label for="n">Name</label> <input id="n" type="text">`
""",
            'order': 1
        },
        {
            'title': 'Validation & Accessibility',
            'content': """# Validating Data at Source

## HTML5 Validation
- **What**: Browser-level checking before data leaves.
- **Attributes**:
    - `required`: Must be filled.
    - `pattern="[A-Za-z]{3}"`: Regex check.
    - `min="0"`, `max="100"`: Range check.
- **Why**: Saves server resources. Instant feedback.

## Accessibility (A11y)
- **Problem**: How does a blind user know an input has an error?
- **ARIA**: `aria-invalid="true"`, `aria-describedby="error-msg"`.
- **Focus Management**: When error occurs, move focus to the input.
""",
            'order': 2
        }
    ]
    
    for t in topics_s3:
        Topic.objects.create(stage=stage3, **t)
    print(f"   ✨ Added {len(topics_s3)} topics to Stage 3")


    # ==========================================
    # STAGE 4: SEO, ACCESSIBILITY & PERFORMANCE
    # ==========================================
    stage4 = Stage.objects.create(
        roadmap=roadmap,
        title='SEO, Accessibility & Performance',
        description='Making HTML production-ready.',
        order=4,
        is_free=False
    )
    
    topics_s4 = [
        {
            'title': 'SEO-Friendly Markup',
            'content': """# Speaking to Search Engines

## Meta Tags
- **Title**: The blue link in Google results. (< 60 chars).
- **Description**: The snippet below the link. (High CTR).
- **Robots**: `<meta name="robots" content="noindex">` (Hide from Google).

## Open Graph (Social SEO)
- **What**: Controls how links look on Facebook/Twitter/LinkedIn.
- `og:image`: The thumbnail.
- `og:title`: The headline.
- **Why**: Bad preview = No clicks.

## Canonical Links
- **Problem**: `site.com` and `site.com?ref=twitter` are duplicate content.
- **Fix**: `<link rel="canonical" href="https://site.com">`.
""",
            'order': 1
        },
        {
            'title': 'Performance Considerations',
            'content': """# HTML that Loads Fast

## Resources Blocking Render
- **CSS**: Put `<link rel="stylesheet">` in `<head>`. (Render blocking, but good prevents FOUC).
- **JS**: Put `<script>` at end of `<body>` OR use `defer`/`async`.
    - `async`: Download parallel, execute when ready (Good for Analytics).
    - `defer`: Download parallel, execute after HTML parse (Good for UI code).

## Image Optimization
- Use `loading="lazy"` for images below the fold.
- Use `srcset` for responsive images (serve small jpg to mobile).
- Specify `width` and `height` to prevent Cumulative Layout Shift (CLS).
""",
            'order': 2
        }
    ]
    
    for t in topics_s4:
        Topic.objects.create(stage=stage4, **t)
    print(f"   ✨ Added {len(topics_s4)} topics to Stage 4")


    # ==========================================
    # STAGE 5: MODERN FRONTEND ECOSYSTEM
    # ==========================================
    stage5 = Stage.objects.create(
        roadmap=roadmap,
        title='HTML in Modern Ecosystem',
        description='HTML inside React, Angular, and Components.',
        order=5,
        is_free=False
    )
    
    topics_s5 = [
        {
            'title': 'HTML in React (JSX)',
            'content': """# Component-Based HTML

## The Shift
- **Old**: HTML file + Separate JS file.
- **New (React/Vue)**: JS file generates HTML (JSX).

## Key Differences
- `class` -> `className` (JS keyword conflict).
- `for` -> `htmlFor`.
- **Components as Custom Tags**:
    `<Button variant="primary" />` renders to `<button class="btn btn-primary">`.

## Maintaining Semantics
- **Mistake**: Making everything a `<div>` because "Components wrap things".
- **Fix**: Use `React.Fragment` (`<>...</>`) to avoid extra divs in DOM.
""",
            'order': 1
        },
        {
            'title': 'Interview Expectations',
            'content': """# What they ask Senior Frontend Engineers

## 1. Do you know Semantic HTML?
- Q: "Structure a blog post page."
- Expect: Header, Nav, Main, Article, Aside, Footer.

## 2. Accessibility
- Q: "How to make a custom dropdown accessible?"
- Expect: Keyboard navigation (Enter/Space), ARIA roles.

## 3. SEO
- Q: "How to improve CTR on Google?"
- Expect: Meta descriptions, Schema.org markup.

## 4. Performance
- Q: "What is Critical Rendering Path?"
- Expect: HTML -> DOM -> Render Tree -> Layout -> Paint.
""",
            'order': 2
        }
    ]
    
    for t in topics_s5:
        Topic.objects.create(stage=stage5, **t)
    print(f"   ✨ Added {len(topics_s5)} topics to Stage 5")

    # Update stats
    roadmap.update_stats()
    print("✅ Professional HTML Roadmap creation complete! Stats updated.")

if __name__ == '__main__':
    create_html_pro_roadmap()
