import random
import matplotlib.pyplot as plt
import numpy as np
from scipy import constants

# dimensions
x = 10
y = 10
z = 10
n = 2
k = 1 / (4 * constants.pi * constants.epsilon_0)
zi = 5


# function to generate an electrical charge
def electric_charge(n):
    number = random.randrange(n)
    ox = np.random.uniform(0, x, number)
    oy = np.random.uniform(0, y, number)
    oz = np.random.uniform(0, z, number)
    q = np.random.uniform(0, 10, number)

    ox1 = np.random.uniform(0, x, n - number)
    oy1 = np.random.uniform(0, y, n - number)
    oz1 = np.random.uniform(0, z, n - number)
    q1 = np.random.uniform(-10, 0, n - number)

    return ox, oy, oz, q, ox1, oy1, oz1, q1


ox, oy, oz, q, ox1, oy1, oz1, q1 = electric_charge(n)


# graf which represents the electric charge in 3d
def plot_3d(ox, oy, oz, ox1, oy1, oz1):
    ax = plt.axes(projection='3d')
    ax.scatter(ox, oy, oz, c='red')
    ax.scatter(ox1, oy1, oz1, c='blue')
    ax.set_xlabel("Axis X, m")

    ax.set_ylabel("Axis Y, m")

    ax.set_zlabel("Axis Z, m")

    plt.show()


plot_3d(ox, oy, oz, ox1, oy1, oz1)


def mesh_plus(ox, oy, zi, oz):
    xlist = np.linspace(0, 10, len(ox))
    ylist = np.linspace(0, 10, len(ox))
    print(xlist)
    r1=np.subtract(xlist,ox)
    r2=(ylist-oy)**2
    r3 = (zi - oz) ** 2
    print(r1)


r1 = mesh_plus(ox, oy, zi, oz)
r2 = mesh_plus(ox, oy, zi, oz)
r3 = mesh_plus(ox, oy, zi, oz)


def mesh_minus(ox1, oy1, zi, oz1):
    x1list = np.linspace(0, 10, len(ox1))
    y1list = np.linspace(0, 10, len(ox1))
    r_min1 = (x1list - ox1) ** 2
    r_min2 = (y1list - oy1) ** 2
    r_min3 = (zi - oz1) ** 2
    return r_min1,r_min2,r_min3

r_min1 = mesh_minus(ox1, oy1, zi, oz1)
r_min2 = mesh_minus(ox1, oy1, zi, oz1)
r_min3 = mesh_minus(ox1, oy1, zi, oz1)


# def contour(r_min1, r_min2, r_min3, r1, r2, r3):
#     # rx = np.array([r1, r_min1])
#     # ry = np.array([r2, r_min2])
#     # rz = np.array([r3, r_min3])
#     # print(rx)
#
#
# contour(r_min1, r_min2, r_min3, r1, r2, r3)
