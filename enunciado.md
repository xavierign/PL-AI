# Trabajo Práctico: Planificación Óptima de Cultivos

## Investigación Operativa — FIUBA / FAUBA

---

## Contexto

Un productor agropecuario posee un campo de **600 hectáreas** en la localidad de **Pergamino, provincia de Buenos Aires** (zona núcleo argentina). Para la campaña **2024/25** debe decidir qué proporción de su campo destinar a cada una de las siguientes **tres alternativas productivas**:

| Alternativa | Descripción |
|---|---|
| **Trigo / Soja 2da** | Doble cultivo: trigo de invierno seguido de soja de segunda |
| **Maíz** | Maíz de primera (ciclo completo) |
| **Soja 1ra** | Soja de primera (ciclo completo) |

El productor dispone de datos históricos de **9 campañas anteriores** (precios y rendimientos) y los **precios vigentes** para la campaña 2024/25. Los **rendimientos** de la campaña 2024/25 son inciertos al momento de la decisión.

---

## Datos

### 1. Rendimientos históricos (tn/ha, zona Pergamino)

| Campaña | Trigo | Soja 2da | Maíz | Soja 1ra |
|---|---|---|---|---|
| 2015/16 | 4.5 | 3.0 | 10.2 | 4.0 |
| 2016/17 | 3.8 | 2.4 | 8.5 | 3.4 |
| 2017/18 | 4.8 | 3.2 | 11.0 | 4.2 |
| 2018/19 | 3.6 | 2.3 | 8.2 | 3.3 |
| 2019/20 | 4.0 | 2.7 | 9.2 | 3.7 |
| 2020/21 | 3.5 | 2.2 | 7.8 | 3.2 |
| 2021/22 | 2.8 | 1.8 | 6.0 | 2.5 |
| 2022/23 | 4.3 | 2.9 | 10.5 | 4.1 |
| 2023/24 | 4.6 | 3.1 | 10.8 | 4.3 |

> **Nota:** La alternativa Trigo/Soja 2da genera **dos productos** en la misma hectárea (ej: 4.5 tn de trigo + 3.0 tn de soja en 2015/16). Los rendimientos de la campaña 2024/25 son **desconocidos** al momento de planificar.

### 2. Precios históricos y vigentes (USD/tn)

| Campaña | Trigo | Soja | Maíz |
|---|---|---|---|
| 2015/16 | 150 | 320 | 155 |
| 2016/17 | 145 | 340 | 150 |
| 2017/18 | 175 | 325 | 160 |
| 2018/19 | 190 | 300 | 145 |
| 2019/20 | 180 | 335 | 155 |
| 2020/21 | 295 | 480 | 215 |
| 2021/22 | 400 | 545 | 275 |
| 2022/23 | 330 | 500 | 240 |
| 2023/24 | 210 | 370 | 180 |
| **2024/25** | **195** | **350** | **175** |

> Los precios de 2024/25 son los precios forward vigentes al momento de la planificación.

### 3. Costos fijos directos (USD/ha)

Estos costos se incurren por hectárea sembrada, independientemente del ingreso. Incluyen semillas, fertilizantes, agroquímicos y labores. Se pagan **antes de la cosecha** con el capital disponible del productor.

| Alternativa | Costo fijo (USD/ha) |
|---|---|
| Trigo / Soja 2da | 560 |
| Maíz | 420 |
| Soja 1ra | 280 |

### 4. Costos variables de comercialización (% del ingreso bruto)

Estos costos son proporcionales al ingreso bruto e incluyen flete, comisiones, impuestos y gastos de acondicionamiento/secada. Se descuentan al momento de la venta.

| Alternativa | Costo variable (% del ingreso bruto) |
|---|---|
| Trigo / Soja 2da | 25% |
| Maíz | 28% |
| Soja 1ra | 23% |

### 5. Restricciones agronómicas, operativas y financieras

- **Capital disponible:** El productor dispone de **USD 250.000** para financiar los costos directos de la campaña (semillas, fertilizantes, agroquímicos y labores). Estos costos se afrontan **antes de la cosecha** y no pueden exceder el capital disponible. Los costos de comercialización, en cambio, se descuentan al momento de la venta.
- Por razones de **rotación y salud del suelo**, al menos el **20%** del campo debe destinarse a un cultivo que incluya gramíneas (trigo/soja 2da o maíz).
- Por capacidad de **maquinaria y logística de siembra**, no se puede sembrar más del **50%** del campo con maíz.

---

## Consigna

> **Nota importante:** Este TP es exigente y entendemos que puede resultar abrumador. No se preocupen: respondan lo que puedan, con las herramientas que tengan (papel, Excel, Python, calculadora), y va a estar bien igual. Lo importante es que intenten razonar el problema.

### Parte A — Modelo y análisis

1. **Formular** un modelo de Programación Lineal que maximice el **margen bruto esperado** del campo para la campaña 2024/25. Utilizar los precios forward 2024/25 y los rendimientos que consideren más apropiados a partir de los datos históricos. La formulación no es obligatoria pero ayuda a ordenar el razonamiento — pueden presentarla como prefieran (texto, fórmulas, pseudocódigo).

2. **Resolver** el modelo y reportar la solución óptima:
   - Hectáreas asignadas a Trigo/Soja 2da (entero, ha)
   - Hectáreas asignadas a Maíz (entero, ha)
   - Hectáreas asignadas a Soja 1ra (entero, ha)
   - Margen bruto total óptimo (entero, USD)

3. **Análisis de sensibilidad:**
   - ¿Cuánto aumenta el margen bruto si se dispone de una hectárea adicional? (entero, USD/ha)
   - ¿Cuánto aumenta el margen bruto si se dispone de un dólar adicional de capital? (entero, USD/USD — redondeado)

### Parte B — Incertidumbre

4. Considerar tres **escenarios de rendimientos** basados en los datos históricos:
   - **Malo**: promedio de las 3 peores campañas
   - **Normal**: promedio de las 9 campañas
   - **Bueno**: promedio de las 3 mejores campañas

   Resolver el modelo para cada escenario y reportar la asignación óptima y el margen bruto en cada caso.

5. Si el productor fuera **averso al riesgo** y quisiera maximizar el margen bruto del **peor escenario** (criterio maximin), resolver el modelo y reportar la asignación y el margen bruto garantizado.

### Parte C — Competencia

La competencia tiene **dos componentes**:

#### C1. Asignación fija

6. Cada grupo debe entregar su asignación definitiva de hectáreas **(números enteros)** para la campaña 2024/25. Completar las variables `HA_TRIGO_SOJA`, `HA_MAIZ` y `HA_SOJA_1RA` en el archivo `estrategia.py`.

   Los rendimientos reales de 2024/25 serán revelados en clase. El grupo cuya asignación genere el **mayor margen bruto real** gana este componente.

#### C2. Función adaptativa

7. Además, cada grupo debe implementar la función `asignar(precio_trigo, precio_soja, precio_maiz)` en el mismo archivo `estrategia.py`. La función recibe tres precios y debe devolver una tupla de tres enteros con las hectáreas a destinar a cada alternativa.

   **Reglas:**
   - Solo se permite importar `pulp` como librería externa
   - La asignación retornada debe respetar **todas las restricciones** del problema
   - Si la función falla o retorna una asignación inválida, se descalifica esa evaluación

   La función será evaluada con **múltiples escenarios de precios** no conocidos de antemano. El grupo cuya función genere el **mayor margen bruto acumulado** en todos los escenarios gana este componente.

---

## Entrega

> **El trabajo es individual.**

Las respuestas se entregan a través del formulario: **[Link al formulario — TBD](#)**

El formulario solicita:
- Resultados numéricos de las Partes A y B (enteros)
- Archivo `estrategia.py` con la asignación fija y la función adaptativa (Parte C)
- Campo libre de comentarios (no evaluado — pueden usarlo para aclaraciones, explicar su enfoque, o lo que quieran)

---

## Datos disponibles

- Datos en formato CSV en la carpeta `data/`
- Template del archivo de entrega: `estrategia.py`
