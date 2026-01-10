from db.db import get_connection

from models.todo import ToDoList


class ToDoRepo:
    def __init__(self):
        self.model = ToDoList

    def addTaskRepo(self, task: ToDoList):
        conn = get_connection()
        c = conn.cursor()

        c.execute(
            "INSERT INTO tasks (task) VALUES (?)",
            (task.task_name,)
        )

        conn.commit()
        conn.close()
    def deleteTask(self, task_id):
        conn = get_connection()
        c = conn.cursor()

        c.execute("DELETE FROM tasks WHERE task_id = (?)", (task_id,))



        conn.commit()
        conn.close()

    def completeTask(self, task_id):
        conn = get_connection()
        c = conn.cursor()

        c.execute("UPDATE tasks SET complete = 1 WHERE task_id = (?)", (task_id,))


        conn.commit()
        conn.close()

    def listTasks(self):
        conn = get_connection()
        c = conn.cursor()

        c.execute("SELECT * FROM tasks;")
        exists = c.fetchall()

        conn.commit()
        conn.close()
        return exists

    def existsByTask(self, task: str) -> bool:
        conn = get_connection()
        c = conn.cursor()

        c.execute(
            "SELECT 1 FROM tasks WHERE task = ? LIMIT 1",
            (task,)
        )

        exists = c.fetchone() is not None
        conn.close()

        return exists

    def getByIndex(self, task_id):
        conn = get_connection()
        c = conn.cursor()

        c.execute("SELECT * FROM tasks WHERE task_id = (?)", (task_id,))

        exists = c.fetchone()
        conn.commit()
        conn.close()

        return exists