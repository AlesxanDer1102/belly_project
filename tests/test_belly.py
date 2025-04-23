import pytest
import time
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

def test_cantidad_excesiva_error():
    """Prueba que se lanza un error cuando se intenta comer más de 100 pepinos"""
    belly = Belly()
    with pytest.raises(ValueError) as excinfo:
        belly.comer(101)
    assert "100 pepinos" in str(excinfo.value)
    
def test_cantidades_limite():
    """Prueba comportamiento con valores límite"""
    belly = Belly()
    
    # 100 pepinos es el máximo permitido (debe funcionar)
    try:
        belly.comer(100)
    except ValueError:
        pytest.fail("No debería fallar con exactamente 100 pepinos")
    
    # Reiniciar para probar el valor 101
    belly.reset()
    
    # 101 pepinos debe lanzar error
    with pytest.raises(ValueError) as excinfo:
        belly.comer(101)
    assert "100 pepinos" in str(excinfo.value)


def test_rendimiento_grandes_cantidades():
    """Prueba que el sistema maneja grandes cantidades de pepinos eficientemente"""
    start_time = time.time()
    
    belly = Belly(modo_stress=True)
    
    # Probar con una cantidad grande
    belly.comer(10000)
    belly.esperar(50)
    
    # Verificar que funciona correctamente
    assert belly.esta_gruñendo() is True
    
    # Verificar tiempo de ejecución
    elapsed_time = time.time() - start_time
    assert elapsed_time < 1, f"La prueba tardó {elapsed_time:.2f} segundos, demasiado tiempo"
    
    print(f"Prueba de rendimiento completada en {elapsed_time:.4f} segundos")