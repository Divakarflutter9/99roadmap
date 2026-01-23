# Production Deployment Guide for 99Roadmap

## Pre-Deployment Checklist

### 1. Environment Variables (.env file)

Create a `.env` file in the project root:

```env
# Django Settings
SECRET_KEY=your-super-secret-key-here-generate-new-one
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# Database (Use PostgreSQL for production)
DATABASE_URL=postgresql://user:password@localhost:5432/roadmap99_db

# Email Configuration
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.sendgrid.net
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=apikey
EMAIL_HOST_PASSWORD=your-sendgrid-api-key
DEFAULT_FROM_EMAIL=99Roadmap <noreply@99roadmap.com>

# Site URL
SITE_URL=https://yourdomain.com

# API Keys
OPENAI_API_KEY=your-openai-api-key
CASHFREE_APP_ID=your-cashfree-app-id
CASHFREE_SECRET_KEY=your-cashfree-secret-key
CASHFREE_ENV=PROD

# AWS S3 (for static files - optional)
AWS_ACCESS_KEY_ID=your-aws-access-key
AWS_SECRET_ACCESS_KEY=your-aws-secret-key
AWS_STORAGE_BUCKET_NAME=your-bucket-name
AWS_S3_REGION_NAME=us-east-1

# Security
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

---

## 2. Update settings.py for Production

Add this code to `roadmap99/settings.py`:

```python
import os
from pathlib import Path
import dj_database_url

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'your-default-key-change-this')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# Database
if os.getenv('DATABASE_URL'):
    DATABASES = {
        'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Static files (CSS, JavaScript, Images) for Production
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Security Settings (Production)
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
```

---

## 3. Install Production Dependencies

```bash
pip install gunicorn psycopg2-binary python-dotenv dj-database-url whitenoise
```

Update `requirements.txt`:
```bash
pip freeze > requirements.txt
```

---

## 4. Configure Static Files with WhiteNoise

Add to `settings.py`:

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this
    # ... other middleware
]

# WhiteNoise configuration
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

---

## 5. Collect Static Files

```bash
python manage.py collectstatic --noinput
```

---

## 6. Database Migration

For PostgreSQL:

```bash
# Create PostgreSQL database
sudo -u postgres psql
CREATE DATABASE roadmap99_db;
CREATE USER roadmap99_user WITH PASSWORD 'your-password';
GRANT ALL PRIVILEGES ON DATABASE roadmap99_db TO roadmap99_user;
\q

# Run migrations
python manage.py migrate
python manage.py createsuperuser
```

---

## 7. Gunicorn Configuration

Create `gunicorn_config.py`:

```python
bind = "0.0.0.0:8000"
workers = 3
worker_class = "sync"
worker_connections = 1000
max_requests = 1000
max_requests_jitter = 50
timeout = 30
keepalive = 2
errorlog = "-"
accesslog = "-"
loglevel = "info"
```

Start Gunicorn:
```bash
gunicorn --config gunicorn_config.py roadmap99.wsgi:application
```

---

## 8. Nginx Configuration

Create `/etc/nginx/sites-available/99roadmap`:

```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        alias /path/to/your/project/staticfiles/;
    }

    location /media/ {
        alias /path/to/your/project/media/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Enable the site:
```bash
sudo ln -s /etc/nginx/sites-available/99roadmap /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

---

## 9. SSL Certificate (Let's Encrypt)

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

---

## 10. Systemd Service for Gunicorn

Create `/etc/systemd/system/99roadmap.service`:

```ini
[Unit]
Description=99Roadmap Gunicorn daemon
After=network.target

[Service]
User=your-user
Group=www-data
WorkingDirectory=/path/to/your/project
EnvironmentFile=/path/to/your/project/.env
ExecStart=/path/to/your/project/venv/bin/gunicorn \
          --config gunicorn_config.py \
          roadmap99.wsgi:application

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl daemon-reload
sudo systemctl start 99roadmap
sudo systemctl enable 99roadmap
sudo systemctl status 99roadmap
```

---

## 11. Logging Configuration

Add to `settings.py`:

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs/django.log',
        },
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
```

Create logs directory:
```bash
mkdir logs
```

---

## 12. Backup Strategy

### Database Backups
```bash
# PostgreSQL backup
pg_dump roadmap99_db > backup_$(date +%Y%m%d_%H%M%S).sql

# Restore
psql roadmap99_db < backup_20260123_220000.sql
```

### Media Files Backup
```bash
tar -czf media_backup_$(date +%Y%m%d).tar.gz media/
```

---

## 13. Monitoring (Optional)

### Install Sentry for Error Tracking

```bash
pip install sentry-sdk
```

Add to `settings.py`:
```python
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

if not DEBUG:
    sentry_sdk.init(
        dsn="your-sentry-dsn",
        integrations=[DjangoIntegration()],
        traces_sample_rate=0.1,
    )
```

---

## 14. Performance Optimization

1. **Enable Caching**
```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}
```

2. **Database Optimization**
- Add database indexes
- Use select_related() and prefetch_related()
- Enable database connection pooling

3. **CDN for Static Files**
- Use AWS CloudFront or Cloudflare
- Serve static files from CDN

---

## Quick Deployment Commands

```bash
# 1. Pull latest code
git pull origin main

# 2. Install dependencies
pip install -r requirements.txt

# 3. Migrate database
python manage.py migrate

# 4. Collect static files
python manage.py collectstatic --noinput

# 5. Restart Gunicorn
sudo systemctl restart 99roadmap

# 6. Check status
sudo systemctl status 99roadmap
```

---

## Checklist Before Going Live

- [ ] DEBUG = False
- [ ] SECRET_KEY changed and secured
- [ ] ALLOWED_HOSTS configured
- [ ] Database backed up
- [ ] Static files collected
- [ ] SSL certificate installed
- [ ] Email configuration tested
- [ ] Error pages (404, 500) working
- [ ] Gunicorn and Nginx configured
- [ ] Logging enabled
- [ ] Monitoring set up (optional)
- [ ] Backup strategy in place
- [ ] Domain DNS configured
- [ ] Privacy Policy accessible
- [ ] Terms & Conditions accessible
- [ ] Contact form working

---

## Common Issues

### Static files not loading
```bash
python manage.py collectstatic --clear
sudo systemctl restart nginx
```

### Database connection issues
- Check PostgreSQL is running
- Verify DATABASE_URL in .env
- Check firewall rules

### Gunicorn not starting
- Check logs: `sudo journalctl -u 99roadmap`
- Verify .env file path
- Check file permissions

---

## Support Resources

- Django Deployment: https://docs.djangoproject.com/en/stable/howto/deployment/
- Gunicorn: https://docs.gunicorn.org/
- Nginx: https://nginx.org/en/docs/
- PostgreSQL: https://www.postgresql.org/docs/
