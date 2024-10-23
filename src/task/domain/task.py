from uuid import uuid4
from dataclasses import dataclass, field
from .task_errors import TaskAlReadyCompletedError


@dataclass
class Task:
    _id: str = field(default_factory=lambda: str(uuid4()))
    _name: str = field(init=False)
    _description: str = field(init=False)
    _completed: bool = field(init=False, default=False)

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, value: str):
        self._id = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not value or value.isspace():
            raise ValueError("El nombre de la tarea no puede estar vacío")
        self._name = value

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str):
        if not value or value.isspace():
            raise ValueError("La descripción de la tarea no puede estar vacía")
        self._description = value

    @property
    def completed(self) -> bool:
        return self._completed

    @completed.setter
    def completed(self, value: bool):
        if self._completed and value & value:
            raise TaskAlReadyCompletedError()
        self._completed = value
