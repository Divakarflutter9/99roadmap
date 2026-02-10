
import os
import django
import sys

# Add project root to sys.path
sys.path.append('/Users/saitejakaki/Divakar/devaproject')

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import Roadmap, RoadmapCategory, Stage, Topic

def create_web_perf_roadmap():
    """Create Web Performance Optimization Roadmap"""
    
    print("🚀 Initializing Web Performance Roadmap Creation...")
    
    # 1. Get or Create Category
    # 'development'
    category, _ = RoadmapCategory.objects.get_or_create(
        slug='development',
        defaults={'name': 'Development'}
    )
    
    # 2. Create Roadmap
    roadmap_slug = 'web-performance-mastery'
    roadmap_title = 'Web Performance Optimization'
    
    roadmap, created = Roadmap.objects.get_or_create(
        slug=roadmap_slug,
        defaults={
            'title': roadmap_title,
            'short_description': 'Master the science of speed. Learn browser rendering, asset optimization, Core Web Vitals, and runtime performance tuning.',
            'description': 'Stop guessing why your site is slow. deep dive into the browser\'s rendering engine, learn how to optimize the Critical Rendering Path, and master industry metrics like LCP and CLS.',
            'category': category,
            'difficulty': 'advanced',
            'estimated_hours': 30,
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
    # STAGE 1: PERFORMANCE BASICS (FREE)
    # ==========================================
    stage1 = Stage.objects.create(
        roadmap=roadmap,
        title='Performance Basics',
        description='Understand what actually affects loading speed.',
        order=1,
        is_free=True
    )
    
    topics_s1 = [
        {
            'title': 'The Page Load Lifecycle',
            'content': """# It Starts Before the screen is white

## 1. Network Negotiation (The Invisible Cost)
- **DNS Lookup**: Finding server IP.
- **TCP Handshake**: Establishing connection (SYN/ACK).
- **SSL Negotiation**: Decrypting the connection.
- **TTFB (Time To First Byte)**: Backend processing time.

## 2. Resource Waterfall
- Browsers have a limit on parallel downloads (usually 6 per domain).
- If you have 20 JS files, the browser creates a "Queue".
- **Goal**: Minimize requests to avoid queueing.
""",
            'order': 1
        },
        {
            'title': 'Browser Rendering Flow',
            'content': """# From HTML to Pixels

## The Critical Rendering Path (CRP)
1.  **DOM Construction**: Parse HTML.
2.  **CSSOM Construction**: Parse CSS (Render Blocking!).
3.  **Render Tree**: Combine DOM + CSSOM (Invisible elements removed).
4.  **Layout (Reflow)**: Calculate geometry (width/height).
5.  **Paint**: Fill pixels (color, shadow).
6.  **Composite**: Layer management (GPU acceleration).

## Key Takeaway
- If you change `width` with JS, the browser restarts at **Step 4** (Layout). Expensive!
- If you change `opacity`, it starts at **Step 6** (Composite). Cheap!
""",
            'order': 2
        }
    ]
    
    for t in topics_s1:
        Topic.objects.create(stage=stage1, **t)
    print(f"   ✨ Added {len(topics_s1)} topics to Stage 1")


    # ==========================================
    # STAGE 2: FRONTEND PERFORMANCE
    # ==========================================
    stage2 = Stage.objects.create(
        roadmap=roadmap,
        title='Frontend Performance',
        description='Optimizing UI delivery.',
        order=2,
        is_free=False
    )
    
    topics_s2 = [
        {
            'title': 'Asset Optimization',
            'content': """# Shrinking the Payload

## Text Compression
- **Gzip**: Standard. Good.
- **Brotli** (`br`): Better. Industry standard for static assets.

## Minification
- Removing whitespace/comments. (UglifyJS, Terser).
- **Tree Shaking**: Removing *unused* code (ES Modules required).

## Image Optimization
- **Formats**: Use **WebP** or **AVIF** instead of PNG/JPEG.
- **Responsive Images**: `<img srcset="...">` to serve small images to mobile.
- **Lazy Loading**: `loading="lazy"` (Native browser support).
""",
            'order': 1
        },
        {
            'title': 'CSS & JS Impact',
            'content': """# Unblocking the Render

## CSS
- **Render Blocking**: Browser waits for ALL CSS before painting.
- **Critical CSS**: Inline the styles for "Above the Fold" content. Defer the rest.

## JavaScript
- **Parser Blocking**: Stops HTML parsing to read JS.
- **Async**: `p`arse HTML and download JS in parallel. Execute when ready.
- **Defer**: Parse HTML and download JS in parallel. Execute *after* HTML is done. (Best Practice).
""",
            'order': 2
        }
    ]
    
    for t in topics_s2:
        Topic.objects.create(stage=stage2, **t)
    print(f"   ✨ Added {len(topics_s2)} topics to Stage 2")


    # ==========================================
    # STAGE 3: RUNTIME PERFORMANCE
    # ==========================================
    stage3 = Stage.objects.create(
        roadmap=roadmap,
        title='Runtime Performance',
        description='Improving user interactions (60fps).',
        order=3,
        is_free=False
    )
    
    topics_s3 = [
        {
            'title': 'Main Thread Blocking',
            'content': """# JavaScript is Expensive

## The Cost
- Downloading 1MB Image = Easy (Running on Network Thread).
- Downloading 1MB JS = Hard (Must Parse, Compile, Execute on Main Thread).

## Blocking
- Long Tasks (>50ms) freeze the UI.
- **Solution**: Web Workers (Move heavy logic to background thread).

## Event Handlers
- **Debounce**: "Wait until user stops typing". (Search Input).
- **Throttle**: "Run at most once per 100ms". (Scroll Listener).
""",
            'order': 1
        },
        {
            'title': 'Repaints & Reflows',
            'content': """# Layout Thrashing

## What Causes Reflow (Expensive)?
- Changing `width`, `height`, `margin`, `font-size`.
- Reading layout properties: `offsetHeight`, `scrollTop` (Forces browser to calculate instantly).

## What Causes Repaint (Cheaper)?
- Changing `color`, `background`, `visibility`.

## What is GPU Accelerated (Cheapest)?
- `transform`, `opacity`.
- Use `will-change: transform` sparingly to hint the browser.
""",
            'order': 2
        }
    ]
    
    for t in topics_s3:
        Topic.objects.create(stage=stage3, **t)
    print(f"   ✨ Added {len(topics_s3)} topics to Stage 3")


    # ==========================================
    # STAGE 4: PRODUCTION OPTIMIZATION
    # ==========================================
    stage4 = Stage.objects.create(
        roadmap=roadmap,
        title='Production Optimization',
        description='Industry-level tuning and monitoring.',
        order=4,
        is_free=False
    )
    
    topics_s4 = [
        {
            'title': 'Web Vitals (Metrics)',
            'content': """# Google's Report Card

## Core Web Vitals (SEO Impact)
1.  **LCP (Largest Contentful Paint)**: Loading. (Target: < 2.5s).
    - Measures how fast the main content appears.
2.  **INP (Interaction to Next Paint)**: Interactivity. (Target: < 200ms).
    - Replaces FID. Measures UI responsiveness.
3.  **CLS (Cumulative Layout Shift)**: Visual Stability. (Target: < 0.1).
    - Did elements jump around while loading?

## Tools
- **Lighthouse**: Lab data (Simulation).
- **Chrome UX Report (CrUX)**: Real user data.
""",
            'order': 1
        },
        {
            'title': 'Monitoring Strategies',
            'content': """# Watching in Production

## RUM (Real User Monitoring)
- Capturing metrics from actual user devices.
- "Lighthouse gave me 100, but my users on 3G in India are seeing 50."

## CDNs (Content Delivery Networks)
- physically closer servers = lower latency (TTFB).
- Caching policies (`Cache-Control: public, max-age=31536000`).

## Interview Questions
- "How do you optimize a slow React app?"
    - Profiler -> Memoization -> Code Splitting -> Virtualization.
""",
            'order': 2
        }
    ]
    
    for t in topics_s4:
        Topic.objects.create(stage=stage4, **t)
    print(f"   ✨ Added {len(topics_s4)} topics to Stage 4")

    # Update stats
    roadmap.update_stats()
    print("✅ Web Performance Roadmap creation complete! Stats updated.")

if __name__ == '__main__':
    create_web_perf_roadmap()
