
from random import randint, uniform

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

WIDTH = 10
ROW = 10
COL = 10
epsilon0 = 8.8541878128e-12
k = 1 / 4 / np.pi / epsilon0

cube = np.zeros((ROW, COL, WIDTH))


class electric_charge:
    def __init__(self, x, y, z, q):
        self.x = x
        self.y = y
        self.z = z
        self.q = q
        self.vel_x = 0
        self.vel_y = 0
        self.vel_z = 0
        if self.q > 0:
            self.color = 'blue'
        else:
            self.color = 'red'

    def distance(self, other):
        other_x, other_y, other_z = other.x, other.y, other.z
        return np.sqrt((other_x - self.x) ** 2 + (other_y - self.y) ** 2 + (other_z - self.z) ** 2)

    def distance_from_point(self, x, y, z):
        return np.sqrt((x - self.x) ** 2 + (y - self.y) ** 2 + (z - self.z) ** 2)

    def calculate_potential(self, charge):
        r = self.distance(charge)
        return k * self.q / r

    def calculate_potential_from_point(self, x, y, z):
        r = self.distance_from_point(x, y, z)
        return k * self.q / r

    def length_of_vector(self, x, y, z):
        E = k * self.q/self.distance_from_point(x, y, z) ** 2


    # def attraction(self, other):
    #     force = k * self.q * other.q / other.distance ** 2
    #     theta_xy = atan2(distance_x, distance_y)
    #     theta_xz = atan2(distance_x, distance_z)
    #     force_x = force * sin(theta_xy)
    #     force_y = force * cos(theta_xy)
    #     force_z = force * cos(theta_xz)
    #     return force_x, force_y, force_z


n = randint(2, 5)
charges = []
for i in range(n):
    charges.append(electric_charge(randint(0, 10), randint(0, 10), randint(0, 10), uniform(1e-6, 5e-6)))
# for charge in charges:
#     if charge.q > 0:
#         cube[charge.x][charge.y][charge.z] = 1
#     elif charge.q < 0:
#         cube[charge.x][charge.y][charge.z] = -1

# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# charge: electric_charge
# for charge in charges:
#     for i in range(1000):
#         charge.update_pos(charges, 1)
#         ax.scatter(charge.x, charge.y, charge.z, c='black')
#     ax.scatter(charge.x, charge.y, charge.z, c=charge.color)
#     print(charge.x)
# plt.show()


x_list = np.linspace(0, 10, 100)
y_list = np.linspace(0, 10, 100)

X, Y = np.meshgrid(x_list, y_list)
Z = charges[0].calculate_potential_from_point(X, Y, 0)
for charge in charges[1:]:
    Z += charge.calculate_potential_from_point(X, Y, 0)
fig, ax = plt.subplots(1, 1)
ax.set_aspect('equal', 'box')
levels = np.linspace(Z.min(), Z.max(), 10)
cp = ax.contourf(X, Y, Z, levels=levels, cmap=cm.autumn)
fig.colorbar(cp)  # Add a colorbar to a plot
ax.set_title('Potential')
ax.set_xlabel('x (cm)')
ax.set_ylabel('y (cm)')
plt.show()

print(f'number of charges:{n}')
for charge in charges:
    print(f'x:{charge.x}, y:{charge.y}, z:{charge.y}')