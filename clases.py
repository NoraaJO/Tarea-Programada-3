#Elaborado por: Aarón Ortiz, Alana Calvo
#Fecha de creación: 01/06/2022 09:42
#Fecha de modificación: 01/06/2022 12:14
#version: 3.10.0
class persona:
    def __init__(self):
        """
        Funcionamiento: Datos de la persona.
        Entrada:
        Salida: Estructura de la persona.
        """
        self.cedula = ""
        self.nombre = ""
        self.genero = True
        self.personalidad = ()
        self.pais = 0
        self.estado = []
    def definirCedula(self, pcedula):
        """
        Funcionamiento: Define o cambia el dato de cédula de la persona.
        Entrada: pcedula(str): Cédula de la persona.
        Salida: Cédula cambiada.
        """
        self.cedula=pcedula
        return
    def definirNombre(self, pnombre):
        """
        Funcionamiento: Define o cambia el dato de nombre de la persona.
        Entrada: pnombre(str): Dato nombre de la persona.
        Salida: Nombre cambiado.
        """
        self.nombre=pnombre
        return
    def definirGenero(self, pgenero):
        """
        Funcionamiento: Define o cambia el dato del género de la persona.
        Entrada: pgenero(bool): Dato género de la persona.
        Salida: Genero cambiado.
        """
        self.genero=pgenero
        return
    def definirPersonalidad(self, ppersonalidad):
        """
        Funcionamiento: Define o cambia los datos de personalidad de la persona.
        Entrada: ppersonalidad(tuple): Dato personalidad de la persona.
        Salida: Personalidad cambiada.
        """
        self.personalidad = ppersonalidad
        return
    def definirPais(self, ppais):
        """
        Funcionamiento: Define o cambia los datos del país de la persona.
        Entrada: ppais(tuple): Dato país de la persona.
        Salida: País cambiada.
        """
        self.pais= ppais
        return
    def definirEstado(self, pestado):
        """
        Funcionamiento: Define o cambia los datos de estado de la persona.
        Entrada: ppestado(tuple): Datos estado de la persona.
        Salida: Estado cambiado.
        """
        self.estado = pestado
        return
    def mostrarCedula(self):
        """
        Funcionamiento: Consigue el dato de la cédula.
        Entrada:
        Salida: Cédula de la persona.
        """
        return self.cedula
    def mostrarNombre(self):
        """
        Funcionamiento: Consigue el dato del nombre.
        Entrada:
        Salida: Nombre de la persona.
        """
        return self.nombre
    def mostrarGenero(self):
        """
        Funcionamiento: Consigue el dato del género.
        Entrada:
        Salida: Género de la persona.
        """
        return self.genero
    def mostrarPersonalidad(self):
        """
        Funcionamiento: Consigue el dato de la personalidad.
        Entrada:
        Salida: Personalidad de la persona.
        """
        return self.personalidad
    def mostrarPais(self):
        """
        Funcionamiento: Consigue el dato del país.
        Entrada:
        Salida: País de la persona.
        """
        return self.pais
    def mostrarEstado(self):
        """
        Funcionamiento: Consigue el dato del estado.
        Entrada:
        Salida: Estado de la persona.
        """
        return self.estado
    def mostrarTodo(self):
        """
        Funcionamiento: Consigue todos los datos.
        Entrada:
        Salida: Todos los datos de la persona.
        """
        return self.cedula, self.nombre, self.genero, self.personalidad, self.pais, self.estado











