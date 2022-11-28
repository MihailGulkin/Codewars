from itertools import count


def is_triangle_number(number):
    if type(number) != int:
        return False
    for i in count():
        triangle = int(0.5 * i * (i + 1))
        if triangle == number:
            return True
        if triangle > number:
            return False
