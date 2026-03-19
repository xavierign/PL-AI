"""
TP Planificación de Cultivos — Estrategia del grupo
====================================================

Completar la función `asignar` que recibe los precios de los tres
commodities y devuelve la cantidad de hectáreas (enteros) a destinar
a cada alternativa.

IMPORTANTE:
- Solo se permite importar `pulp` como librería externa
- La función debe devolver tres enteros
- La asignación debe respetar TODAS las restricciones:
    * Superficie total: ha_trigo_soja + ha_maiz + ha_soja_1ra <= 600
    * Capital: 560*ha_trigo_soja + 420*ha_maiz + 280*ha_soja_1ra <= 250000
    * Gramíneas: ha_trigo_soja + ha_maiz >= 120
    * Maíz máximo: ha_maiz <= 300
    * Todas las cantidades >= 0
- Si la asignación viola alguna restricción, se descalifica la entrega
"""

import pulp

# Nombre del grupo (completar)
GRUPO = "Nombre del grupo"

# Asignación fija para la campaña 2024/25 (completar con enteros)
HA_TRIGO_SOJA = 0
HA_MAIZ = 0
HA_SOJA_1RA = 0


def asignar(precio_trigo, precio_soja, precio_maiz):
    """
    Decide la asignación óptima de hectáreas dado un escenario de precios.

    Parámetros:
        precio_trigo (float): precio del trigo en USD/tn
        precio_soja  (float): precio de la soja en USD/tn
        precio_maiz  (float): precio del maíz en USD/tn

    Retorna:
        tuple de 3 enteros: (ha_trigo_soja, ha_maiz, ha_soja_1ra)

    Datos que pueden usar dentro de la función:
        - Rendimientos históricos (pueden hardcodear los promedios u otros)
        - Costos fijos: T/S = 560, Maíz = 420, Soja = 280 USD/ha
        - Costos variables: T/S = 25%, Maíz = 28%, Soja = 23% del ingreso bruto
        - Capital máximo: 250000 USD
        - Superficie: 600 ha
        - Gramíneas mínimo: 120 ha
        - Maíz máximo: 300 ha
    """

    # --- Implementar su estrategia aquí ---

    # Ejemplo trivial (reemplazar con su lógica):
    ha_trigo_soja = 120
    ha_maiz = 0
    ha_soja_1ra = 480

    return (ha_trigo_soja, ha_maiz, ha_soja_1ra)
