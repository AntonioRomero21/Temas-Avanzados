import pytest
from geometry import calcular_area_rectangulo

def test_calcular_area_rectangulo_caso_normal():
    assert calcular_area_rectangulo(5, 10) == 50

def test_calcular_area_rectangulo_base_cero():
    assert calcular_area_rectangulo(0, 10) == 0

def test_calcular_area_rectangulo_altura_cero():
    assert calcular_area_rectangulo(5, 0) == 0

def test_calcular_area_rectangulo_caso_limite():
    assert calcular_area_rectangulo(0, 0) == 0

def test_calcular_area_rectangulo_valores_negativos():
    with pytest.raises(ValueError, match="La base y la altura deben ser mayores o iguales a cero."):
        calcular_area_rectangulo(-5, 10)
    with pytest.raises(ValueError, match="La base y la altura deben ser mayores o iguales a cero."):
        calcular_area_rectangulo(5, -10)