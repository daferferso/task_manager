class TaskAlReadyCompletedError(Exception):
    def __init__(self, msg="La tarea ya se encuentra marcada como hecha"):
        super().__init__(msg)


class TaskNotFound(Exception):
    def __init__(self, msg="La tarea no fue encontrada"):
        super().__init__(msg)
