from vehiculo import Vehiculo
""" Atributo _puertas (int).

Implementar impuesto() con la regla:

8% del precio base; si tiene 5 puertas, restar 1% del precio base a ese impuesto.--ok

Sobrescribir ficha() para incluir puertas. ---ok"""
class Automovil(Vehiculo):
    def __init__(self,marca,modelo,precio_base,puertas):
        super().__init__(marca,modelo,precio_base)
        self._puertas = max(1,puertas)

    def get_puertas(self):
        return self._puertas
    
    def ficha(self):
        return f"{super().ficha()}\n Numero de puertas: {self._puertas}"
    
    def impuesto(self):
        impuesto = super().get_precio_base() * 0.08 
        descuento = 0 if self.get_puertas() != 5 else super().get_precio_base() * 0.01
        return impuesto - descuento
    

