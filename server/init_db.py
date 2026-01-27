import sqlite3

DB_FILE = "server/meeter.db"

def connect():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

# Create tables
def init_db():
    conn = connect()
    c = conn.cursor()
    
    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password_hash TEXT,
        pfp TEXT,
        banner TEXT,
        status TEXT
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS ignore_list (
        user_id INTEGER,
        ignored_id INTEGER,
        UNIQUE(user_id, ignored_id)
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS block_list (
        user_id INTEGER,
        blocked_id INTEGER,
        UNIQUE(user_id, blocked_id)
    )
    """)

    conn.commit()
    conn.close()

init_db()