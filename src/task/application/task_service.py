from typing import List
from dataclasses import dataclass
from task.domain.task import Task
from task.domain.interfaces.task_repository import ITaskRepository
from task.domain.task_errors import TaskNotFound


@dataclass
class TaskService:
    _task_repository: ITaskRepository

    def add_task(self, task_name: str, task_description: str):
        task = Task()
        task.name = task_name
        task.description = task_description
        self._task_repository.add_task(task)

    def get_task(self, task_id: str):
        task: Task = self._task_repository.get_task(task_id)
        if not task:
            raise TaskNotFound()
        return task

    def get_pending_tasks(self):
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
        task: Task = self._task_repository.get_task(task_id)
        if not task:
            raise TaskNotFound()
        self._task_repository.delete_task(task_id)

    def mark_task_as_completed(self, task_id: str):
        task: Task = self._task_repository.get_task(task_id)
        if not task:
            raise TaskNotFound()
        task.completed = True
        self._task_repository.update_task(task_id, task)
