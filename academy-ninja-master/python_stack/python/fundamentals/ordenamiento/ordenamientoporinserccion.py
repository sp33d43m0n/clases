#Ordenamiento por insercción   
array = [8,2,3,1,10,-2,4] 
for i in range(1, (len(array))):
    for k in range(i, -1, -1):
        if array[i] < array[k]:
            array[i], array[k] = array[k], array[i]
            i=i-1 #hacer pregunta con respecto a esta variable i, si es local dentro del if?
print(array)