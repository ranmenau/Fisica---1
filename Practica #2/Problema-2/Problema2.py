def tiempo_crecimiento(longitud_actual, longitud_final, tasa=2):
    """
    Calcula el tiempo necesario para que el cabello crezca hasta la longitud deseada.
    
    Parámetros:
    longitud_actual (float): Longitud actual del cabello en cm.
    longitud_final (float): Longitud deseada en cm.
    tasa (float): Tasa de crecimiento en cm/mes (por defecto, 2 cm/mes).
    
    Retorna:
    float: Tiempo en meses.
    """
    return (longitud_final - longitud_actual) / tasa  # Se usa t = (xf - xi) / v

# Solicitar datos al usuario
long_actual = float(input("Ingrese la longitud actual del cabello (cm): "))
long_final = float(input("Ingrese la longitud deseada (cm): "))

# Calcular el tiempo
tiempo = tiempo_crecimiento(long_actual, long_final)

# Mostrar el resultado con formato
print(f"Tiempo estimado: {tiempo:.2f} meses")
