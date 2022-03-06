# Cuenta regresiva
def cuenta_Regresiva(num):
        for i in range(num,-1,-1):
            print(i)

cuentatras(7)

# Imprimir y volver
def print_and_return(num1):
    print(num1[0])
    return num1.pop()
    
    
z = print_comeback([1,2])
print(z)

#   first_plus_length

def first_plus_length(z):
    print("a. primer numero es",z[0])
    print("b. Tamano del array es",len(z))
    print("el resultado es a+b", z[0] + len(z))
    
first_plus_length([1,4,2,5,8])

# valores mayores que el segundos 

def values_greather_than_second(t):
    if (len(t) > 2):
        list_ordenada = sorted(t)
        print(list_ordenada)    
        for i in range (0, (len(t))):
            print(t[i],list_ordenada)
            if (t[i] > list_ordenada[1]):
                resultado.append(t[i])
                print(resultado)
    else:
        print("false")

    return(resultado)
        
        
resultado = []
z = values_greather_than_second([1,4,2,5,8])
print(z)

# Esta longitud, este valor

def lengthAndValue(size, value):
    newArr = []
    for i in range(0, size):
        newArr.append(value)
        print(newArr)
    return newArr

print(lengthAndValue(3,2))        


