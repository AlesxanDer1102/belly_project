from src.belly import Belly
import time

def before_scenario(context, scenario):
    # Inicializar el belly según si es un test de stress o no
    if 'stress_test' in scenario.tags:
        context.belly = Belly(modo_stress=True)
    else:
        context.belly = Belly()
    
    # Inicializar otras variables de contexto
    context.exception = None
    context.execution_times = {}  # Para pruebas de rendimiento

def before_step(context, step):
    # Registrar el tiempo antes de cada paso
    if step.step_type == "when" and step.name.startswith("espero"):
        context.step_start_time = time.time()

def after_step(context, step):
    # Registrar el tiempo después del paso relevante
    if step.step_type == "when" and step.name.startswith("espero"):
        end_time = time.time()
        context.execution_times['wait_step'] = end_time - context.step_start_time
        print(f"Tiempo de espera procesado en: {context.execution_times['wait_step']:.6f} segundos")

"""
# features/environment.py

from unittest.mock import MagicMock
from src.belly import Belly
import time

def before_scenario(context, scenario):
    # Creamos un mock del reloj para poder simular tiempo
    fake_clock = MagicMock()
    # Valor inicial del reloj
    initial_time = 10000.0
    fake_clock.return_value = initial_time
    
    context.current_time = initial_time

    def advance_time(hours):
        # Convierte horas a segundos
        context.current_time += (hours * 3600)
        fake_clock.return_value = context.current_time

    context.advance_time = advance_time

    # Instanciamos Belly con el servicio de reloj mockeado
    context.belly = Belly(clock_service=fake_clock)
    context.exception = None

def after_scenario(context, scenario):
    # Limpieza al final del escenario
    pass

"""
