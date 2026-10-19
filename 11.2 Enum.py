from enum import Enum

# 1. Definición del catálogo de roles válidos (Enum)
class TipoUsuario(Enum):
    ADMINISTRADOR = "ADM"
    DOCENTE = "DOC"
    ESTUDIANTE = "EST"

# 2. Definición de la clase principal
class Usuario:
    def __init__(self, nombre, rolUsuario):
        self.nombre = nombre
        
        # TODO: Valida si 'rolUsuario' es una instancia válida de la clase TipoUsuario
        if isinstance(rolUsuario, TipoUsuario):
            # Si es válido, se guarda en el atributo del objeto
            self.rolUsuario = rolUsuario
        else:
            # Si no es válido, lanzamos un error que detiene la creación del objeto
            raise ValueError(f"Error Crítico: El rol '{rolUsuario}' no es un TipoUsuario válido.")

    def mostrarPerfil(self):
        # Accedemos de forma segura al .name (nombre constante) y .value (código ADM/DOC/EST)
        print(f"Usuario: {self.nombre} | Rol: {self.rolUsuario.name} ({self.rolUsuario.value})")


# ==============================================================================
# PRUEBAS DE EJECUCIÓN (Área de simulación en el flujo principal)
# ==============================================================================
print("=== Caso 1: Creación de un usuario VÁLIDO ===")
try:
    # Pasamos correctamente la constante del Enum como argumento
    usuarioCorrecto = Usuario("Karla America", TipoUsuario.ADMINISTRADOR)
    usuarioCorrecto.mostrarPerfil()
except ValueError as error:
    print(error)


print("\n=== Caso 2: Creación de un usuario INVÁLIDO ===")
try:
    # ERROR COMÚN: El programador intenta pasar un texto simple "ESTUDIANTE" 
    # en lugar del objeto constante TipoUsuario.ESTUDIANTE
    usuarioIncorrecto = Usuario("Pedro Páramo", "ESTUDIANTE")
    usuarioIncorrecto.mostrarPerfil()
except ValueError as error:
    print(error)
