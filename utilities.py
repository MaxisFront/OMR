#!/usr/bin/env python3

# TODO: Crear archivo "consultas.py" para las consultas específicas y el graficado

# Libraries
import time
from pathlib import Path # Encargado de crear un objeto "Path" para el subdirectorio

# Import script
import main

# Variables
SUBFOLDER = Path("datos")

# Asignar la ruta y nombre del archivo a crear
def asignar_ruta(file_name):

    # Crea el subdirectorio "datos" si no existe
    SUBFOLDER.mkdir(exist_ok=True)

    # Asignamos la ruta completa del archivo (datos/nombre_archivo)
    # y lo devolvemos a la función que llamó a "asignar_ruta()"
    return SUBFOLDER / file_name


# Registrar respuestas correctas
def registrar_respuestas_correctas():
    target_file = asignar_ruta("respuestas_correctas.txt")
    allowed_chars = {"A", "B", "C", "D"}

    while True:
        try:
            right_answers = input("Por favor, inserte 10 carácteres (Permitidos: A, B, C, D): ")

            # All: Recorre todos los carácteres de "right_answers". Devuelve "True" si 
            # todos los carácteres insertados son A, B, C o D
            if (all(char in allowed_chars for char in right_answers) and len(right_answers) == 10):
                
                # Si la cadena es válida, se almacena la respuesta
                with open(target_file, "w") as f: # "w" para sobreescribir el contenido
                    f.write(right_answers)
                    print("[+] ¡Respuestas correctas guardadas exitosamente!")
                break
        except:
            pass

# Registrar alumno
def registrar_alumno():
    target_file = asignar_ruta("alumnos.txt")

    print("")

# Registrar respuestas de un alumno
def registrar_respuestas_alumno():
    target_file = asignar_ruta("respuestas_alumnos.txt")

    print("")

# Realizar calificado
def realizar_calificado():
    target_file = asignar_ruta("calificaciones.txt")

    print("")


if __name__ == "__main__":
    print("ERROR. Script 'utilidades.py' ejecutado directamente")
    
    # Debugging stuff
    # -------------------------------
    # main.limpiar_pantalla()
    # registrar_respuestas_correctas()

    # registrar_respuestas_correctas()
    # main.limpiar_pantalla()
    # print("uwu")
    # time.sleep(2)
    # -------------------------------
