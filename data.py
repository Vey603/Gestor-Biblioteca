from libros import LibroFisico
from usuarios import Estudiante

# Creación de 10 libros de progreso personal
libro1 = LibroFisico("Hábitos Atómicos", "James Clear", "978-84-18118-04-1")
libro2 = LibroFisico("No Me Puedes Lastimar", "David Goggins", "978-84-16720-56-8")
libro3 = LibroFisico("El Poder del Ahora", "Eckhart Tolle", "978-84-7953-436-3")
libro4 = LibroFisico(
    "Los 7 Hábitos de la Gente Altamente Efectiva", "Stephen Covey", "978-84-493-2906-5"
)
libro5 = LibroFisico("Piense y Hágase Rico", "Napoleon Hill", "978-16-040-5075-4")
libro6 = LibroFisico(
    "El Sutil Arte de Que Te Importe Un Carajo", "Mark Manson", "978-60-735-6801-4"
)
libro7 = LibroFisico(
    "Mindset: La Actitud del Éxito", "Carol Dweck", "978-84-995-3832-9"
)
libro8 = LibroFisico("Las 48 Leyes del Poder", "Robert Greene", "978-84-253-4222-6")
libro9 = LibroFisico(
    "El Monje Que Vendió Su Ferrari", "Robin Sharma", "978-84-9793-711-2"
)
libro10 = LibroFisico("Padre Rico Padre Pobre", "Robert Kiyosaki", "978-16-945-1873-5")
libro_no_disponible = LibroFisico.crear_no_disponible(
    "Libro de prueba", "Autor de Prueba", "1234-4563-14523-45"
)

# Creación de 10 estudiantes
estudiante1 = Estudiante("Carlos Ramírez", 1005234567, "Ingeniería de Sistemas")
estudiante2 = Estudiante("María Fernández", 1003456789, "Administración de Empresas")
estudiante3 = Estudiante("Juan Pérez", 1007654321, "Psicología")
estudiante4 = Estudiante("Ana López", 1002345678, "Derecho")
estudiante5 = Estudiante("Luis González", 1008765432, "Medicina")
estudiante6 = Estudiante("Laura Martínez", 1004567890, "Arquitectura")
estudiante7 = Estudiante("Diego Torres", 1009876543, "Economía")
estudiante8 = Estudiante("Sofía Rodríguez", 1001234567, "Diseño Gráfico")
estudiante9 = Estudiante("Andrés Castillo", 1006543210, "Contaduría")
estudiante10 = Estudiante("Valentina Morales", 1003210987, "Ingeniería Industrial")
estudiante_sistemas = Estudiante.estudiante_sistemas("Bayron", 1114219584)

data_libros = [
    libro1,
    libro2,
    libro3,
    libro4,
    libro5,
    libro6,
    libro7,
    libro8,
    libro9,
    libro10,
    libro_no_disponible,
]

data_estudiantes = [
    estudiante1,
    estudiante2,
    estudiante3,
    estudiante4,
    estudiante5,
    estudiante6,
    estudiante7,
    estudiante8,
    estudiante9,
    estudiante10,
    estudiante_sistemas,
]
