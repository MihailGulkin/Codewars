def differentiate(poly):
    if poly.replace('-', '') == 'x':
        return poly.replace('x', '1')
    if 'x' not in poly:
        return '0'
    if '^' not in poly:
        poly = poly.split('x')
        return str(int(poly[0]) * 1)
    poly = poly.split('x^')
    if poly[0].replace('-', '') != '':
        return f'{int(poly[0]) * int(poly[1])}x{f"^{int(poly[1]) - 1}" if int(poly[1]) - 1 != 1 else ""}'
    poly[0] = poly[0] + '1'
    return f'{int(poly[0]) * int(poly[1])}x{f"^{int(poly[1]) - 1}" if int(poly[1]) - 1 != 1 else ""}'
