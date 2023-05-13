"""[7:52 a. m., 13/5/2023] Liliana Gómez Cesde: # 1: Crea una funcion que reciba un numero como parametro y devuelva true si es primo y false si no lo es

def es_primo(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for divisor in range(2, num):
            if num % divisor == 0:
                return False
        return True
    
num = 67
if es_primo(num):
    print(f"{num} es un número primo")
else:
    print(f"{num} no es un número primo")"""
    
    
    
    
"""# 2: utilizando la funcion del punto1, realizar otra funcion que reciba del parametro una lista de numeros  y devuelva en una lista solo aquellos que son primos
def listaPrimo(lista):
    primos = []
    for num in lista:
        if es_primo(num):
            primos.append(num)
    return prim…
[7:53 a. m., 13/5/2023] Liliana Gómez Cesde: # 3: crea una funcion que , al recibir una lista de numeros, devuelva el que mas se repite y cuantas veces lo hace. si hay mas de una repetida q devuelva cualquiera

def numero_mas_repetido(lista):
    frecuencias = {}
    for numero in lista:
        if numero in frecuencias:
            frecuencias[numero] += 1
        else:
            frecuencias[numero] = 1
    numero_mas_repetido = None
    frecuencia_maxima = 0
    for numero, frecuencia in frecuencias.items():
        if frecuencia > frecuencia_maxima:
            frecuencia_maxima = frecuencia
            numero_mas_repetido = numero
    return numero_mas_repetido, frecuencia_maxima

numeros = [1, 2, 3, 2, 4, 1, 5, 1, 6, 6, 6]
numero_mas_comun, frecuencia = numero_mas_repetido(numeros)
print(f"El número más común es {numero_mas_comun} y se repite {frecuencia} veces.")"""

# 3: crea una funcion que , al recibir una lista de numeros, devuelva el que mas se repite y cuantas veces lo hace. si hay mas de una repetida q devuelva cualquiera

"""def numero_mas_repetido(lista):
    frecuencias = {}
    for numero in lista:
        if numero in frecuencias:
            frecuencias[numero] += 1
        else:
            frecuencias[numero] = 1
    numero_mas_repetido = None
    frecuencia_maxima = 0
    for numero, frecuencia in frecuencias.items():
        if frecuencia > frecuencia_maxima:
            frecuencia_maxima = frecuencia
            numero_mas_repetido = numero
    return numero_mas_repetido, frecuencia_maxima

numeros = [1, 2, 3, 2, 4, 1, 5, 1, 6, 6, 6]
numero_mas_comun, frecuencia = numero_mas_repetido(numeros)
print(f"El número más común es {numero_mas_comun} y se repite {frecuencia} veces.")"""

#4. Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos


"""temperaturas = ["alta", "media", "baja"]

for temp1 in temperaturas:
    for temp2 in temperaturas:
        for temp3 in temperaturas:
            print(f"Combinación de temperaturas: {temp1}, {temp2}, {temp3}")"""