import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass, field
import math

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
        
        if self.length >= 0:
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
        return f"Vector x={self.x}, y={self.y}, z={self.y}. \nLength={self.length}\nUnit vector={self._dir_x}, {self._dir_y}, {self._dir_z}"
    
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
        if isinstance(other, (int, float)):
            if other != 0:
                return Vector(self.x / other, self.y / other, self.z / other)
            else:
                raise ZeroDivisionError
        else:
            return np.NAN
    
    def __neg(self):
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
    
    def potential(self, p: Point):
        r = self.distance_from_point(p)
        if r == 0:
            raise InfinitePotentalException
        return k * self.value / r
    
    def electric_field(self, p: Point):
        direction = Vector(p.x - self.location.x, p.y - self.location.y, p.z - self.location.z).unit_dir_vector
        r = self.distance_from_point(p)
        if r == 0:
            raise InfiniteElectricFieldException
        else:
            return direction * k * self.value / self.distance_from_point(p) ** 2


Q1 = Charge(2.4e-6, Point(2, 3, 4))
Q1 = Charge(-2.4e-6, Point(4, 5, 6))

print(Q1.potential(Point(3, 3, 4)))
print(Q1.distance_from_point(Point(3, 3, 4)))
print(Q1.electric_field(Point(2, 10, 16)))

# v1 = Vector(3, 3, 3)
# print(v1)
# print(v1 * 2)
# print(2 * v1)
#
# v2 = Vector(4, 5, 7)
#
# print(v1 * v2)
# print(v1 + v2)
# print(v2 + v1)


# print(v1.unit_dir_vector)
