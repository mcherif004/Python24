"""
Ejercicio 1

Escribe sentencias Python para realizar cada una de las siguientes tareas: 

a) Muestra el valor del elemento 6 de un array f.
b) Inicializa los 5 primeros elementos de un array unidimensional de enteros a 8.
c) Total de los 100 elementos de punto-flotante de un array c. 
d) Copia los 11 elementos de un array a en la primera porción de un array b, el cual contiene 34 elementos. 
e) Calcula y muestra el valor mayor y menor contenidos en un array w de 99 elementos de punto-flotante
"""

# Apartado a)

f = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f[5])

# Apartado b)

array = [0] * 10 # Sera un array con 10 ceros

for i in range(5):
    array[i] = 8

print(array)

# Apartado c)

c = [0.1] * 100

total = sum(c)

print(total)

# Apartado d)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] 
b = [0] * 34

b[:11] = a # Con los puntos delante coloca al principio y al final los pone al final

print(b)

# Apartado e)

w = [1.5, 1.2, 0.5] * 33

print(max(w)) #max()
print(min(w)) #min()