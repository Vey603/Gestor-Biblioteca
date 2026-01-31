from exceptions import LibroNoDisponibleError, UsuarioNoEncontradoError


class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        self.usuarios = []

    def libros_disponibles(self):
        return [libro for libro in self.libros if libro.disponible]

    def buscar_usuario(self, cedula: int):
        for usuario in self.usuarios:
            if usuario.cedula == cedula:
                return usuario
        raise UsuarioNoEncontradoError(
            f"Error. El usuario con la cédula {cedula} no ha sido encontrado."
        )

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower() and libro.disponible:
                return libro
        raise LibroNoDisponibleError(
            f"Error. El libro con el título '{titulo}' no existe o no se encuentra disponible."
        )
