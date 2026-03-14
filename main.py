#!/usr/bin/env python3

# option: Respuesta del usuario
# TODO: Limpiar la consola para evitar acumulación de texto (library OS)
# TODO: Lógica para el submenú
# TODO: Implementar lógica para llamar a consultas

# Libraries
import time

# Import script
import utilities

from utilities import printowo

def menu():
    print("\n" + "="* 40)
    print("SISTEMA DE CALIFICACIÓN POR LÁSER ÓPTICO\n")
    
    
    print("1) Registrar respuestas correctas")
    print("2) Registrar alumno")
    print("3) Registrar respuesta de alumno")
    print("4) Realizar calificado")
    print("5) Desplegar consultas específicas")
    print("6) Salir")

    print("\n" + "="* 40 + "\n")


def consultas():
    print("\n" + "="* 40)

    print("DESPLEGANDO SUBMENÚ...\n")
    print("1) Calificaciones generales")
    print("2) Calificación de un estudiante")
    print("3) Top 3 calificaciones")
    print("4) Promedio de aciertos por reactivo")
    print("5) Graficación (Top 3 y calificaciones)")
    print("6) Regresar al menú")

    print("\n" + "="* 40 + "\n")

def utilidades(option):

    # Llamar al archivo utilidades y realizar la lógica respectiva de cada opción
    pass

    # Debugigng stuff
    # ---------------------------
    #uwu = input("choting uwu: ")
    #if (uwu == "uwu"):
    #    print("awa")
    # ---------------------------

# Program executed directly
if __name__ == "__main__":
    
    menu()
    printowo()

    while True:
        
        time.sleep(2)
        
        # Check if answer is valid (Answer from 1 to 6)
        try:
            option = int(input("\n[!] Seleccione una de las siguientes 5 opciones: "))

            if (option == 6):
                break # Close Program

            if (option in range(1, 6)):
                utilidades(option) # Call utils later for each instruction
                time.sleep(1)
                # Doesn't break until user selects option 6
            else:
                print("Respuesta inválida. Seleccione una de las seis opciones.")
        
        except: 
            print("ERROR: Valor insertado inválido")
