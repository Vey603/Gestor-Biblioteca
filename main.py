PRESTAMOS = "Prestamos.txt"


class Libro:
    def __init__(self, titulo: str, autor: str, isbn: str, disponible: bool):
        self.titulo = titulo
        self.autor = autor
        if len(isbn) >= 17:
            self.isbn = isbn
        self.disponible = disponible

    def __str__(self):
        return f"Título: {self.titulo} -- Autor: {self.autor} -- Disponible: {self.disponible}"

    def prestar(self):
        if self.disponible:
            self.disponible = False
            with open(PRESTAMOS, "a", encoding="utf-8") as prestamo:
                prestamo.write(self.titulo + "\n")
            return f"El libro '{self.titulo}' ha sido prestado exitosamente. Ya no está disponible."
        return f"El libro '{self.titulo}' no está disponible en este momento."

    def devolver(self):
        self.disponible = True
        return f"El libro {self.titulo} ha sido devuelto exitosamente. Ahora está disponible."

    def es_popular(self):
        counter = 0
        try:
            with open(PRESTAMOS, "r", encoding="utf-8") as archivo:
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


mi_libro = Libro(
    "100 Años de Soledad", "Gabriel García Márquez", "978-958-8886-21-3", True
)
otro_libro = Libro(
    "El principito", "Antoine de Saint-Exupéry", "978-84-7888-719-4", False
)

catalogo: list = [mi_libro, otro_libro]

# for index, libro in enumerate(catalogo, start=1):
#     print(f"No.{index} -- {libro}")

print(mi_libro.prestar())
print(mi_libro.prestar())
