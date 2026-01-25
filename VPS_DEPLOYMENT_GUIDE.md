# 🛡️ Zero-Risk Production Deployment Manual
**Objective**: Deploy "99Roadmap" to a shared VPS without interrupting any running services.

## ⚠️ Safety Protocols (Read First)
1.  **Isolation**: We will use a **Unix Socket** (`99roadmap.sock`) instead of a TCP port. This guarantees no "Port already in use" errors.
2.  **Separate Configs**: We will create a *new* Nginx config file. We will **NEVER** edit the main `nginx.conf`.
3.  **Validation**: We will run `nginx -t` (Test Configuration) before reloading. If this fails, we stop. We do not restart if tests fail.

---

## Phase 1: Local Preparation (Your Computer)
We need to upload the new `deploy/` scripts I created to GitHub so your server can download them.

1.  **Open your Local Terminal**.
2.  **Run these exact commands:**
    ```bash
    git add deploy/ VPS_DEPLOYMENT_GUIDE.md
    git commit -m "Add safe deployment configuration"
    git push
    ```
    *(Verify that the push is successful).*

---

## Phase 2: Server Prep & Installation (Your VPS)
**Login to your VPS:** `ssh user@your_ip`

### 1. Run the Auto-Installer (Safe Mode)
Copy and paste this block into your VPS terminal. It creates a secluded folder `/var/www/99roadmap` and installs dependencies there.

```bash
# Set specific permission to avoid conflicts
sudo mkdir -p /var/www/99roadmap
sudo chown -R $USER:www-data /var/www/99roadmap

# Download the code
git clone https://github.com/Divakarflutter9/99roadmap.git /var/www/99roadmap
cd /var/www/99roadmap

# Setup Isolated Environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn psycopg2-binary
```

### 2. Configure Secrets
Create the environment file.
```bash
nano .env
```
Paste your secrets (`SECRET_KEY`, `DEBUG=False`, etc).
**Save**: `Ctrl+O`, `Enter`, `Ctrl+X`.

---

## Phase 3: Service Isolation (Gunicorn)
We use a systemd service to keep the app running in its own "box".

1.  **Copy the service file**:
    ```bash
    sudo cp deploy/gunicorn.service /etc/systemd/system/99roadmap.service
    ```
2.  **Start the specific service**:
    ```bash
    sudo systemctl start 99roadmap
    sudo systemctl enable 99roadmap
    ```
3.  **Verify it's running**:
    ```bash
    sudo systemctl status 99roadmap
    ```
    *You must see a green dot (●) or "active (running)". If not, STOP and check logs.*

---

## Phase 4: Traffic Routing (Nginx) - CRITICAL STEP
We will add a new "block" for your site.

1.  **Copy the config**:
    ```bash
    sudo cp deploy/nginx_template /etc/nginx/sites-available/99roadmap
    ```
2.  **Edit the Domain**:
    ```bash
    sudo nano /etc/nginx/sites-available/99roadmap
    ```
    Change `server_name your_domain_or_ip;` to your real domain (e.g., `server_name 99roadmap.com;`).
    **Save & Exit**.

3.  **Enable the Site**:
    ```bash
    sudo ln -s /etc/nginx/sites-available/99roadmap /etc/nginx/sites-enabled/
    ```

4.  **SAFETY CHECK (Do not skip)**:
    Run this command:
    ```bash
    sudo nginx -t
    ```
    *   **IF IT SAYS "syntax is ok":** Proceed to step 5.
    *   **IF IT FAILS**: You made a typo. `rm /etc/nginx/sites-enabled/99roadmap` and start Phase 4 again. **DO NOT RELOAD NGINX.**

5.  **Safe Reload**:
    ```bash
    sudo systemctl reload nginx
    ```
    *(Note: We use `reload`, not `restart`. Reload keeps other sites alive while loading yours).*

---

## Phase 5: Final Polish
Initialize the database and static files.

```bash
cd /var/www/99roadmap
source venv/bin/activate
python manage.py migrate
python manage.py collectstatic --noinput
```

**DEPLOYMENT COMPLETE.**
Your app is now live and isolated.
