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


def show_tasks_and_get_choice():
    while True:
        clear_screen()
        tasks = task_service.get_pending_tasks()
        if not tasks:
            print("No hay tareas pendientes.\n")
            input("Presiona enter para continuar")
            return None

        print("Tareas Pendientes:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. Nombre: {task['name']}")

        try:
            choice = int(input("Ingresa el número de la tarea o 0 para volver: "))
            if choice == 0:
                return None
            elif 1 <= choice <= len(tasks):
                selected_task = tasks[choice - 1]
                return selected_task["id"]
            else:
                print("El número de la tarea no es válido")
        except ValueError:
            print("Opción incorrecta, ingresa un número")

        input("Presiona enter para continuar")


if __name__ == "__main__":
    FIRST_CHOICES = {
        "1": "Añadir tarea",
        "2": "Listar tareas pendientes",
        "3": "Salir",
    }
    SECOND_CHOICES = {
        "1": "Eliminar tarea",
        "2": "Marcar tarea como completada",
        "3": "Volver",
    }

    while True:
        paint_display(FIRST_CHOICES)
        choice = input("Elige una opción: ")

        if choice == "1":
            name = input("Nombre: ")
            description = input("Descripción: ")
            task_service.add_task(name, description)
        elif choice == "2":
            task_id = show_tasks_and_get_choice()
            if task_id:
                while True:
                    paint_display(SECOND_CHOICES)
                    action_choice = input("Elige una opción: ")
                    if action_choice == "1":
                        task_service.delete_task(task_id)
                        print("La tarea se eliminó")
                        break
                    elif action_choice == "2":
                        task_service.mark_task_as_completed(task_id)
                        print("Tarea completada")
                        break
                    elif action_choice == "3":
                        break
                    else:
                        print("Opción incorrecta, ingresa un número")
                    input("Presiona enter para continuar")
        elif choice == "3":
            break
        else:
            print("Opción incorrecta, intenta de nuevo")
        input("Presiona enter para continuar")
