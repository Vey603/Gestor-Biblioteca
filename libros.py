from abc import ABC, abstractmethod
from typing import Protocol

from exceptions import LibroNoDisponibleError


class LibroProtocol(Protocol):
    """Define una interfazo o contrato con los métodos prestar"""

    def prestar(self) -> str:
        """Método para prestar la instancia de libro"""
        ...

    def devolver(self) -> str:
        """Método para devolver la instancia de libro"""
        ...

    def calcular_duracion(self) -> str:
        """Calcula la duración de lectura del libro."""
        ...


class LibroBase(ABC):
    @abstractmethod
    def prestar(self) -> str:
        pass

    @abstractmethod
    def devolver(self) -> str:
        pass

    @abstractmethod
    def es_popular(self) -> str:
        pass

    @abstractmethod
    def calcular_duracion(self) -> str:
        """Calcula la duración de lectura del libro."""
        pass


class Libro(LibroBase):
    _PRESTAMOS = "Prestamos.txt"

    def __init__(self, titulo: str, autor: str, isbn: str, disponible: bool = True):
        self.titulo = titulo
        self.autor = autor
        if len(isbn) >= 17:
            self.isbn = isbn
        self.disponible = disponible

    def __str__(self):
        return f"Título: {self.titulo} -- Autor: {self.autor} -- Disponible: {self.disponible}"

    def prestar(self):
        if not self.disponible:
            raise LibroNoDisponibleError(
                f"Error, el libro '{self.titulo}' no está disponible."
            )
        if self.disponible:
            self.disponible = False
            with open(self._PRESTAMOS, "a", encoding="utf-8") as prestamo:
                prestamo.write(self.titulo + "\n")
            return f"El libro '{self.titulo}' ha sido prestado exitosamente. Ya no está disponible."

    def devolver(self):
        self.disponible = True
        return f"El libro {self.titulo} ha sido devuelto exitosamente. Ahora está disponible."

    def es_popular(self):
        counter = 0
        try:
            with open(self._PRESTAMOS, "r", encoding="utf-8") as archivo:
                prestamos = archivo.readlines()
                if prestamos:
                    for prestamo in prestamos:
                        if prestamo.strip() == self.titulo.strip():
                            counter += 1
                    if counter >= 5:
                        return f"¡El libro '{self.titulo}' es popular! Se han realizado {counter} préstamos de este título."
        except FileNotFoundError:
            print(
                "ERROR. No se ha realizado ningún préstamo hasta el momento. Intentalo denuevo más tarde."
            )


class LibroFisico(Libro):
    def __init__(self, titulo, autor, isbn, disponible: bool = True):
        super().__init__(titulo, autor, isbn, disponible)

    def calcular_duracion(self):
        return "7 días"


class LibroElectronico(Libro):
    def __init__(self, titulo, autor, isbn, disponible: bool = True):
        super().__init__(titulo, autor, isbn, disponible)

    def calcular_duracion(self):
        return "14 días"
