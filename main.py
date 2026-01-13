from fastapi import FastAPI
from api.todo_router import router as todo_router
from api.auth_router import router as auth_router
from services.userService import UserService
from services.ToDoService import ToDoService

app = FastAPI(title="Todo API")

app.include_router(auth_router)
app.include_router(todo_router)

todo = UserService()
a = todo.register('islam', '21gdg')
#
# a = ToDoService()
# b = a.add('gasgas', 1)

