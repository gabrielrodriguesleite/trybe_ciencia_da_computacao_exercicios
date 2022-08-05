def triangleType(a, b, c):
    if a == b and b == c and c == a:
        return "Equilátero."
    if a != b and b != c and c != a:
        return "Escaleno."
    if a + b == c or b + c == a or a + c == b:
        return "Isóceles."
    if a + b > c:
        return "Triangulo."
    return "Não é triangulo."


def test_triangleType():
    assert triangleType(3, 3, 3) == "Equilátero."
    assert triangleType(3, 2, 1) == "Escaleno."
    assert triangleType(6, 6, 12) == "Isóceles."
    assert triangleType(6, 6, 10) == "Triangulo."
