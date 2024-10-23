"""
Capa de infrastructura - Implementación de repositorio en JSON
"""

import json
from typing import List, Optional
from task.domain.task import Task
from task.domain.interfaces.task_repository import ITaskRepository


class TaskRepositoryJson(ITaskRepository):
    """
    Implementación de ITaskRepoitory que almacena tareas en un archivo JSON.

    Atributos:
        filename (str): Nombre del archivo donde se almacenan las tareas.
        _data (List[Task]): Lista de tareas cargadas desde el archivo.
    """

    def __init__(self, filename):
        """
        Inicializa el repositorio con el nombre del archivo y carga los datos existentes.

        Parámetros:
            filename (str): Nombre del archivo donde se guardan las tareas.
        """
        self.filename = filename
        self._data: List[Task] = []
        self._load_data()

    def add_task(self, task: Task):
        """
        Agrega una nueva tarea al repositorio y guarda los cambios en el archivo.

        Parámetros:
            task (Task): La tarea a agregar.
        """
        self._data.append(task)
        self._save_data()

    def get_task(self, task_id: str) -> Optional[Task]:
        """
        Obtiene una tarea por su ID.

        Parámetros:
            task_id (str): ID de la tarea a obtener.

        Retorna:
            Optional[Task]: La tarea solicitada o None si no se encuentra.
        """
        for i, obj in enumerate(self._data):
            if obj.id == task_id:
                return self._data[i]

    def get_tasks(self) -> List[Task]:
        """
        Obtiene todas las tareas.

        Retorna:
            List[Task]: Lista de todas las tareas.
        """
        return self._data

    def update_task(self, task_id: str, task: Task):
        """
        Actualiza una tarea existente en el repositorio y guarda los cambios en el archivo.

        Parámetros:
            task_id (str): ID de la tarea a actualizar.
            task (Task): Objeto de tarea con los nuevos datos.
        """
        for i, obj in enumerate(self._data):
            if obj.id == task_id:
                self._data[i] = task
                return self._save_data()

    def delete_task(self, task_id: str):
        """
        Elimina una tarea por su ID y guarda los cambios en el archivo.

        Parámetros:
            task_id (str): ID de la tarea a eliminar.
        """
        for i, obj in enumerate(self._data):
            if obj.id == task_id:
                self._data.pop(i)
                return self._save_data()

    def _load_data(self):
        """
        Carga las tareas desde el archivo JSON. Si el archivo no existe, inicializa la lista vacía.
        """
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data_loaded = json.load(f)
                self._data = [
                    self._convert_dict_to_task(task_dict) for task_dict in data_loaded
                ]
        except FileNotFoundError:
            self._data = []

    def _save_data(self):
        """
        Guarda las tareas actuales en el archivo JSON.
        """
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(
                [self._convert_task_to_dict(task) for task in self._data], f, indent=4
            )

    def _convert_task_to_dict(self, task: Task) -> dict:
        """
        Convierte un objeto Task a un diccionario.

        Parámetros:
            task (Task): La tarea que se deberá convertir.

        Retorna:
            dict: La tarea convertida a tipo diccionario.
        """
        return {
            "id": task.id,
            "name": task.name,
            "description": task.description,
            "completed": task.completed,
        }

    def _convert_dict_to_task(self, task_dict: dict) -> Task:
        """
        Convierte un diccionario a un objeto Task.

        Parámetros:
            task_dict (dict): Diccionario con los datos de la tarea.

        Retorna:
            Task: El objeto Task creado a partir del diccionario.
        """
        task = Task()
        task.id = task_dict["id"]
        task.name = task_dict["name"]
        task.description = task_dict["description"]
        task.completed = task_dict["completed"]
        return task
