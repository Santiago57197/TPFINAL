import csv
from funciones import agregar
from funciones import actualizar
from funciones import buscar
from funciones import filtrar
from funciones import ordenar
from funciones import estadistica
paises = []
while True:
    opcion = input("----MENU----\n1. Agregar paises\n2. Actualizar datos\n3. Buscar pais\n4. Filtrar paises\n5. Ordenar paises\n6. Mostrar estadisticas\n:")
    try:
      opcion = int(opcion)
    except ValueError:
       print("\nIngrese un numero entero!\n")
       continue
    match opcion:
       case 1:
          pais = agregar()
          paises.append(pais)
       case 2:
        actualizar()  
       case 3:
         buscar()
       case 4:
          filtrar()
       case 5:
          ordenar()  
       case 6:
          estadistica()         
       case _:
          print("Ingrese una opcion entre 1-8")