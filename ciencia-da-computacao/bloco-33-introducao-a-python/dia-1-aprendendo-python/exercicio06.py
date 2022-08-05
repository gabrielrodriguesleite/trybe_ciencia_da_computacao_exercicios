def trigangulate(a, b, c):
    if a == b and b == c and c == a:
        return "Equilátero"
    if a != b and b != c and c != a:
        return "Escaleno"
    if a + b == c or b + c == a or a + c == b:
        return "Isóceles"