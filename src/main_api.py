"""
Capa externa - API (FastAPI)
"""

import uvicorn
from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
from task.application.task_service import TaskService
from task.infrastructure.task_repository_json import TaskRepositoryJson
from task.domain.task_errors import TaskAlReadyCompletedError, TaskNotFound

task_repository = TaskRepositoryJson("./data.json")
task_service = TaskService(task_repository)


class Task(BaseModel):
    """
    Modelo de validación de datos para crear una tarea.

    Atributos:
        name (str): El nombre de la tarea.
        description (str): La descripción de la tarea.
    """

    name: str
    description: str


class TaskResponseModel(BaseModel):
    """
    Modelo de respuesta para una tarea.

    Atributos:
        id (str): El id de la tarea.
        name (str): El nombre de la tarea.
        description (str): La descripción de la tarea.
        completed (bool): El estado de la tarea.
    """

    id: str
    name: str
    description: str
    completed: bool


app = FastAPI()
router = APIRouter(prefix="/tareas")


@router.post("/", status_code=202)
def add_task(task: Task):
    """
    Agrega una nueva tarea.

    Parámetros:
        task (Task): La tarea a agregar.

    Retorna:
        dict: Mensaje de éxito.
    """
    task_service.add_task(task_name=task.name, task_description=task.description)
    return {"message": "Task added successfull"}


@router.delete("/{task_id}")
def delete_task(task_id: str):
    """
    Elimina una tarea por su ID.

    Parámetros:
        task_id (str): El id de la tarea a eliminar.

    Retorna:
        dict: Mensaje de éxito.

    Lanza:
        HTTPException: Si la tarea no se encuentra.
    """
    try:
        task_service.delete_task(task_id=task_id)
        return {"message": "Task deleted successfull"}
    except TaskNotFound:
        raise HTTPException(status_code=404, detail="Task not found")


@router.put("/{task_id}")
def mark_as_completed_task(task_id: str):
    """
    Marca una tarea como completada.

    Parámetros:
        task_id (str): El id de la tarea a marcar como completada.

    Retorna:
        dict: Mensaje de éxito.

    Lanza:
        HTTPException: Si la tarea ya está completada o no se encuentra.
    """
    try:
        task_service.mark_task_as_completed(task_id=task_id)
        return {"message": "Task completed successfull"}
    except TaskAlReadyCompletedError:
        raise HTTPException(status_code=409, detail="Task already completed")
    except TaskNotFound:
        raise HTTPException(status_code=404, detail="Task not found")


@router.get("/")
def get_all_pending_tasks():
    """
    Obtiene todas las tareas pendientes.

    Retorna:
        List[dict]: Lista de tareas pendientes.
    """
    return task_service.get_pending_tasks()


@router.get("/{task_id}", response_model=TaskResponseModel)
def get_task(task_id):
    """
    Obtiene una tarea por su ID.

    Parámetros:
        task_id (str): El identificador de la tarea.

    Retorna:
        TaskResponseModel: La tarea solicitad.

    Lanza:
        HTTPException: Si la tarea no se encuentra.
    """
    try:
        return task_service.get_task(task_id)
    except TaskNotFound:
        raise HTTPException(status_code=404, detail="Task not found")


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main_api:app", host="127.0.0.1", port=8000, reload=True)
