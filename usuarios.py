from abc import ABC, abstractmethod
from typing import Protocol

from exceptions import TituloInvalidoError


class SolicitanteProtocol(Protocol):
    def solicitar_libro(self, titulo: str) -> str:
        """Método que debe implementar cualquier solicitante"""
        ...


class UsuarioBase(ABC):
    @abstractmethod
    def solicitar_libro(self):
        pass


class Usuario:
    def __init__(self, nombre, cedula: int):
        self.nombre = nombre
        self.cedula = cedula
        self.libros_prestados: list = []

    def solicitar_libro(self, titulo):
        return f"Solicitud de libro {titulo} realizada."

    def devolver_libro(self, titulo):
        if titulo in self.libros_prestados:
            self.libros_prestados.remove(titulo)
            return f"Has regresado el libro '{titulo}'. Muchas gracias."
        return f"Error. No has realizado un préstamo del título '{titulo}'"


class Estudiante(Usuario):
    def __init__(self, nombre, cedula, carrera):
        super().__init__(nombre, cedula)
        self.carrera = carrera
        self.limite_libros = 3

    def solicitar_libro(self, titulo):
        if not titulo:
            raise TituloInvalidoError(f"El título {titulo} no existe.")
        if len(self.libros_prestados) < self.limite_libros:
            self.libros_prestados.append(titulo)
            return f"Prestamo del libro '{titulo}' realizado."
        else:
            return f"Error, no se pudo completar el préstamo. Límite de libros alcanzado: {self.limite_libros}"


class Profesor(Usuario):
    def __init__(self, nombre, cedula):
        super().__init__(nombre, cedula)
        self.limite_libros = None

    def solicitar_libro(self, titulo):
        self.libros_prestados.append(titulo)
        return f"Prestamo del libro '{titulo}' realizado."
