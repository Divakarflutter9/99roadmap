#!/bin/bash

# Configuration
PROJECT_DIR="/var/www/99roadmap"
REPO_URL="https://github.com/Divakarflutter9/99roadmap.git"

echo "🚀 Starting Deployment Setup..."

# 1. Install Dependencies
echo "📦 Installing system dependencies..."
sudo apt-get update
sudo apt-get install -y python3-pip python3-venv nginx git postgresql postgresql-contrib libpq-dev

# 2. Clone Repository
if [ -d "$PROJECT_DIR" ]; then
    echo "📂 Directory exists. Pulling latest code..."
    cd $PROJECT_DIR
    git pull
else
    echo "📂 Cloning repository..."
    sudo mkdir -p $PROJECT_DIR
    sudo chown -R $USER:www-data $PROJECT_DIR
    git clone $REPO_URL $PROJECT_DIR
    cd $PROJECT_DIR
fi

# 3. Setup Virtual Environment
echo "🐍 Setting up Python Virtual Environment..."
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 4. Collect Static Files
echo "🎨 Collecting Static Files..."
python manage.py collectstatic --noinput

echo "✅ Setup Complete!"
echo "Now follow the 'VPS_DEPLOYMENT_GUIDE.md' to configure .env, Gunicorn, and Nginx."
