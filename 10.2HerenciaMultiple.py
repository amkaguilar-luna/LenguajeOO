class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Contacto:

    def __init__(self, correo, telefono):
        self.correo = correo
        self.telefono = telefono


class Alumno(Persona, Contacto):

    def __init__(self, nombre, edad, correo, telefono, matricula):
        Persona.__init__(self, nombre, edad)
        Contacto.__init__(self, correo, telefono)
        self.matricula = matricula

    def __str__(self):
        return 

# Programa principal
