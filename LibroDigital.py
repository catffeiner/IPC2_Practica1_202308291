from MaterialBiblioteca import MaterialBiblioteca

class Digital(MaterialBiblioteca):
    def __init__(self, titulo, autor, tamanoarchivo):
        super().__init__(titulo, autor)
        self.tamanoarchivo = tamanoarchivo
        self.dias = 0

    def get_tamanoarchivo(self):
        return self.tamanoarchivo
    
    def set_tamanoarchivo(self, tamanoarchivo):
        self.tamanoarchivo = tamanoarchivo

    def prestarMaterial(self):
        if not self.get_estadoprestamo():
            self.set_estadoprestamo(True)
            self.dias = 0
            print("Libro digital prestado con un máximo de 3 días")
        else:
            print("Ya está prestado")

    def devolverMaterial(self):
        if self.get_estadoprestamo():
            self.set_estadoprestamo(False)
            if self.dias > 3:
                print("No devolvió el libro a tiempo")
            else:
                print("Libro devuelto a tiempo")
        else:
            print("El libro ya estaba disponible")