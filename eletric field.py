import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

#dimensions
x=10
y=10
z=10
number=random.randrange(10000)

def electric_charge(number):
    ox=np.random.uniform(0,x,number)
    oy=np.random.uniform(0,y,number)
    oz=np.random.uniform(0,z,number)
    q=np.random.uniform(-10,10,number)
    return ox,oy,oz,q
ox,oy,ox,oz=electric_charge(number)
def plot_3d(ox,oy,oz):
    fig = plt.figure()

    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(ox, oy, oz)

    plt.show()

plot_3d(ox,oy,oz)