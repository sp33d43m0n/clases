class MathDojo:

    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for i in nums:
            self.result += i
        print(f"la suma es {self.result}")
        return self
    
    def subtract(self, num, *nums):
        self.result -= num
        for i in nums:
            self.result -= i
        print(f"la resta es {self.result}")
        return self
    
    def endresult(self):
        print(f"El valor de toda la operacion es {self.result}")
        
        
    

# crear una instruccion:
prueba = MathDojo()
# para probar:
prueba.add(2).add(2,5,1).add(3,2,1).subtract(3,2).endresult()	# debe imprimir 11

