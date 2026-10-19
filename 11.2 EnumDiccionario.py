from enum import Enum, unique

# ==============================================================================
# 1. CATALOGO SEGURO CON ENUMS (Llaves constantes)
# ==============================================================================
# TODO: Coloca el decorador para evitar duplicados y completa las constantes del Enum
@unique
class TipoPersonaje(Enum):
    GUERRERO = 1
    MAGO = 2
    ARQUERO = 3


# ==============================================================================
# 2. BASE DE DATOS COMPLEMENTARIA (Diccionario de Atributos)
# ==============================================================================
# TODO: Completa el diccionario vinculando los Enums con sus estadísticas base
atributosPersonajes = {
    TipoPersonaje.GUERRERO: {"vida": 150, "ataque": 35},
    TipoPersonaje.MAGO:     {"vida": 80,  "ataque": 60},
    TipoPersonaje.ARQUERO:  {"vida": 110, "ataque": 45}
}


# ==============================================================================
# 3. CLASE PRINCIPAL: Personaje (Modelo POO)
# ==============================================================================
class Personaje:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        
        # TODO: Valida con un 'if' si la variable 'rol' es una instancia de 'TipoPersonaje'
        if isinstance(rol, TipoPersonaje):
            self.rol = rol
            
            # TODO: Usa el 'rol' aprobado como llave para extraer los datos del diccionario 'atributosPersonajes'
            # Guarda la información en variables internas usando camelCase
            datosBase = atributosPersonajes[rol]
            self.vidaActual = datosBase["vida"]
            self.ataqueBase = datosBase["ataque"]
        else:
            # Si no es un Enum válido, levantamos una excepción para destruir la instancia corrupta
            raise ValueError(f"Error Crítico: El rol '{rol}' no existe en el catálogo de personajes.")

    def mostrarEstadisticas(self):
        # TODO: Imprime los datos usando .name para ver la constante en texto plano
        print(f"Héroe: {self.nombre} | Clase: {self.rol.name}")
        print(f" -> Vida: {self.vidaActual} HP | Daño: {self.ataqueBase} pts\n")


# ==============================================================================
# 4. FLUJO PRINCIPAL DE PRUEBAS (Corrida de Consola sin funciones def)
# ==============================================================================
print("=== Caso 1: Creación Segura usando Enum ===")
try:
    # TODO: Pasa la constante del Enum en el segundo argumento para crear al Guerrero
    heroeIncial = Personaje("Aragorn", TipoPersonaje.GUERRERO)
    heroeIncial.mostrarEstadisticas()
except ValueError as error:
    print(error)


print("=== Caso 2: Intento de Creación Incorrecta usando un String genérico ===")
try:
    # ERROR INTENCIONAL: El programador pasa un texto libre "MAGO" en vez del Enum
    # TODO: Ejecuta el código para observar cómo la validación detiene la ejecución
    heroeErroneo = Personaje("Gandalf", "MAGO")
    heroeErroneo.mostrarEstadisticas()
except ValueError as error:
    print(f"Fallo controlado exitosamente -> {error}\n")


print("=== Caso 3: Recorrido Completo del Diccionario Mixto ===")
# TODO: Completa el ciclo para listar en consola todos los roles y sus daños base
for rolActual in atributosPersonajes:
    # Pista: Accede al diccionario usando 'rolActual' y busca la clave de daño
    danoBase = atributosPersonajes[rolActual]["ataque"]
    print(f"Clase Disponible: {rolActual.name:<10} | Daño Estándar: {danoBase} pts")
