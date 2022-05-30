from math import atan2, sin, cos, sqrt
import matplotlib.pyplot as plt
import numpy as np

WIDTH = 10
ROW = 10
COL = 10

cube = np.zeros((ROW, COL, WIDTH))


class electric_charge:
    k = 8.9 * 10 ** 9

    def __init__(self, x, y, z, q, mass):
        self.x = x
        self.y = y
        self.z = z
        self.q = q
        self.mass = mass
        self.orbit_x = [self.x]
        self.orbit_y = [self.y]
        self.orbit_z = [self.z]
        self.vel_x = 0
        self.vel_y = 0
        self.vel_z = 0
        if self.q > 0:
            self.color = 'blue'
        else:
            self.color = 'red'

    def attraction(self, other):
        other_x, other_y, other_z = other.x, other.y, other.z
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance_z = other_z - self.z
        distance = sqrt(distance_x ** 2 + distance_y ** 2 + distance_z ** 2)
        force = self.k * self.q * other.q / distance ** 2
        theta_xy = atan2(distance_x, distance_y)
        theta_xz = atan2(distance_x, distance_z)
        force_x = force * sin(theta_xy)
        force_y = force * cos(theta_xy)
        force_z = force * cos(theta_xz)
        return force_x, force_y, force_z

    def update_pos(self, charges, N):
        for i in range(N):
            for charge in charges:
                total_fx = 0
                total_fy = 0
                total_fz = 0
                if self == charge:
                    continue

                fx, fy, fz = self.attraction(charge)
                total_fx += fx
                total_fy += fy
                total_fz += fz

                self.vel_x += (fx * 0.1) / self.mass
                self.vel_x += (fy * 0.1) / self.mass
                self.vel_x += (fz * 0.1) / self.mass

                self.x += self.vel_x * 0.1
                self.y += self.vel_y * 0.1
                self.z += self.vel_z * 0.1
                self.orbit_x.append(self.orbit_x)
                self.orbit_y.append(self.orbit_y)
                self.orbit_z.append(self.orbit_z)


Q1 = electric_charge(1, 1, 1, 1, 1000)
Q2 = electric_charge(9, 9, 9, -1, 1000)
alfa = electric_charge(0, 0, 0, 1, 1)
alfa.vel_x = 10
charges = [Q1, Q2, alfa]
for charge in charges:
    if charge.q > 0:
        cube[charge.x][charge.y][charge.z] = 1
    elif charge.q < 0:
        cube[charge.x][charge.y][charge.z] = -1

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
charge: electric_charge
for charge in charges:
    for i in range(1000):
        charge.update_pos(charges, 1)
        ax.scatter(charge.x, charge.y, charge.z, c='black')
    ax.scatter(charge.x, charge.y, charge.z, c=charge.color)
plt.show()
