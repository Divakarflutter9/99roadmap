import os
import django
import sys

# Setup Django environment
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import Roadmap, RoadmapCategory, Stage, Topic
from django.utils.text import slugify

def clear_roadmaps():
    """Delete all existing roadmaps"""
    count = Roadmap.objects.count()
    Roadmap.objects.all().delete()
    print(f"✅ Deleted {count} existing roadmaps\n")

def populate():
    clear_roadmaps()
    
    # 1. Create Category
    category_name = "CSE / IT / Software"
    category, _ = RoadmapCategory.objects.get_or_create(
        slug=slugify(category_name),
        defaults={
            'name': category_name,
            'description': 'Comprehensive roadmaps for Computer Science, IT, and Software Engineering.',
            'icon': 'fa-laptop-code'
        }
    )
    print(f"📁 Category '{category.name}' ready.\n")

    # 2. Roadmap Data with 4 stages each
    roadmaps_data = [
        ("Programming Fundamentals", "Master the core concepts of programming applicable across all languages.", [
            ("Programming Basics", "Foundation concepts every programmer needs", [
                ("What is programming", "Understanding how computers execute instructions and the role of programming languages."),
                ("Variables & data types", "Storing and working with different types of data (numbers, text, booleans)."),
                ("Conditions", "Making decisions in code using if-else statements."),
                ("Loops", "Repeating tasks efficiently with for and while loops.")
            ]),
            ("Logical Thinking", "Develop problem-solving and algorithmic thinking", [
                ("Flowcharts", "Visual representation of program logic and decision flows."),
                ("Pseudocode", "Writing algorithm logic in plain language before coding."),
                ("Breaking problems", "Decomposing complex problems into smaller, manageable parts."),
                ("Input–output logic", "Understanding data flow and program behavior.")
            ]),
            ("Structured Programming", "Write clean, maintainable, and reusable code", [
                ("Functions", "Creating reusable blocks of code with parameters and return values."),
                ("Modularity", "Organizing code into logical, independent modules."),
                ("Reusability", "Writing code once and using it multiple times."),
                ("Code readability", "Best practices for naming, formatting, and documentation.")
            ]),
            ("Programming Mindset", "Think like a professional developer", [
                ("Time complexity intuition", "Basic understanding of algorithm efficiency (Big-O concepts)."),
                ("Debugging strategies", "Systematic approaches to finding and fixing bugs."),
                ("Common beginner mistakes", "Avoiding pitfalls and writing robust code from the start.")
            ])
        ]),
        
        ("Python Programming", "Complete Python mastery from basics to practical applications.", [
            ("Python Basics", "Get started with Python programming", [
                ("Syntax & setup", "Installing Python, IDE setup, and basic syntax rules."),
                ("Variables & I/O", "Working with variables and taking user input/output."),
                ("Conditions & loops", "Control flow with if-else and iteration with for/while loops.")
            ]),
            ("Core Python", "Essential Python data structures and functions", [
                ("Functions", "Defining functions, parameters, return values, and lambda functions."),
                ("Lists, tuples", "Working with ordered collections and their methods."),
                ("Dictionaries & sets", "Key-value pairs and unique collections.")
            ]),
            ("File & Error Handling", "Robust Python programs", [
                ("File operations", "Reading and writing files, working with CSV and JSON."),
                ("Exceptions", "Try-except blocks and handling errors gracefully."),
                ("Modules", "Importing standard libraries and creating custom modules.")
            ]),
            ("Practical Python", "Real-world Python applications", [
                ("Automation scripts", "Automating repetitive tasks with Python scripts."),
                ("CLI tools", "Building command-line applications."),
                ("Mini projects", "Hands-on projects like calculators, file organizers, web scrapers.")
            ])
        ]),
        
        ("Data Structures", "Master the fundamental building blocks of efficient algorithms.", [
            ("DS Foundations", "Understanding data structures and complexity", [
                ("What is DS", "Why data structures matter and their role in programming."),
                ("Arrays", "Fixed-size collections and array operations."),
                ("Strings", "Character arrays and string manipulation techniques."),
                ("Time complexity basics", "Introduction to Big-O notation and algorithm analysis.")
            ]),
            ("Linear DS", "Sequential data structures", [
                ("Stack", "LIFO (Last In First Out) principle and stack operations."),
                ("Queue", "FIFO (First In First Out) principle and queue variants."),
                ("Linked list", "Dynamic memory allocation with singly and doubly linked lists.")
            ]),
            ("Non-Linear DS", "Hierarchical and complex structures", [
                ("Trees", "Binary trees, BST, and tree traversals (inorder, preorder, postorder)."),
                ("Graphs", "Representation and basic graph concepts."),
                ("Hashing", "Hash tables, collision handling, and hash functions.")
            ]),
            ("Problem Patterns", "Apply DS to solve real problems", [
                ("Traversal patterns", "Common patterns for iterating through data structures."),
                ("Optimization thinking", "Choosing the right data structure for the problem."),
                ("DS selection logic", "When to use which data structure and trade-offs.")
            ])
        ]),
        
        ("Algorithms", "Master algorithmic thinking and problem-solving techniques.", [
            ("Algorithm Basics", "Foundation of algorithmic problem solving", [
                ("What is an algorithm", "Definition, characteristics, and importance."),
                ("Brute force", "Simple exhaustive search approaches."),
                ("Simple sorting", "Bubble sort, selection sort, and insertion sort.")
            ]),
            ("Core Techniques", "Essential algorithmic paradigms", [
                ("Binary search", "Efficient searching in sorted arrays."),
                ("Recursion", "Solving problems by breaking them into smaller subproblems."),
                ("Divide & conquer", "Merge sort and quick sort implementations.")
            ]),
            ("Optimization Methods", "Advanced problem-solving patterns", [
                ("Greedy algorithms", "Making locally optimal choices (activity selection, Huffman coding)."),
                ("Two pointers", "Efficient array/string manipulation technique."),
                ("Sliding window", "Optimizing subarray/substring problems.")
            ]),
            ("Advanced Thinking", "Master complex algorithmic techniques", [
                ("Dynamic programming", "Memoization and tabulation (knapsack, LCS, LIS)."),
                ("Backtracking", "Exploring all possible solutions (N-Queens, Sudoku)."),
                ("Real problem mapping", "Identifying which technique to apply to interview problems.")
            ])
        ]),
        
        ("Git & GitHub", "Master version control for modern software development.", [
            ("Version Control Basics", "Understanding Git fundamentals", [
                ("Why Git", "Version control importance and Git's role in development."),
                ("init, add, commit", "Creating repos and tracking changes."),
                ("GitHub intro", "Remote repositories and GitHub basics.")
            ]),
            ("Daily Git Usage", "Core Git workflows", [
                ("Branching", "Creating and switching between branches."),
                ("Merging", "Combining changes from different branches."),
                ("Conflict basics", "Understanding and resolving merge conflicts.")
            ]),
            ("Collaboration", "Working with teams", [
                ("Pull requests", "Proposing and reviewing code changes."),
                ("Code reviews", "Best practices for reviewing others' code."),
                ("Issues", "Tracking bugs and features in GitHub.")
            ]),
            ("Real-World Workflow", "Professional Git practices", [
                ("Open-source flow", "Contributing to open-source projects."),
                ("Best practices", "Commit messages, branch naming, and gitignore."),
                ("Repo hygiene", "Keeping repositories clean and organized.")
            ])
        ]),
        
        ("Web Development Fundamentals", "Understand how the web works and build modern web applications.", [
            ("How Web Works", "Internet and web foundations", [
                ("Internet basics", "How data travels across the internet."),
                ("Client–server", "Understanding the request-response cycle."),
                ("HTTP", "HTTP methods, status codes, and headers.")
            ]),
            ("Frontend Foundations", "Building blocks of web pages", [
                ("HTML structure", "Semantic HTML and document structure."),
                ("CSS basics", "Styling, layout, and the box model."),
                ("JS intro", "JavaScript fundamentals and DOM manipulation.")
            ]),
            ("Interactive Web", "Creating dynamic user experiences", [
                ("DOM manipulation", "Selecting and modifying HTML elements with JavaScript."),
                ("Forms & validation", "Handling user input and validation."),
                ("Responsive design", "Media queries and mobile-first design.")
            ]),
            ("Production Basics", "Taking websites live", [
                ("Deployment", "Hosting static sites on Netlify, Vercel, or GitHub Pages."),
                ("Performance", "Optimization techniques for faster load times."),
                ("Browser tools", "Using DevTools for debugging and performance analysis.")
            ])
        ]),
        
        ("Database & SQL", "Master relational databases and SQL for data management.", [
            ("Database Thinking", "Understanding databases", [
                ("What is a DB", "Database concepts and why they're essential."),
                ("Tables & rows", "Organizing data in tables with rows and columns."),
                ("Primary keys", "Unique identifiers and their importance.")
            ]),
            ("SQL Basics", "Core SQL queries", [
                ("SELECT", "Retrieving data from tables."),
                ("WHERE", "Filtering results with conditions."),
                ("ORDER BY", "Sorting query results.")
            ]),
            ("Relational SQL", "Advanced queries and relationships", [
                ("JOINs", "Combining data from multiple tables (INNER, LEFT, RIGHT)."),
                ("GROUP BY", "Aggregating data with COUNT, SUM, AVG."),
                ("Subqueries", "Nested queries for complex data retrieval.")
            ]),
            ("Advanced DB Concepts", "Database optimization and design", [
                ("Indexing", "Speeding up queries with indexes."),
                ("Normalization", "Organizing data to reduce redundancy (1NF, 2NF, 3NF)."),
                ("Transactions", "ACID properties and maintaining data integrity.")
            ])
        ]),
        
        ("Operating Systems", "Understand how operating systems manage computer resources.", [
            ("OS Basics", "Operating system fundamentals", [
                ("What OS does", "Role of OS in managing hardware and software."),
                ("Processes vs threads", "Understanding execution units."),
                ("Memory overview", "RAM management and virtual memory concepts.")
            ]),
            ("Process Management", "How OS handles programs", [
                ("Scheduling", "CPU scheduling algorithms (FCFS, SJF, Round Robin)."),
                ("Context switching", "How OS switches between processes."),
                ("IPC basics", "Inter-process communication mechanisms.")
            ]),
            ("Memory & Storage", "Resource management", [
                ("Paging", "Memory management technique for virtual memory."),
                ("Virtual memory", "Extending physical RAM with disk space."),
                ("File systems", "How OS organizes data on storage (FAT, NTFS, ext4).")
            ]),
            ("System Design View", "Advanced OS concepts", [
                ("Deadlocks", "Detection, prevention, and avoidance strategies."),
                ("Performance", "System optimization and bottleneck identification."),
                ("OS case studies", "Linux, Windows architecture comparisons.")
            ])
        ]),
        
        ("Computer Networks", "Master networking fundamentals and protocols.", [
            ("Networking Foundations", "Basics of computer networking", [
                ("OSI model", "7-layer model for network communication."),
                ("IP, DNS", "IP addressing and domain name system."),
                ("LAN vs WAN", "Local and wide area network differences.")
            ]),
            ("Core Protocols", "Essential network protocols", [
                ("TCP vs UDP", "Reliable vs unreliable transport protocols."),
                ("HTTP/HTTPS", "Web protocols and secure communication."),
                ("Ports", "Port numbers and their significance.")
            ]),
            ("Network Operations", "How networks function", [
                ("Routing basics", "How data finds its path across networks."),
                ("NAT", "Network Address Translation for IP management."),
                ("Firewalls", "Network security and traffic filtering.")
            ]),
            ("Advanced Networking", "Professional networking concepts", [
                ("Network security", "Encryption, VPNs, and secure protocols."),
                ("Performance tuning", "Optimizing network speed and reliability."),
                ("Real-world scenarios", "Troubleshooting common network issues.")
            ])
        ]),
        
        ("Cyber Security Basics", "Introduction to cybersecurity principles and practices.", [
            ("Security Awareness", "Security fundamentals", [
                ("What is security", "CIA triad (Confidentiality, Integrity, Availability)."),
                ("Common attacks", "Phishing, malware, social engineering."),
                ("Password hygiene", "Creating strong passwords and using password managers.")
            ]),
            ("System Security", "Securing systems", [
                ("Linux basics", "Command-line security tools and practices."),
                ("File permissions", "Understanding and managing access control."),
                ("User management", "Creating users, groups, and principle of least privilege.")
            ]),
            ("Web Security", "Securing web applications", [
                ("OWASP basics", "Top 10 web application security risks."),
                ("Vulnerabilities", "SQL injection, XSS, CSRF explained."),
                ("Attack surface", "Identifying and minimizing security risks.")
            ]),
            ("Ethical Hacking Intro", "Introduction to penetration testing", [
                ("Recon basics", "Information gathering techniques."),
                ("Vulnerability testing", "Using tools to identify security weaknesses."),
                ("Safe practice rules", "Legal and ethical considerations in security testing.")
            ])
        ])
    ]

    # 3. Create Roadmaps
    print("🚀 Creating roadmaps...\n")
    for idx, (title, description, stages_data) in enumerate(roadmaps_data, 1):
        slug = slugify(title)
        roadmap = Roadmap.objects.create(
            slug=slug,
            title=title,
            category=category,
            description=description,
            is_active=True,
            is_premium=True,
            price=499.00,
            estimated_hours=50
        )
        
        print(f"[{idx}/10] ✅ {title}")
        
        # Create Stages
        for stage_num, (stage_title, stage_desc, topics_list) in enumerate(stages_data, 1):
            stage = Stage.objects.create(
                roadmap=roadmap,
                order=stage_num,
                title=stage_title,
                description=stage_desc,
                is_free=(stage_num == 1),  # Only first stage is free
                xp_reward=100 * stage_num
            )
            
            # Create Topics
            for topic_idx, (topic_title, topic_content) in enumerate(topics_list, 1):
                Topic.objects.create(
                    stage=stage,
                    title=topic_title,
                    content=f"## {topic_title}\n\n{topic_content}\n\n### Learning Objectives\n\n- Understand core concepts\n- Apply practical examples\n- Master through practice\n\n### Next Steps\n\nComplete this topic to unlock the next lesson and earn XP!",
                    order=topic_idx,
                    duration_minutes=20,
                    xp_reward=25,
                    content_type='text'
                )

        roadmap.update_premium_status()
        roadmap.update_stats()

    print("\n" + "="*50)
    print(f"✨ Successfully created {len(roadmaps_data)} roadmaps!")
    print("="*50)

if __name__ == '__main__':
    populate()
