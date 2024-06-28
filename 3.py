# Script 3: Listas, Tuplas y Diccionarios

# En este tercer script, exploraremos las estructuras de datos más comunes en Python:
# listas, tuplas y diccionarios.
# Aprenderemos cómo crearlas, acceder a sus elementos y manipularlos.

# Listas
# Las listas son colecciones ordenadas y mutables que permiten elementos duplicados.

# Crear una lista
mi_lista = [1, 2, 3, 4, 5]

# Acceder a elementos de la lista
primer_elemento = mi_lista[0]  # Acceder al primer elemento
ultimo_elemento = mi_lista[-1]  # Acceder al último elemento

# Modificar elementos de la lista
mi_lista[0] = 10

# Agregar elementos a la lista
mi_lista.append(6)

# Eliminar elementos de la lista
mi_lista.remove(10)  # Eliminar el elemento con valor 10
elemento_eliminado = mi_lista.pop(0)  # Eliminar y retornar el primer elemento

print("Lista después de modificaciones:", mi_lista)
print("Elemento eliminado:", elemento_eliminado)

# Tuplas
# Las tuplas son colecciones ordenadas e inmutables que permiten elementos duplicados.

# Crear una tupla
mi_tupla = (1, 2, 3, 4, 5)

# Acceder a elementos de la tupla
primer_elemento_tupla = mi_tupla[0]  # Acceder al primer elemento
ultimo_elemento_tupla = mi_tupla[-1]  # Acceder al último elemento

# Las tuplas no pueden ser modificadas (son inmutables), así que no se pueden agregar ni eliminar elementos.

print("Tupla:", mi_tupla)

# Diccionarios
# Los diccionarios son colecciones desordenadas, mutables y no permiten claves duplicadas.
# Consisten en pares clave-valor.

# Crear un diccionario
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Acceder a elementos del diccionario
nombre = mi_diccionario["nombre"]
edad = mi_diccionario.get("edad")  # Otra forma de acceder a los valores

# Modificar elementos del diccionario
mi_diccionario["edad"] = 31

# Agregar nuevos pares clave-valor al diccionario
mi_diccionario["profesion"] = "Ingeniero"

# Eliminar pares clave-valor del diccionario
del mi_diccionario["ciudad"]  # Eliminar el par con clave "ciudad"
profesion_eliminada = mi_diccionario.pop("profesion")  # Eliminar y retornar el valor asociado a "profesion"

print("Diccionario después de modificaciones:", mi_diccionario)
print("Profesión eliminada:", profesion_eliminada)

# Este es el final del tercer script. Continúa con el siguiente script para aprender más
# sobre Python.
