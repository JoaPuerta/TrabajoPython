"""lista = [] # Lista vacia
listas = [2,1.30,"Hola", True, False]"""
#mutables: se pueden modificar 
#indexadas: tienen un indice el ultimo elemento de la lista es -1
#len(): Muestra la longitud 
"""print (len(listas))"""
#acceder a la lista 
"""print (listas[2])
print (listas[-2])"""

#modificar elemento 
"""listas [2] = "Colecciones" 
print (listas)"""
#Recorrer una lista 
"""for elemento in listas:
    print (elemento)"""
#indice (posicion)
"""for elem in range (len(listas)):
    print (f"{listas[elem]} esta en la posicion {elem}")"""

#Insertar elemento: insert (posicion, dato o elemento a ingresar),
#append (dato o elemento a ingresar) ingrese el elemento en la ultima posicion,
"""marcas_autos = ["renault","chevrolet","suzuki","Audi","Kia"]
marcas_autos.insert(3,"Mazda")
marcas_autos.append("Toyota")
print(marcas_autos)"""
#Eliminar elemento: pop(posicion), remove(elemento)
"""marcas_autos.pop(5)
marcas_autos.remove("chevrolet")
print (marcas_autos)"""
#Conocer la posicion del elemento: index(elemento)
"""Posicion = marcas_autos.index("suzuki")
print(Posicion)"""
#Organizar lista: ascendente sort (), descendente sort(reverse=True)
"""marcas_autos.sort()
print(marcas_autos)
marcas_autos.sort(reverse=True)
print(marcas_autos)"""
#Extender la lista: extend(lista)
"""otras_marcas = ["Bmw","Ferrari","Telsa","Mercedez Benz"]
marcas_autos.extend(otras_marcas)
print(marcas_autos)"""
#Recorrer 2 o más listas al mismo tiempo 
"""animales = ["Gato","Leon","Ballena","Pajaro","Serpiente"]
tipo_a = ["Terrestre","Salvaje","Mamifero","Aereo","Reptil"]
for animal, tipo in zip(animales, tipo_a):
    print(f"{animal} es un animal tipo {tipo}")"""

#Contar elementos repetidos: count()
"""numeros = [1,2,3,4,5,1,345,1,45,2,1,1,1,456]
contar = numeros.count(1)
print(contar)"""

#Ejercicio
#Crear 2 listas vacias una llamada tienda, otra llamada precio, 
#el usuario debe ingresar el numero de articulos de la tienda y 
#los elementos de cada lista, estos elementos deben ser agregados 
#a la lista correspondiente, debe mostrar los elementos de la tienda con su respectivo precio. (for, while)

"""print("Tu tienda")
tienda = []
precio = []

num_articulos = int(input("Ingrese el número de artículos de la tienda: "))

# Ciclo for para pedir al usuario que ingrese los elementos de la lista tienda y precio
for i in range(num_articulos):
    item = input(f"Ingrese el nombre del artículo {i+1}: ")
    tienda.append(item)
    
    precio_item = float(input(f"Ingrese el precio de {item}: "))
    precio.append(precio_item)

# Mostrar cada elemento de la tienda junto con su precio correspondiente
print("Lista de tienda y precios:")
for i in range(num_articulos):
    print(f"{tienda[i]}: ${precio[i]:.2f}")"""












