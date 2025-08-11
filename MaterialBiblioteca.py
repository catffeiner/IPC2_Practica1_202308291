class MaterialBiblioteca:
    def __init__(self, titulo, autor, codigounico, estadoprestamo):
        self.titulo = titulo
        self.autor = autor
        self.codigounico = codigounico
        self.estadoprestamo = estadoprestamo

        #Getters y Setters

        def get_titulo(self):
            return self.titulo
        
        def set_titulo(self, titulo):
            self.titulo = titulo

        def get_autor(self):
            return self.autor
        
        def set_autor(self, autor):
            self.autor = autor

        def get_codigounico(self):
            return self.codigounico
        
        def set_codigounico(self, codigounico):
            self.codigounico = codigounico

        def get_estadoprestamo(self):
            return self.estadoprestamo
        
        def set_estadoprestamo(self, estadoprestamo):
            self.estadoprestamo = estadoprestamo

        #Metodos

        def prestarMaterial(self):
            if self.estadoprestamo == "Disponible":
                self.estadoprestamo = "Prestado"
                return "Material prestado con éxito"
            else:
                return "Material ya prestado"
            
        def devolverMaterial(self):
            if self.estadoprestamo == "Prestado":
                self.estadoprestamo = "Disponible"
                return "Material devuelto con éxito"
            else:
                return "Material ya disponible"
        
        def mostrarInformacion(self):
            return f"Título: {self.titulo}, Autor: {self.autor}, Código Único: {self.codigounico}, Estado de Préstamo: {self.estadoprestamo}"