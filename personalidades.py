#Elaborado por: Aarón Ortiz, Alana Calvo
#Fecha de creación: 01/06/2022 09:42
#Fecha de modificación: 01/06/2022 09:42
#version: 3.10.0
#Importaciones
import re
from tkinter import *
from funciones import *
from tkinter import messagebox
from tkinter import ttk
from archivos import *
#variables
personalidades=cargarPersonalidades("personalidades.txt")
paises=cargarPaises("paises.txt")
personasRegis=cargarBd("infoPersonas")
#crearReportPais(personasRegis, personalidades, paises)
for registros in personasRegis:
    print(registros.mostrarTodo())
#df Secciones
class ventanaRegistro:
    def __init__(self, master):
        """
        Funcionamiento: Encargada de cargar objetos de la ventana registrar
        Entrada: master, objeto Tk, ventanta donde se almacenara la pantalla
        Salida: Ventana de registrar participante.
        """
        self.ventana = master
        self.canvasRegistrar = Canvas(self.ventana, width=700, height=750)
        self.canvasRegistrar.pack(fill="both", expand=True)
        self.tituloRegistra = Label(self.canvasRegistrar, text="Inserta un participante", font=("Helvetica", 20, "bold"))
        self.tituloRegistra.place(x=25, y=60)
        #Sección de fecha.
        self.tituloCed = Label(self.canvasRegistrar, text="Cédula:", font=("Helvetica", 16, "bold"))
        self.tituloCed.place(x=40, y=130)
        self.entradaCed = Entry(self.canvasRegistrar, font=("Helvetica", 16))
        self.entradaCed.place(x=350, y=130, height=50, width=300)
        # Nombre completo
        self.tituloNombr = Label(self.canvasRegistrar, text="Nombre Completo:", font=("Helvetica", 16, "bold"))
        self.tituloNombr.place(x=40, y=210)
        self.entradaNombre = Entry(self.canvasRegistrar, font=("Helvetica", 16))
        self.entradaNombre.place(x=350, y=210, height=50, width=300)
        # Genero.
        self.tituloGene = Label(self.canvasRegistrar, text="Genero:", font=("Helvetica", 16, "bold"))
        self.tituloGene.place(x=40, y=270)
        self.opcionMasc = Radiobutton(self.canvasRegistrar, text="Masculino", font=("Helvetica", 14, "bold"), variable=tipoGene,
                                      value=True)
        self.opcionMasc.place(x=350, y=270, height=30, width=250)
        self.opcionFeme = Radiobutton(self.canvasRegistrar, text="Femenino", font=("Helvetica", 14, "bold"), variable=tipoGene, value=False)
        self.opcionFeme.place(x=350, y=300, height=30, width=248)
        # Titulo de Personalidades
        self.tituloPerso = Label(self.canvasRegistrar, text="Personalidad:", font=("Helvetica", 16, "bold"))
        self.tituloPerso.place(x=40, y=360)
        self.menuPerso= ttk.Combobox(self.canvasRegistrar, values=personaLista, state="readonly", font=("Helvetica", 15))
        self.menuPerso.place(x=350, y=360, height=50, width=300)
        # Pais.
        self.tituloPais = Label(self.canvasRegistrar, text="País", font=("Helvetica", 16, "bold"))
        self.tituloPais.place(x=40, y=435)
        self.menuPais = ttk.Combobox(self.canvasRegistrar, values=paises, state="readonly", font=("Helvetica", 15))
        self.menuPais.place(x=350, y=435, height=50, width=300)
        # Estado
        self.tituloEst = Label(self.canvasRegistrar, text="Estado", font=("Helvetica", 16, "bold"))
        self.tituloEst.place(x=40, y=525)
        self.entradaEst = Entry(self.canvasRegistrar, font=("Helvetica", 14, "bold"), state="disabled")
        self.entradaEst.place(x=350, y=525, height=30, width=300)
        # Boton Insertar
        self.botonInsert = Button(self.canvasRegistrar, text="Insertar", font=("Helvetica", 14), fg="white", bg="black", command=self.registrarAux)
        self.botonInsert.place(x=65, y=600, height=50, width=150)
        # Boton limpiar
        self.botonLimpiar = Button(self.canvasRegistrar, text="Limpiar", font=("Helvetica", 14), fg="white", bg="black", command=self.limpiar)
        self.botonLimpiar.place(x=275, y=600, height=50, width=150)
        # boton Regresar.
        self.botonRegresar = Button(self.canvasRegistrar, text="Regresar", font=("Helvetica", 14), fg="white", bg="black", command=self.cambio)
        self.botonRegresar.place(x=485, y=600, height=50, width=150)
    def cambio(self):
        self.canvasRegistrar.pack_forget()
        app=ventanaReportes(self.ventana)
    def registrarAux(self):
        pers=()
        cedula=self.entradaCed.get()
        nombre=self.entradaNombre.get()
        genero=tipoGene.get()
        personalidad=self.menuPerso.get()
        pais=self.menuPais.get()
        if re.match("^[1-9]{1}\-{1}\d{4}\-{1}\d{4}", cedula):
            if re.match("[a-zñA-ZÑ\u00C0-\u017F]", nombre):
                if nombre.istitle():
                    if personalidad!="":
                        personalidad = personalidad.split("-")
                        num=0
                        for llave, info in personalidades.items():
                            if llave==personalidad[0]:
                                pers=(num,)
                                num2=0
                                for sub in info:
                                    if personalidad[1] in sub:
                                        pers+=(num2-1,)
                                        break
                                    num2+=1
                            num+=1
                        if pais !="":
                            pais=paises.index(pais)
                            registrarPersona(cedula, nombre, genero, pers, pais, personasRegis)
                            return
                        messagebox.showerror("Error", "Introduzca un país.")
                        return
                    messagebox.showerror("Error", "Introduzca una personalidad.")
                    return
            messagebox.showerror("Error","Tienes que introducir un nombre valido")
            return
        messagebox.showerror("Error", "Tienes que introducir una cédula valida. ej: 2-0000-0000")
        return
    def limpiar(self):
        """
        Funcionamiento: Vacia el formulario de la sección de registrar.
        Entrada:
        Salida: El formulario vaciado.
        """
        self.entradaCed.delete(0, END)
        self.entradaNombre.delete(0, END)
        self.menuPais.set("")
        self.menuPerso.set("")
        return
    def regresar(self):
        self.ventanaRegiN= Toplevel()
        self.ventanaRegiN.geometry("675x250")
        self.ventanaRegiN.resizable(False, False)
        app=registroDinamico(self.ventanaRegiN)
class registroDinamico:
    def __init__(self, master):
        """
        Funcionamiento: Encargada de cargar objetos de ventana Registrar n cantidad de participantes.
        Entrada: master, objeto Tk, ventanta donde se almacenara la pantalla
        Salida: Ventana Registrar n cantidad de participantes.
        """
        self.ventanaRegistarN=master
        self.tituloInsertN=Label(self.ventanaRegistarN, text="Registro Dinamico.", font=("Helvetica", 20, "bold"))
        self.tituloInsertN.place(y=30, height=40, width=350)
        self.tituloGene = Label(self.ventanaRegistarN, text="Cantidad a generar", font=("Helvetica", 14))
        self.tituloGene.place(y=100, height=30, width=200)
        self.entradaGene = Entry(self.ventanaRegistarN, font=("Helvetica", 15))
        self.entradaGene.place(x=320, y=85, height=40, width=325)
        self.botonInserRn = Button(self.ventanaRegistarN, text="Insertar", bg="black", font=("Helvetica", 12, "bold",),fg="white", command=self.regisDinamicoAux)
        self.botonInserRn.place(x=30, y=160, height=50, width=180)
        self.botonlimpRn = Button(self.ventanaRegistarN, text="Limpiar", bg="black", font=("Helvetica", 12, "bold"), fg="white", command= self.limpiar)
        self.botonlimpRn.place(x=250, y=160, height=50, width=180)
        self.botonRegrRn = Button(self.ventanaRegistarN, text="Regresar", bg="black", font=("Helvetica", 12, "bold"),
                                  fg="white")
        self.botonRegrRn.place(x=470, y=160, height=50, width=180)
    def regisDinamicoAux(self):
        """
        Funcionamiento: Válida los datos de entrada para registrar la cantidad de participantes indicados por el usuario.
        Entrada: num(str): Número indicado por el usuario.
        Salida: Crea la n cantidad de participantes dado.
        """
        num= self.entradaGene.get()
        if re.match("\d", num):
            if int(num)>=10:
                registrarPerDinamico(int(num), personasRegis, personalidades, paises)
                messagebox.showinfo("Hecho", "Se agrego la cantidad de participantes a la base de datos.")
                return
        messagebox.showwarning("Error", "Tienes que introducir la cantidad en números mayores 10")
        return
    def limpiar(self):
        """
        Funcionamiento: Limpia los datos en la entrada.
        Entrada:
        Salida: Entrada limpia.
        """
        self.entradaGene.delete(0, END)
        return
class ventanaReportes:
    def __init__(self, master):
        """
        Funcionamiento: Encargada de cargar ventana de reportes.
        Entrada: master, objeto Tk, ventanta donde se almacenara la pantalla
        Salida: Ventana de Reportes.
        """
        self.ventana = master
        self.canvasReporte= Canvas(self.ventana, width=700, height=750)
        self.canvasReporte.pack(fill="both", expand=True)
        self.tituloReportes= Label(self.canvasReporte,text="Reportes", font=("Helvetica", 30, "bold"))
        self.tituloReportes.place(x=40, y=40)
        self.botonOpcion1= Button(self.canvasReporte, text="Reporte Personalidades.", font=("Helvetica", 16, "bold"), bg="black", fg="white",
                                  command= lambda:crearReportPersonali(personalidades))
        self.botonOpcion1.place(x=40, y=120, height=65, width=620)
        self.botonOpcion2= Button(self.canvasReporte, text="Reporte por Tipo de personalidad.", font=("Helvetica", 16, "bold"),bg="black", fg="white",
                                  command= self.generarVenTipoPers)
        self.botonOpcion2.place(x=40, y=200, height=65, width=620)
        self.botonOpcion3= Button(self.canvasReporte, text="Reporte de Persona.", font=("Helvetica", 16, "bold"), bg="black", fg="white", command=self.generarVenPersona)
        self.botonOpcion3.place(x=40, y=280, height=65, width=620)
        self.botonOpcion4= Button(self.canvasReporte, text="Reporte toda Base de datos.", font=("Helvetica", 16, "bold"), bg="black", fg="white",
                                  command=lambda: crearReportBd(personasRegis, personalidades, paises))
        self.botonOpcion4.place(x=40, y=360, height=65, width=620)
        self.botonOpcion5= Button(self.canvasReporte, text="Reporte personas retiradas", font=("Helvetica", 16, "bold"), bg="black", fg="white",
                                  command= lambda: reporteInactivos(participantes))
        self.botonOpcion5.place(x=40, y=440, height=65, width=620)
        self.botonOpcion6= Button(self.canvasReporte, text="Reporte ordenado por país", font=("Helvetica", 16, "bold"), bg="black", fg="white")
        self.botonOpcion6.place(x=40, y=520, height=65, width=620)
        self.botonregresar= Button(self.canvasReporte, text="Regresar", font=("Helvetica", 16, "bold"), bg="black", fg="white")
        self.botonregresar.place(x=40, y=600, height=65, width=620)
    def generarVenTipoPers(self):
        self.ventanaTipoPers= Toplevel()
        self.ventanaTipoPers.geometry("675x250")
        self.ventanaTipoPers.resizable(False, False)
        app=ventanaTipoPers(self.ventanaTipoPers)
    def generarVenPersona(self):
        self.ventanaPersona=Toplevel()
        self.ventanaPersona.geometry("675x250")
        self.ventanaPersona.resizable(False, False)
        app=ventanaReportPersona(self.ventanaPersona)
class ventanaTipoPers():
    def __init__(self, master):
        self.ventanaTipoPers=master
        self.tituloTipoPers= Label(self.ventanaTipoPers, text="Seleccione tipo de personalidad", font=("Helvetica", 20, "bold"))
        self.tituloTipoPers.place(x=40, y=40)
        self.menuPers= ttk.Combobox(self.ventanaTipoPers, values=personaLista, state="readonly", font=("Helvetica", 15))
        self.menuPers.place(x=180, y=100, height=50, width=326)
        self.botonCrear= Button(self.ventanaTipoPers, text="Crear", font=("Helvetica", 15), bg="black", fg="white", command=self.crearReportTiPersAux)
        self.botonCrear.place(x=65, y=180, height=55, width=150)
        self.botonLimpiar= Button(self.ventanaTipoPers, text="Limpiar", font=("Helvetica", 15), bg="black", fg="white", command= lambda: self.menuPers.set(""))
        self.botonLimpiar.place(x=265, y=180, height=55, width=150)
        self.botonRegresar= Button(self.ventanaTipoPers, text="Regresar", font=("Helvetica", 15), bg="black", fg="white",
                                   command=lambda: self.ventanaTipoPers.destroy())
        self.botonRegresar.place(x=465, y=180, height=55, width=150)
    def crearReportTiPersAux(self):
        tipoPers =self.menuPers.get()
        if tipoPers!="":
            crearReportTipPersonali(tipoPers, personasRegis, personalidades, paises)
            return
        else:
            messagebox.showerror("Error", "Introduzca una personalidad para hacer el reporte.")
            return
class ventanaReportPersona:
    def __init__(self, master):
        self.ventanaReportPersona= master
        self.tituloTipoPers = Label(self.ventanaReportPersona, text="Digite la cédula:", font=("Helvetica", 20, "bold"))
        self.tituloTipoPers.place(x=40, y=40)
        self.entradaCedula= Entry(self.ventanaReportPersona, font=("Helvetica", 15))
        self.entradaCedula.place(x=180, y=100, height=50, width=326)
        self.botonCrear= Button(self.ventanaReportPersona, text="Crear", font=("Helvetica", 15), bg="black", fg="white",command=self.crearReportPersonAux)
        self.botonCrear.place(x=65, y=180, height=55, width=150)
        self.botonLimpiar= Button(self.ventanaReportPersona, text="Limpiar", font=("Helvetica", 15), bg="black", fg="white",
                                  command=lambda: self.entradaCedula.delete(0, END))
        self.botonLimpiar.place(x=265, y=180, height=55, width=150)
        self.botonRegresar= Button(self.ventanaReportPersona, text="Regresar", font=("Helvetica", 15), bg="black", fg="white",
                                   command=lambda: self.ventanaReportPersona.destroy())
        self.botonRegresar.place(x=465, y=180, height=55, width=150)
    def crearReportPersonAux(self):
        cedula=self.entradaCedula.get()
        if re.match("^[1-9]{1}\-{1}\d{4}\-{1}\d{4}", cedula):
            crearReportPersona(cedula, personasRegis, personalidades, paises)
            self.ventanaReportPersona.destroy()
        else:
            messagebox.showerror("Error", "Tienes que introducir una cédula valida. Ej: 2-0000-0000")
#PP
ventana= Tk()
ventana.geometry("700x750")
ventana.title("Personalidades")
ventana.resizable(False, False)
tipoGene=BooleanVar()
personaLista= cargarListaPer(personalidades)
app=ventanaRegistro(ventana)
ventana.mainloop()