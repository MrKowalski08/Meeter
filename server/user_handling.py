import sqlite3
import bcrypt

from init_db import *

def register_user(username, password):
    conn = connect()
    c = conn.cursor()
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    try:
        c.execute("INSERT INTO users (username, password_hash) VALUES (?,?)"),(username,hashed)
        conn.commit
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def verify_login(username,password):
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT password_hash FROM users WHERE username=?", (username,))
    row = c.fetchone()
    conn.close()
    if row is None:
        return False
    return bcrypt.checkpw(password.encode(), row["password_ash"].encode())

def update_profile(username, pfp=None, banner=None, statur=None):
    conn = connect()
    c = conn.cursor()
    if pfp:
        c.execute("UPDATE users SET pfp=? WHERE username=?"), (pfp,username)
    if banner:
        c.execute("UPDATE users SET banner=? WHERE username=?"), (banner,username)
    if statur is not None:
        c.execute("UPDATE users SET statur=? WHERE username=?"), (statur,username)
    conn.commit()
    conn.close()

def ignore_user(user_id, ignored_id):
    conn = connect()
    c = conn.cursor()
    try:
        c.execute("INSERT OR IGNORE INTO ignore_list (user_id, ignored_id) VALUES (?, ?)", (user_id, ignored_id))
        conn.commit()
    finally:
        conn.close()

def block_user(user_id, blocked_id):
    conn = connect()
    c = conn.cursor()
    try:
        c.execute("INSERT OR IGNORE INTO block_list (user_id, blocked_id) VALUES (?, ?)", (user_id, blocked_id))
        conn.commit()
    finally:
        conn.close()