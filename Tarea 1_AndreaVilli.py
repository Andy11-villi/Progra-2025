# tarea1_strings.py


# 1. Concatenar un número a un string
# Opción: convertir el número a string con str()
texto = "Número: " + str(5)
print(texto)  # Resultado: Número: 5

# 2. Tipos de variables
a = "1"        # str
b = 1.0        # float
c = 1.5 + True # float (True = 1, entonces 1.5 + 1 = 2.5)
d = 1.5 + 2.5  # float
e = 1 + True   # int (True = 1, entonces 1+1=2)
f = False + True # int (0+1=1)
g = True * 0   # int (1*0=0)

print(type(a), type(b), type(c), type(d), type(e), type(f), type(g))

# 3. Manipulación de strings
# a. cambiar letras por números
palabra = "hola"
palabra_mod = palabra.replace("h", "H").replace("o", "0").replace("l", "1").replace("a", "4")
print(palabra_mod)  # Ho14

# b. remover espacios
palabra = "  hola"
print(palabra.strip())  # hola

# c. cambiar mayúsculas y minúsculas
palabra = "HoLa"
print(palabra.swapcase())  # hOlA

# d. primera en mayúscula
palabra = "hola"
print(palabra.capitalize())  # Hola

# 4. Métodos de strings
# count(): cuenta ocurrencias
print("banana".count("a"))  # 3

# find(): devuelve índice de la primera coincidencia
print("banana".find("na"))  # 2

# isdigit(): verifica si todos los caracteres son dígitos
print("123".isdigit())  # True
print("12a".isdigit()) # False

# replace(): reemplaza subcadenas
print("hola mundo".replace("mundo", "Python"))  # hola Python

# 5. Problemas al declarar variables
# oración larga = 'hola mundo'  -> Error: contiene espacio en el nombre
# palabra = 'hola' 'mundo'      -> Se concatena automáticamente: 'holamundo'

# 6. f-strings
# Son una forma de formatear strings usando {}
nombre = "Andrea"
edad = 22
print(f"Hola, me llamo {nombre} y tengo {edad} años.")