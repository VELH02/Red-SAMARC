import numpy as np
import matplotlib.pyplot as plt

# Valores de potencia activa (P) de 0 a 100
P = np.linspace(0, 100, 100)
# Valores de potencia reactiva (Q) en función de P
Q = np.sqrt((100**2) - P**2)  # Ejemplo de potencia aparente constante de 100 VA

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.plot(P, Q, label='Curva PQ', color='blue')
plt.fill_between(P, 0, Q, alpha=0.1, color='blue')

plt.title('Curva PQ en un Sistema Eléctrico')
plt.xlabel('Potencia Activa (P) [W]')
plt.ylabel('Potencia Reactiva (Q) [VAR]')
plt.grid()
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.legend()
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.show()
