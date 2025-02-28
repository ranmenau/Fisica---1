import math

def calcular_separacion(a1, a2, d0, t):
    """
    Calcula la separación entre dos carritos después de un tiempo t.

    Parámetros:
    a1 (float): Aceleración del carrito 1 en m/s².
    a2 (float): Aceleración del carrito 2 en m/s².
    d0 (float): Distancia inicial entre carritos en metros.
    t (float): Tiempo en segundos.

    Retorna:
    float: Separación final en metros.
    """
    x1 = 0.5 * a1 * t**2
    x2 = d0 + 0.5 * a2 * t**2
    return abs(x2 - x1)

def calcular_tiempo_encuentro(a1, a2, d0):
    """
    Calcula el tiempo en el que los carritos se encuentran.

    Parámetros:
    a1 (float): Aceleración del carrito 1 en m/s².
    a2 (float): Aceleración del carrito 2 en m/s².
    d0 (float): Distancia inicial entre carritos en metros.

    Retorna:
    float: Tiempo en segundos.
    """
    t2 = (2 * d0) / (a1 - a2)
    return math.sqrt(t2) if t2 > 0 else None  # Validamos que t² sea positivo

# Datos del problema
a1, a2, d0, t = 2.0, 1.0, 10, 3.0

# Cálculo de la separación final
separacion = calcular_separacion(a1, a2, d0, t)
print(f"Separación después de {t} s: {separacion:.2f} m")

# Cálculo del tiempo de encuentro
tiempo_encuentro = calcular_tiempo_encuentro(a1, a2, d0)
if tiempo_encuentro:
    print(f"Tiempo de encuentro: {tiempo_encuentro:.2f} s")
else:
    print("Los carritos nunca se encuentran.")
