# 1. Lista que funcione como conjunto


def agregar_a_conjunto(lista, elemento):
    """Agrega un elemento a la lista si no existe (simula un set)."""
    if elemento not in lista:
        lista.append(elemento)
    return lista

def agregar_valor(diccionario, llave, valor):
    """Agrega o sobreescribe un valor en un diccionario simulado con lista de tuplas."""
    for i, (k, v) in enumerate(diccionario):
        if k == llave:
            diccionario[i] = (llave, valor)  # sobreescribe
            break
    else:
        diccionario.append((llave, valor))  # agrega nuevo
    return diccionario



# 2. Dos listas que funcionen como diccionario


def crear_diccionario(llaves, valores):
    """Crea dos listas que simulan un diccionario."""
    return llaves, valores

def obtener_valor(llaves, valores, llave):
    """Busca el valor correspondiente a una llave."""
    if llave in llaves:
        idx = llaves.index(llave)
        return f"La llave {llave} tiene valor {valores[idx]}"
    else:
        return f"La llave {llave} no existe"



# 3. Convertir nucleótidos en proteína


# Diccionario del código genético simplificado
codigo_genetico = {
    "AUG": "M",  # Start codon (Metionina)
    "UUU": "F", "UUC": "F",
    "UUA": "L", "UUG": "L",
    "UAA": "*", "UAG": "*", "UGA": "*",  # Stop codons
    # Puedes agregar más codones según sea necesario
}

def traducir_a_proteina(secuencia):
    """Convierte una secuencia de ARN en proteína."""
    proteina = ""
    # Verificar que la longitud sea múltiplo de 3
    if len(secuencia) % 3 != 0:
        return "Error: la secuencia no tiene longitud múltiplo de 3"
    
    for i in range(0, len(secuencia), 3):
        codon = secuencia[i:i+3]
        aminoacido = codigo_genetico.get(codon, "?")  # ? si no está en el diccionario
        proteina += aminoacido
    return proteina


# Ejemplos de uso
# ---------------------------

if __name__ == "__main__":
    # 1. Conjunto
    conjunto = []
    conjunto = agregar_a_conjunto(conjunto, "a")
    conjunto = agregar_a_conjunto(conjunto, "b")
    conjunto = agregar_a_conjunto(conjunto, "a")  # no se repite
    print("Conjunto simulado:", conjunto)

    dicc_lista = []
    dicc_lista = agregar_valor(dicc_lista, "uno", 1)
    dicc_lista = agregar_valor(dicc_lista, "dos", 2)
    dicc_lista = agregar_valor(dicc_lista, "uno", 100)  # sobreescribe
    print("Diccionario simulado con lista de tuplas:", dicc_lista)

    # 2. Diccionario con dos listas
    llaves, valores = crear_diccionario(["uno", "dos", "tres"], [1, 2, 3])
    print(obtener_valor(llaves, valores, "uno"))
    print(obtener_valor(llaves, valores, "cuatro"))

    # 3. Traducción de nucleótidos
    secuencia = "AUGUUUUAA"
    print("Proteína traducida:", traducir_a_proteina(secuencia))