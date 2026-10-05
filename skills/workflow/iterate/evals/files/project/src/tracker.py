"""Mossgate Habits core (invented example)."""

import sqlite3


class Tracker:
    def __init__(self, path: str = "habits.db") -> None:
        self.db = sqlite3.connect(path)
        self.db.execute("CREATE TABLE IF NOT EXISTS habit (name TEXT PRIMARY KEY)")
        self.db.execute("CREATE TABLE IF NOT EXISTS checkin (habit TEXT, day TEXT)")

    def add_habit(self, name: str) -> None:
        self.db.execute("INSERT INTO habit (name) VALUES (?)", (name,))
        self.db.commit()

    def check_in(self, name: str, day: str) -> None:
        self.db.execute("INSERT INTO checkin (habit, day) VALUES (?, ?)", (name, day))
        self.db.commit()
