# Enfriamiento de un cuerpo — Caso Forense

Este proyecto implementa los métodos de euler y separación de variables para resolver una ecuación diferencial sacada de un caso forense mediante el **modelo de enfriamiento de Newton**. El objetivo del problema es determinar el momento aproximado de la muerte de una persona, basándose en mediciones reales de temperatura tomadas por un forense.

## Planteamiento del problema

> La policía encuentra el cuerpo de una profesora de ecuaciones diferenciales. El forense llega al mediodía y mide la temperatura corporal en **30 °C**. Una hora después, la temperatura ha bajado a **29 °C**. La temperatura ambiente es constante a **27 °C**. Se asume que la temperatura inicial del cuerpo al morir fue de **37 °C**.

Utilizando estos datos, se modela la temperatura del cuerpo con la ley de enfriamiento de Newton, descrita por la ecuación diferencial:

$$
\frac{dT}{dt} = -k(T - T_{\text{amb}})
$$


Donde:

- T(t): Temperatura del cuerpo en el tiempo t
- T_amb = 27°C: Temperatura ambiente
- k: Constante de enfriamiento
- T(0) = 30°C: Temperatura al llegar el forense

## Objetivos

- Resolver analíticamente la ecuación diferencial con separación de variables.
- Aproximar la solución numéricamente usando el **método de Euler**.
- Comparar ambos resultados.

## Contenido

- `enfriamiento.py`: Contiene el código principal que resuelve el problema de forma analítica y numérica.
- Se utiliza la librería `numpy` para cálculos matemáticos.

## Cómo ejecutar

1. Asegúrate de tener Python instalado.
2. Instala las dependencias (solo `numpy`):

```bash
pip install numpy
```

3. Ejecuta el script:

```bash
python enfriamiento.py
```

Esto imprimirá una tabla comparativa entre el método numérico (Euler) y el método de separación de variables en el intervalo [0,1]:

```
 t     Euler     Exacta
0.0   30.0000   30.0000
0.2   29.1892   29.1884
0.4   28.5027   28.4995
...
```

## Métodos utilizados

- **SSolución analítica**: Derivada por separación de variables, fórmula exacta:  
T(t) = T_amb + (T₀ - T_amb) * exp(-k * t)



- **Método de Euler**: Método numérico paso a paso para aproximar soluciones diferenciales.

## Constante de enfriamiento

La constante k ≈ -0.405465 fue determinada usando los datos de temperatura a los 0 y 1 horas, resolviendo la ecuación de Newton hacia atrás.

## Solución exacta del problema

El valor t que da a conocer la hora de muerte de la profesora es -2.97, el cual nos indica que murió a las 09:02:00 am.

