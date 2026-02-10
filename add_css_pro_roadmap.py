
import os
import django
import sys

# Add project root to sys.path
sys.path.append('/Users/saitejakaki/Divakar/devaproject')

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import Roadmap, RoadmapCategory, Stage, Topic

def create_css_pro_roadmap():
    """Create Professional CSS & Layouts Roadmap"""
    
    print("🚀 Initializing Professional CSS Roadmap Creation...")
    
    # 1. Get or Create Category
    category, _ = RoadmapCategory.objects.get_or_create(
        slug='development',
        defaults={'name': 'Development'}
    )
    
    # 2. Create Roadmap
    roadmap_slug = 'css-professional-mastery'
    roadmap_title = 'Professional CSS & Layouts'
    
    roadmap, created = Roadmap.objects.get_or_create(
        slug=roadmap_slug,
        defaults={
            'title': roadmap_title,
            'short_description': 'Master modern layouts (Flexbox/Grid), responsive systems, and maintainable CSS architectures.',
            'description': 'Stop guessing CSS properties. Learn the engineering behind layouts, how browsers render styles, and how to write scalable CSS for large applications.',
            'category': category,
            'difficulty': 'intermediate',
            'estimated_hours': 45,
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
    # STAGE 1: CSS FUNDAMENTALS (FREE)
    # ==========================================
    stage1 = Stage.objects.create(
        roadmap=roadmap,
        title='CSS Fundamentals',
        description='What CSS actually controls in real applications.',
        order=1,
        is_free=True
    )
    
    topics_s1 = [
        {
            'title': 'The Role of CSS',
            'content': """# More Than Just Colors

## Visual Data Control
CSS doesn't just "paint" the screen. It controls:
- **Layout**: Where elements sit (Geometry).
- **Visibility**: Whether data is shown or hidden (`display: none` vs `visibility: hidden`).
- **Interactivity**: Hover, Focus, and Active states.

## The Cascade
- **Problem**: What happens when 3 rules target the same Title?
- **Hierarchy**:
    1.  `!important` (Avoid!)
    2.  Inline Styles (`style="..."`)
    3.  ID Selector (`#header`)
    4.  Class Selector (`.btn`)
    5.  Element Selector (`div`)
- **Professional Impact**: Understanding cascade prevents "Specificity Wars" in large teams.
""",
            'order': 1
        },
        {
            'title': 'The Box Model (Reality vs Theory)',
            'content': """# Everything is a Box

## The Data Layers
1.  **Content**: The actual text/image data.
2.  **Padding**: Breathing room *inside* the box.
3.  **Border**: The wall around the box.
4.  **Margin**: The space *outside* pushing other boxes away.

## The `box-sizing: border-box` Standard
- **Default**: `width: 100px` + `padding: 20px` = **140px** wide box. (Confusing).
- **Professional Fix**: `* { box-sizing: border-box; }`
    - Now `width: 100px` means the *total* width is 100px. Padding eats internal space.
    - **Usage**: Used in 99.9% of modern frameworks (Bootstrap, Tailwind).
""",
            'order': 2
        }
    ]
    
    for t in topics_s1:
        Topic.objects.create(stage=stage1, **t)
    print(f"   ✨ Added {len(topics_s1)} topics to Stage 1")


    # ==========================================
    # STAGE 2: LAYOUT SYSTEMS
    # ==========================================
    stage2 = Stage.objects.create(
        roadmap=roadmap,
        title='Layout Systems',
        description='Building structured, scalable layouts.',
        order=2,
        is_free=False
    )
    
    topics_s2 = [
        {
            'title': 'Flexbox (One-Dimensional)',
            'content': """# Aligning Items in a Row/Column

## When to use?
- Navbars, Button groups, Form inputs, Card content.
- **Data Control**: Distributing space among items.

## Key Concepts
- `justify-content`: Main Axis (e.g., Center items horizontally).
- `align-items`: Cross Axis (e.g., Center items vertically).
- `flex-grow`: "Take up remaining space".

## Industry Pattern: The "Holy Grail" Input
```css
.input-group { display: flex; }
input { flex-grow: 1; } /* Fills space */
button { /* Static width */ }
```
""",
            'order': 1
        },
        {
            'title': 'CSS Grid (Two-Dimensional)',
            'content': """# The Blueprint of the Page

## When to use?
- Whole Page Layouts (Header, Sidebar, Content).
- Photo Galleries.
- **Data Control**: Placing items in specific X/Y coordinates.

## The Power of `fr`
- `grid-template-columns: 1fr 3fr;`
- "Split space into 4 parts. Give 1 part to sidebar, 3 parts to content."
- Solves calculation errors of percentages (`25%` + `75%`).

## Grid vs Flexbox
- **Flexbox**: Content-first (Size depends on content inside).
- **Grid**: Layout-first (Content fits into defined slots).
""",
            'order': 2
        },
        {
            'title': 'Positioning Strategies',
            'content': """# Escaping the Flow

## 1. Static (Default)
Element sits where it lands in the HTML flow.

## 2. Relative
"Move me 10px from where I *should* be." (Keeps original space reserved).
- **Usage**: Creating a context for `absolute` children.

## 3. Absolute
"Remove me from flow. Position relative to nearest *positioned* parent."
- **Usage**: Notification badges on icons, Dropdown menus.

## 4. Fixed
"Glue me to the viewport."
- **Usage**: Sticky Headers, Chat widgets.

## 5. Sticky
"Act like Relative until I scroll to top, then act Fixed."
- **Usage**: Section headers in long lists.
""",
            'order': 3
        }
    ]
    
    for t in topics_s2:
        Topic.objects.create(stage=stage2, **t)
    print(f"   ✨ Added {len(topics_s2)} topics to Stage 2")


    # ==========================================
    # STAGE 3: RESPONSIVE DESIGN
    # ==========================================
    stage3 = Stage.objects.create(
        roadmap=roadmap,
        title='Responsive Design',
        description='Building device-independent interfaces.',
        order=3,
        is_free=False
    )
    
    topics_s3 = [
        {
            'title': 'Mobile-First Design',
            'content': """# Small Screens First

## The Philosophy
- Start with the constraints of mobile (simpler layout).
- Add complexity as screen gets bigger (`min-width` queries).

## Why?
- **Performance**: Mobile loads less CSS.
- **UX**: Forces prioritization of content.

## Example
```css
/* Base (Mobile) */
.col { width: 100%; }

/* Tablet */
@media (min-width: 768px) {
  .col { width: 50%; }
}
```
""",
            'order': 1
        },
        {
            'title': 'Responsive Units',
            'content': """# Beyond Pixels

## 1. px (Absolute)
- Good for: Borders (`1px`), Shadows.
- Bad for: Font sizes (User can't scale).

## 2. em (Relative to Parent)
- Good for: Padding inside buttons (scales with button text).
- Risk: Compounding (2em inside 2em = 4em).

## 3. rem (Relative to Root HTML)
- **Industry Standard** for Font Sizes, Margins, Padding.
- `1rem` = Usually 16px.
- Respects user's browser font settings (Accessibility).

## 4. vh / vw (Viewport)
- `100vh`: Full screen height (Hero sections).
""",
            'order': 2
        }
    ]
    
    for t in topics_s3:
        Topic.objects.create(stage=stage3, **t)
    print(f"   ✨ Added {len(topics_s3)} topics to Stage 3")


    # ==========================================
    # STAGE 4: MODERN CSS PRACTICES
    # ==========================================
    stage4 = Stage.objects.create(
        roadmap=roadmap,
        title='Modern CSS Practices',
        description='Writing maintainable, scalable CSS.',
        order=4,
        is_free=False
    )
    
    topics_s4 = [
        {
            'title': 'Architecture: BEM',
            'content': """# Block Element Modifier

## The Naming Convention
A strict rule to prevent style leaks.

## Structure
- **Block**: `.card`
- **Element**: `.card__title`, `.card__image` (Two underscores).
- **Modifier**: `.card--featured`, `.btn--primary` (Two dashes).

## Why Industry Uses It
- **Self-Documenting**: You know exactly what `.nav__item--active` does.
- **No Cascading Issues**: Low specificity (all classes).
- **Scalable**: Teams can work on different blocks without conflict.
""",
            'order': 1
        },
        {
            'title': 'CSS Variables (Custom Properties)',
            'content': """# Dynamic Styling without JS

## The Syntax
```css
:root {
  --primary-color: #3498db;
  --spacing-md: 1rem;
}

.btn {
  background: var(--primary-color);
  padding: var(--spacing-md);
}
```

## Industry Use Case: Theming
- **Dark Mode**: Just redefine variables in `[data-theme="dark"]`.
- No need to rewrite every selector.
""",
            'order': 2
        }
    ]
    
    for t in topics_s4:
        Topic.objects.create(stage=stage4, **t)
    print(f"   ✨ Added {len(topics_s4)} topics to Stage 4")


    # ==========================================
    # STAGE 5: INDUSTRY & PERFORMANCE
    # ==========================================
    stage5 = Stage.objects.create(
        roadmap=roadmap,
        title='Industry & Performance',
        description='Meeting production-level UI standards.',
        order=5,
        is_free=False
    )
    
    topics_s5 = [
        {
            'title': 'Performance Impact',
            'content': """# Styles that Slow You Down

## 1. Critical Rendering Path
- Browser pauses rendering until CSS is downloaded.
- **Fix**: Critical CSS inline, load rest asynchronously.

## 2. Reflow vs Repaint
- **Repaint** (Cheap): Changing color, opacity.
- **Reflow** (Expensive): Changing width, margin, flex order. (Forces browser to recalculate geometry).
- **Animation Tip**: Only animate `transform` and `opacity`. Never animate `width` or `left` (Janky).
""",
            'order': 1
        },
        {
            'title': 'Accessibility Styling',
            'content': """# Styling for Everyone

## 1. Focus States
- **Never do**: `*:focus { outline: none; }`
- **Why**: Keyboard users rely on the focus ring to know where they are.
- **Fix**: Customize it, but don't remove it.

## 2. Contrast Ratios
- Text must have sufficient contrast with background (WCAG AA Standard).
- Use Tools: Chrome DevTools > Accessibility.

## 3. Reduced Motion
- Respect user preference to disable animations.
```css
@media (prefers-reduced-motion: reduce) {
  * { animation: none; transition: none; }
}
```
""",
            'order': 2
        }
    ]
    
    for t in topics_s5:
        Topic.objects.create(stage=stage5, **t)
    print(f"   ✨ Added {len(topics_s5)} topics to Stage 5")

    # Update stats
    roadmap.update_stats()
    print("✅ Professional CSS Roadmap creation complete! Stats updated.")

if __name__ == '__main__':
    create_css_pro_roadmap()
