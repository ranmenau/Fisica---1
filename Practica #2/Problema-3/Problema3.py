def calcular_tiempo_aceleracion(vi, vf, d):
    """
    Calcula el tiempo y la aceleración de un electrón en movimiento rectilíneo uniformemente acelerado.

    Parámetros:
    vi (float): Velocidad inicial en m/s.
    vf (float): Velocidad final en m/s.
    d (float): Distancia recorrida en m.

    Retorna:
    tuple: Tiempo en segundos, aceleración en m/s².
    """
    # Calculamos la aceleración usando la ecuación de Torricelli
    a = (vf**2 - vi**2) / (2 * d)
    
    # Calculamos el tiempo usando la ecuación del MRUA
    t = (vf - vi) / a

    return t, a

# Datos
vi = 2.00e4  # m/s
vf = 6.00e6  # m/s
d = 0.015  # m

# Cálculo
t, a = calcular_tiempo_aceleracion(vi, vf, d)

# Mostrar resultados en notación científica
print(f"Tiempo: {t:.2e} s")
print(f"Aceleración: {a:.2e} m/s²")
