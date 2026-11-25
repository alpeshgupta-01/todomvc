"""Sample module with intentionally seeded defects for AI review PoC."""
import sqlite3
import subprocess

API_KEY = "sk_live_51Hardcoded0Secret0Key"          # D1: hard-coded secret


def get_user(conn: sqlite3.Connection, user_id: str):
    # D2: SQL injection
    query = "SELECT * FROM users WHERE id = '" + user_id + "'"
    return conn.execute(query).fetchone()


def apply_discount(amount: float, percent: float) -> float:
    # D3: logic bug - discount added instead of subtracted, no bounds check
    return amount + amount * percent / 100


