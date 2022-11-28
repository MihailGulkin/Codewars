from math import sqrt


class Vector:
    def __init__(self, *args):
        if len(args) == 1:
            self.x = args[0][0]
            self.y = args[0][1]
            self.z = args[0][2]
        else:
            self.x = args[0]
            self.y = args[1]
            self.z = args[2]

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def cross(self, other):
        return Vector(self.y * other.z - self.z * other.y,
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def to_tuple(self):
        return (self.x, self.y, self.z)

    @property
    def magnitude(self):
        return sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def __repr__(self):
        return f'<{self.x}, {self.y}, {self.z}>'
