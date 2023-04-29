"""EJERCICIO WHILE
Hacer una calculadora en Python usando el ciclo while, teniendo en cuenta lo siguiente:
- El usuario debe ingresar los datos a tener en cuenta en las operaciones.
- La calculadora debe contener las siguientes opciones:
o Suma
o Resta
o Multiplicación
o División: para realizar esta operación debe tener una restricción que evite que el
usuario ingrese 0 como divisor.
o Potenciación
o Factorial de un numero ingresado
o Raíz cuadrada, debe especificar que el dato a ingresar debe ser entero positivo
o Cambiar números
o Salir
- Crear in código que arroje el resultado de la operación escogida por el usuario.
math — Funciones matemáticas
Este módulo proporciona acceso a las funciones matemáticas definidas
math.sqrt(x)
Retorna la raíz cuadrada de x."""

"""print ("Mi calculadora en Python")
import math

# Función para pedir un número entero positivo
def pedir_entero_positivo():
    while True:
        num = input("Ingresa un número entero positivo: ")
        if num.isdigit() and int(num) > 0:
            return int(num)
        print("Por favor, ingresa un número entero positivo.")

# Función para cambiar los números ingresados
def cambiar_numeros():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    return num1, num2

# Menú de opciones
menu = """
"""Calculadora:
1. Suma
2. Resta
3. Multiplicación
4. División
5. Potenciación
6. Factorial
7. Raíz cuadrada
8. Cambiar números
9. Salir"""
"""

# Inicialización de variables
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
opcion = 0

# Ciclo while para la calculadora
while opcion != 9:
    print(menu)
    opcion = int(input("Selecciona una opción: "))
    if opcion == 1:
        resultado = num1 + num2
        print(f"El resultado de la suma es: {resultado}")
    elif opcion == 2:
        resultado = num1 - num2
        print(f"El resultado de la resta es: {resultado}")
    elif opcion == 3:
        resultado = num1 * num2
        print(f"El resultado de la multiplicación es: {resultado}")
    elif opcion == 4:
        if num2 == 0:
            print("Error: No se puede dividir entre 0.")
        else:
            resultado = num1 / num2
            print(f"El resultado de la división es: {resultado}")
    elif opcion == 5:
        resultado = num1 ** num2
        print(f"El resultado de la potenciación es: {resultado}")
    elif opcion == 6:
        num = pedir_entero_positivo()
        resultado = math.factorial(num)
        print(f"El factorial de {num} es: {resultado}")
    elif opcion == 7:
        num = pedir_entero_positivo()
        resultado = math.sqrt(num)
        print(f"La raíz cuadrada de {num} es: {resultado}")
    elif opcion == 8:
        num1, num2 = cambiar_numeros()
    elif opcion == 9:
        print("Adiós!")
    else:
        print("Opción inválida. Por favor, selecciona una opción del menú.")"""
