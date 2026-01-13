from db.db import get_connection
from models.todo import ToDoList

class ToDoRepo:

    def add(self, todo: ToDoList):
        conn = get_connection()
        c = conn.cursor()
        c.execute(
            "INSERT INTO tasks(task, complete, user_id) VALUES (?, ?, ?)",
            (todo.task_name, int(todo.complete), todo.user_id)
        )
        conn.commit()
        conn.close()

    def delete(self, task_id: int, user_id: int):
        conn = get_connection()
        c = conn.cursor()
        c.execute(
            "DELETE FROM tasks WHERE task_id = ? AND user_id = ?",
            (task_id, user_id)
        )
        conn.commit()
        conn.close()

    def complete(self, task_id: int, user_id: int):
        conn = get_connection()
        c = conn.cursor()
        c.execute(
            "UPDATE tasks SET complete = 1 WHERE task_id = ? AND user_id = ?",
            (task_id, user_id)
        )
        conn.commit()
        conn.close()

    def get(self, task_id: int, user_id: int):
        conn = get_connection()
        c = conn.cursor()
        c.execute(
            "SELECT * FROM tasks WHERE task_id = ? AND user_id = ?",
            (task_id, user_id)
        )
        row = c.fetchone()
        conn.close()
        return row

    def list_all(self, user_id: int):
        conn = get_connection()
        c = conn.cursor()
        c.execute(
            "SELECT * FROM tasks WHERE user_id = ?",
            (user_id,)
        )
        rows = c.fetchall()
        conn.close()
        return rows