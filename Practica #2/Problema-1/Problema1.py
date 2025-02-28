# Función para calcular el tiempo que tarda el impulso en recorrer una distancia determinada
def calcular_tiempo_impulso(distancia, velocidad=100):
    """
    Calcula el tiempo que tarda un impulso nervioso en recorrer una distancia dada.
    
    Parámetros:
    distancia (float): La distancia en metros que recorre el impulso.
    velocidad (float): La velocidad del impulso en m/s (por defecto, 100 m/s).
    
    Retorna:
    float: Tiempo en segundos.
    """
    return distancia / velocidad  # Usamos la ecuación t = d / v

# Solicitar al usuario la distancia en metros
distancia = float(input("Ingrese la distancia en metros: "))

# Calcular el tiempo
tiempo = calcular_tiempo_impulso(distancia)

# Mostrar resultado con formato
print(f"Tiempo estimado: {tiempo:.5f} segundos")
