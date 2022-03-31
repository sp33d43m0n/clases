# Push al frente
# Dada una matriz y un valor adicional, inserta este valor al principio de la matriz. 
# Haz esto sin utilizar ningún método de matriz incorporado.

numbers = [1, 2, 3]
numbers[len(numbers): ] = [4]
print(numbers)
numbers = numbers + [5]
print(numbers)

# Pop al frente
# Dada una matriz, elimina y devuelve el valor al principio de la matriz. Haz esto sin utilizar ningún método de matriz incorporado, excepto pop().

numbers_end = [7, 8, 9]
numbers_end[:0] = [6]
print(numbers_end) 
numbers_end = [5] + numbers_end
print(numbers_end)

# Insertar en
# Dado una matriz, índice y valor adicional, inserta el valor en la matriz en el índice dado. Haz esto sin utilizar métodos de matriz integrados. Puedes pensar en pushFront(arr, val) como equivalente a insertAt(arr, 0, val).

numbers_index = [1,2,3,4,5]
numbers_index[3:4] = [0]
n = 0
num = 20
long = len(numbers_index)
print(numbers_index)
numbers_index = numbers_index[0:n] + [num] + numbers_index[n:long]
print(numbers_index)

# Eliminar en
# Dada una matriz y un índice en una matriz, elimina y devuelve el valor de la matriz en ese índice. Haz esto sin usar métodos de matriz integrados, excepto pop(). Piensa en popFront(arr) como equivalente a removeAt(arr, 0).
numbers_del = [5,6,7,8,9]
n = 2
long = len(numbers_del)
suma=0
# numbers_del = numbers_del[0:n] + [for x in numbers_del: suma=x+suma] + numbers_Del[n:long]
for x in numbers_del: 
    suma=x+suma
numbers_del = numbers_del[0:n] + [suma] + numbers_del[n+1:long]
print(numbers_del)

# Pares de intercambio
# Intercambia posiciones de pares sucesivos de los valores de una matriz dada. Si la longitud es impar, no cambies el elemento final. Para [1,2,3,4], devuelve [2,1,4,3]. Por ejemplo, cambia la entrada ["Brendan", verdadero, 42] a [verdadero, "Brendan", 42]. Al igual que con todos los desafíos de arreglos, hazlo sin utilizar ningún método de arreglo incorporado.

matriz = [1,2,3,4,5]
longstatus0=len(matriz)
for i in range(0, len(matriz), 2):
    matriz[len(matriz): ] =  matriz[i+1], matriz[i]
    print(f'este es el valor {i}',matriz)

matriz=matriz[longstatus0:]
print(f'valor final', matriz)

    


# matriz[long-1],matriz[long] = matriz[0], matriz[1] 
# if long % 2 != 0:
#     long = long-1
    
# for key,val in matriz.items():
    
    
    
print(matriz) 





