"""
Patron de arquitectura Hexagonal
Capa de dominio - definición de la entidad (Task) validaciones del negocio.
"""

from uuid import uuid4
from dataclasses import dataclass, field
from .task_errors import TaskAlReadyCompletedError


@dataclass
class Task:
    """
    Representa una tarea con un ID, nombre, descripción y estado de completado.
    """

    _id: str = field(default_factory=lambda: str(uuid4()))
    _name: str = field(init=False)
    _description: str = field(init=False)
    _completed: bool = field(init=False, default=False)

    @property
    def id(self) -> str:
        """Devuelve el ID de la tarea."""
        return self._id

    @id.setter
    def id(self, value: str):
        """Establece el ID de la tarea."""
        self._id = value

    @property
    def name(self) -> str:
        """Devuelve el nombre de la tarea."""
        return self._name

    @name.setter
    def name(self, value: str):
        """Establece el nombre de la tarea. Lanza ValueError si está vacío."""
        if not value or value.isspace():
            raise ValueError("El nombre de la tarea no puede estar vacío")
        self._name = value

    @property
    def description(self) -> str:
        """Devuelve la descripción de la tarea."""
        return self._description

    @description.setter
    def description(self, value: str):
        """Establece la descripción de la tarea. Lanza ValueError si está vacía."""
        if not value or value.isspace():
            raise ValueError("La descripción de la tarea no puede estar vacía")
        self._description = value

    @property
    def completed(self) -> bool:
        """Devuelve True si la tarea está completada, False si no."""
        return self._completed

    @completed.setter
    def completed(self, value: bool):
        """
        Marca la tarea como completada o no
        Lanza TaskAlReadyCompletedError si es que ya está.
        """
        if self._completed and value & value:
            raise TaskAlReadyCompletedError()
        self._completed = value
