from vehiculo import Vehiculo
from automovil import Automovil
from moto import Moto

""" 2 autos (uno de 5 puertas y otro de 4 puertas).--ok

2 motos (una de ≤ 250cc y otra de > 250cc).--ok

Recorrer la lista e imprimir cada vehículo (debe verse ficha + precio final).--ok

Imprimir el total del inventario (suma de precio_final()). """

v1 = Automovil("Subaru","Impreza",240000000,4)
v2 = Automovil("Mini","Cooper",180000000,5)
m1 = Moto("Yamaha","XTZ150",10000000,150)
m2 = Moto("Royal Enflied","Cafe Racer",25000000,450)

lista = [v1,v2,m1,m2]

k=0
for n in lista:
    print(n.ficha())
    k += n.precio_final()

print("EL valor del inventario total es de: "+str(k)+" pesos colombianos") 