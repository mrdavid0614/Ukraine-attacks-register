from os import system
from time import sleep
from menu import agregarAtaque, borrarAtaque, exportarAtaque, exportarAtaques

while True:
    system("cls")
    print("-------- Ataques de Ucrania --------\n")
    print("1. Agregar ataque")
    print("2. Borrar ataque")
    print("3. Exportar ataque")
    print("4. Exportar todos los ataques a un mapa")
    print("5. Salir")

    opcion = input("\nIngrese la opción deseada: ")

    system("cls")

    if opcion == "1":
        agregarAtaque()
    elif opcion == "2":
        borrarAtaque()
    elif opcion == "3":
        exportarAtaque()
    elif opcion == "4":
        exportarAtaques()
    elif opcion == "5":
        break
    else:
        print("Opción incorrecta...")
    sleep(1.2)