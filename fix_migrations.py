import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Remove socialaccount migrations from history so we can re-apply correctly
cursor.execute("DELETE FROM django_migrations WHERE app = 'socialaccount'")
conn.commit()
print("Removed socialaccount from migration history.")
conn.close()
