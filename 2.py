# Script 2: Operaciones Básicas y Estructuras de Control

# En este segundo script, exploraremos las operaciones básicas y las estructuras de control en Python.
# Aprenderemos cómo realizar operaciones matemáticas, usar condicionales y loops.

# Importar la librería math para operaciones matemáticas avanzadas
import math

# Operaciones Matemáticas Básicas
a = 10
b = 5

suma = a + b  # Suma
resta = a - b  # Resta
multiplicacion = a * b  # Multiplicación
division = a / b  # División
modulo = a % b  # Módulo (resto de la división)
potencia = a ** b  # Potencia
raiz_cuadrada = math.sqrt(a)  # Raíz cuadrada

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("Módulo:", modulo)
print("Potencia:", potencia)
print("Raíz cuadrada:", raiz_cuadrada)

# Estructuras de Control: Condicionales
# Las estructuras de control permiten alterar el flujo de ejecución del programa.

# Condicional 'if'
if a > b:
    print("a es mayor que b")

# Condicional 'if-else'
if a < b:
    print("a es menor que b")
else:
    print("a no es menor que b")

# Condicional 'if-elif-else'
if a == b:
    print("a es igual a b")
elif a > b:
    print("a es mayor que b")
else:
    print("a es menor que b")

# Estructuras de Control: Loops
# Los loops permiten ejecutar un bloque de código varias veces.

# Loop 'while'
contador = 0
while contador < 5:
    print("Contador (while):", contador)
    contador += 1  # Incrementar el contador

# Loop 'for'
# La función 'range' genera una secuencia de números.
for i in range(5):
    print("Contador (for):", i)

# Loop 'for' con listas
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print("Fruta:", fruta)

# Este es el final del segundo script. Continúa con el siguiente script para aprender más
# sobre Python.
