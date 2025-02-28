def calcular_tiempo_perdido(vi, a_freno, a_acel, t_parada):
    """
    Calcula el tiempo total perdido por la parada del tren.

    Parámetros:
    vi (float): Velocidad inicial en m/s.
    a_freno (float): Desaceleración en m/s².
    a_acel (float): Aceleración en m/s².
    t_parada (float): Tiempo de parada en segundos.

    Retorna:
    float: Tiempo total perdido en segundos.
    """
    t_frenado = -vi / a_freno
    t_aceleracion = vi / a_acel
    return t_frenado + t_parada + t_aceleracion

# Datos
vi = 20  # m/s
a_freno = -1.0
a_acel = 0.5
t_parada = 120  # s

# Cálculo
tiempo_perdido = calcular_tiempo_perdido(vi, a_freno, a_acel, t_parada)
print(f"Tiempo total perdido: {tiempo_perdido:.2f} s")
