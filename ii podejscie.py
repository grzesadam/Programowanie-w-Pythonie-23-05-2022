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
    ox = np.random.uniform(0, x, n)
    oy = np.random.uniform(0, y, n)
    oz = np.random.uniform(0, z, n)
    q = random.choice([-1, 1]) * np.random.uniform(1e-9, 100e-9,n)

    print(q)
    return ox, oy, oz, q


ox, oy, oz, q = electric_charge(n)
# graf which represents the electric charge in 3d
def plot_3d(ox, oy, oz):
    # Calculate an outlier limit (I chose 2 Standard deviations from the mean)
    q_bar = np.mean(q)

    # Generate a colour vector
    kcolors = ['red' if (q_bar) > 0 else 'blue' ]

    ax = plt.axes(projection='3d')
    ax.scatter(ox, oy, oz, c=kcolors)

    ax.set_xlabel("Axis X, m")

    ax.set_ylabel("Axis Y, m")

    ax.set_zlabel("Axis Z, m")

    plt.show()


plot_3d(ox, oy, oz)

def mesh(ox, oy, zi, oz,size):
    xlist = np.linspace(0, 10, size)
    ylist = np.linspace(0, 10,size )


    rx= []
    ry= []
    rz=[]
    for i in range(size):
        for b,c in zip(ox,oy):
            r1 = (xlist[i] - b) ** 2
            r2 = (ylist[i] - c) ** 2
            rx = np.append(rx, r1)
            ry = np.append(ry, r2)
    for s in oz:
        r3=(zi-s)**2
        rz=np.append(rz,r3)
    print(rx)
    return rx,ry,rz


rx,ry,rz= mesh(ox, oy, zi, oz,size)

def contour(rx,ry,rz,k,q,n):
    X,Y=np.meshgrid(rx,ry)
    Z=k*q[0]/((X+Y+rz[0])**0.5)
    fig, ax = plt.subplots(1, 1)
    cp = ax.contourf(X, Y, Z)
    fig.colorbar(cp)  # Add a colorbar to a plot
    plt.show()


contour(rx, ry,rz,k,q,n)
