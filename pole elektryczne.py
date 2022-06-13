import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import random

q = []
i = 0
Z = 2

while i < 10:
    znak = random.choice([-1, 1])
    if znak < 0:
        q.append(-1 * (random.uniform(9e-9, 10e-9)))
        i += 1
    elif znak > 0:
        q.append(1 * random.uniform(9e-9, 10e-9))
        i += 1
print("q", q)

wspolrzedne = []
x_ujemne = []
y_ujemne = []
z_ujemne = []

x_dodatnie = []
y_dodatnie = []
z_dodatnie = []
for j in range(len(q)):
    x = (random.uniform(0, 10))
    y = (random.uniform(0, 10))
    z = (random.uniform(0, 10))
    wspolrzedne.append((x, y, z))
    if q[j] < 0:
        x_ujemne.append(x)
        y_ujemne.append(y)
        z_ujemne.append(z)
    else:
        x_dodatnie.append(x)
        y_dodatnie.append(y)
        z_dodatnie.append(z)
print(wspolrzedne)

k = 9 * 10 ** 9


def potential():
    plane = np.zeros((10, 10))
    Vc = 0
    for l in wspolrzedne:
        for m in range(0, 10):
            for n in range(0, 10):
                for L in q:
                    r = np.sqrt((l[0] - m) ** 2 + (l[1] - n) ** 2 + (l[2] ** 2))
                    V = (k * L) / r
                    Vc += V
                    plane[[m], [n]] += Vc
    return plane


print(potential())


X, Y = np.meshgrid(np.linspace(0, 10, 100, endpoint=True), np.linspace(0, 10, 100, endpoint=True))

Z = q[0] * k / ((X - wspolrzedne[0][0]) ** 2 + (Y - wspolrzedne[0][1]) ** 2 + (0 - wspolrzedne[0][2]) ** 2) ** 0.5
for i, Q in enumerate(q[1:]):
    Z += Q * k / ((X - wspolrzedne[i][0]) ** 2 + (Y - wspolrzedne[i][1]) ** 2 + (0 - wspolrzedne[i][2]) ** 2) ** 0.5


fig, ax = plt.subplots(1, 2, constrained_layout=True, figsize=(8, 4))
ax[1].set_aspect('equal', 'box')
levels = np.linspace(Z.min(), Z.max(), 20)
cp = ax[1].contourf(X, Y, Z, levels=levels, cmap=cm.spring)
cbar = fig.colorbar(cp)
cbar.ax.set_ylabel('electric potential')
ax[0] = fig.add_subplot(1, 2, 1, projection="3d")
ax[0].scatter(x_ujemne, y_ujemne, z_ujemne, color="blue")
ax[0].scatter(x_dodatnie, y_dodatnie, z_dodatnie, color="red")
ax[0].set_title("Rozmieszczenie ładunków")


plt.show()
