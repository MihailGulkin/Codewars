def solve_for_x(equation):
    equation = equation.replace('=', '==').replace(' ', '')
    x = '-1000'
    first_x = equation[:]
    second_x = equation[:]
    while True:
        first_x = first_x.replace('x', x)
        if eval(first_x):
            return int(x)
        first_x = second_x[:]
        x = str(int(x) + 1)
