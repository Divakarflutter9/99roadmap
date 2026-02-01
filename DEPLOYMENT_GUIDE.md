# 🚀 Deployment Guide: VPS (Ubuntu/Debian)

This guide will help you deploy **99Roadmap** to your VPS at `/var/www/Divakar/` using **Nginx**, **Gunicorn**, and **MySQL**.

---

## 📌 Phase 0: High Concurrency Setup (Required for 1000+ Users)
As of the latest update, the system uses **Celery + Redis** to handle large email blasts without freezing.

**1. Install Redis:**
```bash
sudo apt update
sudo apt install redis-server -y
sudo systemctl enable redis-server
sudo systemctl start redis-server
```

**2. Configure Celery Service:**
We need to run Celery alongside Gunicorn.

Create service file:
```bash
sudo nano /etc/systemd/system/celery-roadmap99.service
```

Paste this (adjusting paths if needed):
```ini
[Unit]
Description=Celery Service for 99Roadmap
After=network.target

[Service]
Type=forking
User=root
Group=www-data
EnvironmentFile=/etc/environment
WorkingDirectory=/var/www/Divakar
ExecStart=/var/www/Divakar/venv/bin/celery -A roadmap99 multi start worker1 \
  --pidfile=/var/run/celery/%n.pid \
  --logfile=/var/log/celery/%n%I.log \
  --loglevel=INFO
ExecStop=/var/www/Divakar/venv/bin/celery multi stopwait worker1 \
  --pidfile=/var/run/celery/%n.pid

[Install]
WantedBy=multi-user.target
```

**3. Start Celery:**
```bash
sudo mkdir -p /var/run/celery /var/log/celery
sudo chown -R root:www-data /var/run/celery /var/log/celery
sudo systemctl enable celery-roadmap99
sudo systemctl start celery-roadmap99
```

---

## 📌 Phase 1: Server Preparation

**1. Login to your VPS:**
```bash
ssh root@your_server_ip
```

**2. Update System & Install Dependencies:**
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv python3-dev libmysqlclient-dev mysql-server nginx git -y
```

**3. Start MySQL:**
```bash
sudo systemctl start mysql
sudo systemctl enable mysql
```

---

## 📌 Phase 2: Database Setup

**1. Log in to MySQL:**
```bash
sudo mysql -u root -p
# Enter your root password if set, or just enter if new installation
```

**2. Create Database & User:**
Run these SQL commands (using your provided credentials):

```sql
CREATE DATABASE roadmap99 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'PhaniUddagiri@2005';
FLUSH PRIVILEGES;
EXIT;
```

---

## 📌 Phase 3: Project Setup

**1. Clone Repository:**
```bash
# Create directory
sudo mkdir -p /var/www/Divakar
sudo chown -R $USER:$USER /var/www/Divakar

# Go to directory
cd /var/www/Divakar

# Clone your code
git clone https://github.com/Divakarflutter9/99roadmap.git .
```

**2. Set Up Virtual Environment:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install Dependencies:**
```bash
pip install -r requirements.txt
pip install gunicorn mysqlclient
```

**4. Create .env File:**
```bash
nano .env
```
Paste this content (I've pre-filled your DB details):

```ini
DEBUG=False
SECRET_KEY=django-insecure-99roadmap-prod-key-change-this-to-something-secret-99
ALLOWED_HOSTS=99roadmap.droptechie.com,194.163.173.57
# MySQL Database (Server)
DATABASE_URL=mysql://root:PhaniUddagiri%402005@127.0.0.1:3306/roadmap99

# Cashfree (Production)
CASHFREE_APP_ID=YOUR_CASHFREE_APP_ID
CASHFREE_SECRET_KEY=YOUR_CASHFREE_SECRET_KEY
CASHFREE_ENV=PRODUCTION

# OpenAI
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
OPENAI_BASE_URL=https://api.groq.com/openai/v1/
OPENAI_MODEL_NAME=llama-3.1-8b-instant

# Email
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=99roadmap@gmail.com
EMAIL_HOST_PASSWORD=YOUR_EMAIL_PASSWORD

# Site URL
SITE_URL=http://99roadmap.droptechie.com
```
*Press `Ctrl+X`, then `Y`, then `Enter` to save.*

**5. Run Migrations & Collect Static:**
```bash
# Apply DB structure
python manage.py migrate

# Collect CSS/JS files
python manage.py collectstatic --noinput

# Load your roadmaps data (which we exported earlier)
python manage.py loaddata fixtures/roadmaps_data.json
```

**6. Create Superuser:**
```bash
python manage.py createsuperuser
```

---

## 📌 Phase 4: Gunicorn Setup

**1. Test Gunicorn Manually:**
```bash
gunicorn --bind 0.0.0.0:8000 roadmap99.wsgi
```
*Visit `http://your_server_ip:8000` to see if it works. Press `Ctrl+C` to stop.*

**2. Create Systemd Service:**
*We use a unique name (gunicorn-roadmap99) to avoid conflicting with other apps on your server.*

```bash
sudo nano /etc/systemd/system/gunicorn-roadmap99.service
```

Paste this:
```ini
[Unit]
Description=gunicorn daemon for 99Roadmap
After=network.target

[Service]
User=root
Group=www-data
WorkingDirectory=/var/www/Divakar
ExecStart=/var/www/Divakar/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/var/www/Divakar/roadmap99.sock roadmap99.wsgi:application

[Install]
WantedBy=multi-user.target
```
*Save and exit.*

**3. Start Gunicorn:**
```bash
sudo systemctl start gunicorn-roadmap99
sudo systemctl enable gunicorn-roadmap99
```

---

## 📌 Phase 5: Nginx Configuration

**1. Create Nginx config:**
*IMPORTANT: Replace 'your_domain.com' with your actual domain or a subdomain (e.g., app.yourdomain.com). Do NOT use the raw IP if other sites are already using it.*

```bash
sudo nano /etc/nginx/sites-available/roadmap99
```

Paste this:
```nginx
server {
    listen 80;
    server_name 99roadmap.droptechie.com 194.163.173.57;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        alias /var/www/Divakar/staticfiles/;
    }

    location /media/ {
        alias /var/www/Divakar/media/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/var/www/Divakar/roadmap99.sock;
    }
}
```
*Save and exit.*

**2. Enable Site:**
```bash
sudo ln -s /etc/nginx/sites-available/roadmap99 /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

---

## 🚀 Done!
Your site should now be live at `http://your_server_ip`.

**Next Step (SSL/HTTPS):**
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your_domain.com
```
