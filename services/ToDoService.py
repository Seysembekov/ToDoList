from models.todo import ToDoList
from repositories.todo_repo import ToDoRepo

class ToDoService:
    def __init__(self):
        self.repo = ToDoRepo()


    def add(self, task):

        todo = ToDoList(task)
        self.repo.addTaskRepo(todo)
        return todo

    def delete(self, task_id):
        if not self.repo.getByIndex(task_id):
            raise ValueError('task doesnt exist')

        self.repo.deleteTask(task_id)

    def complete(self, task_id):
        a = self.repo.completeTask(task_id)
        return a


    def get(self, task_id):
        if not self.repo.getByIndex(task_id):
            raise ValueError('task doesnt exist')

        a = self.repo.getByIndex(task_id)
        return a

    def listAll(self):
        if len(self.repo.listTasks()) <1:
            raise ValueError('hasnt data')

        return self.repo.listTasks()




