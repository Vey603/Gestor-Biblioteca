import json

from exceptions import LibroNoDisponibleError, UsuarioNoEncontradoError
from persistencia import Persistencia

persistencia = Persistencia()
try:
    biblioteca = persistencia.cargar_datos()
except FileNotFoundError:
    print("Error al guardar. El archivo no existe.")

print("Bienvenido a Platzi Biblioteca.")
print("Libros Disponibles:")
for libro in biblioteca.libros_disponibles:
    print(f"  - {libro.descripcion_completa}")
print("")

cedula = int(input("Por favor, digite su número de cédula: "))
try:
    usuario = biblioteca.buscar_usuario(cedula)
    print(usuario.nombre_completo)
except UsuarioNoEncontradoError as e:
    print(e)

titulo = input("Digite el título del libro deseado: ")
try:
    print(resultado := biblioteca.buscar_libro(titulo))
    print(usuario.solicitar_libro(titulo))
except LibroNoDisponibleError as e:
    print(e)

try:
    persistencia.guardar_datos(biblioteca)
except PermissionError:
    print("Error al guardar. No tienes permisos para sobrescribir el archivo.")
except json.JSONDecodeError:
    print("Error. Archivo corrupto.")
