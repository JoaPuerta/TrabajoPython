#EJERCICIOS TUPLAS Y DICCIONARIOS
"""1. Crear una tupla con números que usted desee, crear dos tuplas vacías llamadas par 
y la otra impar. A través de un ciclo for recorrer la tupla numérica si el numero evaluado 
es para ingresar el valor a la tupla par, de lo contrario insertar a la tupla impar."""

# Crear una tupla con números
"""numeros = (2, 5, 8, 9, 10, 13, 15, 16)

# Crear tuplas vacías
par = ()
impar = ()

# Recorrer la tupla de números
for numero in numeros:
    if numero % 2 == 0:  # si el número es par
        par += (numero,)  # agregar a la tupla par
    else:  # si el número es impar
        impar += (numero,)  # agregar a la tupla impar

# Imprimir las tuplas resultantes
print("Tupla de números pares:", par)
print("Tupla de números impares:", impar)"""

#-------------------------------------------------------------------------------------------

"""2. Crear una tupla con diferentes valores numéricos o cadenas de texto, crear un programa 
que muestre el elemento mayor y menor de la tupla usando la función correspondiente."""

# Crear una tupla con diferentes valores
"""mis_valores = (23, 5, 13, 54, 9, 87, 11)

# Encontrar el elemento mayor y menor de la tupla
elemento_mayor = max(mis_valores)
elemento_menor = min(mis_valores)

# Imprimir los resultados
print("La tupla es:", mis_valores)
print("El elemento mayor de la tupla es:", mis_valores)
print("El elemento menor de la tupla es:", mis_valores)"""

#-------------------------------------------------------------------------------------------

"""3. Crea una tupla numérica, pide al usuario que ingrese un número y crea un programa que 
cuente cuantas veces está el numero ingresado en la tupla, de lo contrario muestre que el 
número no se encuentra."""

# Creamos una tupla numérica
"""mi_tupla = (2, 5, 6, 7, 5, 4, 8, 5, 9)

# Pedimos al usuario que ingrese un número
numero_usuario = int(input("Ingrese un número: "))

# Creamos una variable para contar las veces que aparece el número
contador = 0

# Iteramos sobre la tupla y contamos las veces que aparece el número
for num in mi_tupla:
    if num == numero_usuario:
        contador += 1

# Mostramos el resultado al usuario
if contador > 0:
    print(f"El número {numero_usuario} aparece {contador} veces en la tupla.")
else:
    print("El número no se encuentra en Python.")"""


#-------------------------------------------------------------------------------------------

"""4. Crea un diccionario donde la clave sea el nombre del usuario y el valor sea el teléfono. 
Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere insertar más. 
No se podrán meter nombres repetidos. Debe imprimir el diccionario creado."""


"""agenda = {}

while True:
    nombre = input("Ingrese el nombre del contacto o 'q' para salir: ")
    if nombre == "q":
        break

    if nombre in agenda:
        print("El nombre ya existe en la agenda.")
        continue

    telefono = input("Ingrese el teléfono del contacto: ")
    agenda[nombre] = telefono

print("Agenda de contactos:")
print(agenda)"""

#-------------------------------------------------------------------------------------------

""" 5. Teniendo en cuenta el punto anterior, crea un programa que solicite al usuario la clave(usuario) 
y muestre el teléfono correspondiente """

""" agenda = {}

while True:
    nombre = input("Ingrese el nombre del contacto o 'q' para salir: ")
    if nombre == "q":
        break

    if nombre in agenda:
        print("El nombre ya existe en la agenda.")
        continue

    telefono = input("Ingrese el teléfono del contacto: ")
    agenda[nombre] = telefono

print("Agenda de contactos:")
print(agenda)

while True:
    nombre_buscar = input("Ingrese el nombre del contacto a buscar o 'q' para salir: ")
    if nombre_buscar == "q":
        break

    if nombre_buscar in agenda:
        print(f"El teléfono de {nombre_buscar} es {agenda[nombre_buscar]}.")
    else:
        print("El nombre no se encuentra en la agenda.") """

#-------------------------------------------------------------------------------------------

""" 6. Crea una tupla con valores ya predefinidos del 1 al 10, pide un índice por 
teclado y muestra los valores de la tupla. """

# Crear la tupla
""" mi_tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Pedir el índice al usuario
indice = int(input("Ingrese un índice para mostrar el valor de la tupla: "))

# Mostrar el valor correspondiente en la tupla
if indice >= 0 and indice < len(mi_tupla):
    print(f"El valor de la tupla en el índice {indice} es: {mi_tupla[indice]}")
else:
    print("El índice ingresado no es válido.") """

#-------------------------------------------------------------------------------------------

#LISTAS
#1. Encuentra los errores en los siguientes ejemplos de lista:

# A= El igual 
# B= Hay dos errores en el código. 1.la coma / 2. Está tratando de acceder al primer elemento 
#    de la lista utilizando paréntesis en lugar de corchetes []
# C= negativo, debe manejar un indice valido -0 es igual a 0 y -4 no existe 

#-------------------------------------------------------------------------------------------

"""2. Crea una lista vacía llamada departamentos Colombia, pida al usuario la cantidad de 
departamentos a ingresar, a través de un ciclo for pida al usuario que ingrese el departamento 
de Colombia que desee, agregue esta información a la lista y luego esta sea ordenada en orden descendente.
    a. Se debe imprimir la lista con los valores organizados de forma descendentes.
    b. Debe imprimir además los 2 últimos departamentos ingresados."""


# Crear lista vacía de departamentos de Colombia
"""departamentos_colombia = []

# Pedir cantidad de departamentos a ingresar
cantidad_departamentos = int(input("Ingrese la cantidad de departamentos que desea ingresar: "))

# Pedir al usuario que ingrese los departamentos y agregarlos a la lista
for i in range(cantidad_departamentos):
    departamento = input(f"Ingrese el departamento {i+1} de Colombia: ")
    departamentos_colombia.append(departamento)

# Ordenar la lista en orden descendente
departamentos_colombia.sort(reverse=True)

# Imprimir la lista de departamentos organizados de forma descendente
print("Lista de departamentos de Colombia organizados en orden descendente:")
for departamento in departamentos_colombia:
    print(departamento)

# Imprimir los 2 últimos departamentos ingresados
print(f"\nLos 2 últimos departamentos ingresados son: {departamentos_colombia[-2:]}")"""

#-------------------------------------------------------------------------------------------

""" 3. crea una lista vacía llamada números, a través de un bucle for o while pide al usuario que 
ingrese números enteros, agrega los números a la lista y luego ordena esta de forma ascendente y 
descendente. Mostrar ambas listas (ascendente y descendente) """

# Crear lista vacía de números
"""numeros = []

# Pedir al usuario que ingrese números enteros
while True:
    num = input("Ingrese un número entero o escriba 'fin' para terminar: ")
    if num == 'fin':
        break
    numeros.append(int(num))

# Ordenar la lista en orden ascendente y descendente
ascendente = sorted(numeros)
descendente = sorted(numeros, reverse=True)

# Imprimir las listas ordenadas
print("Lista de números ordenados en forma ascendente: ")
print(ascendente)

print("\nLista de números ordenados en forma descendente: ")
print(descendente) """




