# Script 5: Manipulación de Archivos

# En este quinto script, aprenderemos cómo trabajar con archivos en Python.
# Veremos cómo abrir, leer, escribir y cerrar archivos, así como algunos métodos útiles para la manipulación de archivos.

# Abrir y leer un archivo
# La función open() se usa para abrir archivos. El primer argumento es la ruta del archivo y el segundo argumento es el modo.
# 'r' para leer, 'w' para escribir (sobrescribiendo el archivo si existe), 'a' para agregar, y 'b' para modos binarios.

# Leer todo el contenido de un archivo
try:
    archivo = open('archivo_ejemplo.txt', 'r')  # Abre el archivo en modo lectura
    contenido = archivo.read()  # Lee todo el contenido del archivo
    print("Contenido del archivo:")
    print(contenido)
finally:
    archivo.close()  # Asegurarse de cerrar el archivo

# Leer el archivo línea por línea
try:
    archivo = open('archivo_ejemplo.txt', 'r')
    for linea in archivo:
        print("Línea:", linea.strip())  # strip() elimina los caracteres de nueva línea
finally:
    archivo.close()

# Escribir en un archivo
# Si el archivo no existe, será creado.
try:
    archivo = open('archivo_salida.txt', 'w')  # Abre el archivo en modo escritura
    archivo.write("Primera línea.\n")
    archivo.write("Segunda línea.\n")
finally:
    archivo.close()

# Agregar contenido a un archivo existente
try:
    archivo = open('archivo_salida.txt', 'a')  # Abre el archivo en modo agregar
    archivo.write("Tercera línea agregada.\n")
finally:
    archivo.close()

# Uso del bloque 'with' para manipular archivos
# El bloque 'with' maneja automáticamente la apertura y el cierre del archivo.

# Leer un archivo usando 'with'
with open('archivo_ejemplo.txt', 'r') as archivo:
    contenido = archivo.read()
    print("Contenido leído con 'with':")
    print(contenido)

# Escribir en un archivo usando 'with'
with open('archivo_salida.txt', 'w') as archivo:
    archivo.write("Escribiendo con 'with'.\n")

# Manejo de errores al trabajar con archivos
# Se recomienda manejar posibles excepciones, como FileNotFoundError, al trabajar con archivos.

try:
    with open('archivo_no_existente.txt', 'r') as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("Error: El archivo no existe.")

# Este es el final del quinto script. Continúa con el siguiente script para aprender más
# sobre Python.
