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
size=100

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
    ylist = np.linspace(0, 10,size)


    X, Y = np.meshgrid(xlist, ylist)
    i = [1, 1, 1]
    j = [9, 1, 1]
    for c in enumerate(q):
        Z = k*c/((-X)**2+(oy-Y)**2+(oz-zi)**2)**0.5
    Z1=sum(Z)
    fig, ax = plt.subplots(1, 1)
    cp = ax.contourf(X, Y, Z1)
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
    u = k*q[0]/x**2
    v = k*q[0]/y**2
    w = k*q[0]/z**2
    ax.quiver(x, y, z, u, v, w, normalize=True)

    plt.show()
lines_field(ox,oy,oz,q)