#Repite una instruccion hasta que la condicion sea falsa 

#Imprimir numeros menores o iguales que 10
"""numero = 0
while numero <= 10:
    print(numero)
    numero +=  1 # numero = numero + 1
print("Fin del ciclo")"""

#Pedir numeros por teclado, hasta que el usuario ingrese 0. Debe mostrar la suma de los valores ingresados.
"""suma = 0
valor = int(input("Ingrese un número entero positivo: "))
while valor != 0:
    suma += valor 
    valor = int(input("Ingrese un número entero positivo: "))
print("sumatoria = ",suma)"""
 
#Crear dos listas vacias llamadas par e impar, pida dos numeros,debe indicar que el segundo numero debe ser mayor 
# qur el primero, evaluar los mumeros del rango (desde el numero 1 hasta el numero 2), si el numero es par ingresar 
# a la lista par, de lo contrario ingresar a la lista impar     
"""par = []
impar = []
n1 = int(input("Ingrese numero entero positivo: "))
n2 = int(input("Ingrese numero entero positivo mayor que numero 1: "))
while n1 < n2:
    if n1 % 2 == 0:
        par.append(n1) #agregando elemento a la lista 
    else:
        impar.append(n1)
    n1 += 1
print("par =",par)
print("impar =",impar)"""
#-----------------------------------------------------------------------------------------------------------------
#Pedir la edad del usuario, mientras la edad sea mayor o igual que 18, el usuario debe escoger que bebida comprar
#(ron, cerveza, aguardiente) y debe mostrar la bebida escogida, de lo contrario debe mostrar (El mensaje que desee)

"""edad = int(input("Ingrese su edad: "))

# Verificar si el usuario tiene que tributar
while edad >= 18:
    bebida = int(input("Ingresa bebida que deseas tomar\n1. ron \n2. cerveza \n3. aguardiente\n")) 
if bebida == 1:
    print("La bebida escogida fue ron")
elif bebida == 2:
    print("La bebida escogida fue cerveza")
elif bebida == 3:
    print("La bebida escogida fue cerveza")
else:
    print("ingrese un numero entre 1 y 3")


print("los menores de edad no pueden BEBER busque a sus padres")"""
    

#

"""while num < 10:
    num += 1 
    if num == 5:
        continue
    print(fib(x))"""
#--------------------------------------------------------------------------------------------------------------   
#for: repite instrucciones   

"""texto = "python" 

for letra in texto:
    print(letra) 
    if letra == "h":"""
    
"""numeros = [10,23,38,42,59,66]

for i in range (len(numeros)):
    elemento = numeros[i]
    print(elemento, " esta en la posicion " ,i)"""

#Imprimir los numeros desde el 2 al 40 con un salto de 2 
 
"""for num in range (0,41,2):
     print (num)"""
    
    
# i anidado 
"""for i in  [1,2,3,4]:
    for j in [10,20,30,40]:
     print (i,j)"""
     
#Imprimir la tabla del 1 al 9
"""for f in range(1,11): 
    print(f'1 x {f} = {9 * f}')"""






    
            