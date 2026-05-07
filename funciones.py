import csv
def menu():
   while True:
    opcion = input("----MENU----\n1. Mostrar paises\n:")
    while not opcion.isdigit():
       opcion = input("Ingrese un numero valido!")
    opcion = int(opcion)   
    match opcion:
       case 1:
          mostrar()
       case _:
          print("Ingrese una opcion valida!")   
def mostrar():
 paises = []
 with open("paises.csv", encoding="utf-8") as archivo:
     lector = csv.DictReader(archivo)
     for fila in lector:
         pais = {
            "nombre": fila["nombre"],
            "poblacion": int(fila["poblacion"]),
            "superficie": int(fila["superficie"]),
            "continente": fila["continente"]
         }

         paises.append(pais)

 for pais in paises:
    print("Nombre:", pais["nombre"])
    print("Población:", pais["poblacion"])
    print("Superficie:", pais["superficie"])
    print("Continente:", pais["continente"])
    print()