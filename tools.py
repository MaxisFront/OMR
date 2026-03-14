#!/usr/bin/env python3

# Lbraries
import os

# Clean screen
def limpiar_pantalla():
    os.system('cls' if os.name == "nt" else 'clear') # Clean terminal if the os is "windows"

if __name__ == "__main__":
    print("ERROR. Script 'tools.py' ejecutado directamente")
