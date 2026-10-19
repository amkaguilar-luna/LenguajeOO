from enum import Enum, unique
# ==============================================================================
# 1. CATÁLOGO SEGURO CON ENUMS (Llaves constantes e inmutables)
# ==============================================================================
# TODO: Coloca aquí el decorador oficial que garantiza que no existan valores duplicados (alias).
# Pista: Inicia con el símbolo '@'.
[ ]

# TODO: Declara la clase 'TipoPersonaje' asegurando que herede de la clase 'Enum'.
class TipoPersonaje([ ]):
    # TODO: Registre las 3 constantes del catálogo con sus identificadores numéricos:
    # 1. GUERRERO asignado al valor 1
    # 2. MAGO asignado al valor 2
    # 3. ARQUERO asignado al valor 3
    [ ] = 1
    [ ] = 2
    [ ] = 3
# ==============================================================================
# 2. BASE DE DATOS COMPLEMENTARIA (Diccionario de Atributos Auxiliares)
# ==============================================================================
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
        
        # TODO: Valida si la variable recibida 'rol' es una instancia de la clase 'TipoPersonaje'
        if isinstance([ ], [ ]):
            self.rol = rol
            
            # TODO: Extrae el diccionario interno de estadísticas usando la variable 'rol' como llave
            datosBase = atributosPersonajes[ ]
            
            # TODO: Asigna a los atributos del objeto la "vida" y el "ataque" correspondientes de datosBase
            self.vidaActual = [ ]
            self.ataqueBase = [ ]
        else:
            # TODO: Lanza una excepción ValueError con un mensaje descriptivo si el rol es inválido
            [ ]

    def mostrarEstadisticas(self):
        # TODO: Imprime en consola el nombre del héroe, el nombre del rol (usando .name) 
        # y las estadísticas de salud actual y daño base.
        pass

    def recibirDanio(self, puntos):
        print(f"💥 ¡{self.nombre} recibe un impacto de {puntos} puntos de daño!")
        
        # TODO: Resta la variable 'puntos' a la propiedad de salud actual de este personaje
        [ ]
        
        # TODO: Desarrolla la validación lógica para que si la vida actual cae por debajo o igual a cero,
        # se nivele estrictamente en cero y se notifique en pantalla que el personaje cayó en combate.
        if [ ]:
            [ ]
            print(f"💀 {self.nombre} ha caído en combate.\n")
        else:
            print(f"❤️ Vida restante de {self.nombre}: {self.vidaActual} HP\n")


# ==============================================================================
# 4. FLUJO PRINCIPAL INTERACTIVO (Corrida de Consola Simulada)
# ==============================================================================

# --- PASO 1: Mostrar el catálogo de personajes disponibles por primera vez ---
print("==================================================")
print("===      CATÁLOGO DE PERSONAJES DISPONIBLES    ===")
print("==================================================")
# TODO: Completa el ciclo for para que recorra de forma automática la estructura 'TipoPersonaje'
for rolActual in [ ]:
    datosRol = atributosPersonajes[rolActual]
    print(f"[{rolActual.value}] {rolActual.name:<10} | Vida: {datosRol['vida']} HP | Daño: {datosRol['ataque']} pts")
print("==================================================\n")


# TODO: Inicia un bloque de control de excepciones para prevenir caídas catastróficas del programa
try:
    # --- PASO 2: Preguntar al usuario qué personaje quiere elegir ---
    seleccionUsuario = input("Digita el número de la clase que deseas elegir para tu héroe: ")
    
    # TODO: Convierte la entrada 'seleccionUsuario' a un número entero
    numeroClase = [ ]
    
    # TODO: Mapea directamente el 'numeroClase' al Enum 'TipoPersonaje' para validar la opción
    rolElegido = TipoPersonaje([ ]) 
    
    nombreHeroe = input("Escribe el nombre de tu personaje: ")
    print("\n--- ¡Personaje Creado con Éxito! ---")
    
    # TODO: Instancia el objeto de la clase Personaje usando las variables correspondientes
    heroeUsuario = Personaje([ ], [ ])
    heroeUsuario.mostrarEstadisticas()
    
    # --- PASO 3: Generar el enemigo fijo (Un Mago) para el combate ---
    print("--- ¡Un enemigo ha aparecido! ---")
    enemigoMago = Personaje("Mago Oscuro", TipoPersonaje.MAGO)
    enemigoMago.mostrarEstadisticas()
    
    print("==================================================")
    print("===             FASE DE COMBATE                ===")
    print("==================================================")
    
    # --- PASO 4: Preguntar el impacto y validar que esté dentro de lo permitido ---
    entradaImpacto = input(f"Ingresa los puntos de daño que deseas causarle a {enemigoMago.nombre}: ")
    puntosImpacto = int(entradaImpacto)
    
    # TODO: Desarrolla la condicional que verifique si los 'puntosImpacto' son un valor negativo
    if [ ]:
        print("❌ Error: No se permiten impactos con valores negativos. El ataque ha fallado.")
    else:
        # TODO: Invoca el método pertinente para aplicarle los 'puntosImpacto' al objeto 'enemigoMago'
        [ ]

# TODO: Define la excepción específica que debe capturar el bloque cuando el usuario ingresa datos erróneos
except [ ]:
    print("\n❌ Entrada Inválida: Asegúrate de seleccionar una opción correcta del menú y usar números válidos para el daño.")

print("\n[Sistema]: Simulación interactiva finalizada.")
