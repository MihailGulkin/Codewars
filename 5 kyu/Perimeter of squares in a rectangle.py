def perimeter(n):
    a = 0
    b = 1
    answer = 0
    for i in range(n):
        a, b = b, a + b
        answer += b
    return (4 * answer) + 4