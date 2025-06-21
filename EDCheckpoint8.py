import numpy as np

# Parámetros
T_amb = 27
T0 = 30
k = -0.405465
h = 0.2
t_final = 1.0

# Derivada para método de Euler
def f(T, t):
    return k * (T - T_amb)

# Solución analítica por separación de variables:
# T(t) = T_amb + (T0 - T_amb) * e^(kt)
def T_exacta(t):
    return T_amb + 3 * np.exp(k * t)

# Método de Euler
t_valores = np.arange(0, t_final + h, h)
T_euler = [T0]
for i in range(1, len(t_valores)):
    T_anterior = T_euler[-1]
    T_nueva = T_anterior + h * f(T_anterior, t_valores[i-1])
    T_euler.append(T_nueva)

# Solución exacta
T_exacto = [T_exacta(t) for t in t_valores]

# Mostrar tabla comparativa
print(" t     Euler     Exacta")
for t, Te, Tex in zip(t_valores, T_euler, T_exacto):
    print(f"{t:.1f}   {Te:.4f}   {Tex:.4f}")