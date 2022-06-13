import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from dataclasses import dataclass, field
from random import randint, uniform, choice

epsilon0 = 8.8541878128e-12
k = 1 / 4 / np.pi / epsilon0


class InfinitePotentalException(Exception):
    pass


class InfiniteElectricFieldException(Exception):
    pass


@dataclass
class Point:
    x: float
    y: float
    z: float


# class Point1:
#     def __init__(self, x:float, y:float, z:float):
#         self.x = x
#         self.y = y
#         self.z = z

@dataclass
class Vector:
    """
    Class implementing basic 3D vector operations
    For a list of magic methods see https://python-course.eu/oop/magic-methods.php
    """
    x: float
    y: float
    z: float
    length: float = field(init=False)
    _dir_x: float = field(init=False)
    _dir_y: float = field(init=False)
    _dir_z: float = field(init=False)
    
    def __post_init__(self):
        self.length = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
        
        if np.all(self.length > 0):
            self._dir_x = self.x / self.length
            self._dir_y = self.y / self.length
            self._dir_z = self.z / self.length
        else:
            self._dir_x = np.NAN
            self._dir_y = np.NAN
            self._dir_z = np.NAN
    
    @property
    def unit_dir_vector(self):
        """Returns a vector of length 1 in the same direction and the vector itself"""
        return Vector(self._dir_x, self._dir_y, self._dir_z)
    
    def __str__(self):
        """Representation for print
        """
        return f"Vector x={self.x}, y={self.y}, z={self.z}. \nLength={self.length}\nUnit vector={self._dir_x}, {self._dir_y}, {self._dir_z}"
    
    def __mul__(self, other):
        """Multiplication. For two vectors returns a dot product, for a vector and number returns vector multiplied by a number
        """
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __add__(self, other):
        """
        Addition of two vectors
        :param other:
        :return:
        """
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __truediv__(self, other):
        """Division of vector by a number
        """
        if np.all(other != 0):
            return Vector(self.x / other, self.y / other, self.z / other)
        else:
            raise ZeroDivisionError
    
    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)


@dataclass
class Charge:
    value: float = field(init=True)
    location: Point = field(init=True)
    sign: int = field(init=False)
    
    def __post_init__(self):
        self.sign = -1 if self.value < 0 else 1
    
    def distance_from_point(self, p: Point):
        return ((p.x - self.location.x) ** 2 + (p.y - self.location.y) ** 2 + (p.z - self.location.z) ** 2) ** 0.5
    
    def distance_from_xyz(self, x, y, z):
        return ((x - self.location.x) ** 2 + (y - self.location.y) ** 2 + (z - self.location.z) ** 2) ** 0.5
    
    def potential(self, p: Point):
        r = self.distance_from_point(p)
        if r == 0:
            raise InfinitePotentalException
        else:
            return k * self.value / r
    
    def potential_xyz(self, x, y, z):
        r = self.distance_from_xyz(x, y, z)
        if np.any(r == 0):
            raise InfinitePotentalException
        else:
            return k * self.value / r
    
    def electric_field(self, p: Point):
        direction = Vector(p.x - self.location.x, p.y - self.location.y, p.z - self.location.z).unit_dir_vector
        r = self.distance_from_point(p)
        if np.any(r == 0):
            raise InfiniteElectricFieldException
        else:
            return direction * k * self.value / self.distance_from_point(p) ** 2
    
    def electric_field_xyz(self, x, y, z):
        direction = Vector(x - self.location.x, y - self.location.y, z - self.location.z).unit_dir_vector
        r = self.distance_from_xyz(x, y, z)
        if np.any(r == 0):
            raise InfiniteElectricFieldException
        else:
            return direction * k * self.value / r ** 2


n = randint(5, 20)
Q = []
for _ in range(n):
    Q.append(Charge(choice([-1, 1]) * uniform(1e-6, 5e-6), Point(uniform(0.5, 10), uniform(0.5, 10), uniform(0.5, 10))))

x = np.linspace(0, 10, 100, endpoint=True)
y = np.linspace(0, 10, 100, endpoint=True)

X, Y = np.meshgrid(x, y)

Z = Q[0].potential_xyz(X, Y, 0)
for q in Q[1:]:
    Z += q.potential_xyz(X, Y, 0)

fig, ax = plt.subplots(constrained_layout=True, figsize=(6, 6))
ax.set_aspect('equal', 'box')
levels = np.linspace(Z.min(), Z.max(), 20)
cp = ax.contourf(X, Y, Z, levels=levels, cmap=cm.coolwarm)
cbar = fig.colorbar(cp)
cbar.ax.set_ylabel('electric potential')
plt.show()
