import sqlite3
from datetime import datetime

# This connects to the database, or makes one if there isn't one already.
conn = sqlite3.connect('calendar_data.db')
cursor = conn.cursor()

# Create tables for reminders, notes, and events
cursor.execute('''CREATE TABLE IF NOT EXISTS reminders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    due_date TEXT,
                    completed INTEGER)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS notes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    content TEXT,
                    created_at TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    start_time TEXT,
                    end_time TEXT,
                    location TEXT)''')

conn.commit()

# Adding reminders ("nudges")
def add_reminder(title, due_date):
    cursor.execute("INSERT INTO reminders (title, due_date, completed) VALUES (?, ?, ?)", (title, due_date, 0))
    conn.commit()
    print(f"Reminder '{title}' added for {due_date}.")

# Viewing Reminders

def view_reminders():
    cursor.execute("SELECT * FROM reminders WHERE completed = 0")
    reminders = cursor.fetchall()
    for reminder in reminders:
        print(f"{reminder[0]}. {reminder[1]} - Due: {reminder[2]}")

# Marking reminders as completed

def complete_reminder(reminder_id):
    cursor.execute("UPDATE reminders SET completed = 1 WHERE id = ?", (reminder_id,))
    conn.commit()
    print(f"Reminder {reminder_id} marked as completed.")

# Adding Notes and viewing them

def add_note(content):
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO notes (content, created_at) VALUES (?, ?)", (content, created_at))
    conn.commit()
    print(f"Note added: {content}")

def view_notes():
    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()
    for note in notes:
        print(f"{note[0]}. {note[1]} (Created at: {note[2]})")


# Adding and viewing calendar events.

def add_event(title, start_time, end_time, location):
    cursor.execute("INSERT INTO events (title, start_time, end_time, location) VALUES (?, ?, ?, ?)",
                   (title, start_time, end_time, location))
    conn.commit()
    print(f"Event '{title}' scheduled from {start_time} to {end_time} at {location}.")

def view_events():
    cursor.execute("SELECT * FROM events")
    events = cursor.fetchall()
    for event in events:
        print(f"{event[0]}. {event[1]} from {event[2]} to {event[3]} at {event[4]}")

