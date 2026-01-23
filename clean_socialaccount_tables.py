import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Tables to drop
tables = [
    'socialaccount_socialapp_sites',
    'socialaccount_socialapp',
    'socialaccount_socialtoken',
    'socialaccount_extra_data', 
    'socialaccount_socialaccount'
]

for table in tables:
    try:
        cursor.execute(f"DROP TABLE IF EXISTS {table}")
        print(f"Dropped table {table}")
    except Exception as e:
        print(f"Error dropping {table}: {e}")

# Also clean migration history
cursor.execute("DELETE FROM django_migrations WHERE app = 'socialaccount'")
print("Cleaned migration history for socialaccount")

conn.commit()
conn.close()
