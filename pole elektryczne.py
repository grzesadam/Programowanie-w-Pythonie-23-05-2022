import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import random

axes = [10, 10, 10]

dane_test = np.ones(axes)

alpha = 0.3
colors = np.empty(axes + [4], dtype=np.float32)
colors = [1, 1, 1, alpha]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.voxels(dane_test, facecolors=colors)

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

for j in range(len(q)):
    x = (random.uniform(0, 10))
    y = (random.uniform(0, 10))
    z = (random.uniform(0, 10))
    wspolrzedne.append((x, y, z))
    if q[j] < 0:
        ax.scatter(x, y, z, c='blue')
    else:
        ax.scatter(x, y, z, c='red')
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

# fig = plt.figure(figsize=plt.figaspect(2.))
# fig.suptitle('Rozmieszczenie ładunków w przestrzeni i izolinie potencjału elektrycznego')
# ax = fig.add_subplot(2, 1, 1, projection="3d")

X, Y = np.meshgrid(np.linspace(0, 10, 100, endpoint=True), np.linspace(0, 10, 100, endpoint=True))

Z = q[0] * k / ((X - wspolrzedne[0][0]) ** 2 + (Y - wspolrzedne[0][1]) ** 2+(0 - wspolrzedne[0][2]) ** 2) ** 0.5
for i, Q in enumerate(q[1:]):
    Z += Q * k / ((X - wspolrzedne[i][0]) ** 2 + (Y - wspolrzedne[i][1]) ** 2+(0 - wspolrzedne[i][2]) ** 2) ** 0.5

fig, ax = plt.subplots(constrained_layout=True, figsize=(6, 6))
ax.set_aspect('equal', 'box')
levels = np.linspace(Z.min(), Z.max(), 20)
cp = ax.contourf(X, Y, Z, levels=levels, cmap=cm.coolwarm)
cbar = fig.colorbar(cp)
cbar.ax.set_ylabel('electric potential')
# ax2 = fig.add_subplot(1,2,1,projection="3d")
# for o in range (len(q)):
#     for x,y,z in wspolrzedne:
#         if q[o] < 0:
#             ax.scatter(x, y, z, c='blue')
#         else:
#             ax.scatter(x, y, z, c='red')

plt.show()
