# 1. Tamaño grande: dada una lista, escriba una función que cambie todos los números positivos de la lista a "big".
# Ejemplo: biggie_size ([- 1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores son ahora [-1, "big", "big", -5]

def biggie_size(array):
    for i in range(0, len(array)):
        if (array[i] < 0):
            array[i] = "big"
    return array

array= [- 1, 3, 5, -5]
print(biggie_size(array))

# 2. Contar positivos : dada una lista de números, cree una función para reemplazar el último valor con el número de valores positivos. (Tenga en cuenta que cero no se considera un número positivo).
# Ejemplo: count_positives([- 1, 1, 1,1 ]) cambia la lista original a [-1, 1, 1, 3] y la devuelve
# Ejemplo: count_positives([1, 6, -4, -2, -7, -2]) cambia la lista a [1, 6, -4, -2, -7, 2] y la devuelve

def count_positives(array):
    cont = 0
    for x in range(0, len(array)):
        if (array[x] > 0):
            cont = cont + 1
            print(cont)
    
        array[len(array)-1] = cont
    return array

array = [- 1, 1, 1,1 ]
salida = count_positives(array)
print(salida)

# Suma total : crea una función que toma una lista y devuelve la suma de todos los valores de la matriz.
# Ejemplo: sum_total ([1,2,3,4]) debería devolver 10
# Ejemplo: sum_total ([6,3, -2]) debería devolver 7

def sum_total(array):
    suma = 0
    for i in range(len(array)):
        suma = suma + array[i]
    return suma

print(sum_total([6,3,-2])) 

# Promedio : crea una función que toma una lista y devuelve el promedio de todos los valores.
# Ejemplo: el promedio ([1,2,3,4]) debería devolver 2.5

def sum_total(array):
    suma = 0
    for i in range(len(array)):
        suma = suma + array[i]
    return suma/len(array)

print(sum_total([6,3,-2])) 

# Longitud : crea una función que toma una lista y devuelve la longitud de la lista.
# Ejemplo: la longitud ([37,2,1, -9]) debería devolver 4
# Ejemplo: longitud ([]) debería devolver 0

def longitud(array):
    contador = 0
    for item in array:
        contador += 1
    return contador

print(longitud([37,2,1,-9]))

# 6. Mínimo : crea una función que tome una lista de números y devuelva el valor mínimo en la lista. Si la lista está vacía, haga que la función devuelva False.
# Ejemplo: mínimo ([37,2,1, -9]) debería devolver -9
# Ejemplo: mínimo ([]) debería devolver False


def minimo(array):
    min = array[0]
    if (len(array) == 0):
        return "false"
    for item in range(0, (len(array))):
        if (min <= array[item]):
            min = min
        else:
            min = array[item]
    return min

print(minimo([37,2,42, -9]))

# 7. Máximo : crea una función que toma una lista y devuelve el valor máximo en la matriz. Si la lista está vacía, haga que la función devuelva False.
# Ejemplo: máximo ([37,2,1, -9]) debería devolver 37
# Ejemplo: máximo ([]) debería devolver False

def maximo(array):
    max = array[0]
    if (len(array) == 0):
        return "false"
    for item in range(0, (len(array))):
        if (max >= array[item]):
            max = max
        else:
            max = array[item]
    return max

print(maximo([37,2,42, -9]))

# 8. Análisis final : crea una función que tome una lista y devuelva un diccionario que tenga la suma total, promedio, mínimo, máximo y longitud de la lista.
# Ejemplo: ultimate_analysis ([37,2,1, -9]) debería devolver {'total': 31, 'promedio': 7.75, 'minimo': -9, 'maximo': 37, 'longitud': 4}

def ultimate_analisys(array):
    
    def maximo(array):
        max = array[0]
        if (len(array) == 0):
            return "false"
        for item in range(0, (len(array))):
            if (max >= array[item]):
                max = max
            else:
                max = array[item]
        return max
    
    def minimo(array):
        min = array[0]
        if (len(array) == 0):
            return "false"
        for item in range(0, (len(array))):
            if (min <= array[item]):
                min = min
            else:
                min = array[item]
        return min
    
    def longitud(array):
        contador = 0
        for item in array:
            contador += 1
        return contador

    def sum_total(array):
        suma = 0
        for i in range(len(array)):
            suma = suma + array[i]
        promedio = suma/len(array)
        return suma, promedio
    
    maximo_dict=maximo(array)
    minimo_dict=minimo(array)
    longitud_dict=longitud(array)
    sumatotal_dict=sum_total(array)
    
    my_dict = {
        "el_maximo" : maximo(array),
        "el_minimo" : minimo(array),
        "la_longitud" : longitud(array),
        "la_suma" : sum_total(array)[0],
        "el_promedio" :  sum_total(array)[1]           
    }
    

    return  my_dict

array = [37,2,1, -9]
print(ultimate_analisys(array))


# # 10. Lista inversa : crea una función que tome una lista y la devuelva con los valores invertidos. Haz esto sin crear una segunda lista. (Se sabe que este desafío aparece durante las entrevistas técnicas básicas).
# # Ejemplo: reverse_list ([37,2,1, -9]) debería devolver [-9,1,2,37]

        
def reverse_list(array):
    left= 1 
    right= 1 
    div = round(len(array)/2)
    for i in range(0, div):     
        array.insert(left,array[len(array)-right])
        array.insert(len(array)-left,array[right-1])
        array.pop(len(array)-right)
        array.pop(left-1)
        left = left+1
        right = right+1
    return array


array = [0, 3, -1, 4, 1, 7, 9]  
print(reverse_list(array))   



