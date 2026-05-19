import csv
import unicodedata
from statistics import mean
######## Validaciones ########
#Validacion de texto
def validarletras(texto):
  texto = texto.strip()
  if not texto.isalpha():
    return False
  return texto.isalpha
##############################
#Validacion de enteros
def validarnumint(numero):
  try:
    numero = int(numero)
    if numero < 1:
      print("Error: Ingrese un valor mayor o igual a 1!")
      return False
    return True  
  except ValueError:
    print("Error: Ingrese solamente numeros enteros!")
    return False
##############################
#Validacion de paises, retorna una tupla con el valor sobre si lo encontro, su posicion, y la lista de diccionarios actualizada
def validarpais(nombre):
  with open("Paises.csv", "r", encoding="utf-8") as archivo:
     lector = csv.DictReader(archivo)
     filas = list(lector)
     for posicion, fila in enumerate(filas):
       if fila["nombre"] == nombre.title():     
         return True, posicion, filas
     return False, -1, filas
##############################
#Toma palabras y las retorna sin tildes
def quitartildes(texto):

    texto = unicodedata.normalize("NFD", texto)

    texto = "".join(
        letra for letra in texto
        if unicodedata.category(letra) != "Mn"
    )

    return texto 
##############################
#Mediante una lista preestablecida de continentes , comparamos si el ingresado por el usuario es valido o no
#y retornamos una tupla con el valor sobre si es o no valido, el lugar pero escrito correctamente, y la lista de diccionarios actualizada  
def validarcontinente(lugar):
  with open("Paises.csv", "r", encoding="utf-8") as archivo:
     lector = csv.DictReader(archivo)
     filas = list(lector)
  continentes = ["América","África","Oceanía","Asia","Europa"]
  for i,j in enumerate(continentes):
    if quitartildes(lugar).lower() == quitartildes(continentes[i]).lower():
      lugar = continentes[i]
      return True, lugar, filas
  return False, lugar, filas
#######################################     
###########Procesos############
#Importamos la lista de diccionarios del CSV     
def listafilas():
  with open("Paises.csv", "r", encoding="utf-8") as archivo:
     lector = csv.DictReader(archivo)
     filas = list(lector)
     return filas
##########################################  
#Escribimos o sobrescribimos una fila entera del archivo CSV
def modificar(filas):
  with open("Paises.csv", "w", newline="", encoding="utf-8") as archivo:

        campos = ["nombre", "poblacion", "superficie", "continente"]

        escritor = csv.DictWriter(archivo, fieldnames=campos)

        escritor.writeheader()

        escritor.writerows(filas)
#######################################
#Tomamos el metodo de orden(ordenado) y la forma en la que se requiera, ascendente o descendente(invertido).
#Luego mostramos la lista de diccionarios ordenada segun el metodo
def ordenamiento(ordenado,invertido):
  filas = listafilas()
  if ordenado == 'poblacion' or ordenado == 'superficie':
   filas.sort(key=lambda x:int(x[ordenado]), reverse=invertido)
  else:  
   filas.sort(key=lambda x:x[ordenado], reverse=invertido)
  for fila in filas:
    print(f"Pais: {fila['nombre']}\nPoblacion: {fila['poblacion']}\nSuperficie: {fila['superficie']}\nContinente: {fila['continente']}\n------------------------")       
#####Opcion 1#####
#Solicitamos al usuario un nombre,continente,superficie y poblacion validamos mediante las funciones de arriba
#Y luego las agregamos al archivo CSV siguiendo el formato
def agregar():
  while True: 
   nombre = input("Ingrese el nombre del pais: ")
   if not validarletras(nombre):
     print("Error: El nombre solo debe contener letras!")
     break
   continente = input("Ingrese continente del pais: ")
   if not validarletras(continente):
      print("Error: El continente solo debe contener letras!")
      break
   poblacion = input("Ingrese la poblacion del pais: ")
   if not validarnumint(poblacion):
     break  
   superficie = input("Ingrese la superficie del pais: ")
   if not validarnumint(superficie):
     break
   existe, pos, filas = validarpais(nombre)
   if existe:
    print("\nEl pais ya se encuentra en la lista!\n")
    break 
   pais = {"nombre": nombre.title(),
           "poblacion": poblacion,
           "superficie": superficie, 
           "continente": continente.title()}
   with open("Paises.csv", "a", newline="", encoding="utf-8") as archivo:
     campos = ["nombre","poblacion","superficie","continente"]
     escritor = csv.DictWriter(archivo,fieldnames=campos)
     escritor.writerow(pais)
   print("\nPais agregado correctamente\n")
   return pais
#####Opcion 2#####
#El usuario ingresa el pais que desea cambiar y se valida mediante las funciones de arriba
#En el caso de que lo encuentre se solicita los numeros a cambios que tambien son validados 
def actualizar():
 while True: 
  with open("Paises.csv", "r", encoding="utf-8") as archivo:
   lector = csv.DictReader(archivo)
   for fila in lector:
     print(fila["nombre"])
  nombre = input("Ingrese el pais a cambiar: ")
  if validarletras(nombre):
   existe, posicion, filas = validarpais(nombre)
   if existe:
     poblacion = input("Ingrese la nueva cantidad de poblacion: ")
     if validarnumint(poblacion):
      filas[posicion]["poblacion"] = poblacion
     else:
       print("Error: Ingrese un numero mayor o igual a 1!")
       break
     superficie = input("Ingrese la nueva superficie: ")
     if validarnumint(superficie):
       filas[posicion]["superficie"] = superficie
       modificar(filas)
       print("La poblacion y superficie han sido modificadas correctamente")
       break
     else:
      print("Error: Ingrese un numero mayor o igual a 1!")
      break    
   else:
     print("Error: El pais no se encuentra!")  
     break
  else:
    print("Error: Ingrese un nombre valido!")
    break
###########################################
#####Opcion 3#####
#Se valida si el pais que desea buscar el usuario se encuentra mediante las funciones de arriba y luego
#El programa toma valido abreviaciones tambien, como por ejemplo de América, amer.
#En el caso de que retorne verdadero, lo muestra con toda su informacion
def buscar():
  while True:
   busqueda = input("Ingrese el pais que desea buscar: ")
   if not validarletras(busqueda):
     print("Error: Ingrese solo letras!")
     break
   encontrado, posicion, filas = validarpais(busqueda)
   if encontrado:
     print(f"-----------------\nPais: {filas[posicion]["nombre"]}\nPoblacion: {filas[posicion]["poblacion"]}\nSuperficie: {filas[posicion]["superficie"]}\nContinente: {filas[posicion]["continente"]}\n-----------------")
     break
   else:
     for vueltas,fila in enumerate(filas):
      if busqueda.lower() in filas[vueltas]["nombre"].lower():
       print(f"-----------------\nPais: {filas[vueltas]["nombre"]}\nPoblacion: {filas[vueltas]["poblacion"]}\nSuperficie: {filas[vueltas]["superficie"]}\nContinente: {filas[vueltas]["continente"]}\n-----------------")
       break
      else:
       print("Error: El pais buscado no se encuentra!")
       break
     break 
###################
#####Opcion 4#####
#El usuario elige la manera de filtro y luego
#Si elige filtrar por continentes este validara si el continente existe y luego recorrera la lista mostrando todos los archivos de este mismo continente
#Si elige rango de poblacion o superficie, este recorrera la lista mostrando los paises que esten dentro de ese rango, el cual fue establecido por el usuario
def filtrar():
 while True:
  filtro = input("Filtrar paises por:\n1. Continente\n2. Rango de poblacion\n3. Rango de superficie")
  if not validarnumint(filtro):
    print("Error: Ingrese una opcion valida!")
    break
  filtro = int(filtro)
  match filtro:
    case 1:
      lugar = input("América,Europa,Asia,Oceanía,África\nIngrese el continente: ")
      if not validarletras(lugar):
        print("Error: Ingrese un nombre valido!")
        break
      existe, lugar, filas = validarcontinente(lugar)
      if existe:
        for vueltas,fila in enumerate(filas):
         if filas[vueltas]["continente"] == lugar:
          print(f"-----------------\nContinente filtrado: {lugar}\nPais: {filas[vueltas]["nombre"]}\nPoblacion: {filas[vueltas]["poblacion"]}\nSuperficie: {filas[vueltas]["superficie"]}")
    case 2:
      minimo = input("Ingrese el minimo rango de poblacion: ")
      if not validarnumint(minimo):
        print("Error: Ingrese un numero valido!")
        break
      minimo = int(minimo)
      maximo = input("Ingrese el maximo rango de poblacion: ")
      if not validarnumint(maximo):
        print("Error: Ingrese un numero valido!")
        break
      maximo = int(maximo)
      if minimo > maximo:
        print("Error: El minimo es mayor al maximo!")
        break
      elif minimo == maximo:
        print("Error: El minimo y el maximo no pueden ser iguales!")
        break
      filas = listafilas()
      for vueltas,fila in enumerate(filas):
         if int(filas[vueltas]['poblacion']) <= maximo and int(filas[vueltas]['poblacion']) >= minimo :
          print(f"-----------------\nRango de poblacion filtrada: {maximo}-{minimo}\nPais: {filas[vueltas]['nombre']}\nPoblacion: {filas[vueltas]['poblacion']}\nSuperficie: {filas[vueltas]['superficie']}\nContinente: {filas[vueltas]['continente']}")
      break
    case 3:
      minimo = input("Ingrese el minimo rango de superficie: ")
      if not validarnumint(minimo):
        print("Error: Ingrese un numero valido!")
        break
      minimo = int(minimo)
      maximo = input("Ingrese el maximo rango de superficie: ")
      if not validarnumint(maximo):
        print("Error: Ingrese un numero valido!")
        break
      maximo = int(maximo)
      if minimo > maximo:
        print("Error: El minimo es mayor al maximo!")
        break
      elif minimo == maximo:
        print("Error: El minimo y el maximo no pueden ser iguales!")
        break
      filas = listafilas()
      for vueltas,fila in enumerate(filas):
         if int(filas[vueltas]['superficie']) <= maximo and int(filas[vueltas]['superficie']) >= minimo :
          print(f"-----------------\nRango de superficie filtrada: {minimo}-{maximo}\nPais: {filas[vueltas]['nombre']}\nPoblacion: {filas[vueltas]['poblacion']}\nSuperficie: {filas[vueltas]['superficie']}\nContinente: {filas[vueltas]['continente']}")
      break
    case _:
      print("Error: Ingrese una opcion entre 1-3!")
      break
##########################
#####Opcion 5#####
#Segun la manera que decida ordenar el usuario es la informacion que envia a la funcion ordenar
#Esta funcion solamente envia la forma en la que se debe ordenar la lista y si debe ser de manera ascendente o descendente
def ordenar():
 while True:
  orden = input("Ingrese de que manera desea ordenar los paises:\n1. Nombre\n2. Poblacion\n3. Superficie\n:")
  validarnumint(orden)
  if not validarnumint:
     print("Error: Ingrese un numero valido!") 
     break
  orden = int(orden)
  match orden:
    case 1:
      ordenamiento('nombre',False)
      break
    case 2:
      ordenamiento('poblacion',False)
      break
    case 3:
      opcion = input("1. Ordenar de manera ascendente\n2. Ordenar de manera descendente\n:")
      validarnumint(opcion)
      if not validarnumint():
        print("Error: Ingrese un numero valido!")
        break
      opcion = int(opcion)
      match opcion:
        case 1:
          ordenamiento('superficie',False)
          break
        case 2: 
          ordenamiento('superficie',True) 
          break
    case _:
      print("Error: Ingrese una opcion entre 1-2!")
      break
##################################
#####Opcion 6######
def estadistica():
  while True:
   calculado = input("Ingrese la opcion que desea:\n1. Pais con mayor poblacion\n2. Pais con menor poblacion\n3. Promedio de poblacion\n4. Promedio de superficie\n5. Cantidad de paises por continente\n:")
   if not validarnumint(calculado):
    print("Error: Ingrese un numero valido!")
    break
   calculado = int(calculado)
   filas = listafilas()
   match calculado:
     #Se recorren todas las filas de la lista usando la funcion max y mostramos el mayor valor
     case 1:

      mayor = max(filas, key=lambda x:int(x['poblacion']))
      for clave, valor in mayor.items():
       print(f"{clave.title()}: {valor}")
      print("----------------------")
      break
     #Se recorren todas las filas de la lista usando la funcion min y mostramos el menor valor 
     case 2: 
      menor = min(filas, key=lambda x:int(x['poblacion']))
      for clave, valor in menor.items():
       print(f"{clave.title()}: {valor}")
      print("----------------------")
      break
     #Usando la funcion mean importada de statistics sumamos todos los valores de poblacion y sacamos un promedio
     #Estos valores los obtenemos recorriendo la lista con un for
     case 3:
       poblacionsumada = mean([int(x['poblacion']) for x in filas])
       print(f"El promedio de poblacion es de {poblacionsumada} por pais\n-------------------")
       break
     #Exactamente lo mismo que recien, solamente que con superficie
     case 4:
       superficiesumada = mean([int(x['superficie']) for x in filas])
       print(f"El promedio de superficie es de {superficiesumada} por pais\n-------------------")
       break
     # Creamos un diccionario vacío llamado "continentes". Este diccionario almacenará:
     # clave   -> nombre del continente
     # valor   -> cantidad de países de ese continente
     case 5:
      continentes = {}
      # Recorremos cada país de la lista "filas".
      # Cada "fila" es un diccionario con los datos de un país.
      for fila in filas:
          continente = fila["continente"]
          # Verificamos si ese continente ya existe
          # dentro del diccionario "continentes".
          if continente in continentes:
              continentes[continente] += 1
          # Si NO existe, creamos la clave y comenzamos en 1.    
          else:
              continentes[continente] = 1
      print("Cantidad de paises por continente")
      print("--------------------------------")
      # Recorremos el diccionario final usando .items()
      # para obtener:
      # continente -> clave
      # cantidad   -> valor
      for continente, cantidad in continentes.items():
          print(f"{continente}: {cantidad}")
      print("--------------------------------")