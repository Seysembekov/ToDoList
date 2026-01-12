from fastapi import APIRouter, HTTPException, Depends
from models.dependencies import get_current_user
from services.ToDoService import ToDoService

router = APIRouter(prefix="/tasks", tags=["Tasks"])
service = ToDoService()

@router.post("/")
def add_task(task: str, current_user = Depends(get_current_user)):
    todo = service.add(task=task, user_id=current_user.user_id)
    return {
        "task": todo.task_name,
        "complete": todo.complete
    }

@router.get("/")
def list_tasks(current_user = Depends(get_current_user)):
    tasks = service.listAll(current_user.user_id)
    return [
        {"id": t[0], "task": t[1], "complete": bool(t[2])}
        for t in tasks
    ]

@router.get("/{task_id}")
def get_task(task_id: int, current_user = Depends(get_current_user)):
    t = service.get(task_id, current_user.user_id)
    return {"id": t[0], "task": t[1], "complete": bool(t[2])}

@router.delete("/{task_id}")
def delete_task(task_id: int, current_user = Depends(get_current_user)):
    service.delete(task_id, current_user.user_id)
    return {"status": "deleted"}

@router.put("/{task_id}/complete")
def complete_task(task_id: int, current_user = Depends(get_current_user)):
    service.complete(task_id, current_user.user_id)
    return {"status": "completed"}