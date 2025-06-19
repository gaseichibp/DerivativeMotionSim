import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Define a variável simbólica do tempo
t = sp.symbols('t')

# Função posição s(t) (exemplo fornecido no enunciado)
s_t = t**3 - 6*t**2 + 9*t

# Derivações
v_t = sp.diff(s_t, t)
a_t = sp.diff(v_t, t)

# Converte funções simbólicas para funções numéricas
s_func = sp.lambdify(t, s_t, 'numpy')
v_func = sp.lambdify(t, v_t, 'numpy')
a_func = sp.lambdify(t, a_t, 'numpy')

# Intervalo de tempo
t_values = np.linspace(0, 10, 400)

# Avaliação das funções
s_values = s_func(t_values)
v_values = v_func(t_values)
a_values = a_func(t_values)

# Plotagem dos gráficos
plt.figure(figsize=(12, 8))

# Posição
plt.subplot(3, 1, 1)
plt.plot(t_values, s_values, 'b', label='s(t) - Posição')
plt.title('Função Posição s(t)')
plt.xlabel('Tempo t')
plt.ylabel('s(t)')
plt.grid(True)
plt.legend()

# Velocidade
plt.subplot(3, 1, 2)
plt.plot(t_values, v_values, 'g', label='v(t) - Velocidade')
plt.title('Função Velocidade v(t)')
plt.xlabel('Tempo t')
plt.ylabel('v(t)')
plt.grid(True)
plt.legend()

# Aceleração
plt.subplot(3, 1, 3)
plt.plot(t_values, a_values, 'r', label='a(t) - Aceleração')
plt.title('Função Aceleração a(t)')
plt.xlabel('Tempo t')
plt.ylabel('a(t)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

# Impressão simbólica
print("Função posição s(t):", s_t)
print("Função velocidade v(t):", v_t)
print("Função aceleração a(t):", a_t)
