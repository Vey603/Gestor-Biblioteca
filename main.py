from biblioteca import Biblioteca
from exceptions import UsuarioNoEncontradoError
from libros import LibroFisico
from usuarios import Estudiante, Profesor

biblioteca = Biblioteca("Platzi Biblioteca")

estudiante = Estudiante("Bayron", 1114209584, "Sistemas")
estudiante_uno = Estudiante("Juan", 11159834682, "Diseño")
profesor = Profesor("Jhon", 1112204554)


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

biblioteca.usuarios = [
    estudiante,
    estudiante_uno,
    profesor,
]
biblioteca.libros = [
    habitos_atomicos,
    no_me_puedes_lastimar,
]

print("Bienvenido a Platzi Biblioteca.")
print("Libros Disponibles:")
for titulo in biblioteca.libros_disponibles():
    print(f"  - {titulo}")
print("")

cedula = int(input("Por favor, digite su número de cédula: "))
try:
    usuario = biblioteca.buscar_usuario(cedula)
    print(f"Cédula: {usuario.cedula} -- Nombre: {usuario.nombre}")
except UsuarioNoEncontradoError:
    print("Error, el usuario no fue encontrado")
