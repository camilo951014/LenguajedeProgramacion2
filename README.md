# Documentación del sistema de inventario de vehículos

> **Objetivo**: Este documento describe la arquitectura, reglas de negocio y uso del pequeño sistema en Python que modela vehículos (autos y motos) y calcula su precio final con impuestos, además de imprimir un inventario y su total.

---

## Estructura del proyecto

```
├─ vehiculo.py   # Clase abstracta base Vehiculo
├─ automovil.py  # Subclase Automovil con lógica de puertas
├─ moto.py       # Subclase Moto con lógica de cilindraje
└─ main.py       # Script de ejemplo: crea instancias, imprime fichas y total
```

---

## Conceptos clave y API

### 1) `Vehiculo` (clase base abstracta)

* **Atributos (encapsulados)**: `__marca`, `__modelo`, `__precio_base` (se valida para que sea ≥ 1).
* **Getters**: `get_marca()`, `get_modelo()`, `get_precio_base()`.
* **Métodos abstractos**: `impuesto(self) -> float` (cada subclase define cómo se calcula).
* **Métodos concretos**:

  * `precio_final(self) -> float`: `precio_base + impuesto()`.
  * `ficha(self) -> str`: string legible con marca, modelo y **precio final**.
  * `__str__(self)`: representación breve.

**Contrato esperado**: las subclases deben devolver en `impuesto()` **un monto** (no un porcentaje), para que `precio_final = precio_base + impuesto` tenga sentido aritmético.

---

### 2) `Automovil` (subclase)

* **Atributo**: `_puertas` (mínimo 1).
* **Regla de impuesto**:

  * Base: **8%** del `precio_base`.
  * Ajuste: si **tiene 5 puertas**, **se resta** un **1%** adicional del `precio_base` al impuesto calculado (es decir, el impuesto neto es `0.08*precio_base - 0.01*precio_base`).
* **`ficha()`**: extiende la de `Vehiculo` agregando el número de puertas.

---

### 3) `Moto` (subclase)

* **Atributo**: `_cc` (cilindraje, mínimo 1).
* **Regla de impuesto**:

  * Si `cc ≤ 250` → **5%** del `precio_base`.
  * Si `cc > 250` → **9%** del `precio_base`.
* **`ficha()`**: extiende la de `Vehiculo` agregando el cilindraje.

---

## Flujo de ejecución (`main.py`)

1. Se crean 4 vehículos de ejemplo:

   * 2 automóviles: uno de **4** puertas y otro de **5** puertas.
   * 2 motos: una de **150cc** y otra de **450cc**.
2. Se guardan en una lista y se recorre imprimiendo la **ficha** de cada uno (marca, modelo, precio final y dato específico: puertas/cc).
3. Se acumula el `precio_final()` de cada vehículo y se imprime el **total del inventario**.

---

## Ejecución local

Requisitos: Python 3.9+ (recomendado).

```bash
python main.py
```

El script no requiere dependencias externas.

---

## **Salida esperada** (con el código tal como está)

La siguiente salida fue obtenida ejecutando `main.py` con los archivos provistos:

```
Marca: Subaru,
Modelo: Impreza,
Precio Final: 259200000.0
 Numero de puertas: 4
Marca: Mini,
Modelo: Cooper,
Precio Final: 192600000.0
 Numero de puertas: 5
Marca: Yamaha,
Modelo: XTZ150,
Precio Final: 10500000.0
 Cilindraje: 150
Marca: Royal Enflied,
Modelo: Cafe Racer,
Precio Final: 27250000.0
 Cilindraje: 450
EL valor del inventario total es de: 489550000.0 pesos colombianos

```
## Validaciones incluidas

* `precio_base` mínimo **1** (si se pasa 0 o negativo, se ajusta a 1).
* `puertas` y `cc` mínimo **1**.

---

## Glosario

* **Precio base**: Precio antes de impuestos.
* **Impuesto**: Monto adicional calculado según reglas específicas por tipo de vehículo.
* **Precio final**: `precio_base + impuesto`.

---

## Licencia y autoría

Este material es de uso didáctico; ajuste la sección de licencia y autoría según sus necesidades de curso o proyecto.
