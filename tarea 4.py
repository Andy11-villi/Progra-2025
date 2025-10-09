#Ejercicio 1
#1. MiEsDigito
#Input: MiEsDigito
#Output: Booleano indicando si el string se compone de puros números
# MiEsDigito("1234") == True # probamos si funciona con puros números
# MiEsDigito("abcd") == False # probamos si funciona con puras letras
# MiEsDigito("123a") == False # probamos si hay números y letras
# MiEsDigito("12a4") == False # probamos que la letra esté a la mitad de los números

def MiEsDigito(a):
    return a.isdigit()
print(MiEsDigito("1234") == True )
print(MiEsDigito("abcd") == False )
print(MiEsDigito("123a") == False   )
print(MiEsDigito("12a4") == False)

#2. MiConteo
# Input: dos strings, el segundo es sólo un caracter
# Output: un entero con el número de veces que aparece el segundo string en el primer string
# MiConteo("hola mundo","o") == 2
# MiConteo("hola mundo","h") == 1
# MiConteo("hola mundo"," ") == 1
# MiConteo("hola mundo","r") == 0
# MiConteo("hola mundo","!") == 0
# MiConteo("hola mundo","") == 0
# MiConteo("","A") == 0
#if len(caracter) !=1: significa: Si la longitud de caracter no es igual a 1.

def MiConteo(cadena, caracter):
    if len(caracter) !=1:
        return 0
    return cadena.count (caracter)
print(MiConteo("hola mundo","o") == 2)
print(MiConteo("hola mundo","h") == 1)
print(MiConteo("hola mundo"," ") == 1)
print(MiConteo("hola mundo","r") == 0)
print(MiConteo("hola mundo","!") == 0)
print(MiConteo("hola mundo","") == 0)
print(MiConteo("","A") == 0)

# 3. GCcontent
# Input: un string con una secuencia de ADN
# Output: porcentaje de caracteres que son "G" ó "C"
# GCcontent("ATGC") == .5
# GCcontent("") == 0
# GCcontent("AAAA") == 0
# GCcontent("ATgc") == .5
# GCcontent("GGCC") == 1
#Regresa el resultadode dividirlo g_c entre la longitud de la secuencia.

def GCcontent(secuencia):
    if len(secuencia)== 0:
        return 0
    secuencia = secuencia.upper()
    gc_count= secuencia.count("G")+ secuencia. count("C")
    return gc_count / len(secuencia)

print(GCcontent("ATGC"))
print(GCcontent(""))
print(GCcontent("AAAA"))
print(GCcontent("ATgc"))
print(GCcontent("GGCC"))

# 4. MiSwapCase
# Input: un string
# Output: un string que invierta las mayúsculas y minúsculas
#"Hola Mundo"


def MiSwapCase(s):
    return s.swapcase()
print(MiSwapCase("Hola Mundo"))

#Escogí este codigo porque la función MiSwapCase tiene una sola responsabilidad, invertir las mayúsculas y minusculas, al usar este codigo es mas rapido y se ve mas ordenado ya que ocupa muy pocas lineas.



# 5. MiCapitalize
# Input: un string
# Output: un string que tenga la primera letra en mayúsculas

def  MiCapitalize(a):
    if len(a)==0:
        return ""
    return a[0].upper()

  
#Escogí este codigo porque solo cambia la primera letra, sin tocar el resto del texto y NO modifica mayúsculas/minúsculas del resto del string.



  
#  6. EsPar
#Input: Un número entero
#Output: Imprime si el número es par o impar, no debe regresar nada

def EsPar(numero):
    if numero % 2== 0:
        print("El número es par")
    else:
        print("El número es impar")


#Escogí este codigo porque:
#El operador módulo (%) devuelve el residuo de una división.
# Si numero % 2 es 0, significa que el número es divisible entre 2 es par.
# Si no, es impar.
# Es la forma más directa en Python para comprobar si un número es par.        
