import os
from task.application.task_service import TaskService
from task.infrastructure.task_repository_json import TaskRepositoryJson

task_repository = TaskRepositoryJson("./data.json")
task_service = TaskService(task_repository)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def paint_display(choices):
    clear_screen()
    print("Opciones:")
    for key, value in choices.items():
        print(f"{key}. {value}")


if __name__ == "__main__":
    FIRST_CHOICES = {
        "1": "Añadir tarea",
        "2": "Listar tareas pendientes",
        "3": "Salir",
    }

    while True:
        paint_display(FIRST_CHOICES)
        choice = input("Elige una opción: ")

        if choice == "1":
            name = input("Nombre: ")
            description = input("Descripción: ")
            task_service.add_task(name, description)
        elif choice == "3":
            break
        else:
            print("Opción incorrecta, intenta de nuevo")
        input("Presiona cualquier tecla para continuar")
