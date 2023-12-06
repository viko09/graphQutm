import matplotlib.pyplot as plt
import numpy as np


def psi0(x):
    return ((1/np.pi)**(1/4))*np.exp(-1/2 * x**2)


x = np.arange(-5, 5, 0.0001)
plt.plot(x, psi0(x), 'orangered', linewidth=2.0, label=r"$\psi_0 (x)$", alpha=0.47)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.title(r"Gráfica para $\psi_0 (x)$")
plt.axis("off")
plt.legend()
plt.grid()
plt.savefig("/home/vikoluna/Apps/PyCharm/graphQutm/imagenes/psi0.png")
plt.show()
