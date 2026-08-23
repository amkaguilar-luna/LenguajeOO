#Estructa de control if
"""
x=int(input("Da un número="))
if x>5:
    print(x,"es mayor que 5")
elif x<5:
    print(x,"es menor que 5")
else:
    print(x, "es igual a 5")


x=int(input("Da un número: "))
if x>5:
    print(f"x={x} es mayor que 5")
elif x<5:
    print(f"x={x} es menor que 5")
else:
    print(f"x={x} es igual que 5")


# Solicitar la calificación
calificacion = float(input("Introduce una calificación: "))

# Evaluar la calificación
if calificacion > 9:
    print("Sobresaliente")
elif calificacion > 8:
    print("Notable")
elif calificacion > 7:
    print("Bien")
elif calificacion >= 6:
    print("Suficiente")
else:
    print("Insuficiente")


nota = 85
asistencia = 0.9 # 90%

if nota >= 70 and asistencia >= 0.8:
    print("Aprobado")
elif nota >= 70 and asistencia < 0.8:
    print("Reprobado por inasistencia")
else:
    print("Reprobado por nota")


# Solicitar la edad al usuario
edad = int(input("Introduce tu edad: "))
# Evaluar las condiciones
if edad < 6:
    print("Entrada gratis. Motivo: Eres menor de 6 años.")
elif edad > 65:
    print("Entrada gratis. Motivo: Eres mayor de 65 años.")
else:
    print("No entras en el rango de gratuidad. Por favor, solicitar el pago de la entrada.") """


alphabet="abcdefghijklmnñopqrstuvwxyz"

print("aeiou" in alphabet)

a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)

x, y, z = 5, 10, 8
x, y, z = z, y, x
 
print(x > z)
print((y - 5) == x)

x = "1"
 
if x == 1:
    print("one")
elif x == "1":
    if int(x) > 1:
        print("two")
    elif int(x) < 1:
        print("three")
    else:
        print("four")
if int(x) == 1:
    print("five")
else:
    print("six") 

a = 6
b = 3
#a /= 2 * b

print(a)

var = 100
var = 200 + 200
print(var)





