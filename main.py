#!/usr/bin/env python3

# option: Respuesta del usuario
# TODO: Implementar lógica para registar respuesta de alumno (registrar_respuesta)
# TODO: Implementar lógica para realizar calificado (calificado_dia_mes_hora.txt)
# TODO: Implementar lógica para llamar a consultas

# Libraries
import time
import os

# Import script
from tools import limpiar_pantalla
import utilities

# Print principal menu options
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

# Print submenu options
def consultas():
    print("\n" + "="* 40)

    print("DESPLEGANDO SUBMENÚ...\n")
    print("a) Calificaciones generales")
    print("b) Calificación de un estudiante")
    print("c) Top 3 calificaciones")
    print("d) Promedio de aciertos")
    print("e) Graficación (Top 3 y calificaciones)")
    print("f) Regresar al menú")

    print("\n" + "="* 40 + "\n")

def utilidades(option):

    match option:
        case 1: # Registrar respuestas correctas
            utilities.registrar_respuestas_correctas()
            time.sleep(1)
        case 2: # Registrar alumno
            utilities.registrar_alumno()
            time.sleep(1)
        case 3: # Registrar respuesta de alumno
            utilities.registrar_respuestas_alumno()
            time.sleep(1)
        case 4: # Realizar calificado
            utilities.realizar_calificado()
            time.sleep(1)
            pass
        case 5: # Desplegar consultas específicas

            while True:

                time.sleep(1)
                consultas()
                # Se registra la respuesta para el submenú
                try:
                    option = input("\n[!] Seleccione una de las siguientes 6 opciones: ")
                    if ("a" <= option <= "f"):
                        limpiar_pantalla()
                        
                        if (option == "f"):
                            break
                        
                        print(f"Respuesta {option} seleccionada")
                        time.sleep(1)

                        # TODO: Llamar a las funciones necesarias del submenú
                        break
                    else:
                         print("[*] Respuesta inválida. Seleccione una de las seis opciones.")
                except ValueError:
                    print("[|-|] Error: Valor insertado inválido (a, b, c, d, e, f)")
                # TODO: Mostrar el submenú y verificar que input esté entre "a" y "f"

# Program executed directly
if __name__ == "__main__":
    
    while True:

        menu()
        time.sleep(1)
        
        # Check if answer is valid (Answer from 1 to 6)
        try:
            option = int(input("\n[!] Seleccione una de las siguientes 6 opciones: "))

            if (option == 6):
                break # Close Program

            if (option in range(1, 6)):
                limpiar_pantalla()
                
                print(f"Respuesta {option} seleccionada")
                time.sleep(1)

                utilidades(option) # Call utils later for each instruction
                # Doesn't break until user selects option 6
            else:
                print("[*] Respuesta inválida. Seleccione una de las seis opciones.")
        
        except: 
            print("[|-|] ERROR: Valor insertado inválido (1, 2, 3, 4, 5, 6)")
