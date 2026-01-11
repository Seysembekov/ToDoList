from fastapi import APIRouter, HTTPException
from services.ToDoService import ToDoService
from models.todo import ToDoList

router = APIRouter(prefix="/tasks", tags=["Tasks"])
service = ToDoService()


@router.post("/")
def add_task(task: str):
    try:
        todo = service.add(task)
        return {
            "task": todo.task_name,
            "complete": todo.complete
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/")
def list_tasks():
    try:
        tasks = service.listAll()
        return [
            {
                "id": t[0],
                "task": t[1],
                "complete": bool(t[2])
            }
            for t in tasks
        ]
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/{task_id}")
def get_task(task_id: int):
    try:
        t = service.get(task_id)
        return {
            "id": t[0],
            "task": t[1],
            "complete": bool(t[2])
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{task_id}")
def delete_task(task_id: int):
    try:
        service.delete(task_id)
        return {"status": "deleted"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.put("/{task_id}/complete")
def complete_task(task_id: int):
    try:
        service.complete(task_id)
        return {"status": "completed"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))