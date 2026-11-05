"""
13.3 SQLitePOO + INICIALES  (PLANTILLA DE CLASE GUIADA)
 
Nombre: ______________________________   Grupo: ____________
 
Programa con un catálogo de alumnos guardado en SQLite.
- El catálogo inicia con 2 registros precargados.
- Los demás registros se capturan desde el teclado mediante un menú.
- Operaciones: insertar, consultar, actualizar y eliminar por ID.
 
INSTRUCCIONES:
Parte 1. Completa el catálogo de ALUMNOS: reemplaza cada ______ por el código
         que falta. Lee la PISTA de cada espacio y prueba al terminar cada paso.
Parte 2. (RETO) Al final del archivo, repite todo para un catálogo de LIBROS
         guiándote con lo que ya hiciste para alumnos.
"""
 
# PASO 1. Importaciones
# PISTA: Path sirve para construir la ruta del archivo .db y sqlite3 para usar SQLite.
from pathlib import ______
import ______
 
 
# ==========================================================
# Clase para la conexión y las operaciones de la base de datos
# ==========================================================
class BaseDatos:
    """Administra la conexión SQLite y las operaciones del catálogo."""
 
    # PASO 2. Constructor
    # PISTA: connect() abre (o crea) el archivo de base de datos.
    #        cursor() es el objeto que ejecuta las instrucciones SQL.
    def __init__(self, rutaBD):
        """Crea la base de datos, la tabla y carga los datos iniciales."""
        self.conexion = sqlite3.______(rutaBD)
        self.cursor = self.conexion.______()
        self.crearTablas()
        self.cargarRegistros()
 
    # ------------------------------------------------------
    # Creación de tabla y datos iniciales
    # ------------------------------------------------------
    # PASO 3. Crear la tabla
    # PISTA: CREATE TABLE IF NOT EXISTS evita error si la tabla ya existe.
    #        La llave primaria se autoincrementa: INTEGER PRIMARY KEY AUTOINCREMENT.
    #        commit() guarda los cambios en el archivo.
    def crearTablas(self):
        """Crea la tabla alumnos si todavía no existe."""
 
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS alumnos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                ______ TEXT
            )
        """)
 
        self.conexion.______()
 
    # PASO 4. Registros iniciales
    # PISTA: SELECT COUNT(*) cuenta los registros. fetchone() regresa una tupla,
    #        el conteo está en la posición [0]. Solo se precarga si la tabla está vacía.
    def cargarRegistros(self):
        """Inserta 2 registros, solo si la tabla está vacía."""
 
        self.cursor.execute("SELECT COUNT(*) FROM alumnos")
 
        if self.cursor.fetchone()[0] == ______:
            self.agregarAlumno("Ana Torres", "Ciencia de Datos")
            self.agregarAlumno("Luis Pérez", "Programación")
 
    # ------------------------------------------------------
    # Insertar
    # ------------------------------------------------------
    # PASO 5. INSERT con parámetros
    # PISTA: Los signos ? se reemplazan por los valores de la tupla, en el mismo orden.
    #        Nunca se arma el SQL pegando texto (f-string); los ? protegen la consulta.
    def agregarAlumno(self, nombre, carrera):
        """Agrega un alumno nuevo al catálogo."""
 
        self.cursor.execute(
            "______ INTO alumnos (nombre, carrera) VALUES (?, ?)",
            (nombre, ______)
        )
 
        self.conexion.commit()
 
    # ------------------------------------------------------
    # Consultar
    # ------------------------------------------------------
    # PASO 6. SELECT y recorrido de resultados
    # PISTA: SELECT * trae todas las columnas.
    #        fetchall() regresa una lista de tuplas, una por registro.
    #        En el for se desempaqueta cada tupla en variables (id, nombre, carrera).
    def mostrarAlumnos(self):
        """Muestra todos los alumnos almacenados."""
 
        self.cursor.execute("______ * FROM alumnos")
        filas = self.cursor.______()
 
        print("\n--- CATÁLOGO DE ALUMNOS ---")
 
        if not ______:
            print("No hay alumnos registrados.")
 
        for idAlumno, nombre, ______ in filas:
            print(
                f"ID: {idAlumno} | "
                f"Nombre: {nombre} | "
                f"Carrera: {carrera}"
            )
 
    # ------------------------------------------------------
    # Actualizar
    # ------------------------------------------------------
    # PASO 7. UPDATE ... WHERE
    # PISTA: Sin WHERE se actualizarían TODOS los registros.
    #        rowcount indica cuántas filas se modificaron; si es 0, el ID no existía.
    def actualizarAlumno(self, idAlumno, nombre, carrera):
        """
        Actualiza nombre y carrera del alumno con ese ID.
        Regresa True si el ID existía.
        """
 
        self.cursor.execute(
            "______ alumnos SET nombre = ?, carrera = ? ______ id = ?",
            (nombre, carrera, idAlumno)
        )
 
        self.conexion.commit()
 
        return self.cursor.______ > 0
 
    # ------------------------------------------------------
    # Eliminar
    # ------------------------------------------------------
    # PASO 8. DELETE ... WHERE
    # PISTA: Igual que UPDATE, sin WHERE se borrarían todos los registros.
    #        Una tupla de un solo elemento lleva coma al final: (idAlumno,)
    def eliminarAlumno(self, idAlumno):
        """Elimina el alumno con ese ID. Regresa True si el ID existía."""
 
        self.cursor.execute(
            "______ FROM alumnos WHERE id = ?",
            (______,)
        )
 
        self.conexion.commit()
 
        return self.cursor.rowcount > ______
 
    # ------------------------------------------------------
    # Cerrar conexión
    # ------------------------------------------------------
    # PASO 9. Cerrar la conexión
    def cerrar(self):
        """Cierra la conexión con la base de datos."""
 
        self.conexion.______()
 
 
# ==========================================================
# Funciones auxiliares
# ==========================================================
# PASO 10. Validar la captura
# PISTA: strip() quita espacios al inicio y al final.
#        Un texto vacío ("") es falso en un if.
def pedirTexto(mensaje):
    """Pide un texto y valida que no esté vacío."""
 
    while ______:
        texto = input(mensaje).______()
 
        if texto:
            return texto
 
        print("El campo no puede estar vacío.")
 
 
# PISTA: int() lanza ValueError si el texto no es un número entero.
def pedirId(mensaje):
    """Pide un número entero para usar como ID."""
 
    while True:
        try:
            return ______(input(mensaje))
        except ______:
            print("Escribe un número entero.")
 
 
# PASO 11. Función mostrarMenu (ESCRÍBELA TÚ)
# INDICACIONES:
#   - No recibe parámetros y no regresa nada: solo imprime con print().
#   - Primero imprime un título, por ejemplo "========== MENÚ ==========".
#     (Si quieres una línea en blanco antes, empieza el texto con \n)
#   - Después imprime estas opciones, una por línea, con el formato "número. texto":
#         1. Agregar alumno
#         2. Mostrar alumnos
#         3. Actualizar alumno
#         4. Eliminar alumno
#         0. Salir
#   - Bórrale el pass a la función cuando termines.
def mostrarMenu():
    """Muestra las opciones del menú."""
 
    pass
 
 
# ==========================================================
# Programa principal
# ==========================================================
def main():
    """Ejecuta el menú principal."""
 
    # PASO 12. Ruta de la base de datos
    # PISTA: __file__ es la ruta de este script; .parent es su carpeta.
    #        El operador / une partes de una ruta con Path.
    rutaBD = Path(______).parent / "catalogos.db"
 
    bd = BaseDatos(______)
 
    # PASO 13. Menú con try / finally
    # PISTA: finally se ejecuta SIEMPRE, aunque ocurra un error o se use break.
    try:
        while True:
 
            # PISTA: llama a la función del PASO 11 para mostrar las opciones.
            ______()
 
            opcion = input("Elige una opción: ").strip()
 
            # Opción 1: pedir nombre y carrera con pedirTexto y llamar a agregarAlumno.
            if opcion == "1":
 
                nombre = pedirTexto("Nombre del alumno: ")
                carrera = pedirTexto("______: ")
 
                bd.______(nombre, carrera)
 
                print("Alumno agregado.")
 
            # Opción 2: solo muestra el catálogo.
            elif opcion == "2":
 
                bd.______()
 
            # Opción 3: muestra los alumnos primero para que el usuario vea los IDs,
            # luego pide el ID (pedirId) y los datos nuevos (pedirTexto).
            # El método regresa True o False: úsalo directamente en el if.
            elif opcion == "3":
 
                bd.mostrarAlumnos()
 
                idAlumno = ______("ID del alumno a actualizar: ")
                nombre = pedirTexto("Nuevo nombre: ")
                carrera = pedirTexto("Nueva carrera: ")
 
                if bd.actualizarAlumno(______, nombre, carrera):
                    print("Alumno actualizado.")
                else:
                    print("No existe un alumno con ese ID.")
 
            # Opción 4: muestra los alumnos, pide el ID y elimina.
            elif opcion == "4":
 
                bd.mostrarAlumnos()
 
                idAlumno = pedirId("ID del alumno a eliminar: ")
 
                if bd.______(idAlumno):
                    print("Alumno eliminado.")
                else:
                    print("No existe un alumno con ese ID.")
 
            # Opción 0: despedirse y salir del ciclo.
            elif opcion == "0":
 
                print("Hasta luego.")
                ______
 
            # Cualquier otra cosa es una opción inválida.
            else:
 
                print("Opción no válida.")
 
    finally:
        bd.______()
 
 
# PASO 14. Ejecutar el programa
# PISTA: llama a la función principal.
______()
