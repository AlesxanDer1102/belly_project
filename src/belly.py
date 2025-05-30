class Belly:
    def __init__(self,modo_stress=False):
        self.pepinos_comidos = 0.0
        self.tiempo_esperado = 0.0
        self.modo_stress = modo_stress 

    def reset(self):
        self.pepinos_comidos = 0
        self.tiempo_esperado = 0

    def comer(self, pepinos):
        # Comprobar que la cantidad de que pepinos no sea negativo
        if pepinos < 0:
            raise ValueError("No se puede comer una cantidad negativa de pepinos")
        
        # Comprobar que no sobrepase la cantidad permitida
        if not self.modo_stress and pepinos > 100:
            raise ValueError("No se puede comer más de 100 pepinos, es peligroso para la salud")
        
        print(f"He comido {pepinos} pepinos.")
        self.pepinos_comidos += pepinos

    def esperar(self, tiempo_en_horas):
        if tiempo_en_horas > 0:
            print(f"He esperado {tiempo_en_horas} horas.")
            self.tiempo_esperado += tiempo_en_horas

    def esta_gruñendo(self):
        # Verificar que ambas condiciones se cumplan correctamente:
        # Se han esperado al menos 1.5 horas Y se han comido más de 10 pepinos
        if self.tiempo_esperado >= 1.5 and self.pepinos_comidos > 10:
            return True
        return False
