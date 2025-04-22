import pytest
from src.belly import Belly

def test_gruñir_si_comido_muchos_pepinos():
    belly = Belly()
    belly.comer(15)
    belly.esperar(2)
    assert belly.esta_gruñendo() is True


def test_no_gruñir_si_pocos_pepinos():
    belly = Belly()
    belly.comer(10)
    belly.esperar(2)
    assert belly.esta_gruñendo() is False

def test_manejo_cantidad_fraccionaria():
    belly = Belly()
    belly.comer(10.5)
    belly.esperar(1.5)
    assert belly.esta_gruñendo() is True

def test_cantidad_negativa_error():
    belly = Belly()
    with pytest.raises(ValueError) as excinfo:
        belly.comer(-2)
    assert "negativa" in str(excinfo.value)

def test_validar_errores_siempre_detectados():
    belly = Belly()
    try:
        belly.comer(-0.1)
        pytest.fail("Se esperaba una excepción por valor negativo pero no ocurrió")
    except ValueError:
        pass