import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

WIDTH = 10
ROW = 10
COL = 10

cube = np.zeros((ROW, COL, WIDTH))


class electric_charge:
    def __init__(self, x, y, z, q):
        self.x = x
        self.y = y
        self.z = z
        self.q = q
        if self.q > 0:
            self.color = 'blue'
        else:
            self.color = 'red'


Q1 = electric_charge(1, 1, 1, 1)
Q2 = electric_charge(9, 9, 9, -1)
charges = [Q1, Q2]
for charge in charges:
    if charge.q > 0:
        cube[charge.x][charge.y][charge.z] = 1
    elif charge.q < 0:
        cube[charge.x][charge.y][charge.z] = -1

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
charge: electric_charge
for charge in charges:
    ax.scatter(charge.x, charge.y, charge.z, c=charge.color)
plt.show()
