from os import read
import re
import string


# Esta función toma una línea de texto y devuelve
# una lista de las palabras en la línea.
def separar_linea(linea):
    return re.findall('[A-Za-zÁ-Úá-ú]+(?:\'[A-Za-zÁ-Úá-ú]+)?',linea)

def distance(str1, str2):
  d=dict()
  for i in range(len(str1)+1):
     d[i]=dict()
     d[i][0]=i
  for i in range(len(str2)+1):
     d[0][i] = i
  for i in range(1, len(str1)+1):
     for j in range(1, len(str2)+1):
        d[i][j] = min(d[i][j-1]+1, d[i-1][j]+1, d[i-1][j-1]+(not str1[i-1] == str2[j-1]))
  return d[len(str1)][len(str2)]


file = open("listado-general.txt")
dictionario_lista= []
for linea in file:
    linea = linea.strip()
    dictionario_lista.append(linea)
file.close()
file = open("texto-prueba.txt")
for linea in file:
    palabras=separar_linea(linea)
    for palabra in palabras :
        clave = palabra.lower()
        i=0
        while (i < len(dictionario_lista) and dictionario_lista[i] != clave):
            i += 1
        
        if i == len(dictionario_lista):
            print( 'La palabra "',clave,'" no estaba en la lista no esta en el Diccionario')
            i=0
            opciones_corregir=[]
            while i < len(dictionario_lista):
                distancia=distance(clave,dictionario_lista[i])
                if distancia<=1:
                    opciones_corregir.append(dictionario_lista[i])
                i += 1
            dic_op_corregir = {(i+1):opciones_corregir[i] for i in range(len(opciones_corregir))}
            print("la palabra se encuentra en la siguiente linea")
            print(linea) 
            print("Es correcta la palabra? Si/No")
            correct=(input()).lower()
            if correct=='no':
                if len(dic_op_corregir)>1:
                    print('Estas son las posibles palabras para corregir')
                    print(dic_op_corregir)
                    op=(input('Ingrese el numero correspondiente a la palabra correcta')).int()
                    palabra=dic_op_corregir.get(op)
                else:
                    if len(dic_op_corregir)==1:
                        print('Se cambiara "',clave,'" por "',dic_op_corregir.get(1),'"' )
                        palabra=dic_op_corregir.get(1)
                    else:
                        print('Por favor ingrese la palabra que realmente es porque no existe en el dicionario')
                        clave=(input()).lower()
                        dictionario_lista.append(clave)
            else:
                dictionario_lista.append(clave)
file.close()
#print(dictionario_lista)