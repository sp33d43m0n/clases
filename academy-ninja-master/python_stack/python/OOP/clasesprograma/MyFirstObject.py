class Auto:
    def __init__(self, color ="Negro",
                motor ="V10",
                chasis = "f1",
                cantidadRuedas = 2,
                direccion = "mecanica"):
        self.color = color
        self.motor =  motor
        self.chasis = chasis
        self.cantidadRuedas = cantidadRuedas 
        self.direccion = direccion
        self.kilometraje = 0
    
    def __str__(self):
       return f"El auto {self.color} tiene el motor {self.motor}"

    def acelerar(self, kilometraje = 5):
        self.kilometraje += kilometraje
        
    def mostarAuto(self):
        print(f"El auto {self.color} es de segunda. Tiene el Motor {self.motor} Y tiene: {self.kilometraje} Kms")
        

auto1 = Auto()
auto2 = Auto("azul","v8","veloster",4,"Manual")
auto2 = Auto(chasis="Craisler") 
print(auto1.motor)
print(auto2.color)
auto1.cantidadRuedas = 24
print(auto1.cantidadRuedas)
print(auto2.chasis)
auto1.acelerar()
auto1.acelerar()
auto1.acelerar()
auto1.mostarAuto()

auto_javi = Auto(color="blanco", motor="v10", direccion="manual", cantidadRuedas=2)
auto_javi.acelerar()
auto_javi.acelerar()
auto_javi.acelerar()
auto_javi.acelerar(20)
auto_javi.mostarAuto()
