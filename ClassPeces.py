class Peces:
    def __init__(self, nombre, color, size, habitad):
        self.__nombre = nombre
        self.color = color
        self.__size = size
        self.__habitad = habitad

    '''def mostrar_informacion(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Color: {self.__color}")
        print(f"Tipo de agua: {self.tipo_agua}")'''
    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def nadar(self):
        print(f"{self.__nombre} esta nadando")

    def descripcion(self):
        print(f"El pez se llama {self.__nombre}  y es color {self.color} y vive en  {self.__habitad}")
