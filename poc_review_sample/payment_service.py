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
    percent = max(0.0, min(percent, 100.0))
    return amount - amount * percent / 100


def average(values: list[float]) -> float:
    # D4: division by zero on empty list
    return sum(values) / len(values)


def get_email(user: dict | None) -> str:
    # D5: None dereference
    return user["email"].lower()


def backup(path: str) -> None:
    # D6: command injection via shell=True
    subprocess.call("tar -czf backup.tgz " + path, shell=True)


def read_config(path: str) -> str:
    # D7: resource leak - file never closed
    f = open(path)
    return f.read()
