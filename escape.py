#importar librerias
import math

#solicitar datos
radio = float(input("Ingrese el radio en metros(m): "))
const = float(input("Ingrese constante gravitacional, en metro por segundo al cuadrado (m/s2): "))

#formula
velocidad = math.sqrt(2 * const * radio)
#aproximar datos
velocidad = math.ceil(velocidad)


#mostrar datos
print(f"La velocidad de escape resultante es: {velocidad}[m/s]")

