# main.py

# 1. Importación del Módulo (Arquitectura Modular - Unidad 1)
from utils import calcular_indice_impacto, filtrar_tendencias

# 2. Gestión de Datos (Estructuras de Datos: Listas y Diccionarios)
DATOS_TECNOLOGIAS = [
    {'Tecnologia': 'IA Generativa', 'Inversion': 0.9, 'Riesgo': 0.1},
    {'Tecnologia': 'Blockchain', 'Inversion': 0.7, 'Riesgo': 0.5},
    {'Tecnologia': 'Ciberseguridad', 'Inversion': 0.8, 'Riesgo': 0.2},
    {'Tecnologia': 'Realidad Virtual', 'Inversion': 0.4, 'Riesgo': 0.6},
    {'Tecnologia': 'Computación Cuántica', 'Inversion': 0.95, 'Riesgo': 0.05},
]

def main():
    print("--- 🔬 Análisis TechFutureViz Iniciado ---")
    
    # 3. Flujo de Análisis (Llamadas Modulares)
    tendencias_futuras = filtrar_tendencias(DATOS_TECNOLOGIAS) # Ejecuta el filter
    resultados_impacto = calcular_indice_impacto(tendencias_futuras) # Ejecuta el map

    print(f"\nTecnologías Analizadas (Riesgo <= 0.3): {len(tendencias_futuras)}")

    # 4. Presentación de Resultados (Estructura Repetitiva 'for' - Unidad 3)
    print("\n--- Índice de Impacto Cuantificado ---")
    
    impacto_total = 0 # Inicialización para la simulación de reduce
    
    for tecnologia in resultados_impacto:
        indice = tecnologia['Indice']
        print(f"-> {tecnologia['Tecnologia']}: Índice de Impacto: {indice:.2f}")
        impacto_total += indice # Simulación de reduce para el Impacto Total

    # 5. Conclusión Programática
    print(f"\nIMPACTO TOTAL ACUMULADO de las Tendencias Futuras: {impacto_total:.2f}")
    print("--- Ejecución Finalizada ---")

if __name__ == "__main__":
    main()
