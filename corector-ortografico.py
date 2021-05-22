import re
 
# Esta función toma una línea de texto y devuelve
# una lista de las palabras en la línea.
def separar_linea(linea):
    return re.findall('[A-Za-zÁ-Úá-ú]+(?:\'[A-Za-zÁ-Úá-ú]+)?',linea)

file = open("listado-general.txt")
dictionario_lista= []
for linea in file:
    linea = linea.strip()
    dictionario_lista.append(linea)
file.close()
file = open("texto-prueba.txt")
for linea in file :
    palabras=separar_linea(linea)
    for palabra in palabras :
        clave = palabra.lower()
        i=0
        
        while i < len(dictionario_lista) and dictionario_lista[i] != clave:
            i += 1
        
        if i == len(dictionario_lista):
            print(clave)
            print( "El nombre no estaba en la lista." )
file.close()
#print(dictionario_lista)