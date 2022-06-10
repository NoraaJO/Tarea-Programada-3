# Elaborado por: Aarón Ortiz, Alana Calvo
# Fecha de creación: 01/06/2022 09:42
# Fecha de modificación: 01/06/2022 09:42
# version: 3.10.0
# Importaciones
from archivos import *
from datetime import datetime
from tkinter import messagebox
from clases import *
from random import *
import xml.etree.ElementTree as xml
import webbrowser
# df Procesamiento.
def cargarListaPer(personalidades):
    """
    Funcionamiento: Carga la lista con los datos del diccionario de personalidades para dar el menu personalidades.
    Entrada: personalidades(dicc): Diccionario con los datos de personalidades.
    Salida: lista(list): Lista con los datos de personalidades.
    """
    lista = []
    try:
        for principal, secundario in personalidades.items():
            for sub in secundario:
                if type(sub) == tuple:
                    lista.append(f"{principal}-{sub[0]}")
    except:
        messagebox.showerror("Error", "No se cargo la lista personalidades.")
    return lista
def registrarPersona(cedula, nombre, genero, personalidad, pais, personasRegis):
    """
    Funcionamiento: Registra la persona con los datos dados por el usuario.
    Entrada:
    cedula(str): Cédula de la persona a registrar.
    nombre(str): Nombre de la persona a registrar.
    genero(bool): True: Masculino/False: Femenino.
    personalidad(tuple): Personalidad de la persona a registrar.
    pais(int): País de pertenencia de la persona a registrar.
    personaRegis(list): Base de datos de las personas registradas.
    Salida: Persona registrada en la base datos.
    """
    try:
        for registros in personasRegis:
            if cedula == registros.mostrarCedula():
                messagebox.showwarning("Cédula ya régistrada", "La cédula ya esta registrada con otro usuario.")
                return
        regisPerso = persona()
        regisPerso.definirCedula(cedula)
        regisPerso.definirNombre(nombre)
        regisPerso.definirGenero(genero)
        regisPerso.definirPersonalidad(personalidad)
        regisPerso.definirPais(pais)
        regisPerso.definirEstado([True, "", datetime.today().strftime("%d/%m/%Y")])
        personasRegis.append(regisPerso)
        guardar("infoPersonas", personasRegis)
        messagebox.showinfo("Hecho", "Se ha registrado a la persona en el sistema.")
    except:
        messagebox.showerror("Error", "No se pudo registrar a la persona en el sistema")
    return
def registrarPerDinamico(num, personasRegis, personalidades, paises):
    """
    Funcionamiento: Registra de manera dinamica la cantidad de personas indicadas por el usuario.
    Entrada:
    num(int): Cantidad de participantes a registrar.
    personasRegis(list): Base de datos con la información de las personas registradas.
    personalidades(dicc): Base datos con la información de las personalidades.
    paises(list): Lista con los países.
    Salida: Registro de las personas indicadas.
    """
    apellidos = ["Gonzalez", "Gomez", "Diaz", "Rodriguez", "López", "Perez", "Martinez", "Silva", "Romero", "Cruz",
                 "Fernández", "Ruiz", "Sanchez",
                 "Martinez", "Florez", "Chavez", "Garcia", "Jara", "Valverde", "Morales", "Castro", "Gutierrez",
                 "Cortes", "Campos", "Guzman", "Peña",
                 "Ortega", "Venegas", "Mendoza", "Reyes", "Castillo", "Jimenez"]
    nombres = ["Juan", "Jose", "Antonio", "Pedro", "Jesús", "Alejandro", "Margarita", "Manuel", "Roberto", "Francisco",
               "Walter", "Ernesto", "Fernando",
               "Roberto", "Daniel", "Carlos", "Ricardo", "Alberto", "Eduardo", "Manuel", "Daniela", "Angel", "María",
               "Guadalupe", "Juana", "Luis", "Raquel",
               "Pilar", "Ana", "Carmen", "Isabel", "Silvia", "Rosa", "Monica", "Paula", "Sara"]
    genero = True
    for n in range(num):
        regisPersona = persona()
        cedula = str(randint(1, 9)) + "-" + str(randint(1000, 9999)) + "-" + str(randint(1000, 9999))
        for registro in personasRegis:
            cedula == registro.mostrarCedula()
            cedula = str(randint(1, 9)) + "-" + str(randint(1000, 9999)) + "-" + str(randint(1000, 9999))
            break
        regisPersona.definirCedula(cedula)
        regisPersona.definirNombre(choice(nombres) + " " + choice(apellidos) + " " + choice(apellidos))
        if genero == True:
            regisPersona.definirGenero(True)
            genero = False
        else:
            regisPersona.definirGenero(False)
            genero = True
        num = randint(0, len(personalidades) - 1)
        seleccion = 0
        for llave, sub in personalidades.items():
            if seleccion == num:
                regisPersona.definirPersonalidad((num, randint(0, len(sub) - 2)))
                break
            seleccion += 1
        regisPersona.definirPais(randint(0, len(paises) - 1))
        regisPersona.definirEstado([True, "", datetime.today().strftime("%d/%m/%Y")])
        personasRegis.append(regisPersona)
    guardar("infoPersonas", personasRegis)
    return
def creaXmlPersonali(personalidades):
    """
    Funcionamiento: Crea un archivo xml de los datos del diccionario de personalidades.
    Entrada:
    personalidades(dicc): Base datos con la información de las personalidades.
    Salida: Persona registrada en la base datos.
    """
    principal = xml.Element("Personalidades")
    for tipo, secundario in personalidades.items():
        personalidad = xml.SubElement(principal, "personalidad", tipo=tipo)
        num = 1
        for subelementos in secundario:
            if type(subelementos) == str:
                informacion = xml.SubElement(personalidad, "descripcion").text = subelementos
            else:
                subtipo = xml.SubElement(personalidad, f"subtipo{num}").text = subelementos[0]
                codigo = xml.SubElement(personalidad, f"codigo{num}").text = subelementos[1]
                num += 1
    archivo = xml.ElementTree(principal)
    archivo.write("personalidades.xml", encoding="utf-8")
    messagebox.showinfo("Archivo creado", "Se creo el archivo.")
    return
# Sección de reportes.
def crearReportPersonali(personalidades):
    """
    Funcionamiento: Crea un reporte en un archivo html con los datos de los tipos de personalidades en la base de datos.
    Entrada:
    personalidades(dicc): Base datos con la información de las personalidades.
    Salida: Archivo html reporte Personalidades generado.
    """
    archivo = open(f"""personalidades-{datetime.today().strftime("%d-%m-%Y-%H-%M-%S")}.html""", "w", encoding="utf-8")
    contenido = """
        <html>
        <head>
        <link rel="stylesheet" href="estilos/estilosPs.css"> 
            <h1>Reporte Personalidades.</h1>
            
        </head>
        <body> 
            <table>
    """
    for llave, info in personalidades.items():
        contenido += f"""<tr> <td>{llave}</td>
        """
        for subelementos in info:
            if type(subelementos) == tuple:
                contenido += f"""<td>{subelementos[0]}</td>"""
        contenido += """</tr>"""
    contenido += """</table>
        </body>
        </html>"""
    archivo.write(contenido)
    archivo.close()
    messagebox.showinfo("Archivo creado", "Se ha creado el reporte.")
    return
def crearReportTipPersonali(tipoPers, personasRegis, personalidades, paises):
    """
    Funcionamiento: Crea un reporte en un archivo html de los datos de personas registradas con la personalidad indicada.
    Entrada:
    tipoPers(str): Personalidad indicada a buscar.
    personasRegis(list): Base de datos con la información de las personas registradas.
    personalidades(dicc): Base datos con la información de las personalidades.
    paises(list): Lista con los países.
    Salida: Archivo html reporte Personalidades generado.
    """
    archivo = open(f"""tipos-{datetime.today().strftime("%d-%m-%Y-%H-%M-%S")}.html""", "w", encoding="utf-8")
    contenido = f"""
        <html>
        <head>
        <link rel="stylesheet" href="estilos/estilos.css"> 
            <h1>Reporte Tipo: {tipoPers}.</h1>
        </head>
        <body> 
            <table>
                <thead>
                    <td>Cédula</td>
                    <td>Nombre</td>
                    <td>Género</td>
                    <td>Subtipo personalidad</td>
                    <td>País</td>
                </thead>
    """
    tipoPers = tipoPers.split("-")
    num = 0
    for llave, info in personalidades.items():
        if llave == tipoPers[0]:
            pers = (num,)
            num2 = 0
            for sub in info:
                if tipoPers[1] in sub:
                    pers += (num2 - 1,)
                    break
                num2 += 1
        num+=1
    for persona in personasRegis:
        if persona.mostrarPersonalidad() == pers and persona.mostrarEstado()[0] == True:
            if persona.mostrarGenero() == True:
                genero = "Masculino"
            else:
                genero = "Femenino"
            contenido += f"""
                <tr>
                    <td>{persona.mostrarCedula()}</td>
                    <td>{persona.mostrarNombre()}</td>
                    <td>{genero}</td>
                    <td>{tipoPers[1]}</td>
                    <td>{paises[persona.mostrarPais()]}</td>
                </tr>
            """
    contenido += """</table>
            </body>
            </html>"""
    archivo.write(contenido)
    archivo.close()
    messagebox.showinfo("Archivo creado", "Se ha creado el reporte.")
    return
def crearReportPersona(cedula, personasRegis, personalidades, paises):
    """
    Funcionamiento: Crea un reporte en un archivo html de los datos perteneciente a la cédula de la persona indicada.
    Entrada:
    cedula(str): Cédula de la persona a buscar.
    personasRegis(list): Base de datos con la información de las personas registradas.
    personalidades(dicc): Base datos con la información de las personalidades.
    paises(list): Lista con los países.
    Salida: Archivo html reporte de la persona indicada generado.
    """
    for persona in personasRegis:
        if persona.mostrarCedula()==cedula:
            archivo=open(f"""persona-{datetime.today().strftime("%d-%m-%Y-%H-%M-%S")}.html""", "w", encoding="utf-8")
            contenido=f"""
                <html>
                <head>
                <link rel="stylesheet" href="estilos/estilos.css"> 
                    <h1>Reporte Persona Cédula: {cedula}.</h1>
                </head>
                <body> 
                    <table>
                        <thead>
                            <td>Cédula</td>
                            <td>Nombre</td>
                            <td>Género</td>
                            <td>Subtipo personalidad</td>
                            <td>País</td>
                            <td>Estado</td>
                        </thead>
                """
            num=0
            for tipo, info in personalidades.items():
                if num==persona.mostrarPersonalidad()[0]:
                    num=0
                    for subelemento in info:
                        if num==persona.mostrarPersonalidad()[1]+1:
                            carac = subelemento
                            break
                        num+=1
                num+=1
            if persona.mostrarGenero()==True:
                genero="Masculino"
            else:
                genero="Femenino"
            contenido+= f"""
                <tr>
                    <td>{persona.mostrarCedula()}</td>
                    <td>{persona.mostrarNombre()}</td>
                    <td>{genero}</td>
                    <td>{carac}</td>
                    <td>{paises[persona.mostrarPais()]}</td>
                    <td>{persona.mostrarEstado()}</td>
                </tr>
                </table>
                </body>
                </html>
                """
            archivo.write(contenido)
            archivo.close()
            messagebox.showinfo("Archivo creado", "Se ha generado el reporte")
            return
    messagebox.showwarning("No se encontró", "No hay una  persona registrada con esa cédula.")
    return
def crearReportBd(personasRegis, personalidades, paises):
    """
    Funcionamiento: Crea un reporte en un archivo html de los datos almacenados en la base de datos.
    Entrada:
    personasRegis(list): Base de datos con la información de las personas registradas.
    personalidades(dicc): Base datos con la información de las personalidades.
    paises(list): Lista con los países.
    Salida: Archivo html reporte del contenido de la base de datos.
    """
    archivo = open(f"""bd-{datetime.today().strftime("%d-%m-%Y-%H-%M-%S")}.html""", "w", encoding="utf-8")
    contenido = f"""
        <html>
        <head>
        <link rel="stylesheet" href="estilos/estilosBd.css"> 
            <h1>Reporte Base de datos.</h1>
        </head>
        <body> 
            <table>
                <thead>
                    <td>Cédula</td>
                    <td>Nombre</td>
                    <td>Género</td>
                    <td>Subtipo personalidad</td>
                    <td>País</td>
                    <td>Estado</td>
                </thead>
        """
    for persona in personasRegis:
        num = 0
        for tipo, info in personalidades.items():
            if num == persona.mostrarPersonalidad()[0]:
                num = 0
                for subelemento in info:
                    if num == persona.mostrarPersonalidad()[1] + 1:
                        carac = subelemento
                        break
                    num += 1
            num += 1
        if persona.mostrarGenero() == True:
            genero = "Masculino"
        else:
            genero = "Femenino"
        contenido += f"""
            <tr>
                <td>{persona.mostrarCedula()}</td>
                <td>{persona.mostrarNombre()}</td>
                <td>{genero}</td>
                <td>{carac}</td>
                <td>{paises[persona.mostrarPais()]}</td>
                <td>{persona.mostrarEstado()}</td>
            </tr>
            """
    contenido += """</table>
        </body>
        </html>
        """
    archivo.write(contenido)
    archivo.close()
    messagebox.showinfo("Archivo creado", "Se genero el reporte.")
    return
def crearReportInac(personasRegis, personalidades, paises):
    """
    Funcionamiento: Crea un reporte en un archivo html de los datos personas registradas que se encuentran inactivas.
    Entrada:
    personasRegis(list): Base de datos con la información de las personas registradas.
    personalidades(dicc): Base datos con la información de las personalidades.
    paises(list): Lista con los países.
    Salida: Archivo html reporte de las personas inactivas generado.
    """
    archivo = open(f"""retirados-{datetime.today().strftime("%d-%m-%Y-%H-%M-%S")}.html""", "w", encoding="utf-8")
    contenido = f"""
           <html>
           <head>
           <link rel="stylesheet" href="estilos/estilos.css"> 
               <h1>Reporte Retirados.</h1>
           </head>
           <body> 
               <table>
                   <thead>
                       <td>Cédula</td>
                       <td>Nombre</td>
                       <td>Género</td>
                       <td>Subtipo personalidad</td>
                       <td>País</td>
                       <td>Estado</td>
                   </thead>
           """
    for persona in personasRegis:
        if persona.mostrarEstado()[0]==False:
            num = 0
            for tipo, info in personalidades.items():
                if num == persona.mostrarPersonalidad()[0]:
                    num = 0
                    for subelemento in info:
                        if num == persona.mostrarPersonalidad()[1] + 1:
                            carac = subelemento
                            break
                        num += 1
                num += 1
            if persona.mostrarGenero() == True:
                genero = "Masculino"
            else:
                genero = "Femenino"
            contenido += f"""
                <tr>
                    <td>{persona.mostrarCedula()}</td>
                    <td>{persona.mostrarNombre()}</td>
                    <td>{genero}</td>
                    <td>{carac}</td>
                    <td>{paises[persona.mostrarPais()]}</td>
                    <td>{persona.mostrarEstado()[1]}</td>
                </tr>
                """
    contenido += """</table>
        </body>
        </html>
        """
    archivo.write(contenido)
    archivo.close()
    messagebox.showinfo("Archivo creado", "Se genero el reporte.")
    return
def crearReportPais(personasRegis, personalidades, paises):
    """
    Funcionamiento: Crea un reporte en un archivo html de los datos de las personas ordenadas por el país de procedencia.
    Entrada:
    personasRegis(list): Base de datos con la información de las personas registradas.
    personalidades(dicc): Base datos con la información de las personalidades.
    paises(list): Lista con los países.
    Salida: Archivo html reporte de las personas ordenada por el país generado.
    """
    archivo= open(f"""pais-{datetime.today().strftime("%d-%m-%Y-%H-%M-%S")}.html""", "w", encoding="utf-8")
    contenido = f"""
        <html>
        <head>
        <link rel="stylesheet" href="estilos/estilos.css"> 
            <h1>Reporte País.</h1>
        </head>
        <body> 
            <table>
                <thead>
                    <td>Cédula</td>
                    <td>Nombre</td>
                    <td>Género</td>
                    <td>Subtipo personalidad</td>
                    <td>País</td>
                    <td>Estado</td>
                </thead>
        """
    for pais in paises:
        for persona in personasRegis:
            if pais==paises[persona.mostrarPais()]:
                num = 0
                for tipo, info in personalidades.items():
                    if num == persona.mostrarPersonalidad()[0]:
                        num = 0
                        for subelemento in info:
                            if num == persona.mostrarPersonalidad()[1] + 1:
                                carac = subelemento
                                break
                            num += 1
                    num += 1
                if persona.mostrarGenero() == True:
                    genero = "Masculino"
                else:
                    genero = "Femenino"
                contenido += f"""
                    <tr>
                        <td>{persona.mostrarCedula()}</td>
                        <td>{persona.mostrarNombre()}</td>
                        <td>{genero}</td>
                        <td>{carac}</td>
                        <td>{pais}</td>
                    """
                if persona.mostrarEstado()[0]==True:
                    contenido+=f"""
                        <td>Activo</td>
                    </tr>
                    """
                else:
                    contenido+=f"""
                        <td>Inactivo</td>
                    </tr>
                    """
    contenido += """</table>
            </body>
            </html>
            """
    archivo.write(contenido)
    archivo.close()
    messagebox.showinfo("Archivo creado", "Se genero el reporte.")
    return