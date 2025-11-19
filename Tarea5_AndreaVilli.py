# abrir el archivo
nombreArchivo = 'ejemplo.fasta'
fasta = open(nombreArchivo,'r')
# print(fasta.read())

def cuentaGC(secuencia):
    if secuencia == '':
        return 0
    secuencia = secuencia.upper()
    return (secuencia.count('C') + secuencia.count('G'))/len(secuencia)

def complement(dna):
    dna2=dna.replace("A","a").replace("T","A").replace("a","T").replace("C","c").replace("G","C").replace("c","G")
    return dna2

salida = open('resultadosEjercico.txt','w')
fastaSalida = open('ejercicoReversas.fasta','w')

numLinea = 0
banderaPrimeraLinea = True
secuenciaCompleta = ''
contigActual = ''

for linea in fasta:
    numLinea += 1
    linea = linea.strip()
    # 1. Para todos los encabezados, lo imprima en el formato
    # "Organismo <el nombre del fasta>, contig <el contenido del encabezado, sin el ">""
    # buscamos los encabezados que empiezan con >
    if linea.startswith('>'):
        print(f'Organismo {nombreArchivo.replace(".fasta","")}, contig {linea[1:]}')
        salida.write(f'Organismo {nombreArchivo.replace(".fasta","")}, contig {linea[1:]}\n')
        banderaPrimeraLinea = True
        contigActual = linea[1:]
    # 2. Para cada línea de secuencia genómica, imprima su contenido de GC en el formato "GC línea <número de línea>: <GC"
    else:
        linea = linea.upper()
        gc = cuentaGC(linea)
        print(f'GC linea {numLinea}: {gc:0.2f}')
        salida.write(f'GC linea {numLinea}: {gc:0.2f}\n')
    # 3. Para la primera secuencia de cada segmento, imprima su secuencia complementaria
        if banderaPrimeraLinea:
            reversaComplementaria = complement(linea)
            print(reversaComplementaria)
            salida.write(f'{reversaComplementaria}\n')
            fastaSalida.write(f'>{contigActual} | {numLinea}\n')
            fastaSalida.write(f'{reversaComplementaria}\n')
        banderaPrimeraLinea = False
    # 4. Imprima el número de línea donde encuentre el codón "ATG" en el formato "ATG en línea <número de línea>"
        if 'ATG' in linea:
            print(f'ATG en linea {numLinea}')
            salida.write(f'ATG en linea {numLinea}\n')
    
    # 5. Calcule el contenido GC total del archivo y lo imprima al final en formato "GC total del archivo: <GC>"
        secuenciaCompleta += linea
        # print(f'sec completa: {secuenciaCompleta}')
gcCompleto = cuentaGC(secuenciaCompleta)
print(f'GC total de archivo: {gcCompleto:0.2f}')
salida.write(f'GC total de archivo: {gcCompleto:0.2f}\n')

salida.close()
fastaSalida.close()