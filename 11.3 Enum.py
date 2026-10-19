# ==============================================================================
# RETO DE CLASE: UNICIDAD EN ENUMS CON @unique Y CAPTURA DE ERRORES
# Instrucciones: Lee con atención las indicaciones de los comentarios e integra
# las palabras clave y sintaxis faltantes dentro de las pistas de código.
# ==============================================================================

# 1. TODO: Importa el componente 'Enum' y el decorador 'unique' desde el módulo 'enum'
from enum import Enum, unique

print("=== PARTE A: Definición del Catálogo Asegurado ===")

# 2. TODO: Coloca el decorador correspondiente arriba de la clase para evitar valores duplicados.
# Pista: Recuerda usar el símbolo '@' antes del nombre del decorador.
@unique
class TipoMoneda(Enum):
    PESO_MEXICANO = "MXN"
    DOLAR_AMERICANO = "USD"
    EURO = "EUR"
    
    # 3. TODO: Descomenta la línea de abajo borrando el símbolo '#' para forzar un alias (duplicado).
    # Al dejar dos constantes con el valor "USD", el decorador activará un filtro de seguridad.
    DOLAR_FALSO = "USD"


print("\n=== PARTE B: Captura de Excepciones con try ... except ===")

# Variable de control en camelCase para registrar el estatus de la carga
estatusSistema = "Iniciando comprobación..."
print(estatusSistema)

# 4. TODO: Completa el bloque try-except para atrapar de forma segura el fallo de duplicados.
# Pista: El decorador '@unique' arroja específicamente un error de tipo 'ValueError'.
try:
    # Intentamos mandar a imprimir un miembro para forzar a Python a compilar e inspeccionar la clase.
    print(f"Verificando catálogo... Moneda principal: {TipoMoneda.PESO_MEXICANO.name}")
    estatusSistema = "Catálogo aprobado sin duplicados."
    
except ValueError:
    # 5. TODO: Escribe el mensaje de alerta que se activará cuando el decorador detenga el alias.
    print("¡Alerta de Seguridad! El decorador @unique detectó valores duplicados (alias) en el Enum.")
    estatusSistema = "Catálogo bloqueado por violar la regla de unicidad."


# Mensaje de control final para validar que el sistema no colapsó
print(f"\n[Estatus Final]: {estatusSistema}")
print("[Sistema]: El flujo del programa concluyó de forma segura y controlada.")
