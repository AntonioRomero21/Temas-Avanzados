def calcular_area_rectangulo(base, altura):
    if base < 0 or altura < 0:
        raise ValueError("La base y la altura deben ser mayores o iguales a cero.")
    return base * altura