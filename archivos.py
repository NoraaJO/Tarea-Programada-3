#Elaborado por: Aarón Ortiz, Alana Calvo
#Fecha de creación: 01/06/2022 09:42
#Fecha de modificación: 01/06/2022 09:42
#version: 3.10.0
#Importaciones.
import pickle
#df Procesamiento
def cargarPaises(paises):
    """
    Funcionamiento: Carga un archivo con los datos de los paises.
    Entrada: paises(str): Nombre del archivo.
    Salida: Lista con los datos de los paises.
    """
    lista = []
    try:
        archivo=open(paises, "r", encoding="utf-8")
        for pais in archivo.readlines():
            pais=pais.split("(")
            lista.append(pais[0][:-1])
        archivo.close()
    except:
        print("No se encontro el archivo: paises.txt")
    return lista
def cargarPersonalidades():
    dicc={}
    try:
        archivo= open("personalidades.txt", "r", encoding="utf-8")
        primero=True
        lista=[]
        for linea in archivo.readlines():
            if linea[0]=="-" and primero==True:
                llave=linea[1:-1]
                primero=False
            elif linea[0]=="-":
                dicc[llave]=lista
                lista=[]
                llave=linea[1:-1]
            elif linea[0]=="*":
                lista+=[tuple(linea[1:-1].split(":"))]
        archivo.close()
    except:
        print("No se pudo carga la base datos de la personalidades")
    return dicc
def cargarBd(archivoLocal):
    """
    Funcionamiento: Carga los datos almacenados de la información de los trabajadores.
    Entrada:
    archivoLocal: Archivo con los datos de los trabajadores.
    Salida: Datos de los trabajadores.
    """
    lista = []
    try:
        archivo=open(archivoLocal, "rb")
        lista=pickle.load(archivo)
        archivo.close()
    except:
        print("No existe datos previos")
    return lista
def guardar(archivo, baseDatos):
    """
    Funcionamiento: Guarda y sobreescribe los datos que contiene la base datos.
    Entrada:
    archivoLocal: Archivo a realizar la sobrescritura.
    baseDatos(dicc): Base de datos local a guardar.
    Salida: Sobreescribe el archivo con los datos de la base datos.
    """
    try:
        archi=open(archivo, "wb")
        pickle.dump(baseDatos, archi)
        archi.close()
        return
    except:
        print("Error al guardar.")


print(cargarPersonalidades())