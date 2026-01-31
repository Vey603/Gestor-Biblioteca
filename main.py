from biblioteca import Biblioteca
from data import data_estudiantes, data_libros
from exceptions import LibroNoDisponibleError, UsuarioNoEncontradoError
from usuarios import Profesor

biblioteca = Biblioteca("Platzi Biblioteca")

profesor = Profesor("Jhon", 1112204554)

biblioteca.usuarios = [profesor] + data_estudiantes
biblioteca.libros = data_libros

print("Bienvenido a Platzi Biblioteca.")
print("Libros Disponibles:")
for libro in biblioteca.libros_disponibles():
    print(f"  - {libro.descripcion_completa}")
print("")

cedula = int(input("Por favor, digite su número de cédula: "))
try:
    usuario = biblioteca.buscar_usuario(cedula)
    print(f"Cédula: {usuario.cedula} -- Nombre: {usuario.nombre}")
except UsuarioNoEncontradoError as e:
    print(e)

titulo = input("Digite el título del libro deseado: ")
try:
    print(resultado := biblioteca.buscar_libro(titulo))
    print(usuario.solicitar_libro(titulo))
except LibroNoDisponibleError as e:
    print(e)
