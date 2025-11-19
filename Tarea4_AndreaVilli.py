# tarea4.py

# 1. MiEsDigito
def MiEsDigito(cadena: str) -> bool:
    return cadena.isdigit()

# Pruebas
print(MiEsDigito("1234"))   # True
print(MiEsDigito("abcd"))   # False
print(MiEsDigito("123a"))   # False
print(MiEsDigito("12a4"))   # False


# 2. MiConteo
def MiConteo(cadena: str, caracter: str) -> int:
    if len(caracter) != 1:
        return 0
    return cadena.count(caracter)

# Pruebas
print(MiConteo("hola mundo", "o"))  # 2
print(MiConteo("hola mundo", "h"))  # 1
print(MiConteo("hola mundo", " "))  # 1
print(MiConteo("hola mundo", "r"))  # 0
print(MiConteo("hola mundo", "!"))  # 0
print(MiConteo("hola mundo", ""))   # 0
print(MiConteo("", "A"))            # 0


# 3. GCcontent
def GCcontent(secuencia: str) -> float:
    if len(secuencia) == 0:
        return 0
    secuencia = secuencia.upper()
    gc_count = secuencia.count("G") + secuencia.count("C")
    return gc_count / len(secuencia)

# Pruebas
print(GCcontent("ATGC"))   # 0.5
print(GCcontent(""))       # 0
print(GCcontent("AAAA"))   # 0
print(GCcontent("ATgc"))   # 0.5
print(GCcontent("GGCC"))   # 1


# 4. MiSwapCase
def MiSwapCase(cadena: str) -> str:
    return cadena.swapcase()

# Pruebas propias
print(MiSwapCase("Hola Mundo"))   # hOLA mUNDO
print(MiSwapCase("Python123"))    # pYTHON123
print(MiSwapCase("MiSWAPcase"))   # mIswapCASE
# Explicación: probamos con mezcla de mayúsculas, minúsculas y números


# 5. MiCapitalize
def MiCapitalize(cadena: str) -> str:
    if len(cadena) == 0:
        return ""
    return cadena[0].upper() + cadena[1:]

# Pruebas propias
print(MiCapitalize("hola"))       # Hola
print(MiCapitalize("python"))     # Python
print(MiCapitalize(""))           # ""
# Explicación: probamos con palabra normal, otra palabra y cadena vacía


# 6. EsPar
def EsPar(numero: int) -> None:
    if numero % 2 == 0:
        print(f"{numero} es par")
    else:
        print(f"{numero} es impar")

# Pruebas propias
EsPar(4)   # 4 es par
EsPar(7)   # 7 es impar
EsPar(0)   # 0 es par
# Explicación: probamos con número par, impar y el cero