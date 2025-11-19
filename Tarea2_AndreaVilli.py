# 1. Crear una lista vacía y llenarla con los números del 1 al 50
lista1 = []
for i in range(1, 51):
    lista1.append(i)
print("Ejercicio 1:", lista1)

# 2. Crear una lista vacía y llenarla con los múltiplos de 5 del 2 al 50
lista2 = []
for i in range(2, 51):
    if i % 5 == 0:
        lista2.append(i)
print("Ejercicio 2:", lista2)

# 3. Imprimir el patrón de asteriscos
print("Ejercicio 3:")
for i in range(1, 11):
    print("*" * i)

# 4. Usar ciclo while para imprimir números del 1 al 10
print("Ejercicio 4:")
num = 1
while num <= 10:
    print(num)
    num += 1