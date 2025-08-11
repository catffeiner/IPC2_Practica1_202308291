from MaterialBiblioteca import MaterialBiblioteca

class Fisico(MaterialBiblioteca):
    def __init__(self, titulo, autor, codigounico, estadoprestamo, numero_ejemplar):
        super().__init__(titulo, autor, codigounico, estadoprestamo)
        self.numero_ejemplar = numero_ejemplar
        self.dias = 0

    #Getters y Setters
    def get_numero_ejemplar(self):
        return self.numero_ejemplar
    
    def set_numero_ejemplar(self, numero_ejemplar):
        self.numero_ejemplar = numero_ejemplar

    # Métodos
    def prestado(self):
        if not self.estadoprestamo:
            self.estadoprestamo = True
            self.dias = 0;
            return "Libro prestado con un máximo de 7 días"
        else:
            return "Ya está prestado"
        
    def devuelto(self):
        if self.estadoprestamo:
            self.estadoprestamo = False
            if self.dias > 7:
                return "No devolvio el libro a tiempo"
            else:
                return "Libro devuelto a tiempo"