import csv
import unicodedata
from statistics import mean
######## Validaciones ########
def validarletras(texto):
  texto = texto.strip()
  if not texto.isalpha():
    return False
  return texto.isalpha
##############################
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
def validarpais(nombre):
  with open("Paises.csv", "r", encoding="utf-8") as archivo:
     lector = csv.DictReader(archivo)
     filas = list(lector)
     for posicion, fila in enumerate(filas):
       if fila["nombre"] == nombre.title():     
         return True, posicion, filas
     return False, -1, filas
##############################
def quitartildes(texto):

    texto = unicodedata.normalize("NFD", texto)

    texto = "".join(
        letra for letra in texto
        if unicodedata.category(letra) != "Mn"
    )

    return texto 
############################## 
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
###########Procesos############    
def listafilas():
  with open("Paises.csv", "r", encoding="utf-8") as archivo:
     lector = csv.DictReader(archivo)
     filas = list(lector)
     return filas
def modificar(filas):
  with open("Paises.csv", "w", newline="", encoding="utf-8") as archivo:

        campos = ["nombre", "poblacion", "superficie", "continente"]

        escritor = csv.DictWriter(archivo, fieldnames=campos)

        escritor.writeheader()

        escritor.writerows(filas)
def ordenamiento(ordenado,invertido):
  filas = listafilas()
  if ordenado == 'poblacion' or ordenado == 'superficie':
   filas.sort(key=lambda x:int(x[ordenado]), reverse=invertido)
  else:  
   filas.sort(key=lambda x:x[ordenado], reverse=invertido)
  for fila in filas:
    print(f"Pais: {fila['nombre']}\nPoblacion: {fila['poblacion']}\nSuperficie: {fila['superficie']}\nContinente: {fila['continente']}\n------------------------")       
#####Opcion 1#####
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
def estadistica():
  while True:
   calculado = input("Ingrese la opcion que desea:\n1. Pais con mayor poblacion\n2. Pais con menor poblacion\n3. Promedio de poblacion\n4. Promedio de superficie\n5. Cantidad de paises por continente\n:")
   if not validarnumint(calculado):
    print("Error: Ingrese un numero valido!")
    break
   calculado = int(calculado)
   filas = listafilas()
   match calculado:
     case 1:

      mayor = max(filas, key=lambda x:int(x['poblacion']))
      for clave, valor in mayor.items():
       print(f"{clave.title()}: {valor}")
      print("----------------------")
      break 
     case 2: 
      menor = min(filas, key=lambda x:int(x['poblacion']))
      for clave, valor in menor.items():
       print(f"{clave.title()}: {valor}")
      print("----------------------")
      break
     case 3:
       poblacionsumada = mean([int(x['poblacion']) for x in filas])
       print(f"El promedio de poblacion es de {poblacionsumada} por pais\n-------------------")
       break
     case 4:
       superficiesumada = mean([int(x['superficie']) for x in filas])
       print(f"El promedio de superficie es de {superficiesumada} por pais\n-------------------")
       break
     case 5:
      continentes = {}
      for fila in filas:
          continente = fila["continente"]
          if continente in continentes:
              continentes[continente] += 1
          else:
              continentes[continente] = 1
      print("Cantidad de paises por continente")
      print("--------------------------------")
      for continente, cantidad in continentes.items():
          print(f"{continente}: {cantidad}")
      print("--------------------------------")