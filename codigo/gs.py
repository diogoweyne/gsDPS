import numpy as np
import matplotlib.pyplot as plt

# DADOS
semanas = np.array([1, 2, 3, 4, 5])
volume  = np.array([43, 58, 79, 104, 138])

# FUNÇÃO LINEAR: f(x) = ax + b
a, b = np.polyfit(semanas, volume, 1)
print(f"Função Linear: f(x) = {a:.2f}x + {b:.2f}")

# FUNÇÃO EXPONENCIAL: f(x) = A * e^(kx)
log_volume = np.log(volume)
k, logA = np.polyfit(semanas, log_volume, 1)
A = np.exp(logA)
print(f"Função Exponencial: f(x) = {A:.2f} * e^({k:.4f}x)")

# PREVISÃO EM 6 MESES (semana 26)
print(f"\nPrevisão semana 26 (linear):      {a*26 + b:.1f} kg")
print(f"Previsão semana 26 (exponencial): {A * np.exp(k*26):.1f} kg")

# GRÁFICO 1: Dados + Modelos
x = np.linspace(1, 26, 200)

plt.figure(figsize=(8, 5))
plt.scatter(semanas, volume, color='red', zorder=5, label='Dados reais')
plt.plot(x, a*x + b,            'b--', label=f'Linear: {a:.1f}x + {b:.1f}')
plt.plot(x, A * np.exp(k * x), 'g-',  label=f'Exponencial: {A:.1f}·e^({k:.3f}x)')
plt.axhline(300, color='orange', linestyle=':', label='Limite crítico (300 kg)')
plt.xlabel('Semana')
plt.ylabel('Volume de lixo (kg)')
plt.title('Descarte Irregular de Resíduos - Projeção 6 meses')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('grafico1.png', dpi=150)
plt.show()

# GRÁFICO 2: Variação semanal
variacao = np.diff(volume)
semanas_var = [2, 3, 4, 5]

plt.figure(figsize=(7, 4))
plt.bar(semanas_var, variacao, color='steelblue', edgecolor='black')
for i, v in zip(semanas_var, variacao):
    plt.text(i, v + 0.5, f'+{v} kg', ha='center', fontweight='bold')
plt.xlabel('Semana')
plt.ylabel('Aumento de volume (kg)')
plt.title('Variação Semanal do Volume de Lixo')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('grafico2.png', dpi=150)
plt.show()
