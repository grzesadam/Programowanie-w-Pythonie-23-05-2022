
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
size = 100
numbers_point = 10
alfa=2*constants.e
v=np.array((10,0,0))
m=6.64*1e-27

# function to generate an electrical charge
def electric_charge(n):
    ox = np.random.uniform(0, x, n)
    oy = np.random.uniform(0, y, n)
    oz = np.random.uniform(0, z, n)
    q = np.random.choice([-1, 1], size=n) * np.random.uniform(1e-9, 100e-9, n)

    return ox, oy, oz, q


ox, oy, oz, q = electric_charge(n)


# graf which represents the electric charge in 3d
def plot_3d(ox, oy, oz, q):
    # Calculate an outlier limit (I chose 2 Standard deviations from the mean)

    kcolors = ['red' if q[i] > 0 else 'blue' for i in range(n)]

    ax = plt.axes(projection='3d')
    ax.scatter(ox, oy, oz, c=kcolors)

    ax.set_xlabel("Axis X, m")

    ax.set_ylabel("Axis Y, m")

    ax.set_zlabel("Axis Z, m")

    plt.show()


plot_3d(ox, oy, oz, q)


def mesh(ox, oy, zi, oz, size):
    xlist = np.linspace(0, 10, size)
    ylist = np.linspace(0, 10, size)
    fig, ax = plt.subplots(1, 1)
    X, Y = np.meshgrid(xlist, ylist)

    for i in range(n):
        Z = (ox[i] - X) ** 2 + (oy[i] - Y) ** 2 + (oz[i] - zi) ** 2
        if i > 0:
            V += k * q[i] / Z ** 0.5
        else:
            V = k * q[i] / Z ** 0.5

    cp = ax.contourf(X, Y, V, cmap='jet')
    fig.colorbar(cp)  # Add a colorbar to a plot
    ax.set_title('Potential')

    plt.show()

mesh(ox, oy, zi, oz, size)


def lines_field(ox, oy, oz, q):
    ax = plt.figure().add_subplot(projection='3d')

     # Make the grid
    x, y, z = np.meshgrid(np.arange(0, 10, 1),
                           np.arange(0, 10, 1),
                           np.arange(0, 10, 1))
    rx = [x - i for i in ox]
    ry = [y - i for i in oy]
    rz = [z - i for i in oz]

    r = [(rx[i] ** 2 + ry[i] ** 2 + rz[i] ** 2) ** 0.5 for i in range(n)]

    wersor1 = [rx[i] / r[i] for i in range(n)]
    wersor2 = [ry[i] / r[i] for i in range(n)]
    wersor3 = [rz[i] / r[i] for i in range(n)]
    e = [k * q[j] / r[j] ** 2 for j in range(n)]
    ex  = [e[i] * wersor1[i] for i in range(n)]
    ey = [e[i] * wersor2[i] for i in range(n)]
    ez = [e[i] * wersor3[i] for i in range(n)]

    arx=[sum(x) for x in zip(*ex)]
    ary = [sum(x) for x in zip(*ey)]
    arz = [sum(x) for x in zip(*ez)]
    ax.quiver(x, y, z, arx, ary, arz, normalize=True)
    ax.set_title('Vectors')
    ax.set_xlim3d(0, 10)
    ax.set_ylim3d(0, 10)
    ax.set_zlim3d(0, 10)
    plt.show()
lines_field(ox, oy, oz, q)


def single_vector( n, numbers_point, ox, oy, oz, q,k):

    ax = plt.figure().add_subplot(projection='3d')
    px = np.random.uniform(0, x, numbers_point)
    py = np.random.uniform(0, y, numbers_point)
    pz = np.random.uniform(0, z, numbers_point)

    rx = [px - i for i in ox]
    ry = [py - i for i in oy]
    rz = [pz - i for i in oz]

    r = [(rx[i] ** 2 + ry[i] ** 2 + rz[i] ** 2) ** 0.5 for i in range(n)]

    wersor1 = [rx[i] / r[i] for i in range(n)]
    wersor2 = [ry[i] / r[i] for i in range(n)]
    wersor3 = [rz[i] / r[i] for i in range(n)]
    e = [k * q[j] / r[j] ** 2 for j in range(n)]
    ex  = [e[i] * wersor1[i] for i in range(n)]
    ey = [e[i] * wersor2[i] for i in range(n)]
    ez = [e[i] * wersor3[i] for i in range(n)]

    arx=[sum(x) for x in zip(*ex)]
    ary = [sum(x) for x in zip(*ey)]
    arz = [sum(x) for x in zip(*ez)]




    ax.quiver(px, py, pz, arx, ary, arz, normalize=True)
    ax.set_title('Vectors')
    ax.set_xlim3d(0, 10)
    ax.set_ylim3d(0, 10)
    ax.set_zlim3d(0, 10)
    plt.show()





single_vector( n, numbers_point, ox, oy, oz, q,k)

def alpha_particle(v,alfa,k,q,ox,oy,oz,m):
    ax = plt.figure().add_subplot(projection='3d')
    cx=5
    cy=5
    cz=0
# #     centre_of_the_wall2 = np.array((0, 5, 5))
# #     centre_of_the_wall3 = np.array((5, 0, 5)# #     centre_of_the_wall=np.random.choice(centre_of_the_wall1,centre_of_the_wall2,centre_of_the_wall3)

    rx=cx-ox
    ry=cy-oy
    rz=cz-oz
    r=(rx**2+ry**2+rz**2)**0.5
    wersor1=rx/r
    wersor2=ry/r
    wersor3=rz/r

    for i in q:
        a=k*i*alfa/(m*r**2)
    ax=a*wersor1
    ay=a*wersor2
    az=a*wersor3
    ax.quiver(cx, cy, cz, ax, ay, az)
    ax.set_title('Vectors')
    ax.set_xlim3d(0, 10)
    ax.set_ylim3d(0, 10)
    ax.set_zlim3d(0, 10)
    plt.show()
alpha_particle(v, alfa,k,q,ox,oy,oz,m)