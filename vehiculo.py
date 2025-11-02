from abc import ABC, abstractmethod

""" Clase abstracta Vehiculo (padre) – vehiculo.py

Atributos “encapsulados” (Pythonic): _marca, _modelo, _precio_base.--ok

Constructor con validación (precio_base > 0).---ok

Propiedades de solo lectura: marca, modelo, precio_base.---ok

Uso de abc.ABC y @abstractmethod para definir impuesto(self) -> float.--okok

Método precio_final(self) -> float = precio_base + impuesto().--okok

Método ficha(self) -> str y __str__ legible.---ok """

class Vehiculo(ABC):
    def __init__(self,marca,modelo,precio_base):
        self.__marca = marca
        self.__modelo = modelo
        self.__precio_base = max(1,precio_base)

    def get_marca(self):
        return self.__marca
    
    def get_modelo(self):
        return self.__modelo
    
    def get_precio_base(self):
        return self.__precio_base

    @abstractmethod
    def impuesto(self):
        pass
    
    def precio_final(self):
        precio_final = self.get_precio_base() + self.impuesto()
        return precio_final

    def ficha(self) -> str:
        return f"Marca: {self.__marca},\nModelo: {self.__modelo},\nPrecio Final: {self.precio_final()}"

    def __str__(self):
        return f"{self.__marca},\n{self.__modelo},\n{self.__precio_base}"









    
