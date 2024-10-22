from typing import List, Optional
from abc import ABC, abstractmethod
from src.task.domain.task import Task


class ITaskRepository(ABC):
    @abstractmethod
    def add_task(task: Task):
        pass

    @abstractmethod
    def get_task(task_id: str) -> Optional[Task]:
        pass

    @abstractmethod
    def get_tasks() -> List[Task]:
        pass

    @abstractmethod
    def update_task(task_id: str, task: Task):
        pass

    @abstractmethod
    def delete_task(task_id: str):
        pass
