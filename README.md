# 99Roadmap - Learning Platform

A comprehensive learning platform where students discover structured roadmaps, track progress with gamification, unlock paid content through subscriptions, and get AI-powered assistance.

## 🚀 Features

### ✅ Core Features Implemented
- ✅ User authentication with email verification
- ✅ Custom registration (Full name, email, phone, study type, branch)
- ✅ Password validation (8+ chars, letters + special characters)
- ✅ Complete roadmap system (Roadmaps → Stages → Topics → Quizzes)
- ✅ Progress tracking with XP, levels, and streaks
- ✅ Cashfree payment integration for subscriptions
- ✅ OpenAI-powered AI assistant
- ✅ Comprehensive Django admin dashboard
- ✅ Modern dark-themed responsive UI

### 📚 Learning System
- Browse roadmaps by category (Skills, Exams, Career, Money, Mindset)
- Complete topics and earn XP
- Take quizzes to verify understanding
- Track mastery and progress per stage
- Free content + premium subscription model

### 🎮 Gamification
- XP points for completing topics and passing quizzes
- Level system (Level = XP / 500 + 1)
- Daily login streak tracking
- Leaderboard-ready data structure

### 💳 Payments & Subscriptions
- Multiple subscription plans (Monthly, Yearly, Lifetime)
- Cashfree payment gateway (Sandbox + Production ready)
- Automatic subscription activation on successful payment
- Webhook support for payment callbacks

### 🤖 AI Assistant
- Context-aware chat (knows current roadmap, stage, user details)
- Explains topics in simple language
- Answers doubts and suggests next steps
- Powered by OpenAI GPT

### 🎨 Design
- Modern dark theme with purple/indigo accents
- Glassmorphism effects
- Smooth animations and micro-interactions
- Fully responsive (desktop, tablet, mobile)

## 📦 Installation

### Prerequisites
- Python 3.8+
- pip
- Virtual environment (recommended)

### Setup Steps

1. **Navigate to project directory:**
```bash
cd /Users/saitejakaki/Divakar/devaproject
```

2. **Activate virtual environment:**
```bash
source venv/bin/activate
```

3. **Install dependencies** (already done):
```bash
pip install -r requirements.txt
```

4. **Configure environment variables:**
Edit `.env` file and add your API keys:
```env
# Cashfree (Get from https://www.cashfree.com/)
CASHFREE_APP_ID=your_app_id
CASHFREE_SECRET_KEY=your_secret_key
CASHFREE_ENV=SANDBOX

# OpenAI (Get from https://platform.openai.com/)
OPENAI_API_KEY=your_openai_key

# Email (Gmail SMTP)
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
```

5. **Run migrations** (already done):
```bash
python manage.py migrate
```

6. **Create superuser:**
```bash
python manage.py createsuperuser
```
Enter email and password when prompted.

7. **Run development server:**
```bash
python manage.py runserver
```

8. **Access the application:**
- **Homepage:** http://localhost:8000/
- **Admin Panel:** http://localhost:8000/admin/
- **Register:** http://localhost:8000/register/
- **Login:** http://localhost:8000/login/

## 🔧 Admin Panel Setup

1. Login to admin panel: http://localhost:8000/admin/
2. Create roadmap categories (Skills, Exams, Career, etc.)
3. Create roadmaps
4. Add stages to roadmaps
5. Add topics to stages
6. Create quizzes (optional)
7. Create subscription plans

### Sample Data Structure
```
Category: Programming Skills
  └─ Roadmap: Full Stack Web Development
      ├─ Stage 1: HTML & CSS Basics (Free)
      │   ├─ Topic 1: HTML Introduction
      │   ├─ Topic 2: CSS Styling
      │   └─ Quiz: HTML/CSS Fundamentals
      ├─ Stage 2: JavaScript (Premium)
      │   ├─ Topic 1: Variables & Data Types
      │   └─ Quiz: JavaScript Basics
      └─ Stage 3: React (Premium)
```

## 📱 User Flow

### Registration & Onboarding
1. User registers with full name, email, phone, study type, branch
2. Email verification sent
3. User clicks verification link
4. Redirected to login
5. After login → Dashboard

### Learning Flow
1. Browse roadmaps
2. Enroll in a roadmap (free stages accessible)
3. Complete topics → Earn XP
4. Take quizzes → Earn more XP
5. Level up and track streak
6. For premium content → Subscribe
7. Use AI assistant for help anytime

### Payment Flow
1. View subscription plans
2. Click "Subscribe Now"
3. Cashfree checkout opens
4. Complete payment
5. Subscription activated automatically
6. Access all premium content

## 🎯 Admin Dashboard Features

### User Management
- View all users with filters (study type, branch, verified status)
- Activate/deactivate users
- View user progress and XP

### Roadmap Management
- Create/edit/delete roadmaps
- Organize by categories
- Mark as free/premium
- Feature roadmaps on homepage

### Subscription Management
- View active subscribers
- Track revenue
- Manage subscription plans
- View payment transactions

### Analytics
- User signups over time
- Popular roadmaps
- Quiz completion rates
- XP distribution

## 🛠️ Technology Stack

- **Backend:** Django 5.2
- **Database:** SQLite (dev) / PostgreSQL (production ready)
- **Frontend:** HTML, CSS, Vanilla JavaScript
- **Payments:** Cashfree Payment Gateway
- **AI:** OpenAI GPT-3.5/4
- **Email:** SMTP (Gmail free tier)

## 📂 Project Structure

```
devaproject/
├── core/               # Main app (users, roadmaps, progress)
├── payments/           # Subscription & Cashfree integration
├── ai_assistant/       # OpenAI integration
├── templates/          # HTML templates
├── static/             # CSS, JS, images
├── media/              # User uploads
├── roadmap99/          # Django project settings
├── manage.py
├── requirements.txt
└── .env               # Environment variables
```

## 🔐 Security Notes

- Never commit `.env` file
- Use strong SECRET_KEY in production
- Set DEBUG=False in production
- Use HTTPS in production
- Cashfree: Use PRODUCTION mode only after testing
- Email: Use app-specific passwords for Gmail

## 📝 Next Steps

1. **Add Content:** Create roadmaps, stages, and topics via admin
2. **Configure APIs:** Add Cashfree and OpenAI keys
3. **Test Email:** Set up SMTP for email verification
4. **Deploy:** Use Gunicorn + Nginx for production
5. **Database:** Migrate to PostgreSQL for production

## 🤝 Support

For issues or questions:
1. Check admin dashboard for data management
2. Use AI assistant for learning help
3. Review code comments for implementation details

## 📄 License

© 2026 99Roadmap. All rights reserved.

---

**Built with ❤️ using Django**
