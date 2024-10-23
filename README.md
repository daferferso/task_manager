# Task Manager
Esta es una aplicación para gestionar tareas.
Basada en la arquitectura hexagonal.
Permite agregar, eliminar,
marcar como completadas y listar tareas pendientes.

## Requisitos

Asegúrate de tener Python 3.11 o superior instalado en tu sistema.

## Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/daferferso/task_manager
   cd task_manager
   ```
2. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución en CLI

Para ejecutar la aplicación en la línea de comandos, utiliza el siguiente comando:

```bash
python .src/main_cli.py
```

Esto te permitirá interactuar con la aplicación a través de la consola.

## Ejecución con FastAPI

Si prefieres ejecutar la aplicación utilizando FastAPI, puedes hacerlo con el siguiente comando:

```bash
python ./src/main_api.py
```

Luego, abre tu navegador y visita:

```
http://localhost:8000/docs
```

Esto te llevará a la documentación interactiva de la OpenAPI, donde podrás probar todos los endpoints disponibles.

## Uso

Una vez que la aplicación esté en ejecución, podrás agregar, eliminar y gestionar tus tareas.
Sigue las instrucciones en la consola o utiliza la interfaz de FastAPI.

## Contribuciones

Si deseas contribuir a este proyecto, siéntete libre de abrir un **issue** o enviar un **pull request**.

## Licencia

Este proyecto está bajo la licencia MIT.
