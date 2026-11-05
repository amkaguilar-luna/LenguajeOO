""" INSTRUCCIONES:
Reemplaza cada ______ por el código que falta. Lee la PISTA de cada espacio.
Avanza por PASOS, en orden, y prueba tu programa al terminar cada paso.
"""

# PASO 1. Importaciones
# PISTA: Path sirve para construir la ruta del archivo .db y sqlite3 para usar SQLite.
from pathlib import ______
import ______

# ==========================================================
# Clase para la conexión y las operaciones de la base de datos
# ==========================================================
class BaseDatos:
    """Administra la conexión SQLite y las operaciones de los catálogos."""

    # PASO 2. Constructor
    # PISTA: connect() abre (o crea) el archivo de base de datos.
    #        cursor() es el objeto que ejecuta las instrucciones SQL.
    def __init__(self, rutaBD):
        """Crea la base de datos, las tablas y carga los datos iniciales."""
        self.conexion = sqlite3.______(rutaBD)
        self.cursor = self.conexion.______()
        self._____________
        ______.cargarIniciales()

    # ------------------------------------------------------
    # Creación de tablas y datos iniciales
    # ------------------------------------------------------
    # PASO 3. Crear las tablas
    # PISTA: CREATE TABLE IF NOT EXISTS evita error si la tabla ya existe.
    #        La llave primaria se autoincrementa: INTEGER PRIMARY KEY AUTOINCREMENT.
    #        commit() guarda los cambios en el archivo.
    def crearTablas(self):
        """Crea las tablas alumnos y libros si todavía no existen."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS alumnos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                ______ TEXT
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS libros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ______ TEXT,
                autor TEXT
            )
        """)
        self.conexion.______()

    # PASO 4. Datos iniciales
    # PISTA: SELECT COUNT(*) cuenta los registros. fetchone() regresa una tupla,
    #        el conteo está en la posición [0]. Solo se precarga si la tabla está vacía.
    def cargarIniciales(self):
        """Inserta 2 registros por catálogo, solo si la tabla está vacía."""
        self.cursor.execute("SELECT COUNT(*) FROM alumnos")
        if self.cursor.fetchone()[0] == ______:
            self.agregarAlumno("Ana Torres", "A001")
            self.agregarAlumno("Luis Pérez", "A002")

        self.cursor.execute("SELECT COUNT(*) FROM libros")
        if self.cursor.fetchone()[0] == ______:
            self.agregarLibro("Cien años de soledad", "Gabriel García Márquez")
            self.agregarLibro("El principito", "Antoine de Saint-Exupéry")

    # ------------------------------------------------------
    # Insertar
    # ------------------------------------------------------
    # PASO 5. INSERT con parámetros
    # PISTA: Los signos ? se reemplazan por los valores de la tupla, en el mismo orden.
    #        Nunca se arma el SQL pegando texto (f-string); los ? protegen la consulta.
    def agregarAlumno(self, nombre, matricula):
        """Agrega un alumno nuevo al catálogo."""
        self.cursor.execute(
            "______ INTO alumnos (nombre, matricula) VALUES (?, ?)",
            (nombre, ______),
        )
        self.conexion.commit()

    def agregarLibro(self, titulo, autor):
        """Agrega un libro nuevo al catálogo."""
        self.cursor.execute(
            "INSERT INTO libros (______, autor) VALUES (?, ?)",
            (______, autor),
        )
        self.conexion.commit()

    # ------------------------------------------------------
    # Consultar
    # ------------------------------------------------------
    # PASO 6. SELECT y recorrido de resultados
    # PISTA: fetchall() regresa una lista de tuplas, una por registro.
    #        En el for se desempaqueta cada tupla en variables.
    #        "id_" lleva guion bajo para no chocar con la función id() de Python.
    def mostrarAlumnos(self):
        """Muestra todos los alumnos almacenados."""
        self.cursor.execute("______ id, nombre, matricula FROM alumnos")
        filas = self.cursor.______()
        print("\n--- CATÁLOGO DE ALUMNOS ---")
        if not ______:
            print("No hay alumnos registrados.")
        for id_, nombre, matricula in filas:
            print(f"ID: {id_} | Nombre: {nombre} | Matrícula: {matricula}")

    def mostrarLibros(self):
        """Muestra todos los libros almacenados."""
        self.cursor.execute("SELECT id, titulo, autor FROM libros")
        filas = self.cursor.fetchall()
        print("\n--- CATÁLOGO DE LIBROS ---")
        if not filas:
            print("No hay libros registrados.")
        for id_, ______, autor in filas:
            print(f"ID: {id_} | Título: {titulo} | Autor: {autor}")

    # ------------------------------------------------------
    # Actualizar
    # ------------------------------------------------------
    # PASO 7. UPDATE ... WHERE
    # PISTA: Sin WHERE se actualizarían TODOS los registros.
    #        rowcount indica cuántas filas se modificaron; si es 0, el ID no existía.
    def actualizarAlumno(self, id_, nombre, matricula):
        """Actualiza nombre y matrícula del alumno con ese ID.
        Regresa True si el ID existía."""
        self.cursor.execute(
            "______ alumnos SET nombre = ?, matricula = ? ______ id = ?",
            (nombre, matricula, id_),
        )
        self.conexion.commit()
        return self.cursor.______ > 0

    def actualizarLibro(self, id_, titulo, autor):
        """Actualiza título y autor del libro con ese ID.
        Regresa True si el ID existía."""
        self.cursor.execute(
            "UPDATE libros SET titulo = ?, autor = ? WHERE id = ?",
            (______, autor, id_),
        )
        self.conexion.commit()
        return self.cursor.rowcount > 0

    # ------------------------------------------------------
    # Eliminar
    # ------------------------------------------------------
    # PASO 8. DELETE ... WHERE
    # PISTA: Igual que UPDATE, sin WHERE se borrarían todos los registros.
    #        Una tupla de un solo elemento lleva coma al final: (id_,)
    def eliminarAlumno(self, id_):
        """Elimina el alumno con ese ID. Regresa True si el ID existía."""
        self.cursor.execute("______ FROM alumnos WHERE id = ?", (______,))
        self.conexion.commit()
        return self.cursor.rowcount > 0

    def eliminarLibro(self, id_):
        """Elimina el libro con ese ID. Regresa True si el ID existía."""
        self.cursor.execute("DELETE FROM libros WHERE id = ?", (id_,))
        self.conexion.commit()
        return self.cursor.rowcount > ______

    # ------------------------------------------------------
    # Cerrar
    # ------------------------------------------------------
    # PASO 9. Cerrar la conexión
    def cerrar(self):
        """Cierra la conexión con la base de datos."""
        self.conexion.______()


# ==========================================================
# Funciones auxiliares para capturar datos del teclado
# ==========================================================
# PASO 10. Validar la captura
# PISTA: strip() quita espacios al inicio y al final.
#        Un texto vacío ("") es falso en un if.
def pedirTexto(mensaje):
    """Pide un texto al usuario y repite hasta que no esté vacío."""
    while ______:
        texto = input(mensaje).______()
        if texto:
            return texto
        print("El campo no puede estar vacío.")


# PISTA: int() lanza ValueError si el texto no es un número entero.
def pedirId(mensaje):
    """Pide un ID numérico entero al usuario y repite si no es válido."""
    while True:
        try:
            return ______(input(mensaje))
        except ______:
            print("Escribe un número entero.")


def mostrarMenu():
    """Imprime las opciones del menú."""
    print("\n========== MENÚ ==========")
    print("1. Agregar alumno")
    print("2. Agregar libro")
    print("3. Mostrar alumnos")
    print("4. Mostrar libros")
    print("5. Actualizar alumno")
    print("6. Actualizar libro")
    print("7. Eliminar alumno")
    print("8. Eliminar libro")
    print("0. Salir")


# ==========================================================
# Programa principal
# ==========================================================
def main():
    """Ejecuta el menú hasta que el usuario elija salir."""
    # PASO 11. Ruta de la base de datos
    # PISTA: __file__ es la ruta de este script; .parent es su carpeta.
    #        El operador / une partes de una ruta con Path.
    rutaBD = Path(______).parent / "catalogos.db"
    bd = BaseDatos(______)

    # PASO 12. Menú con try / finally
    # PISTA: finally se ejecuta SIEMPRE, aunque ocurra un error o se use break.
    try:
        while True:
            mostrarMenu()
            opcion = input("Elige una opción: ").strip()

            if opcion == "1":
                nombre = pedirTexto("Nombre del alumno: ")
                matricula = pedirTexto("Matrícula: ")
                bd.agregarAlumno(nombre, matricula)
                print("Alumno agregado.")
            elif opcion == "2":
                titulo = pedirTexto("Título del libro: ")
                autor = pedirTexto("Autor: ")
                bd.______(titulo, autor)
                print("Libro agregado.")
            elif opcion == "3":
                bd.mostrarAlumnos()
            elif opcion == "4":
                bd.______()
            elif opcion == "5":
                # PISTA: se muestran los alumnos primero para que el usuario vea los IDs.
                bd.mostrarAlumnos()
                id_ = pedirId("ID del alumno a actualizar: ")
                nombre = pedirTexto("Nuevo nombre: ")
                matricula = pedirTexto("Nueva matrícula: ")
                if bd.actualizarAlumno(______, nombre, matricula):
                    print("Alumno actualizado.")
                else:
                    print("No existe un alumno con ese ID.")
            elif opcion == "6":
                bd.mostrarLibros()
                id_ = pedirId("ID del libro a actualizar: ")
                titulo = pedirTexto("Nuevo título: ")
                autor = pedirTexto("Nuevo autor: ")
                if bd.actualizarLibro(id_, titulo, autor):
                    print("Libro actualizado.")
                else:
                    print("No existe un libro con ese ID.")
            elif opcion == "7":
                bd.mostrarAlumnos()
                id_ = pedirId("ID del alumno a eliminar: ")
                if bd.______(id_):
                    print("Alumno eliminado.")
                else:
                    print("No existe un alumno con ese ID.")
            elif opcion == "8":
                bd.mostrarLibros()
                id_ = pedirId("ID del libro a eliminar: ")
                if bd.eliminarLibro(id_):
                    print("Libro eliminado.")
                else:
                    print("No existe un libro con ese ID.")
            elif opcion == "0":
                print("Hasta luego.")
                ______
            else:
                print("Opción no válida.")
    finally:
        bd.______()


# PASO 13. Punto de entrada
# PISTA: este if evita que main() se ejecute si el archivo se importa desde otro.
if __name__ == "______":
    main()


# ==========================================================
# PRUEBAS PARA EL FINAL DE LA CLASE (escribe lo que observaste)
# ==========================================================
# 1. Al correr por primera vez, ¿qué IDs tienen los registros precargados? ________
# 2. Si cierras y vuelves a correr, ¿se vuelven a precargar? ¿Por qué? ________
# 3. ¿Qué pasa si actualizas un ID que no existe? ________
# 4. ¿Qué pasaría si se te olvida el WHERE en un DELETE? ________
