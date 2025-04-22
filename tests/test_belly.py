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

