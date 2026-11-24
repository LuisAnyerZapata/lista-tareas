# Lista de tareas

Una pequeña aplicación de consola en Python para gestionar una lista de tareas.

## Requisitos

- Python 3.10 o superior (se usa `match` / pattern matching).
- No se necesitan dependencias externas: solo la biblioteca estándar (`json`).

## Características

- Añadir nuevas tareas con una descripción.
- Listar todas las tareas registradas.
- Marcar una tarea como hecha.
- Persistencia automática en `tareas.json`.
- Manejo de errores si el archivo no existe o no contiene un JSON válido.
- Menú interactivo en la terminal.

## Uso

1. Clona o descarga este repositorio y entra en la carpeta del proyecto.

2. Ejecuta el script:

   ```bash
   python lista_tareas.py
   ```

   > En algunos sistemas puede ser necesario usar `python3` en lugar de `python`.

3. Elige una opción del menú:

   ```text
   --- Lista de tareas ---
   1. Añadir tarea
   2. Listar tareas
   3. Marcar como hecha
   4. Salir
   ```

   - **1. Añadir tarea**: pide una descripción y guarda la tarea como pendiente.
   - **2. Listar tareas**: muestra el número, el estado (`[x]` hecha / `[ ]` pendiente) y la descripción.
   - **3. Marcar como hecha**: muestra la lista y pide el número de la tarea a marcar.
   - **4. Salir**: termina la aplicación.

El archivo `tareas.json` se crea automáticamente al guardar la primera tarea. Su contenido tiene este formato:

```json
[
  { "descripcion": "Comprar leche", "hecha": false },
  { "descripcion": "Estudiar Python", "hecha": true }
]
```

## Estructura

```text
lista-tareas/
├── .gitignore       # Archivos y carpetas ignorados por Git
├── README.md        # Documentación del proyecto
├── lista_tareas.py  # Código fuente y punto de entrada de la aplicación
└── tareas.json      # Datos persistidos (se ignora en Git)
```
