import matplotlib.pyplot as plt
import numpy as np

t_1 = 0
w_1 = np.sqrt(1/(1 + (2*t_1)**2))

t_2 = 0.5
w_2 = np.sqrt(1/(1 + (2*t_2)**2))

t_3 = 2.5
w_3 = np.sqrt(1/(1 + (2*t_3)**2))

t_4 = 10
w_4 = np.sqrt(1/(1 + (2*t_4)**2))

t_5 = 50
w_5 = np.sqrt(1/(1 + (2*t_5)**2))

t_6 = 90
w_6 = np.sqrt(1/(1 + (2*t_6)**2))


def dis1(x):
    return (np.sqrt(2/np.pi))*w_1*(np.exp(-2*(w_1**2)*(x**2)))


def dis2(x):
    return (np.sqrt(2/np.pi))*w_2*(np.exp(-2*(w_2**2)*(x**2)))


def dis3(x):
    return (np.sqrt(2/np.pi))*w_3*(np.exp(-2*(w_3**2)*(x**2)))


def dis4(x):
    return (np.sqrt(2/np.pi))*w_4*(np.exp(-2*(w_4**2)*(x**2)))


def dis5(x):
    return (np.sqrt(2/np.pi))*w_5*(np.exp(-2*(w_5**2)*(x**2)))


def dis6(x):
    return (np.sqrt(2/np.pi))*w_6*(np.exp(-2*(w_6**2)*(x**2)))


x = np.arange(-5, 5, 0.0001)

plt.plot(x, dis1(x), 'green', linewidth=2.0, label=r"$|\Psi(x, 0)|^2$", alpha=0.47)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.title(r"Gráfica de la distribución de probabilidad.")
# plt.axis("off")
plt.legend()
plt.grid()
# plt.savefig("/home/vikoluna/Apps/PyCharm/graphQutm/imagenes/dstyPlt.png")
plt.show()

plt.plot(x, dis2(x), 'orangered', linewidth=2.0, label=r"$|\Psi(x, 0.5)|^2$", alpha=0.47)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.title(r"Gráfica de la distribución de probabilidad.")
# plt.axis("off")
plt.legend()
plt.grid()
# plt.savefig("/home/vikoluna/Apps/PyCharm/graphQutm/imagenes/dstyPlt.png")
plt.show()

plt.plot(x, dis3(x), 'purple', linewidth=2.0, label=r"$|\Psi(x, 2.5)|^2$", alpha=0.47)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.title(r"Gráfica de la distribución de probabilidad.")
# plt.axis("off")
plt.legend()
plt.grid()
# plt.savefig("/home/vikoluna/Apps/PyCharm/graphQutm/imagenes/dstyPlt.png")
plt.show()

plt.plot(x, dis4(x), 'brown', linewidth=2.0, label=r"$|\Psi(x, 10)|^2$", alpha=0.47)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.title(r"Gráfica de la distribución de probabilidad.")
# plt.axis("off")
plt.legend()
plt.grid()
# plt.savefig("/home/vikoluna/Apps/PyCharm/graphQutm/imagenes/dstyPlt.png")
plt.show()

plt.plot(x, dis5(x), 'purple', linewidth=2.0, label=r"$|\Psi(x, 50)|^2$", alpha=0.47)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.title(r"Gráfica de la distribución de probabilidad.")
# plt.axis("off")
plt.legend()
plt.grid()
# plt.savefig("/home/vikoluna/Apps/PyCharm/graphQutm/imagenes/dstyPlt.png")
plt.show()

plt.plot(x, dis6(x), 'pink', linewidth=2.0, label=r"$|\Psi(x, 90)|^2$", alpha=0.47)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.title(r"Gráfica de la distribución de probabilidad.")
# plt.axis("off")
plt.legend()
plt.grid()
# plt.savefig("/home/vikoluna/Apps/PyCharm/graphQutm/imagenes/dstyPlt.png")
plt.show()

plt.plot(x, dis1(x), 'green', linewidth=2.0, label=r"$|\Psi(x, 0)|^2$", alpha=0.47)
plt.plot(x, dis2(x), 'orangered', linewidth=2.0, label=r"$|\Psi(x, 0.5)|^2$", alpha=0.47)
plt.plot(x, dis3(x), 'purple', linewidth=2.0, label=r"$|\Psi(x, 2.5)|^2$", alpha=0.47)
plt.plot(x, dis4(x), 'brown', linewidth=2.0, label=r"$|\Psi(x, 10)|^2$", alpha=0.47)
plt.plot(x, dis5(x), 'purple', linewidth=2.0, label=r"$|\Psi(x, 50)|^2$", alpha=0.47)
plt.plot(x, dis6(x), 'pink', linewidth=2.0, label=r"$|\Psi(x, 90)|^2$", alpha=0.47)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.title(r"Gráfica de la distribución de probabilidad.")
# plt.axis("off")
plt.legend()
plt.grid()
plt.savefig("/home/vikoluna/Apps/PyCharm/graphQutm/imagenes/dstyPlt.png")
plt.show()
