from fastapi import FastAPI
from api.todo_router import router

app = FastAPI(title="Todo API")
app.include_router(router)
