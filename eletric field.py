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
size=10


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


def mesh_plus(ox, oy, zi, oz,size):
    xlist = np.linspace(0, 10, size)
    ylist = np.linspace(0, 10,size )


    rx0= []
    ry0= []
    for i in range(size):
        r1 = (xlist[i] - ox[0]) ** 2
        r2 = (ylist[i] - oy[0]) ** 2
        rx0 = np.append(rx0, r1)
        ry0 = np.append(ry0, r2)

    return rx0,ry0

rx0,ry0= mesh_plus(ox, oy, zi, oz,size)



def mesh_minus(ox1, oy1, zi, oz1,size):
    x1list = np.linspace(0, 10, size)
    y1list = np.linspace(0, 10, size)
    rx=[]
    ry=[]
    for i in range(size):
        r_min1=(x1list[i]-ox1[0])**2
        r_min2=(y1list[i]-oy1[0])**2
        rx=np.append(rx,r_min1)
        ry = np.append(ry, r_min2)


    return rx,ry

rx,ry = mesh_minus(ox1, oy1, zi, oz1,size)



def contour(rx0,ry0,rx,ry,zi,k,q1):
    rx9=np.concatenate((rx0,rx))
    ry9=np.concatenate((ry0,ry))
    rz=(zi-oz[0])**2
    X,Y=np.meshgrid(rx9,ry9)
    Z=k*q1[0]/((X+Y+rz)**0.5)
    fig, ax = plt.subplots(1, 1)
    cp = ax.contourf(X, Y, Z)
    fig.colorbar(cp)  # Add a colorbar to a plot
    ax.set_title('Filled Contours Plot')
    # ax.set_xlabel('x (cm)')
    ax.set_ylabel('y (cm)')
    plt.show()


contour(rx0, ry0, rx, ry, zi,k,q1)


