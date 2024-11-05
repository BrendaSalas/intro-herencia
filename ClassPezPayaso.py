from ClassPeces import Peces

class PezPayaso(Peces):
    def __init__(self, nombre, color, size, habitad, esconderse):
        super().__init__(nombre, color, size, habitad)
        self.__esconderse = esconderse

    def descripcion(self):
        super().descripcion()
        print(f"Este pez se esconde?{self.__esconderse}")

    def getColor(self):
        return self.color
