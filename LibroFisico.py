from MaterialBiblioteca import MaterialBiblioteca

class Fisico(MaterialBiblioteca):
    def __init__(self, titulo, autor, numero_ejemplar):
        super().__init__(titulo, autor)
        self.numero_ejemplar = numero_ejemplar

    # Getters y Setters
    def get_numero_ejemplar(self):
        return self.numero_ejemplar
    
    def set_numero_ejemplar(self, numero_ejemplar):
        self.numero_ejemplar = numero_ejemplar

    # Métodos
    def prestarMaterial(self):
        if not self.get_estadoprestamo():
            self.set_estadoprestamo(True)
            self.dias = 0
            print("Libro físico prestado con un máximo de 7 días")
        else:
            print("Ya está prestado")

    def devolverMaterial(self):
        if self.get_estadoprestamo():
            dias = int(input("Ingrese el número de días que tuvo el libro: "))
            self.set_estadoprestamo(False)
            self.set_dias(dias)
            if dias > 7:
                print("No devolvió el libro a tiempo")
            else:
                print("Libro devuelto a tiempo")
        else:
            print("El libro ya estaba disponible")