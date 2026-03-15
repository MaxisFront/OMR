#!/usr/bin/env python3

# TODO: Crear archivo "consultas.py" para las consultas específicas y el graficado

# Libraries
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
                print("[*] Respuesta inválida. Longitud válida: 10 | Carácteres permitidos: A, B, C, D.")
        except ValueError:
            print("[|-|] Error. Valor insertado inválido (A, B, C, D).")

# Registrar alumno
def registrar_alumno():
    target_file = asignar_ruta("alumnos.txt")
    
    # Se verifica que no hayan más de 30 registros de respuestas de alumnos
    try:
        with open(target_file, "r") as f_r:
            if (len(f_r.readlines()) >= 30):
                print("[*] El archivo ha llegado a su límite de 30 registros.")
                return
            
    except FileNotFoundError: pass

    while True:
        try:
            # Recibimos la CLAVE y el nombre completo del alumno
            student = input("\nPor favor, inserte la CLAVE del (la) estudiante y su Nombre Completo (XXXX Nombre Del Alumno): ")
            

            # Split: Separa los elementos de una string cuando detecta un espacio " "
            student_clean = student.strip().split()

            # Verificar que se insertaron más de 1 elementoo y si la clave es de exactamente 4 carácteres
            if (len(student_clean) < 2 or len(student_clean[0]) != 4):
                print("\n[*] Respuesta inválida. Debe ingresarse la CLAVE (4 carácteres) y el Nombre Del Alumno (Separados por un espacio).")
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
            code_exist = False
            try:
                with open(target_file, "r") as f_r:
                    for line in f_r:
                        file_line = line.split() # Separamos en partes la línea
                        if not file_line: continue # Cuando un elemento está vacío, se interpreta como "False". Por ello, si hay una línea vacía, se salta
                        
                        # Tras haber verificado que hay contenido en "file_line" (Posibilidad de una línea vacía), podemos asignar 
                        # el valor de "code" tranquilamente
                        code = line.split()[0] # Obtenemos únicamente la Clave del alumno
                        if (student_code == code):
                            print("[*] La clave ya está siendo usada por otro alumno.")
                            code_exist = True
                            break
            
            # Si el archivo no existe, se evita que el programa falle (Después del except se creará)
            except FileNotFoundError:
                print("[*] El archivo no existe. Creándolo...")
                time.sleep(1)
            
            # Si la clave no existe, se registrará el usuario
            if (not code_exist):
                with open(target_file, "a") as f_a:
                    f_a.write(f"{student_code} {student_full_name}\n")
                    print("\n[!] ¡Alumno registrado exitosamente!")
                    break

        except ValueError:
            print("\n[|-|] Error. Valor insertado inválido (XXXX Nombre Del Alumno).")

# Registrar respuestas de un alumno
def registrar_respuestas_alumno():
    target_file = asignar_ruta("respuestas_alumnos.txt")
    students_file = asignar_ruta("alumnos.txt")
    
    while True:
            
        try:
            # Recibimos la CLAVE y respuestas del estudiante
            student = input("\nPor favor, inserte la CLAVE y las respuestas del (la) estudiante (XXXX Respuestas): ")
        
            student_clean = student.strip().split()
            
            # Se verifica que se haya insertado la CLAVE y respuestas, así como que la CLAVE tiene
            # de longitud "4" carácteres | Por último, verifica que no se hayan insertado más de 10 respuestas
            if (len(student_clean) != 2 or len(student_clean[0]) != 4 or len(student_clean[1]) > 10 ):
                print("\n[*] Respuesta inválida. Debe ingresarse la CLAVE (4 carácteres) y las respuestas (No mayor a 10 carácteres).")
                continue
            
            # Obtenemos los valores separados (Clave y respuestas)
            student_code = student_clean[0]
            student_grade = student_clean[1]
        
            code_exist = False
            try: 
                # Verificamos que exista la clave insertada por el usuario en el archivo "datos/alumnos.txt"
                with open(students_file, "r") as f_r:
                    for line in f_r:
                        file_line = line.split()
                        if not file_line: continue
                    
                        code = file_line[0]
                        if (student_code == code):
                            code_exist = True
                            break

            except FileNotFoundError:
                print("\n[*] Error. Aún no se han registrado estudiantes")
            
            answer_already_registered = False
            try:
                # Verificamos que no se haya insertado una calificación en "datos/respuestas_alumnos.txt" anteriormente
                with open(target_file, "r") as f_r:
                    for line in f_r:
                        file_line = line.split()
                        if not file_line: continue
                        
                        code = file_line[0]
                        if (student_code == code):
                            answer_already_registered = True
                            break

            except FileNotFoundError:
                pass # Es normal si aún no se ha registrado la primera calificación


                    
            # Si el código no existe, se reinicia el bucle
            if (not code_exist):
                print("\n[*] La clave insertada no existe. Por favor, verifique el valor insertado.")
                continue
            
            if (answer_already_registered):
                print("\n[*] Ya se ha registrado una calificación para este estudiante")
                continue

            # Insertar "?" cuando falten respuestas (ABCD??????)
            if (len(student_grade) < 10):
                student_grade = student_grade.ljust(10, "?")

            with open(target_file, "a") as f_a:
                f_a.write(f"{student_code} {student_grade}\n")
                print("\n[!] ¡Respuestas registradas exitosamente!")
                break
        
        except ValueError:
            print("\n[|-|] Error. Valor insertado inválido (XXXX XXXXXXXXXX)")


# Realizar calificado
def realizar_calificado():
    target_file = asignar_ruta("calificaciones.txt")
    

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
