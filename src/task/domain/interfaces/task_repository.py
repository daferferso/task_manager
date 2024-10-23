"""
Interface de implementación de repositorio, SQL, NoSQL, JSON, etc...
"""

from typing import List, Optional
from abc import ABC, abstractmethod
from task.domain.task import Task


class ITaskRepository(ABC):
    """
    Interfaz para el repositorio de tareas el cual define los métodos que deben ser implementados
    para gestionar el almacenamiento de las tareas y/o entidades (Patrón repository).
    """

    @abstractmethod
    def add_task(task: Task):
        """Agrega una nueva tarea al repositorio."""
        pass

    @abstractmethod
    def get_task(task_id: str) -> Optional[Task]:
        """Obtiene una tarea por su ID. Devuelve None si no se encuentra."""
        pass

    @abstractmethod
    def get_tasks() -> List[Task]:
        """Obtiene la lista de todas las tareas en el repositorio."""
        pass

    @abstractmethod
    def update_task(task_id: str, task: Task):
        """Actualiza una tarea existente en el repositorio."""
        pass

    @abstractmethod
    def delete_task(task_id: str):
        """Elimina una tarea por su ID del repositorio."""
        pass
