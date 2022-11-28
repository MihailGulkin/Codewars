from math import sqrt


class Vector:
    def __init__(self, vec):
        self.vector = vec

    def add(self, other):
        if len(self.vector) != len(other.vector):
            raise ('Ошибка')
        mass = []
        for index, ele in enumerate(self.vector):
            mass.append(other.vector[index] + ele)
        return Vector(mass)

    def subtract(self, other):
        if len(self.vector) != len(other.vector):
            raise ('Ошибка')
        new_vector = []
        for index, ele in enumerate(self.vector):
            new_vector.append(ele - other.vector[index])
        return Vector(new_vector)

    def dot(self, other):
        if len(self.vector) != len(other.vector):
            raise ('Ошибка')
        answer = 0
        for index, ele in enumerate(self.vector):
            answer += (other.vector[index] * ele)
        return answer

    def norm(self):
        answer = 0
        for ele in self.vector:
            answer += (ele * ele)
        return sqrt(answer)

    def toString(self):
        return str(self)

    def __str__(self):
        return str(tuple(self.vector)).replace(' ', '')

    def equals(self, other):
        return self == other

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.vector == other.vector
        else:
            return self.vector == other
