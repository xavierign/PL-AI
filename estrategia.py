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
- La sección de lectura de datos es obligatoria y no debe modificarse
"""

import pulp
import csv
import os

# =============================================================================
# LECTURA DE DATOS (no modificar esta sección)
# =============================================================================

_data_dir = os.path.join(os.path.dirname(__file__), "data")

def _leer_csv(nombre):
    with open(os.path.join(_data_dir, nombre), newline="") as f:
        return list(csv.DictReader(f))

costos = _leer_csv("costos.csv")
precios_historicos = _leer_csv("precios_historicos.csv")
rendimientos = _leer_csv("rendimientos.csv")

# =============================================================================
# DATOS DEL GRUPO
# =============================================================================

# Nombre del alumno (completar)
GRUPO = "Nombre del alumno"

# Asignación fija para la campaña 2024/25 (completar con enteros)
HA_TRIGO_SOJA = 0
HA_MAIZ = 0
HA_SOJA_1RA = 0


# =============================================================================
# FUNCIÓN ADAPTATIVA
# =============================================================================

def asignar(precio_trigo, precio_soja, precio_maiz):
    """
    Decide la asignación óptima de hectáreas dado un escenario de precios.

    Parámetros:
        precio_trigo (float): precio del trigo en USD/tn
        precio_soja  (float): precio de la soja en USD/tn
        precio_maiz  (float): precio del maíz en USD/tn

    Retorna:
        tuple de 3 enteros: (ha_trigo_soja, ha_maiz, ha_soja_1ra)

    Datos disponibles (ya cargados arriba):
        - rendimientos: lista de dicts con rendimientos históricos por campaña
        - precios_historicos: lista de dicts con precios históricos por campaña
        - costos: lista de dicts con costos fijos y variables por alternativa
    """

    # --- Implementar su estrategia aquí ---

    # Ejemplo trivial (reemplazar con su lógica):
    ha_trigo_soja = 120
    ha_maiz = 0
    ha_soja_1ra = 480

    return (ha_trigo_soja, ha_maiz, ha_soja_1ra)
