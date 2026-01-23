# 🚀 Deploying Roadmaps to Production Server

## The Problem
You're creating roadmaps locally (development) but need them on your live server (production).

---

## ✅ BEST METHOD: Django Fixtures (Recommended)

### What are Fixtures?
Django fixtures are JSON/YAML files containing database data that can be exported from one database and loaded into another.

### Step-by-Step Process

#### 1. Export Roadmaps from Local Database

After creating all your roadmaps locally, export them:

```bash
# Export ONLY roadmaps, stages, and topics
python manage.py dumpdata core.Roadmap core.Stage core.Topic core.RoadmapCategory \
  --indent 2 \
  --output roadmaps_data.json
```

**This creates**: `roadmaps_data.json` file with all roadmap data

#### 2. Transfer File to Production Server

```bash
# Using SCP (Secure Copy)
scp roadmaps_data.json user@your-server.com:/path/to/project/

# Or use Git (recommended)
git add roadmaps_data.json
git commit -m "Add roadmaps data"
git push origin main
```

#### 3. Load Data on Production Server

SSH into your production server:

```bash
ssh user@your-server.com
cd /path/to/project

# Activate virtual environment
source venv/bin/activate

# Load the fixture
python manage.py loaddata roadmaps_data.json
```

**Done!** ✅ Roadmaps are now on production!

---

## Alternative Method 1: Run Import Scripts on Production

### Process

1. **Transfer import scripts** to production server:
```bash
git add import_control_systems_roadmap.py
git commit -m "Add roadmap import scripts"
git push
```

2. **SSH to production** and run:
```bash
ssh user@your-server.com
cd /path/to/project
source venv/bin/activate

# Run the import script
python manage.py shell < import_control_systems_roadmap.py
```

### Pros:
- ✅ Clean, repeatable
- ✅ Can re-run if needed
- ✅ Version controlled

### Cons:
- ❌ Must run each script manually
- ❌ Time-consuming for many roadmaps

---

## Alternative Method 2: Database Export/Import (PostgreSQL)

If using PostgreSQL in both dev and production:

### Export from Local:
```bash
# Dump specific tables
pg_dump -U username -d database_name \
  -t core_roadmap \
  -t core_stage \
  -t core_topic \
  -t core_roadmapcategory \
  --data-only \
  > roadmaps_dump.sql
```

### Import to Production:
```bash
# On production server
psql -U username -d production_database < roadmaps_dump.sql
```

### ⚠️ Warning:
- Can cause ID conflicts
- Need to handle foreign keys carefully
- Not recommended for live databases with existing data

---

## Alternative Method 3: Django Admin (Not Recommended)

Manually recreate roadmaps through Django admin panel.

❌ **Don't do this** - Too time-consuming and error-prone for large roadmaps!

---

## 🎯 RECOMMENDED WORKFLOW

### For Development → Production Deployment:

#### Initial Setup (One-time):
1. Create roadmaps locally
2. Test thoroughly
3. Export as fixture:
   ```bash
   python manage.py dumpdata core.Roadmap core.Stage core.Topic core.RoadmapCategory \
     --indent 2 --output fixtures/initial_roadmaps.json
   ```
4. Add to Git:
   ```bash
   git add fixtures/initial_roadmaps.json
   git commit -m "Add initial roadmaps"
   git push
   ```

#### On Production Server (First Deployment):
```bash
# Pull latest code
git pull origin main

# Load roadmaps
python manage.py loaddata fixtures/initial_roadmaps.json
```

#### For Updates (Adding New Roadmaps):
1. Create new roadmap locally
2. Export **only new roadmap**:
   ```bash
   python manage.py dumpdata core.Roadmap core.Stage core.Topic \
     --pks <roadmap_id> \
     --natural-foreign \
     --natural-primary \
     --indent 2 \
     --output fixtures/new_roadmap_<name>.json
   ```
3. Git add, commit, push
4. On production:
   ```bash
   git pull
   python manage.py loaddata fixtures/new_roadmap_<name>.json
   ```

---

## 📋 Complete Production Deployment Steps

### Pre-Deployment Checklist:
- [ ] All roadmaps created and tested locally
- [ ] Roadmaps exported to fixture file
- [ ] Fixture file added to Git repository
- [ ] Production server ready
- [ ] Database migrations run on production

### Deployment Commands:

```bash
# On Production Server
cd /path/to/your/project
source venv/bin/activate

# 1. Pull latest code (includes fixture files)
git pull origin main

# 2. Run migrations (if any model changes)
python manage.py migrate

# 3. Load roadmaps
python manage.py loaddata fixtures/initial_roadmaps.json

# 4. Collect static files
python manage.py collectstatic --noinput

# 5. Restart server
sudo systemctl restart 99roadmap  # Or your service name
```

---

## 🔄 Keeping Local & Production in Sync

### Best Practice:

1. **Single Source of Truth**: Keep fixtures in Git
2. **Version Control**: Track all roadmap changes
3. **Systematic Updates**: Use fixtures for all data transfers
4. **Backup First**: Before loading new data on production

### Example Workflow:

```bash
# Local Development
1. Create/update roadmap
2. Test thoroughly
3. Export fixture: python manage.py dumpdata ...
4. Git commit & push

# Production Deployment  
5. Git pull
6. Load fixture: python manage.py loaddata ...
7. Restart server
```

---

## ⚠️ Important Warnings

### 1. Primary Keys (IDs)
- Fixtures preserve primary keys
- If roadmap ID=1 exists in production, loading fixture with ID=1 will **update** it
- Be careful with existing data!

### 2. Foreign Keys
- Export related data together (Roadmap + Stages + Topics + Categories)
- Use `--natural-foreign` to avoid ID conflicts

### 3. Media Files (Images)
- Fixtures only export database data
- Must transfer media files separately:
  ```bash
  # Transfer media folder
  rsync -avz media/ user@server:/path/to/project/media/
  ```

---

## 🛠️ Useful Commands

### Export Everything:
```bash
python manage.py dumpdata core \
  --exclude core.User \
  --exclude core.UserProgress \
  --indent 2 \
  --output full_core_data.json
```

### Export Specific Roadmap by ID:
```bash
# Get roadmap ID first
python manage.py shell
>>> from core.models import Roadmap
>>> Roadmap.objects.get(title="Control Systems Learning").id
# Say it returns 5

python manage.py dumpdata core.Roadmap core.Stage core.Topic \
  --pks 5 \
  --natural-foreign \
  --indent 2 \
  --output control_systems_roadmap.json
```

### Load with Verbosity:
```bash
python manage.py loaddata roadmaps_data.json -v 2
```

### Check What Will Be Loaded:
```bash
# Just validate, don't load
python manage.py loaddata roadmaps_data.json --dry-run
```

---

## 📂 Recommended Directory Structure

```
your_project/
├── fixtures/              # Create this directory
│   ├── initial_roadmaps.json
│   ├── roadmap_control_systems.json
│   ├── roadmap_web_dev.json
│   └── categories.json
├── import_scripts/        # Optional: keep import scripts
│   ├── import_control_systems.py
│   └── README.md
└── ...
```

Add fixtures to Git:
```bash
git add fixtures/
git commit -m "Add roadmap fixtures for production deployment"
```

---

## 🎯 Quick Reference

### Local Development:
```bash
# Create roadmaps → Test → Export
python manage.py dumpdata core.Roadmap core.Stage core.Topic core.RoadmapCategory \
  --indent 2 --output fixtures/roadmaps.json

git add fixtures/roadmaps.json
git commit -m "Add roadmaps"
git push
```

### Production Deployment:
```bash
# Pull → Load → Restart
git pull origin main
python manage.py loaddata fixtures/roadmaps.json
sudo systemctl restart 99roadmap
```

---

## Summary

**Best method**: Use Django fixtures (`dumpdata` / `loaddata`)

**Why?**
- ✅ Version controlled
- ✅ Repeatable
- ✅ Database-agnostic
- ✅ Handles relationships automatically
- ✅ Industry standard

**Avoid**: Manual entry, direct database copying

**Remember**: Always backup production database before loading new fixtures!

---

Need help with any step? Let me know! 🚀
