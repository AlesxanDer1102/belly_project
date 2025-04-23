# language: es

Característica: Pruebas de escalabilidad del estómago
  Para garantizar la robustez del sistema
  Como usuario del sistema
  Quiero que funcione correctamente con grandes cantidades

  @stress_test
  Escenario: Comer 1000 pepinos y esperar 10 horas
    Dado que estoy en modo de prueba de escalabilidad
    Y que he comido 1000 pepinos
    Cuando espero 10 horas
    Entonces mi estómago debería gruñir
    Y el sistema responde en menos de 2 segundos

  @stress_test
  Escenario: Comer 5000 pepinos y esperar 24 horas
    Dado que estoy en modo de prueba de escalabilidad
    Y que he comido 5000 pepinos
    Cuando espero 24 horas
    Entonces mi estómago debería gruñir
    Y el sistema responde en menos de 2 segundos
    
  @stress_test @english
  Escenario: Comer 10000 pepinos con tiempo en inglés
    Dado que estoy en modo de prueba de escalabilidad
    Y que he comido 10000 pepinos
    Cuando espero "fifteen hours and thirty minutes"
    Entonces mi estómago debería gruñir
    Y el sistema responde en menos de 2 segundos