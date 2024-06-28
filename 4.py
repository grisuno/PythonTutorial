# Script 4: Funciones y Manejo de Errores

# En este cuarto script, aprenderemos a definir y usar funciones en Python, así como a manejar errores mediante excepciones.

# Funciones
# Las funciones son bloques de código que realizan una tarea específica y pueden ser reutilizadas.

# Definir una función simple
def saludar():
    print("Hola, Mundo!")

# Llamar a la función
saludar()

# Funciones con parámetros
def saludar_persona(nombre):
    print(f"Hola, {nombre}!")

# Llamar a la función con un argumento
saludar_persona("Juan")

# Funciones con retorno de valor
def sumar(a, b):
    return a + b

# Llamar a la función y almacenar el resultado
resultado = sumar(10, 5)
print("Resultado de la suma:", resultado)

# Funciones con parámetros por defecto
def saludar_persona_con_default(nombre="Amigo"):
    print(f"Hola, {nombre}!")

# Llamar a la función sin argumento
saludar_persona_con_default()
# Llamar a la función con un argumento
saludar_persona_con_default("María")

# Manejo de Errores
# El manejo de errores se hace mediante el uso de excepciones, que permiten controlar el flujo de ejecución cuando ocurre un error.

# Ejemplo de manejo de errores con try-except
def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
        return None
    except TypeError:
        print("Error: Ambos argumentos deben ser números.")
        return None
    else:
        return resultado
    finally:
        print("La operación de división ha finalizado.")

# Llamar a la función con argumentos válidos
print("División válida:", dividir(10, 2))
# Llamar a la función con una división por cero
print("División por cero:", dividir(10, 0))
# Llamar a la función con un tipo de dato incorrecto
print("División con tipo incorrecto:", dividir(10, "dos"))

# Este es el final del cuarto script. Continúa con el siguiente script para aprender más
# sobre Python.
