# 🌍 Gestión de Datos de Países en Python

**Trabajo Práctico Integrador - Programación 1**  
**Tecnicatura Universitaria en Programación - UTN**

---

## 📋 Descripción del programa

Este programa permite gestionar un dataset de países desde la consola de Python.
Los datos se leen y guardan en un archivo CSV. El sistema ofrece un menú interactivo
con las siguientes funcionalidades:

- Agregar nuevos países
- Actualizar población y superficie de un país
- Buscar países por nombre (coincidencia parcial)
- Filtrar por continente, rango de población o rango de superficie
- Ordenar por nombre, población o superficie (ascendente o descendente)
- Ver estadísticas del dataset

---

## 📁 Estructura del proyecto

```
tpi_paises/
│
├── main.py        → Código fuente principal del programa
├── paises.csv     → Dataset base con países del mundo
└── README.md      → Este archivo
```

---

## ▶️ Cómo ejecutar el programa

1. Asegurarse de tener **Python 3.x** instalado.
2. Colocar `main.py` y `paises.csv` en la **misma carpeta**.
3. Abrir una terminal en esa carpeta y ejecutar:

```bash
python main.py
```

---

## 🧭 Menú de opciones

Al ejecutar el programa aparece este menú:

```
=============================================
     GESTIÓN DE DATOS DE PAÍSES - UTN
=============================================
  1. Agregar país
  2. Actualizar población y superficie
  3. Buscar país por nombre
  4. Filtrar países
  5. Ordenar países
  6. Ver estadísticas
  7. Listar todos los países
  8. Salir
=============================================
```

---

## 💡 Ejemplos de uso

### Agregar un país
```
Seleccione una opción (1-8): 1

--- AGREGAR PAÍS ---
  Nombre del país: Bolivia
  Población (número entero): 12079472
  Superficie en km² (número entero): 1098581
  Continente: América
  [OK] País 'Bolivia' agregado y guardado correctamente.
```

### Buscar un país
```
Seleccione una opción (1-8): 3

--- BUSCAR PAÍS POR NOMBRE ---
  Ingrese nombre o parte del nombre: arg

  Se encontraron 1 resultado(s):

    Nombre:     Argentina
    Población:  45,376,763 hab.
    Superficie: 2,780,400 km²
    Continente: América
    -----------------------------------
```

### Filtrar por continente
```
Seleccione una opción (1-8): 4

--- FILTRAR PAÍSES ---
  1. Por continente
  2. Por rango de población
  3. Por rango de superficie
  Seleccione una opción: 1
  Continente a filtrar: Europa

  10 país(es) en Europa:
  ...
```

### Ver estadísticas
```
Seleccione una opción (1-8): 6

--- ESTADÍSTICAS ---
  Total de países en el sistema: 46

  País con MAYOR población: China
    → 1,412,600,000 hab.

  País con MENOR población: Uruguay
    → 3,473,730 hab.

  Promedio de población:  120,543,211 hab.
  Promedio de superficie: 1,234,567 km²

  Países por continente:
    - América: 14 país(es)
    - Europa: 10 país(es)
    - Asia: 10 país(es)
    - África: 8 país(es)
    - Oceanía: 3 país(es)
```

---

## 📦 Formato del archivo CSV

El archivo `paises.csv` tiene el siguiente formato:

```
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
```

---

## 👥 Integrantes del equipo

| Nombre | Apellido | Legajo |
|--------|----------|--------|
|Santiago| Silva    | 54265  |
|Lucas   |Elorrieta | 54214  |

---

## 🔗 Links

- 📹 **Video demostrativo:** https://youtu.be/FiXbMNAe1e0
- 📄 **Documentación PDF:** Dentro del zip

---

## 📚 Bibliografía

- Documentación oficial de Python 3: https://docs.python.org/3/
- Módulo csv de Python: https://docs.python.org/3/library/csv.html
- Tutorial de diccionarios en Python: https://docs.python.org/3/tutorial/datastructures.html
