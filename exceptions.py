class BibliotecaError(Exception):
    pass


class LimiteDePrestamosError(BibliotecaError):
    pass


class TituloInvalidoError(BibliotecaError):
    pass


class LibroNoDisponibleError(BibliotecaError):
    pass


class UsuarioNoEncontradoError(BibliotecaError):
    pass
