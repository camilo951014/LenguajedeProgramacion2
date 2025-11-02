from vehiculo import Vehiculo
""" 
Atributo _cc (cilindraje, int).--ok

Implementar impuesto() con la regla:

Si cc ≤ 250 → 5% del precio base; si cc > 250 → 9%.--ok

Sobrescribir ficha() para incluir cilindraje.--ok """

class Moto(Vehiculo):
    def __init__(self,marca,modelo,precio_base,cc):
        super().__init__(marca,modelo,precio_base)
        self._cc = max(1,cc)

    def get_cc(self):
        return self._cc
    
    def ficha(self):
        return f"{super().ficha()}\n Cilindraje: {self._cc}"
    
    def impuesto(self):
        impuesto = super().get_precio_base() * 0.05 if self.get_cc() <= 250 else super().get_precio_base() * 0.09
        return impuesto