import os
import re
import string
#"/home/hernan/Documentos/Trabajos_Independientes/BaiancaLucca/Corrector-Ortografico/listado-general.txt"
#"/home/hernan/Documentos/Trabajos_Independientes/BaiancaLucca/Corrector-Ortografico/texto-prueba.txt"
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

def lectura_path():
    print('Ingrese la direccion absoluta del diccionario\n')
    dir_dic=input()
    print('Ingrese la direccion absoluta del archivo a corregir\n')
    dir_text=input()
    dic=os.path.isfile(dir_dic)
    text=os.path.isfile(dir_text)
    while((not dic) and (not text)):
        if((dic==False) and (text==False)):
            print('ninguna de las rutas es correcta')
            print('vuelva a ingresar la ruta del dicionario \n')
            dir_dic=input()
            print('vuelva a ingresar la ruta del texto a corregir \n')
            dir_text=input()
            dic=os.path.isfile(dir_dic)
            text=os.path.isfile(dir_text)
        else:
            if((dic==True) and (text==False)):
                print('la ruta de diccionario es correcta pero la del texto no')
                print('vuelva a ingresar la ruta del texto a corregir \n')
                dir_text=input()
                text=os.path.isfile(dir_text)
            else:
                print('la ruta de diccionario es no correcta pero la del texto si')
                print('vuelva a ingresar la ruta del dicionario \n')
                dir_dic=input()
                dic=os.path.isfile(dir_dic)
    return(dir_dic,dir_text)


archivos=(lectura_path())
file = open(archivos[0])
dictionario_lista= []
for linea in file:
    pal = linea.strip()
    dictionario_lista.append(pal.lower())
file.close()
file = open(archivos[1])
salida = open("correcion.txt","w")
for linea in file:
    palabras=separar_linea(linea)
    for j in range(len(palabras)):
        clave = palabras[j].lower()
        i=0
        while (i < len(dictionario_lista) and dictionario_lista[i] != clave):
            i += 1
        
        if i == len(dictionario_lista):
            print( 'La palabra "',clave,'" no estaba en la lista no esta en el Diccionario')
            print("la palabra se encuentra en la siguiente horacion")
            print(palabras[j-2]+" "+palabras[j-1]+" "+palabras[j].upper()+" "+palabras[j+1]+" "+palabras[j+2]) 
            print("Es correcta la palabra? Si/No")
            correct=(input()).lower()
            if correct=='no':
                i=0
                opciones_corregir=[]
                while i < len(dictionario_lista):
                    distancia=distance(clave,dictionario_lista[i])
                    if distancia<=1:
                        opciones_corregir.append(dictionario_lista[i])
                    i += 1
                dic_op_corregir = {(i+1):opciones_corregir[i] for i in range(len(opciones_corregir))}
                if (len(dic_op_corregir)>1):
                    print('Estas son las posibles palabras para corregir')
                    print(dic_op_corregir)
                    op=int(input('Ingrese el numero correspondiente a la palabra correcta\n'))
                    palabras[j]=dic_op_corregir.get(op)
                else:
                    if len(dic_op_corregir)==1:
                        print('Se cambiara "',clave,'" por "',dic_op_corregir.get(1),'"' )
                        palabras[j]=dic_op_corregir.get(1)
                    else:
                        print('Por favor ingrese la palabra que realmente es porque no existe en el dicionario')
                        palabras[j]=(input()).lower()
                        dictionario_lista.append(clave)
            else:
                dictionario_lista.append(clave)
        j=j+1
    linea_salida=" ".join(palabras)
    salida.seek(salida.tell())
    salida.write(linea_salida)
    salida.write('\n')
file.close()
salida.close()
