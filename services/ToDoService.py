from repositories.todo_repo import ToDoRepo
from models.todo import ToDoList

class ToDoService:

    def __init__(self):
        self.repo = ToDoRepo()

    def add(self, task: str, user_id: int):
        todo = ToDoList(task, False, user_id)
        self.repo.add(todo)
        return todo

    def delete(self, task_id: int, user_id: int):
        self.repo.delete(task_id, user_id)

    def complete(self, task_id: int, user_id: int):
        self.repo.complete(task_id, user_id)

    def get(self, task_id: int, user_id: int):
        task = self.repo.get(task_id, user_id)
        if not task:
            raise ValueError("task not found")
        return task

    def list_all(self, user_id: int):
        return self.repo.list_all(user_id)
