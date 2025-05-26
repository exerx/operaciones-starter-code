import pytest
from main import Operaciones

def test_suma():
    assert Operaciones.suma(5, 6) == 11, "5 + 6 debería ser 11"
    assert Operaciones.suma(-2, 4) == 2, "-2 + 4 debería ser 2"
    assert Operaciones.suma(0, 0) == 0, "0 + 0 debería ser 0"
