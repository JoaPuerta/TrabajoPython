"""CONDICIONAL IF_ELSE

1. Para tributar un determinado impuesto se debe ser mayor de 18 años y tener
unos ingresos iguales o superiores a 2.500.000 mensuales. Escribir un
programa que pregunte al usuario su edad y sus ingresos mensuales y muestre
por pantalla si el usuario tiene que tributar o no."""

"""edad = int(input("Ingresa tu edad: "))
ingresos = float(input("Ingresa tus ingresos mensuales en COP: "))

if edad >= 18 and ingresos >= 2500000:
    print("Debes tributar.")
else:
    print("No estás obligado a tributar.")"""

"""--------------------------------------------------------------------------------------------------------"""

"""2. Escribir un programa donde se ingrese la nota de las materias: desarrollo de
software, matemáticas, lógica programación, si el promedio es mayor o igual
que 3,0 muestre en pantalla aprobado, de lo contrario muestre en pantalla
reprobado."""

"""desarrollo_software = float(input("Ingresa la nota de Desarrollo de Software: "))
matematicas = float(input("Ingresa la nota de Matemáticas: "))
logica_programacion = float(input("Ingresa la nota de Lógica de Programación: "))

promedio = (desarrollo_software + matematicas + logica_programacion) / 3

if promedio >= 3.0:
    print("Aprobado")
else:
    print("Reprobado")"""
    
"""--------------------------------------------------------------------------------------------------------"""
    
"""3. Solicitar un numero por teclado y mostrar en pantalla si el número es impar y
numero primo."""

"""numero = int(input("Ingresa un número: "))

# Verificar si es impar
if numero % 2 == 1:
    print("El número es impar")
else:
    print("El número es par")

# Verificar si es primo
es_primo = True
for i in range(2, numero):
    if numero % i == 0:
        es_primo = False
        break

if es_primo:
    print("El número es primo")
else:
    print("El número no es primo")"""

"""--------------------------------------------------------------------------------------------------------"""

"""ELIF
1. Comparar 4 números solicitados al usuario, escribir condiciones que permita
mostrar que un número fue escrito 2, que todos son iguales o por el contrario
todos son diferentes."""

"""numeros = []
for i in range(4):
    numero = int(input("Ingresa un número: "))
    numeros.append(numero)

# Verificar si hay algún número repetido
for numero in numeros:
    if numeros.count(numero) == 2:
        print("Un número fue escrito dos veces")
        break

# Verificar si todos los números son iguales
if len(set(numeros)) == 1:
    print("Todos los números son iguales")

# Verificar si todos los números son diferentes
if len(set(numeros)) == 4:
    print("Todos los números son diferentes")"""
    
"""--------------------------------------------------------------------------------------------------------"""







 
 