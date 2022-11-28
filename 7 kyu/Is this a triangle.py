def is_triangle(a, b, c):
    return sum(sorted([a, b, c])[:2])> sorted([a,b,c])[-1]