import matplotlib.pyplot as plt
import numpy as np


def psi2(x):
    return ((1/4*np.pi)**(1/4))*(2*(x**2) - 1)*np.exp(-1/2 * x**2)


x = np.arange(-5, 5, 0.0001)
plt.plot(x, psi2(x), 'green', linewidth=2.0, label=r"$\psi_2 (x)$", alpha=0.47)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.title(r"Gráfica para $\psi_2 (x)$")
plt.axis("off")
plt.legend()
plt.grid()
plt.savefig("/home/vikoluna/Apps/PyCharm/graphQutm/imagenes/psi2.png")
plt.show()
