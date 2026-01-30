from biblioteca import Biblioteca
from exceptions import BibliotecaError
from libros import LibroFisico
from usuarios import Estudiante, Profesor, SolicitanteProtocol

biblioteca = Biblioteca("Platzi")

estudiante = Estudiante("Bayron", 1114209584, "Sistemas")
estudiante_uno = Estudiante("Juan", 11159834682, "Diseño")
profesor = Profesor("Jhon", 1112204554)
usuarios: list[SolicitanteProtocol] = [estudiante, estudiante_uno, profesor]


habitos_atomicos = LibroFisico(
    "Hábitos Atómicos",
    "James Clear",
    "132-9874-12364-14",
    True,
)
no_me_puedes_lastimar = LibroFisico(
    "No me puedes lastimar",
    "David Goggins",
    "195-9474-12564-14",
    True,
)

si_me_puedes_lastimar = LibroFisico(
    "Si me puedes lastimar",
    "David Goggins",
    "195-9474-12564-14",
    True,
)

biblioteca.libros = [habitos_atomicos, no_me_puedes_lastimar, si_me_puedes_lastimar]

try:
    print(estudiante.solicitar_libro(None))
except BibliotecaError:
    print("Error. No se pudo solicitar el libro.")

print(estudiante.solicitar_libro("Hábitos Atómicos"))
