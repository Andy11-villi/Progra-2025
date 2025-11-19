# 1. Operador módulo en Python
# El operador módulo (%) regresa el residuo de una división entre dos números.
# Ejemplo: 10 % 3 = 1, porque 10 dividido entre 3 da 3 y sobra 1.
print("Ejemplo módulo:", 10 % 3)


# 2. Crear lista vacía y llenarla con números pares del 2 al 50
pares = []
for i in range(2, 51):  # recorre del 2 al 50
    if i % 2 == 0:      # condición: si es par
        pares.append(i)
print("Números pares del 2 al 50:", pares)


# 3. Comando break en un for
# El break sirve para detener un ciclo antes de que termine todas sus iteraciones.
# Ejemplo: detener el ciclo cuando encontramos el número 5.
for i in range(1, 11):
    if i == 5:
        print("Se encontró el número 5, se rompe el ciclo.")
        break
    print("Número:", i)


# 4. Programar el método find de strings a mano
palabra = "banana"
buscada = "a"
posicion = -1

for i in range(len(palabra)):
    if palabra[i] == buscada:
        posicion = i
        break  # se detiene en la primera coincidencia

print(f"La primera '{buscada}' está en la posición:", posicion)


# 5. Imprimir todos los números de la lista utilizando ciclos
lista = [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]]

for sublista in lista:       # recorre cada sublista
    for numero in sublista:  # recorre cada número dentro de la sublista
        print(numero)