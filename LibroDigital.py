from MaterialBiblioteca import MaterialBiblioteca

class Digital(MaterialBiblioteca):
    def __init__(self, titulo, autor, codigounico, estadoprestamo, tamañoarchivo):
        super().__init__(titulo, autor, codigounico, estadoprestamo)
        self.tamañoarchivo = tamañoarchivo
        self.dias = 0

    #Getters y Setters

    def get_tamañoarchivo(self):
        return self.tamañoarchivo
    
    def set_tamañoarchivo(self, tamañoarchivo):
        self.tamañoarchivo = tamañoarchivo

    # Métodos
    def prestado(self):
        if self.estadoprestamo == "Disponible":
            self.estadoprestamo = "Prestado"
            self.dias = 0
            return "Libro prestado con un máximo de 3 días"
        else:
            return "Ya está prestado"
        
    def devuelto(self):
        if self.estadoprestamo == "Prestado":
            self.estadoprestamo = "Disponible"
            if self.dias > 3:
                return "No devolvio el libro a tiempo"
            else:
                return "Libro devuelto a tiempo"