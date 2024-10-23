"""
Errores de dominio.
"""


class TaskAlReadyCompletedError(Exception):
    """
    Excepción cuando se intenta completar una tarea que ya está completada.
    """

    def __init__(self, msg="La tarea ya se encuentra marcada como hecha"):
        super().__init__(msg)


class TaskNotFound(Exception):
    """
    Excepción cuando no se encuentra una tarea.
    """

    def __init__(self, msg="La tarea no fue encontrada"):
        super().__init__(msg)
