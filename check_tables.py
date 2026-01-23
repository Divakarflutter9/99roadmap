import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'socialaccount_%';")
tables = cursor.fetchall()

print("Existing socialaccount tables:")
for t in tables:
    print(f"- {t[0]}")

conn.close()
