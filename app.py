import os
import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
DATABASE = "/app/todo.db"  # Ensure the correct path inside Docker

# Function to initialize the database
def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT, completed BOOLEAN)"
        )
        conn.commit()

# Ensure database is created before running the app
with app.app_context():
    init_db()

@app.route("/")
def index():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    task = request.form["task"]
    if task:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tasks (task, completed) VALUES (?, ?)", (task, False))
            conn.commit()
    return redirect("/")

@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET completed = ? WHERE id = ?", (True, task_id))
        conn.commit()
    return redirect("/")

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
