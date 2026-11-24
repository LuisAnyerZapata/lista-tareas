import json

RUTA_TAREAS = "tareas.json"

def cargar_tareas(ruta):
    tareas = []

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            tareas = json.load(archivo)
    except FileNotFoundError:
        print(f"{ruta} no existe; empezamos con la lista vacía.")
    except json.JSONDecodeError as error:
        print(f"{ruta} existe pero su contenido no es JSON válido.")
        print(f"Detalle: {error}")
        tareas = []

    return tareas

def guardar_tareas(ruta, tareas):
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(tareas, archivo, indent=2, ensure_ascii=False)

def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas registradas.")
        return

    for indice, tarea in enumerate(tareas, start=1):
        marca = "x" if tarea["hecha"] else " "
        print(f"{indice}. [{marca}] {tarea['descripcion']}")
    
def marcar_tarea_hecha(tareas, ruta):
    if not tareas:
        print("No hay tareas para marcar.")
        return

    mostrar_tareas(tareas)

    try:
        numero = int(input("Número de tarea a marcar como hecha: "))
    except ValueError:
        print("Debes introducir un número entero.")
        return

    if 1 <= numero <= len(tareas):
        tareas[numero - 1]["hecha"] = True
        guardar_tareas(ruta, tareas)
        print("Tarea marcada como hecha.")
    else:
        print(f"El número debe estar entre 1 y {len(tareas)}.")

def main ():
    tareas = cargar_tareas(RUTA_TAREAS)

    while True:
        print("\n--- Lista de tareas ---")
        print("1. Añadir tarea")
        print("2. Listar tareas")
        print("3. Marcar como hecha")
        print("4. Salir")

        opcion = input("Elige una opción: ").strip()

        match opcion:
            case "1":
                descripcion = input("Descripción de la tarea: ").strip()

                if not descripcion:
                    print("La descripción no puede estar vacía.")
                    continue

                tareas.append({"descripcion": descripcion, "hecha": False})
                guardar_tareas(RUTA_TAREAS, tareas)
                print("Tarea añadida.")
            case "2":
                mostrar_tareas(tareas)
            case "3":
                marcar_tarea_hecha(tareas, RUTA_TAREAS)
            case "4":
                print("¡Hasta luego!")
                break
            case _:
                print("Opción no válida.")

if __name__ == "__main__":
    main()