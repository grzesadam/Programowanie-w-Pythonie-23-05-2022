import random
import matplotlib.pyplot as plt
import numpy as np
from scipy import constants

# dimensions
x = 10
y = 10
z = 10
n = 10
k = 1 / (4 * constants.pi * constants.epsilon_0)
zi = 5
size=100
numbers_point=10
# function to generate an electrical charge
def electric_charge(n):
    ox = np.random.uniform(0, x, n)
    oy = np.random.uniform(0, y, n)
    oz = np.random.uniform(0, z, n)
    q = np.random.choice([-1, 1],size=n) * np.random.uniform(1e-9, 100e-9,n)


    return ox, oy, oz, q


ox, oy, oz, q = electric_charge(n)
# graf which represents the electric charge in 3d
def plot_3d(ox, oy, oz,q):
    # Calculate an outlier limit (I chose 2 Standard deviations from the mean)

    kcolors = ['red' if q[i] > 0 else 'blue' for i in range(n) ]

    ax = plt.axes(projection='3d')
    ax.scatter(ox, oy, oz, c=kcolors)

    ax.set_xlabel("Axis X, m")

    ax.set_ylabel("Axis Y, m")

    ax.set_zlabel("Axis Z, m")

    plt.show()


plot_3d(ox, oy, oz,q)

def mesh(ox, oy, zi, oz,size):
    xlist = np.linspace(0, 10, size)
    ylist = np.linspace(0, 10,size)


    X, Y = np.meshgrid(xlist, ylist)

    for i in range(n):
        Z=(ox[i]-X)**2+(oy[i]-Y)**2+(oz[i]-zi)**2
    for j in range(n):
        V=+k*q[i]/Z**0.5
    fig, ax = plt.subplots(1, 1)
    cp = ax.contourf(X, Y, V)
    fig.colorbar(cp)  # Add a colorbar to a plot
    ax.set_title('Potencial')

    plt.show()


mesh(ox, oy, zi, oz,size)



def lines_field(ox,oy,oz,q):
    ax = plt.figure().add_subplot(projection='3d')

    # Make the grid
    x, y, z = np.meshgrid(np.arange(0, 10, 1),
                          np.arange(0, 10, 1),
                          np.arange(0, 10, 1))

    # Make the direction data for the arrows
    for i in range(n):
        x1=(ox[i]-x)**2
        y1=(oy[i]-y)**2
        z1=(oz[i]-z)**2
    for j in range(n):

        u = k*q[j]/x1
        v = k*q[j]/y1
        w = k*q[j]/z1
    ax.quiver(x, y, z, u, v, w, normalize=True)
    ax.set_title('Lines of electric field')

    plt.show()
lines_field(ox,oy,oz,q)

def single_vector(x,y,z,numbers_point,ox,oy,oz,q):
    ax = plt.figure().add_subplot(projection='3d')
    px= np.random.uniform(0, x, numbers_point)
    py = np.random.uniform(0, y, numbers_point)
    pz = np.random.uniform(0, z, numbers_point)
    x2, y2, z2 = np.meshgrid(px,py,pz)

    x3=(ox-x2)**2
    y3=(oy-y2)**2
    z3=(oz-z2)**2
    for j in range(numbers_point):

        u = k*q[j]/x3
        v = k*q[j]/y3
        w = k*q[j]/z3
    ax.quiver(x, y, z, u, v, w, normalize=True)
    ax.set_title('Lines of electric field')
    plt.show()


single_vector(x,y,z,numbers_point,ox,oy,oz,q)