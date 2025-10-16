#1.- Operador módulo en python y un ejemplo.
#Nos ayuda a devolver el residuo de un división, nos sirve para ver si un número es divisible entre otro.
#Ejemplo:

print(10%3)
print(8%2)

#2.- Crearuna lista vacia y llenarla con los números pares 2 al 50, utlizando for y un condicional para controlar que solo agrege pares.
#Ejemplo:
pares=[]
for i in  range(2,51):
    if i % 2==0:
      pares.append(i)
print(pares)

#3.- Para qué sirv el comando "break" en un for, explicarlo y dar un ejemplo.
#Este comando lo ocupamos para cuando usamos un ciclo y tenemos que detener la ejecución antes de que termine por si solo.
#Ejemplo:

for i in range(12):
   if i ==6:
      break
   print(i)

#Este ciclo imprime del 0 al 5, por lo tanto se detiene al llegar al 6.

#4.- Programar el método find de los strings, palabra = "banana"
#Ejemplo
palabra= "banana"
buscado="a"
posicion= -1
for i in range(len(palabra)):
   if palabra[i]== buscado:
      posicion=i
      break
print(posicion)   

#Imprimir todos los números de la seguiente lista utilizando ciclos:
#lista= [[1], [1,2], [1,2,3],[1,2,3,4], [1,2,3,4,5]]

lista= [[1], [1,2], [1,2,3],[1,2,3,4], [1,2,3,4,5]]
for sublista in lista:
   for numero in sublista:
      print(numero)