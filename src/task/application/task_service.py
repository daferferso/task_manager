"""
Capa de aplicación - Casos de uso
"""

from typing import List
from dataclasses import dataclass
from task.domain.task import Task
from task.domain.interfaces.task_repository import ITaskRepository
from task.domain.task_errors import TaskNotFound


@dataclass
class TaskService:
    """
    Servicio para gestionar los casos de uso con las tareas.

    Atributos:
        _task_repository (ITaskRepository): Repositorio (inyectado)
    """

    _task_repository: ITaskRepository

    def add_task(self, task_name: str, task_description: str):
        """
        Agrega una nueva tarea al repositorio.

        Parámetros:
            task_name (str): Nombre de la tarea.
            task_description (str): Descripción de la tarea.
        """
        task = Task()
        task.name = task_name
        task.description = task_description
        self._task_repository.add_task(task)

    def get_task(self, task_id: str):
        """
        Obtiene una tarea por su ID.

        Parámetros:
            task_id (str): ID de la tarea a obtener.

        Retorna:
            Task: La tarea solicitada.

        Lanza:
            TaskNotFound: Si no se encuentra la tarea.
        """
        task: Task = self._task_repository.get_task(task_id)
        if not task:
            raise TaskNotFound()
        return task

    def get_pending_tasks(self):
        """
        Obtiene todas las tareas pendientes.

        Retorna:
            List[dict]: Lista de tareas que no han sido completadas, cada una con su ID, nombre,
            descripción y estado de completada.
        """
        tasks: List[Task] = self._task_repository.get_tasks()
        pending_tasks = [
            {
                "id": task.id,
                "name": task.name,
                "description": task.description,
                "completed": task.completed,
            }
            for task in tasks
            if not task.completed
        ]
        return pending_tasks

    def delete_task(self, task_id: str):
        """
        Elimina una tarea por su ID.

        Parámetros:
            task_id (str): ID de la tarea a eliminar.

        Lanza:
            TaskNotFound: Si no se encuentra la tarea.
        """
        task: Task = self._task_repository.get_task(task_id)
        if not task:
            raise TaskNotFound()
        self._task_repository.delete_task(task_id)

    def mark_task_as_completed(self, task_id: str):
        """
        Marca una tarea como completada.

        Parámetros:
            task_id (str): ID de la tarea a marcar como completada.

        Lanza:
            TaskNotFound: Si no se encuentra la tarea.
        """
        task: Task = self._task_repository.get_task(task_id)
        if not task:
            raise TaskNotFound()
        task.completed = True
        self._task_repository.update_task(task_id, task)
