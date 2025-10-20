# utils.py

# Función Pura: Es el núcleo del cálculo. No modifica variables externas.
def _evaluar_impacto(tec):
    """
    Calcula el índice de impacto basado en la Inversión (70%) y el Riesgo (30%).
    """
    return (tec['Inversion'] * 0.7) + (tec['Riesgo'] * 0.3)

# Uso de filter (Programación Funcional) para obtener Patrones (Criterio 2)
def filtrar_tendencias(datos):
    """
    Filtra la lista de tecnologías para seleccionar solo aquellas consideradas
    'Tendencias Futuras' (ejemplo: Riesgo bajo o igual a 0.3).
    """
    # Patrón detectado: Tecnologías más estables (bajo riesgo)
    return list(filter(lambda t: t['Riesgo'] <= 0.3, datos))

# Uso de map (Programación Funcional) para calcular Resultados (Criterio 2)
def calcular_indice_impacto(tendencias_filtradas):
    """
    Aplica la función pura _evaluar_impacto a cada tecnología filtrada.
    """
    return list(map(lambda t: {'Tecnologia': t['Tecnologia'], 
                               'Indice': _evaluar_impacto(t)}, 
                    tendencias_filtradas))
