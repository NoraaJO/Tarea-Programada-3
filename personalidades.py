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
pais=cargarPaises("paises.txt")
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
        self.menuPerso= ttk.Combobox(self.canvasRegistrar, values=["1"], state="readonly", font=("Helvetica", 15))
        self.menuPerso.place(x=350, y=360, height=50, width=300)
        # Pais.
        self.tituloPais = Label(self.canvasRegistrar, text="País", font=("Helvetica", 16, "bold"))
        self.tituloPais.place(x=40, y=435)
        self.menuPais = ttk.Combobox(self.canvasRegistrar, values=pais, state="readonly", font=("Helvetica", 15))
        self.menuPais.place(x=350, y=435, height=50, width=300)
        # Estado
        self.tituloEst = Label(self.canvasRegistrar, text="Estado", font=("Helvetica", 16, "bold"))
        self.tituloEst.place(x=40, y=525)
        self.entradaEst = Entry(self.canvasRegistrar, font=("Helvetica", 14, "bold"), state="disabled")
        self.entradaEst.place(x=350, y=525, height=30, width=300)
        # Boton Insertar
        self.botonInsert = Button(self.canvasRegistrar, text="Insertar", font=("Helvetica", 14), fg="white", bg="black")
        self.botonInsert.place(x=65, y=600, height=50, width=150)
        # Boton limpiar
        self.botonLimpiar = Button(self.canvasRegistrar, text="Limpiar", font=("Helvetica", 14), fg="white", bg="black")
        self.botonLimpiar.place(x=275, y=600, height=50, width=150)
        # boton Regresar.
        self.botonRegresar = Button(self.canvasRegistrar, text="Regresar", font=("Helvetica", 14), fg="white", bg="black")
        self.botonRegresar.place(x=485, y=600, height=50, width=150)
#PP
ventana= Tk()
ventana.geometry("700x750")
ventana.title("Personalidades")
ventana.resizable(False, False)
tipoGene=BooleanVar()
app=ventanaRegistro(ventana)
ventana.mainloop()