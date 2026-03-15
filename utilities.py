#!/usr/bin/env python3

# TODO: Crear archivo "consultas.py" para las consultas específicas y el graficado

# Libraries
from os import register_at_fork
from os.path import join
import time
from pathlib import Path # Encargado de crear un objeto "Path" para el subdirectorio

# Import script
from tools import limpiar_pantalla

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
            right_answers = input("\nPor favor, inserte 10 carácteres en mayúscula (Permitidos: A, B, C, D): ")

            # All: Recorre todos los carácteres de "right_answers". Devuelve "True" si 
            # todos los carácteres insertados son A, B, C o D

            if (all(char in allowed_chars for char in right_answers) and len(right_answers) == 10):
                # Si la cadena es válida, se almacena la respuesta
                with open(target_file, "w") as f_w: # "w" para sobreescribir el contenido
                    f_w.write(right_answers)
                    print("[+] ¡Respuestas correctas guardadas exitosamente!")
                break
            else:
                print("[*] Respuesta inválida. Longitud válida: 10 | Carácteres permitidos: A, B, C, D")
        except ValueError:
            print("[|-|] Error. Valor insertado inválido (A, B, C, D)")

# Registrar alumno
def registrar_alumno():
    target_file = asignar_ruta("alumnos.txt")
    
    # Se verifica que no hayan más de 30 registros de respuestas de alumnos
    try:
        with open(target_file, "r") as f_r:
            if (len(f_r.readlines()) >= 30):
                print("[*] El archivo ha llegado a su límite de 30 registros")
                return
            
    except FileNotFoundError: pass

    while True:
        try:
            # Recibimos la CLAVE y el nombre completo del alumno
            student = input("\nPor favor, inserte la CLAVE del alumno y su Nombre Completo (XXXX Nombre Del Alumno): ")
            

            # Split: Separa los elementos de una string cuando detecta un espacio " "
            student_clean = student.strip().split()

            # Verificar que se insertaron más de 1 elementoo y si la clave es de exactamente 4 carácteres
            if (len(student_clean) < 2 or len(student_clean[0]) != 4):
                print("\nRespuesta inválida. Debe ingresarse la CLAVE (4 carácteres) y el Nombre Del Alumno (Separados por un espacio)")
                continue # Reinicia el bucle
            
            # Strip: Elimina espacios " " y saltos de línea "\n"
            # maxsplit: Deja de separar elementos cuando se ha dividido 1 elemento

            # Removemos espacios y saltos de línea al inicio y final de la línea (strip), para después 
            # obtener el primer elemento (La clave) de la string, la cual se asigna a "student_code" 
            student_code = student_clean[0]
            
            # Recreamos el nombre, pues el usuario puede insertar algo como "ADG2   Jorge Castillos",
            # separador.Join(string): De esta manera, se omite el elemento 1 (CLAVE) y se reconstruye el nombre
            # NO evita casos como "ADG2 Jorge      Castillos"
            student_full_name = " ".join(student_clean[1:])

            # Se verifica que la clave insertada no existe en el sistema
            clave_existe = False
            try:
                with open(target_file, "r") as f_r:
                    for line in f_r:
                        code = line.split()[0] # Obtenemos únicamente la Clave del alumno
                        if not code: continue # Cuando un elemento está vacío, se interpreta como "False". Por ello, si hay una línea vacía, se salta
                    
                        if (student_code == code):
                            print("[*] La clave ya está siendo usada por otro alumno")
                            clave_existe = True
                            break
            
            # Si el archivo no existe, se evita que el programa falle (Después del except se creará)
            except FileNotFoundError:
                print("[*] El archivo no existe. Creándolo...")
                time.sleep(1)
            
            # Si la clave no existe, se registrará el usuario
            if (not clave_existe):
                with open(target_file, "a") as f_a:
                    f_a.write(f"{student_code} {student_full_name}\n")
                    print("[!] ¡Alumno registrado exitosamente!")
                    break

        except ValueError:
            print("\n[|-|] Error. Valor insertado inválido (XXXX Nombre Del Alumno)")

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
    # limpiar_pantalla()
    # print("uwu")
    # time.sleep(2)
    # -------------------------------
