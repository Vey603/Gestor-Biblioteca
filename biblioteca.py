from exceptions import UsuarioNoEncontradoError


class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        self.usuarios = []

    def libros_disponibles(self):
        return [libro.titulo for libro in self.libros if libro.disponible]

    def buscar_usuario(self, cedula: int):
        for usuario in self.usuarios:
            if usuario.cedula == cedula:
                return usuario
        raise UsuarioNoEncontradoError(
            f"Error. El usuario con la cédula {cedula} no ha sido encontrado."
        )
