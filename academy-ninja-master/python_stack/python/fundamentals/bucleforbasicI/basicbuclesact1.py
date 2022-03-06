#  Enteros de 0 a 150
for i in range(0, 151):
    print(i)
    
# Multiplos de 5
for i in range(5, 10001, 5):
    print(i)

# si es multiplo de 5 imprima coding, si es multiplo de 10 imprima coding dojo
for i in range(1, 101):
    if (i % 5) == 0:
        if (i % 10) != 0:
            print("coding")
        elif (i % 10) ==0:
            print("coding dojo")
    else:
        print(i)
        
# suma de 0 a 500K de numeros impares
suma = 0
for i in range(1,500001,2):
    suma = suma + i
    
print(suma)

#cuenta regresiva restando 4 desde 2018 a 0
for i in range(2018, 0, -4):
    print(i)
    

#imprimir los Numero que son multiplos de Mult
lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum, highNum+1):
    if (i % mult == 0):
        print(i)

#bonus detectar si un numero es primo de 0 1000

down = 2
up = 1001
vector = []
primo = []

for i in range(down, up):
    for k in range (1, i+1):
        if (i %  k == 0):
            vector.append(i)

    if (vector.count(i) <= 2):
        primo.append(i)

print("los numeros primos son:", primo)   


        
         

  

    
    
        
        
        
        
        

    
