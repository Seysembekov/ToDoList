class ToDoList:
    def __init__(self, task_name: str, complete: bool, user_id: int):
        self.task_name = task_name
        self.complete = complete
        self.user_id = user_id