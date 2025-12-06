# PROYECTO FINAL

# PASO 1: Leer el archivo FASTA

def leer_fasta(archivo):
    secuencias = {}
    with open(archivo, 'r') as f:
        nombre = ""
        secuencia = []
        for linea in f:
            linea = linea.strip()
            if linea.startswith('>'):
                if nombre:
                    secuencias[nombre] = ''.join(secuencia)
                nombre = linea[1:]
                secuencia = []
            else:
                secuencia.append(linea)
        if nombre:
            secuencias[nombre] = ''.join(secuencia)
    return secuencias

# Leer el archivo PROTEIN.fasta
secuencias = leer_fasta('PROTEIN.fasta')
print(f"Secuencias leídas: {len(secuencias)}")
for nombre in secuencias:
    print(f"  - {nombre}: {len(secuencias[nombre])} bases")


# PASO 2: Diccionario de codones para traducción

codones = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    'TGA':'*', 'TGC':'C', 'TGT':'C', 'TGG':'W'
}
# PASO 3: Función para traducir ADN a proteína

def traducir(secuencia):
    proteina = ""
    for i in range(0, len(secuencia), 3):
        codon = secuencia[i:i+3]
        proteina += codones.get(codon, 'X')
    return proteina

# Probar la función
prueba = "ATGAAATAA"
print(f"Prueba traducción: {prueba} -> {traducir(prueba)}")

# PASO 4: Buscar proteínas que cumplan criterios

def buscar_proteinas_en_secuencia(secuencia, nombre):
    resultados = []
    stop_codones = ['TAA', 'TAG', 'TGA']
    
    # Buscar en toda la secuencia
    for i in range(len(secuencia) - 2):
        # Verificar codón de inicio
        if secuencia[i:i+3] == 'ATG':
            # Buscar codón de paro
            for j in range(i + 3, len(secuencia) - 2, 3):
                if secuencia[j:j+3] in stop_codones:
                    # Extraer la secuencia
                    seq = secuencia[i:j+3]
                    # Verificar criterios
                    longitud = len(seq)
                    if longitud % 3 == 0 and 30 <= longitud <= 90:
                        # Traducir
                        prot = traducir(seq)
                        if prot.endswith('*'):
                            resultados.append({
                                'nombre': nombre,
                                'inicio': i + 1,
                                'fin': j + 3,
                                'secuencia_nt': seq,
                                'proteina': prot[:-1],
                                'marco': 1
                            })
                    break
    
    return resultados

# Buscar proteínas en todas las secuencias
todas_proteinas = []
for nombre, seq in secuencias.items():
    proteinas = buscar_proteinas_en_secuencia(seq, nombre)
    todas_proteinas.extend(proteinas)
    print(f"En {nombre}: {len(proteinas)} proteínas")

# PASO 5: Guardar resultados en archivo FASTA

with open('proteinas_encontradas.fasta', 'w') as f:
    for i, prot in enumerate(todas_proteinas, 1):
        f.write(f">{prot['nombre']}_proteina{i}\n")
        f.write(f"{prot['proteina']}\n")

print(f"Archivo FASTA creado: proteinas_encontradas.fasta")

# PASO 6: Opcional - Archivo GFF

with open('proteinas.gff', 'w') as f:
    f.write("##gff-version 3\n")
    for i, prot in enumerate(todas_proteinas, 1):
        f.write(f"{prot['nombre']}\t")
        f.write(f"MiAnalizador\t")
        f.write(f"CDS\t")
        f.write(f"{prot['inicio']}\t")
        f.write(f"{prot['fin']}\t")
        f.write(f".\t")
        f.write(f"+\t")
        f.write(f"0\t")
        f.write(f"ID=proteina{i};Name={prot['proteina'][:10]}...\n")

print("Archivo GFF creado: proteinas.gff")

# PASO 7: Opcional - CSV con información

with open('resultados.csv', 'w') as f:
    f.write("nombre,inicio,fin,longitud_nt,longitud_aa,secuencia_aa,marco\n")
    for prot in todas_proteinas:
        f.write(f"{prot['nombre']},")
        f.write(f"{prot['inicio']},")
        f.write(f"{prot['fin']},")
        f.write(f"{len(prot['secuencia_nt'])},")
        f.write(f"{len(prot['proteina'])},")
        f.write(f"{prot['proteina']},")
        f.write(f"{prot['marco']}\n")

print("Archivo CSV creado: resultados.csv")

# PASO 8: Análisis de contenido GC

def calcular_gc(secuencia):
    gc = 0
    for base in secuencia:
        if base in 'GC':
            gc += 1
    return (gc / len(secuencia)) * 100

# Calcular GC para cada secuencia
with open('contenido_gc.txt', 'w') as f:
    f.write("CONTENIDO GC POR SECUENCIA\n")
    f.write("=" * 30 + "\n")
    
    for nombre, seq in secuencias.items():
        gc_total = calcular_gc(seq)
        f.write(f"\n{nombre}:\n")
        f.write(f"  Longitud: {len(seq)} bp\n")
        f.write(f"  GC total: {gc_total:.2f}%\n")
        
        # GC en ventanas de 50bp
        f.write("  GC en ventanas de 50bp:\n")
        for i in range(0, len(seq), 50):
            ventana = seq[i:i+50]
            if len(ventana) > 0:
                gc_ventana = calcular_gc(ventana)
                f.write(f"    Pos {i+1}-{i+len(ventana)}: {gc_ventana:.2f}%\n")

print("Análisis GC guardado: contenido_gc.txt")


# PASO 9: Buscar promotores


def buscar_promotores(secuencia, pos_inicio):
    tata = False
    ttgaca = False
    
    # TATA box (10 bp antes)
    if pos_inicio >= 10:
        region = secuencia[pos_inicio-10:pos_inicio]
        if 'TATA' in region:
            tata = True
    
    # TTGACA (35 bp antes)
    if pos_inicio >= 35:
        region = secuencia[pos_inicio-35:pos_inicio-30]
        if region == 'TTGACA':
            ttgaca = True
    
    return tata, ttgaca

# Actualizar resultados con información de promotores
for prot in todas_proteinas:
    inicio_idx = prot['inicio'] - 1  # Convertir a índice 0-based
    tata, ttgaca = buscar_promotores(secuencias[prot['nombre']], inicio_idx)
    prot['tata'] = tata
    prot['ttgaca'] = ttgaca

print(f"Promotores analizados para {len(todas_proteinas)} proteínas")

# PASO 10: Buscar Kozak y Shine-Dalgarno

def buscar_kozak_shine(secuencia, pos_inicio):
    kozak = False
    shine = False
    
    # Shine-Dalgarno
    if pos_inicio >= 6:
        for i in range(3, 11):
            if pos_inicio >= i + 6:
                region = secuencia[pos_inicio-i-6:pos_inicio-i]
                if region == 'AGGAGG':
                    shine = True
                    break
    
    # Kozak
    if pos_inicio >= 15:
        region = secuencia[pos_inicio-15:pos_inicio+5]
        if 'GCCACCATGG' in region:
            kozak = True
    
    return kozak, shine

# Actualizar resultados
for prot in todas_proteinas:
    inicio_idx = prot['inicio'] - 1
    kozak, shine = buscar_kozak_shine(secuencias[prot['nombre']], inicio_idx)
    prot['kozak'] = kozak
    prot['shine'] = shine


# PASO 11: Actualizar CSV con nueva información

with open('resultados_completo.csv', 'w') as f:
    f.write("nombre,inicio,fin,longitud_nt,longitud_aa,secuencia_aa,marco,tata,ttgaca,kozak,shine\n")
    for prot in todas_proteinas:
        f.write(f"{prot['nombre']},")
        f.write(f"{prot['inicio']},")
        f.write(f"{prot['fin']},")
        f.write(f"{len(prot['secuencia_nt'])},")
        f.write(f"{len(prot['proteina'])},")
        f.write(f"{prot['proteina']},")
        f.write(f"{prot['marco']},")
        f.write(f"{prot['tata']},")
        f.write(f"{prot['ttgaca']},")
        f.write(f"{prot['kozak']},")
        f.write(f"{prot['shine']}\n")

print("CSV actualizado: resultados_completo.csv")

# PASO 12: Búsqueda en reversa complementaria

def complemento_reverso(secuencia):
    complemento = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    reversa = ""
    for base in secuencia[::-1]:
        reversa += complemento.get(base, base)
    return reversa

# Buscar proteínas en la cadena complementaria
proteinas_reversa = []
for nombre, seq in secuencias.items():
    seq_reversa = complemento_reverso(seq)
    proteinas = buscar_proteinas_en_secuencia(seq_reversa, nombre + "_rev")
    proteinas_reversa.extend(proteinas)
    print(f"En reversa de {nombre}: {len(proteinas)} proteínas")

# Combinar resultados
todas_proteinas.extend(proteinas_reversa)

# PASO 13: Codones de inicio alternativos


# Modificar la función de búsqueda para incluir codones alternativos
def buscar_proteinas_completo(secuencia, nombre):
    resultados = []
    stop_codones = ['TAA', 'TAG', 'TGA']
    start_codones = ['ATG', 'CTG', 'TTG', 'GTG']  # Codones alternativos
    
    for i in range(len(secuencia) - 2):
        if secuencia[i:i+3] in start_codones:
            for j in range(i + 3, len(secuencia) - 2, 3):
                if secuencia[j:j+3] in stop_codones:
                    seq = secuencia[i:j+3]
                    if len(seq) % 3 == 0 and 30 <= len(seq) <= 90:
                        prot = traducir(seq)
                        if prot.endswith('*'):
                            resultados.append({
                                'nombre': nombre,
                                'inicio': i + 1,
                                'fin': j + 3,
                                'secuencia_nt': seq,
                                'proteina': prot[:-1],
                                'marco': 1,
                                'start_codon': secuencia[i:i+3]
                            })
                    break
    
    return resultados

# Volver a buscar con codones alternativos
proteinas_alternativas = []
for nombre, seq in secuencias.items():
    proteinas = buscar_proteinas_completo(seq, nombre)
    proteinas_alternativas.extend(proteinas)

print(f"Proteínas con codones alternativos: {len(proteinas_alternativas)}")

# PASO 14: RESULTADO FINAL

print(f"\nArchivos analizados: PROTEIN.fasta")
print(f"Secuencias encontradas: {len(secuencias)}")
print(f"Proteínas pequeñas encontradas: {len(todas_proteinas)}")
print(f"Proteínas con codones alternativos: {len(proteinas_alternativas)}")

print(f"\nArchivos generados:")
print("  1. proteinas_encontradas.fasta")
print("  2. proteinas.gff")
print("  3. resultados.csv")
print("  4. resultados_completo.csv")
print("  5. contenido_gc.txt")
