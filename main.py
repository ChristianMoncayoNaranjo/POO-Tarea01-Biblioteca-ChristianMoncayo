from modelo.libro import Libro
from modelo.estudiante import Estudiante
from modelo.biblioteca import Biblioteca

from faker import Faker
import random


def main():
    fake = Faker("es_ES")

    print("=" * 60)
    print("  SISTEMA DE GESTIÓN DE BIBLIOTECA UNEMI")
    print("=" * 60)

    biblioteca = Biblioteca("Biblioteca Central UNEMI")
    print(f"\n{biblioteca}\n")

    # Registrar 100 libros automáticamente
    print("── Registrando 100 libros automáticamente ──")

    libros = []

    for _ in range(100):
        libro = Libro(
            f"978-{random.randint(1000000000, 9999999999)}",
            fake.sentence(nb_words=4).replace(".", ""),
            fake.name()
        )
        biblioteca.registrar_libro(libro)
        libros.append(libro)

    print(f"\n  ✓ Total de libros registrados: {len(libros)}")

    # Registrar estudiantes
    print("\n── Registrando estudiantes ──")

    est1 = Estudiante(
        "0926400615",
        "María",
        "López",
        "Ingeniería en Sistemas"
    )

    est2 = Estudiante(
        "0912345678",
        "Carlos",
        "Ramírez",
        "Ingeniería Industrial"
    )

    biblioteca.registrar_estudiante(est1)
    biblioteca.registrar_estudiante(est2)

    print(f"\n{biblioteca}\n")

    # Seleccionar libros para pruebas
    libro1 = libros[0]
    libro2 = libros[1]
    libro3 = libros[2]

    # Realizar préstamos
    print("── Realizando préstamos ──")

    print(
        biblioteca.prestar_libro(
            libro1.isbn,
            est1.cedula,
            "2026-04-15",
            "2026-04-29"
        )
    )

    print(
        biblioteca.prestar_libro(
            libro2.isbn,
            est1.cedula,
            "2026-04-15",
            "2026-05-01"
        )
    )

    print(
        biblioteca.prestar_libro(
            libro3.isbn,
            est2.cedula,
            "2026-04-15",
            "2026-04-22"
        )
    )

    # Intentar prestar un libro ya prestado
    print("\n── Intentando prestar libro ya prestado ──")

    print(
        biblioteca.prestar_libro(
            libro1.isbn,
            est2.cedula,
            "2026-04-16",
            "2026-04-30"
        )
    )

    # Consultar préstamos activos
    print(f"\n── Préstamos activos de {est1.nombre} {est1.apellido} ──")

    for prestamo in biblioteca.consultar_prestamos_activos(est1.cedula):
        print(f"  → {prestamo}")

    # Devolver libro
    print("\n── Devolviendo un libro ──")

    print(
        biblioteca.devolver_libro(
            libro1.isbn,
            est1.cedula
        )
    )

    # Estado del libro devuelto
    print("\n── Estado del libro devuelto ──")
    print(f"  {libro1}")

    # Consultar nuevamente préstamos activos
    print(f"\n── Préstamos activos de {est1.nombre} {est1.apellido} ──")

    prestamos = biblioteca.consultar_prestamos_activos(est1.cedula)

    if prestamos:
        for prestamo in prestamos:
            print(f"  → {prestamo}")
    else:
        print("  (Sin préstamos activos)")

    # Prestar nuevamente el libro devuelto
    print("\n── Prestando el libro devuelto a otro estudiante ──")

    print(
        biblioteca.prestar_libro(
            libro1.isbn,
            est2.cedula,
            "2026-04-16",
            "2026-04-30"
        )
    )

    # Estado final
    print(f"\n{'=' * 60}")
    print(f"  {biblioteca}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()