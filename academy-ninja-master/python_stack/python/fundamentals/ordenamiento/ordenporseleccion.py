array = [8,2,3,1,10,-2,4]
init = 0 
#encontrar el numero  mas pequeño
for j in range(len(array)-1):
    init=init+1
    for i in range(init,(len(array)-1)):
        if (array[j] > array[i+1]):
            array[j], array[i+1] = array[i+1], array[j]
    
print(array)     


            
