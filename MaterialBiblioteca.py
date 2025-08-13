class MaterialBiblioteca:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        self.__codigounico = format(id(titulo + autor), 'x')
        self.__estadoprestamo = False


    # Getters y Setters
    def get_titulo(self):
        return self.__titulo
    
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_autor(self):
        return self.__autor
    
    def set_autor(self, autor):
        self.__autor = autor

    def get_codigounico(self):
        return self.__codigounico

    def get_estadoprestamo(self):
        return self.__estadoprestamo
    
    def set_estadoprestamo(self, estadoprestamo):
        self.__estadoprestamo = estadoprestamo


    # Métodos
    def prestarMaterial(self):
        if self.__estadoprestamo:
            print("Material ya está prestado")
        else:
            self.__estadoprestamo = True
            print(f"Material '{self.__titulo}' prestado con éxito")
        
    def devolverMaterial(self):
        if not self.__estadoprestamo:
            print("Material ya está disponible")
        else:
            self.__estadoprestamo = False
            print(f"Material '{self.__titulo}' devuelto con éxito")
            
    def mostrarInformacion(self):
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.__autor}")
        print(f"Código Único: {self.__codigounico}")
        print(f"Estado de Préstamo: {'Prestado' if self.__estadoprestamo else 'Disponible'}")