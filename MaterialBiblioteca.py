from abc import ABC, abstractmethod

class MaterialBiblioteca(ABC):
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        self.__codigounico = format(id(titulo + autor), 'x')
        self.__estadoprestamo = False
        self.__dias = 0


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

    def get_dias(self):
        return self.__dias
    
    def set_dias(self, dias):
        self.__dias = dias

    # Métodos
    @abstractmethod
    def prestarMaterial(self):
        pass

    @abstractmethod   
    def devolverMaterial(self):
        pass
            
    def mostrarInformacion(self):
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.__autor}")
        print(f"Código Único: {self.__codigounico}")
        print(f"Estado de Préstamo: {'Prestado' if self.__estadoprestamo else 'Disponible'}")