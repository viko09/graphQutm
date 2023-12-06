import matplotlib.pyplot as plt
import numpy as np


def psi0(x):
    return ((1/np.pi)**(1/4))*np.exp(-1/2 * x**2)


def psi1(x):
    return ((1/np.pi)**(1/4))*np.sqrt(2)*x*np.exp(-1/2 * x**2)


def psi2(x):
    return ((1/4*np.pi)**(1/4))*(2*(x**2) - 1)*np.exp(-1/2 * x**2)


x = np.arange(-5, 5, 0.0001)
plt.plot(x, psi0(x), 'orangered', linewidth=2.0, label=r"$\psi_0 (x)$", alpha=0.47)
plt.plot(x, psi1(x), 'blue', linewidth=2.0, label=r"$\psi_1 (x)$", alpha=0.47)
plt.plot(x, psi2(x), 'green', linewidth=2.0, label=r"$\psi_2 (x)$", alpha=0.47)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.title(r"Gráfica de los tres estados superpuestos.")
plt.axis("off")
plt.legend()
plt.grid()
plt.savefig("/home/vikoluna/Apps/PyCharm/graphQutm/imagenes/psi012.png")
plt.show()
