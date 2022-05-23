import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random

q = []
# znak i liczba ładunków
i=0
while i<10:
    znak = random.randint(-10, 10)
    if znak < 0:
        q.append(-1)
        i+=1
    elif znak > 0:
        q.append(1)
        i+=1
print(q)

axes = [10, 10, 10]

dane_test = np.ones(axes)

alpha = 0.3
colors = np.empty(axes + [4], dtype=np.float32)
colors = [1, 1, 1, alpha]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.voxels(dane_test, facecolors=colors)

for j in range(len(q)):
    x = random.uniform(0, 10)
    y = random.uniform(0, 10)
    z = random.uniform(0, 10)
    if q[j] == -1:
        ax.scatter(x,y,z,c='blue')
    else:
        ax.scatter(x,y,z,c='red')

plt.show()
