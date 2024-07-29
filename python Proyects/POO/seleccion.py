# Importamos la clase creada en Coche.py
from Coche import *

print("¡Bienvenido al menú!")

# Creación de coches para meterlo en el array principal
coche1 = Coche("rojo","Toyota","Célica")
coche2 = Coche("negro","Audi","A5")
coche3 = Coche("azul oscuro","Lamborgini","Urus")

a_coches = [coche1,coche2,coche3]

def mostrar_menu():
    print("[1] Ver lista.")
    print("[2] Añadir a la lista.")
    print("[3] Borrar de la lista.")
    print("[4] Salir.")
    opcion = int(input("Elige una opción: "))
    return opcion

def manejo_opcion1():
    i = 1
    for coche in a_coches:
        print(f"{i} "+coche.__str__())
        print("--------------")
        i += 1

def manejo_opcion2():
    print("Creación de coche:")
    color = input("Escoge el color del coche -> ")
    marca = input("Escoge la marca del coche -> ")
    modelo = input("Escoge el modelo del coche -> ")
    cocheAux = Coche(color,marca,modelo)
    a_coches.append(cocheAux)
    print("¡Coche creado!")


def elegir_opcion_borrado():
    opcion = int(input("Introduce el numero del coche que quieres borrar -> "))
    return opcion - 1

def manejo_opcion3():
    print("Selecciona cual quieres eliminar")
    manejo_opcion1()
    opcion = elegir_opcion_borrado()
    a_coches.pop(opcion)
    

opcion = mostrar_menu()
while opcion != 4:
    if opcion == 1:
        manejo_opcion1()
    elif opcion == 2:
        manejo_opcion2()
    elif opcion == 3:
        manejo_opcion3()

    opcion = mostrar_menu()

print("Has salido del menú. Vuelve pronto")