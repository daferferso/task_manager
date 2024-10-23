import json
from typing import List, Optional
from task.domain.task import Task
from task.domain.interfaces.task_repository import ITaskRepository


class TaskRepositoryJson(ITaskRepository):
    def __init__(self, filename):
        self.filename = filename
        self._data: List[Task] = []
        self._load_data()

    def add_task(self, task: Task):
        self._data.append(task)
        self._save_data()

    def get_task(self, task_id: str) -> Optional[Task]:
        for i, obj in enumerate(self._data):
            if obj.id == task_id:
                return self._data[i]

    def get_tasks(self) -> List[Task]:
        return self._data

    def update_task(self, task_id: str, task: Task):
        for i, obj in enumerate(self._data):
            if obj.id == task_id:
                self._data[i] = task
                return self._save_data()

    def delete_task(self, task_id: str):
        for i, obj in enumerate(self._data):
            if obj.id == task_id:
                self._data.pop(i)
                return self._save_data()

    def _load_data(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data_loaded = json.load(f)
                self._data = [
                    self._convert_dict_to_task(task_dict) for task_dict in data_loaded
                ]
        except FileNotFoundError:
            self._data = []

    def _save_data(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(
                [self._convert_task_to_dict(task) for task in self._data], f, indent=4
            )

    def _convert_task_to_dict(self, task: Task) -> dict:
        return {
            "id": task.id,
            "name": task.name,
            "description": task.description,
            "completed": task.completed,
        }

    def _convert_dict_to_task(self, task_dict: dict) -> Task:
        task = Task()
        task.id = task_dict["id"]
        task.name = task_dict["name"]
        task.description = task_dict["description"]
        task.completed = task_dict["completed"]
        return task
