def sum_triangular_numbers(n):
    return sum(0.5 * i * (i + 1) for i in range(1, n  + 1)) if n > 1 else 0