# TRABAJO PRÁCTICO INTEGRADOR - PROGRAMACIÓN 1
# TECNICATURA UNIVERSITARIA EN PROGRAMACIÓN - UTN
# Tema: Gestión de Datos de Países en Python



# SECCIÓN 1: IMPORTACIONES
# Importamos el módulo csv que viene incluido en Python,
# no hace falta instalarlo.

import csv



# SECCIÓN 2: CONSTANTE DEL ARCHIVO
# Definimos el nombre del archivo CSV en una constante
# para no repetirlo en todo el código.

ARCHIVO_CSV = "paises.csv"



# SECCIÓN 3: FUNCIONES DE ARCHIVO (Lectura y Escritura CSV)


def cargar_paises():
   """
   Lee el archivo CSV y devuelve una lista de diccionarios.
   Cada diccionario representa un país con sus datos.
   Si el archivo no existe, avisa y devuelve una lista vacía.
   Si una fila tiene error de formato, la saltea con un mensaje.
   """
   lista_de_paises = []

   try:
      archivo = open(ARCHIVO_CSV, encoding="utf-8")
      lector = csv.DictReader(archivo)

      for fila in lector:
         try:
               # Convertimos los valores numéricos a entero
               pais = {
                  "nombre":     fila["nombre"].strip(),
                  "poblacion":  int(fila["poblacion"]),
                  "superficie": int(fila["superficie"]),
                  "continente": fila["continente"].strip()
               }
               lista_de_paises.append(pais)

         except (ValueError, KeyError):
               # Si la fila tiene un error, la avisamos y seguimos
               print(f"  [!] Fila con error de formato, se omite: {fila}")

      archivo.close()

   except FileNotFoundError:
      print(f"  [!] Archivo '{ARCHIVO_CSV}' no encontrado.")
      print("      Se inicia el sistema con la lista vacía.")

   return lista_de_paises


def guardar_paises(lista_de_paises):
   """
   Guarda toda la lista de países en el archivo CSV.
   Se llama automáticamente después de agregar o actualizar.
   """
   archivo = open(ARCHIVO_CSV, "w", newline="", encoding="utf-8")
   campos = ["nombre", "poblacion", "superficie", "continente"]
   escritor = csv.DictWriter(archivo, fieldnames=campos)
   escritor.writeheader()

   for pais in lista_de_paises:
      escritor.writerow(pais)

   archivo.close()


# SECCIÓN 4: FUNCIÓN AUXILIAR PARA MOSTRAR UN PAÍS
# La usamos en varias partes del programa para no repetir código.


def mostrar_pais(pais):
   """Imprime los datos de un país en pantalla de forma ordenada."""
   print(f"    Nombre:     {pais['nombre']}")
   print(f"    Población:  {pais['poblacion']:,} hab.")
   print(f"    Superficie: {pais['superficie']:,} km²")
   print(f"    Continente: {pais['continente']}")
   print("    " + "-" * 35)

# SECCIÓN 5: FUNCIÓN PARA AGREGAR UN PAÍS

def agregar_pais(lista_de_paises):
   """
   Pide los datos del nuevo país al usuario.
   Valida que ningún campo esté vacío y que los números sean válidos.
   No permite países duplicados.
   """
   print("\n--- AGREGAR PAÍS ---")

   # Pedimos el nombre y validamos que no esté vacío
   nombre = input("  Nombre del país: ").strip()
   if nombre == "":
      print("  [!] El nombre no puede estar vacío.")
      return

   # Verificamos que el país no exista ya en la lista
   for p in lista_de_paises:
      if p["nombre"].lower() == nombre.lower():
         print(f"  [!] El país '{nombre}' ya existe en el sistema.")
         return

   # Pedimos la población y validamos que sea un número entero
   try:
      poblacion = int(input("  Población (número entero): ").strip())
   except ValueError:
      print("  [!] La población debe ser un número entero. Ej: 45000000")
      return

   # Pedimos la superficie y validamos que sea un número entero
   try:
      superficie = int(input("  Superficie en km² (número entero): ").strip())
   except ValueError:
      print("  [!] La superficie debe ser un número entero. Ej: 2780400")
      return

   # Pedimos el continente y validamos que no esté vacío
   continente = input("  Continente: ").strip()
   if continente == "":
      print("  [!] El continente no puede estar vacío.")
      return

   # Si todo está bien, creamos el diccionario y lo agregamos
   nuevo_pais = {
      "nombre":     nombre,
      "poblacion":  poblacion,
      "superficie": superficie,
      "continente": continente
   }

   lista_de_paises.append(nuevo_pais)
   guardar_paises(lista_de_paises)
   print(f"  [OK] País '{nombre}' agregado y guardado correctamente.")


# SECCIÓN 6: FUNCIÓN PARA ACTUALIZAR POBLACIÓN Y SUPERFICIE

def actualizar_pais(lista_de_paises):
   """
   Busca un país por nombre exacto y permite actualizar
   su población y superficie. Luego guarda los cambios.
   """
   print("\n--- ACTUALIZAR DATOS DE UN PAÍS ---")

   nombre = input("  Nombre del país a actualizar: ").strip()

   if nombre == "":
      print("  [!] Debe ingresar un nombre.")
      return

   encontrado = False

   for pais in lista_de_paises:
      if pais["nombre"].lower() == nombre.lower():
         encontrado = True
         print(f"\n  País encontrado: {pais['nombre']}")
         print(f"  Población actual:  {pais['poblacion']:,}")
         print(f"  Superficie actual: {pais['superficie']:,} km²")

         # Actualizamos la población
         try:
               nueva_poblacion = int(
                  input("  Nueva población: ").strip()
               )
         except ValueError:
               print("  [!] Valor inválido. La población debe ser un número entero.")
               return

         # Actualizamos la superficie
         try:
               nueva_superficie = int(
                  input("  Nueva superficie en km²: ").strip()
               )
         except ValueError:
               print("  [!] Valor inválido. La superficie debe ser un número entero.")
               return

         # Aplicamos los cambios al diccionario
         pais["poblacion"]  = nueva_poblacion
         pais["superficie"] = nueva_superficie

         guardar_paises(lista_de_paises)
         print("  [OK] Datos actualizados y guardados correctamente.")
         break

   if not encontrado:
      print(f"  [!] No se encontró ningún país con el nombre '{nombre}'.")



# SECCIÓN 7: FUNCIÓN PARA BUSCAR UN PAÍS POR NOMBRE
# Permite coincidencia parcial (por ejemplo: "arg" encuentra "Argentina")

def buscar_pais(lista_de_paises):
   """
   Busca países cuyo nombre contenga el texto ingresado.
   La búsqueda no distingue mayúsculas de minúsculas.
   """
   print("\n--- BUSCAR PAÍS POR NOMBRE ---")

   termino = input("  Ingrese nombre o parte del nombre: ").strip().lower()

   if termino == "":
      print("  [!] Debe ingresar algo para buscar.")
      return

   resultados = []

   for pais in lista_de_paises:
      if termino in pais["nombre"].lower():
         resultados.append(pais)

   if len(resultados) == 0:
      print(f"  [!] No se encontraron países que contengan '{termino}'.")
   else:
      print(f"\n  Se encontraron {len(resultados)} resultado(s):\n")
      for pais in resultados:
         mostrar_pais(pais)

# SECCIÓN 8: FUNCIONES DE FILTRADO

def filtrar_por_continente(lista_de_paises):
   """Filtra y muestra solo los países de un continente dado."""
   continente = input("  Continente a filtrar: ").strip()

   if continente == "":
      print("  [!] Debe ingresar un continente.")
      return

   resultados = []
   for pais in lista_de_paises:
      if pais["continente"].lower() == continente.lower():
         resultados.append(pais)

   if len(resultados) == 0:
      print(f"  [!] No se encontraron países en el continente '{continente}'.")
   else:
      print(f"\n  {len(resultados)} país(es) en {continente}:\n")
      for pais in resultados:
         mostrar_pais(pais)


def filtrar_por_rango_poblacion(lista_de_paises):
   """Filtra países cuya población esté dentro del rango dado."""
   try:
      minimo = int(input("  Población mínima: ").strip())
      maximo = int(input("  Población máxima: ").strip())
   except ValueError:
      print("  [!] Los valores deben ser números enteros.")
      return

   resultados = []
   for pais in lista_de_paises:
      if minimo <= pais["poblacion"] <= maximo:
         resultados.append(pais)

   if len(resultados) == 0:
      print(f"  [!] No hay países con población entre {minimo:,} y {maximo:,}.")
   else:
      print(f"\n  {len(resultados)} país(es) en ese rango de población:\n")
      for pais in resultados:
         mostrar_pais(pais)


def filtrar_por_rango_superficie(lista_de_paises):
   """Filtra países cuya superficie esté dentro del rango dado."""
   try:
      minimo = int(input("  Superficie mínima en km²: ").strip())
      maximo = int(input("  Superficie máxima en km²: ").strip())
   except ValueError:
      print("  [!] Los valores deben ser números enteros.")
      return

   resultados = []
   for pais in lista_de_paises:
      if minimo <= pais["superficie"] <= maximo:
         resultados.append(pais)

   if len(resultados) == 0:
      print(f"  [!] No hay países con superficie entre {minimo:,} y {maximo:,} km².")
   else:
      print(f"\n  {len(resultados)} país(es) en ese rango de superficie:\n")
      for pais in resultados:
         mostrar_pais(pais)


def filtrar_paises(lista_de_paises):
   """Menú de filtros: muestra las opciones y llama a la función correcta."""
   print("\n--- FILTRAR PAÍSES ---")
   print("  1. Por continente")
   print("  2. Por rango de población")
   print("  3. Por rango de superficie")

   opcion = input("  Seleccione una opción: ").strip()

   if opcion == "1":
      filtrar_por_continente(lista_de_paises)
   elif opcion == "2":
      filtrar_por_rango_poblacion(lista_de_paises)
   elif opcion == "3":
      filtrar_por_rango_superficie(lista_de_paises)
   else:
      print("  [!] Opción inválida.")

# SECCIÓN 9: FUNCIONES AUXILIARES PARA ORDENAMIENTO
# Necesitamos funciones separadas como "clave" para sorted()

def clave_nombre(pais):
   """Devuelve el nombre en minúsculas para ordenar sin importar mayúsculas."""
   return pais["nombre"].lower()


def clave_poblacion(pais):
   """Devuelve la población del país para usarla como clave de ordenamiento."""
   return pais["poblacion"]


def clave_superficie(pais):
   """Devuelve la superficie del país para usarla como clave de ordenamiento."""
   return pais["superficie"]


def ordenar_paises(lista_de_paises):
   """
   Ordena la lista de países por el criterio elegido por el usuario.
   No modifica la lista original, trabaja sobre una copia.
   """
   print("\n--- ORDENAR PAÍSES ---")
   print("  Ordenar por:")
   print("  1. Nombre")
   print("  2. Población")
   print("  3. Superficie")

   criterio = input("  Criterio: ").strip()

   print("\n  Tipo de orden:")
   print("  1. Ascendente (de menor a mayor / A → Z)")
   print("  2. Descendente (de mayor a menor / Z → A)")

   orden = input("  Seleccione: ").strip()

   # Definimos si es descendente según la opción elegida
   if orden == "2":
      descendente = True
   else:
      descendente = False

   # Ordenamos según el criterio elegido
   if criterio == "1":
      ordenados = sorted(lista_de_paises, key=clave_nombre, reverse=descendente)
   elif criterio == "2":
      ordenados = sorted(lista_de_paises, key=clave_poblacion, reverse=descendente)
   elif criterio == "3":
      ordenados = sorted(lista_de_paises, key=clave_superficie, reverse=descendente)
   else:
      print("  [!] Opción inválida.")
      return

   # Mostramos los resultados ordenados
   print(f"\n  Lista ordenada ({len(ordenados)} países):\n")
   for pais in ordenados:
      mostrar_pais(pais)


# SECCIÓN 10: FUNCIÓN DE ESTADÍSTICAS

def mostrar_estadisticas(lista_de_paises):
   """
   Calcula y muestra estadísticas del dataset:
   - País con mayor y menor población
   - Promedio de población
   - Promedio de superficie
   - Cantidad de países por continente
   """
   print("\n--- ESTADÍSTICAS ---")

   if len(lista_de_paises) == 0:
      print("  [!] No hay países cargados. No se pueden calcular estadísticas.")
      return

   # --- País con mayor población ---
   # Empezamos asumiendo que el primero es el mayor, luego comparamos
   pais_mayor_pob = lista_de_paises[0]
   for pais in lista_de_paises:
      if pais["poblacion"] > pais_mayor_pob["poblacion"]:
         pais_mayor_pob = pais

   # --- País con menor población ---
   pais_menor_pob = lista_de_paises[0]
   for pais in lista_de_paises:
      if pais["poblacion"] < pais_menor_pob["poblacion"]:
         pais_menor_pob = pais

   # --- Promedio de población ---
   total_poblacion = 0
   for pais in lista_de_paises:
      total_poblacion = total_poblacion + pais["poblacion"]
   promedio_poblacion = total_poblacion // len(lista_de_paises)

   # --- Promedio de superficie ---
   total_superficie = 0
   for pais in lista_de_paises:
      total_superficie = total_superficie + pais["superficie"]
   promedio_superficie = total_superficie // len(lista_de_paises)

   # --- Cantidad de países por continente ---
   # Usamos un diccionario: clave = nombre del continente, valor = cantidad
   continentes = {}
   for pais in lista_de_paises:
      nombre_continente = pais["continente"]
      if nombre_continente in continentes:
         continentes[nombre_continente] = continentes[nombre_continente] + 1
      else:
         continentes[nombre_continente] = 1

   # --- Mostramos todos los resultados ---
   print(f"\n  Total de países en el sistema: {len(lista_de_paises)}")
   print(f"\n  País con MAYOR población: {pais_mayor_pob['nombre']}")
   print(f"    → {pais_mayor_pob['poblacion']:,} hab.")
   print(f"\n  País con MENOR población: {pais_menor_pob['nombre']}")
   print(f"    → {pais_menor_pob['poblacion']:,} hab.")
   print(f"\n  Promedio de población:  {promedio_poblacion:,} hab.")
   print(f"  Promedio de superficie: {promedio_superficie:,} km²")

   print("\n  Países por continente:")
   for continente in continentes:
      cantidad = continentes[continente]
      print(f"    - {continente}: {cantidad} país(es)")

# SECCIÓN 11: FUNCIÓN PARA LISTAR TODOS LOS PAÍSES


def listar_todos(lista_de_paises):
   """Muestra todos los países cargados en el sistema."""
   print("\n--- TODOS LOS PAÍSES ---")

   if len(lista_de_paises) == 0:
      print("  [!] No hay países cargados en el sistema.")
      return

   print(f"  Total: {len(lista_de_paises)} países\n")
   for pais in lista_de_paises:
      mostrar_pais(pais)


# ---------------------------------------------------------------
# SECCIÓN 12: FUNCIÓN DEL MENÚ PRINCIPAL
# ---------------------------------------------------------------

def mostrar_menu():
   """Imprime el menú principal en pantalla."""
   print("\n" + "=" * 45)
   print("     GESTIÓN DE DATOS DE PAÍSES - UTN")
   print("=" * 45)
   print("  1. Agregar país")
   print("  2. Actualizar población y superficie")
   print("  3. Buscar país por nombre")
   print("  4. Filtrar países")
   print("  5. Ordenar países")
   print("  6. Ver estadísticas")
   print("  7. Listar todos los países")
   print("  8. Salir")
   print("=" * 45)


# ---------------------------------------------------------------
# SECCIÓN 13: FUNCIÓN PRINCIPAL (MAIN)
# Es el punto de entrada del programa. Coordina todo el flujo.
# ---------------------------------------------------------------

def main():
   """
   Función principal. Carga los datos y muestra el menú
   en un bucle hasta que el usuario elija salir.
   """
   print("\n  Bienvenido al Sistema de Gestión de Países")
   print("  Cargando datos desde el archivo CSV...")

   # Cargamos los países al iniciar el programa
   lista_de_paises = cargar_paises()

   print(f"  {len(lista_de_paises)} país(es) cargado(s) correctamente.")

   # Bucle principal: se repite hasta que el usuario elija salir
   seguir = True

   while seguir:
      mostrar_menu()
      opcion = input("  Seleccione una opción (1-8): ").strip()

      if opcion == "1":
         agregar_pais(lista_de_paises)

      elif opcion == "2":
         actualizar_pais(lista_de_paises)

      elif opcion == "3":
         buscar_pais(lista_de_paises)

      elif opcion == "4":
         if len(lista_de_paises) == 0:
               print("  [!] No hay países cargados para filtrar.")
         else:
               filtrar_paises(lista_de_paises)

      elif opcion == "5":
         if len(lista_de_paises) == 0:
               print("  [!] No hay países cargados para ordenar.")
         else:
               ordenar_paises(lista_de_paises)

      elif opcion == "6":
         mostrar_estadisticas(lista_de_paises)

      elif opcion == "7":
         listar_todos(lista_de_paises)

      elif opcion == "8":
         print("\n  ¡Hasta luego! El programa ha finalizado.\n")
         seguir = False

      else:
         print("  [!] Opción inválida. Por favor ingrese un número del 1 al 8.")


# SECCIÓN 14: PUNTO DE ENTRADA DEL SCRIPT
# Esta condición asegura que main() solo se ejecute si corremos
# este archivo directamente (no si lo importamos desde otro).


if __name__ == "__main__":
   main()