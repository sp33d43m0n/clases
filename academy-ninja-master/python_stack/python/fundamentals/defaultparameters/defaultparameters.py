import random
def randInt(min='' ,max='' ):
    if (not min and not max):
        num = random.random()*100
        print('empty',num)
        return num
    elif (min != '' and not max):
        num = random.random()*((min-100)+100)
        print('empty minimo',num)
        return num
    elif (not min and max != ''):
        num = random.random()*max
        print('empty maximo',num)
        return num
    elif (max < 0 and min != ''):
        num = random.random()*((max-min)+min)
        print('El maximo menor a cero',num)
        return num
    elif (min > max):
        print('El valor minimo es mayor que el maximo')
        return 'false'
    else:
        num = random.random()*((min-max)+max)
        print('entre min y max',num)
        return num

print('campos vacios',randInt())
print('solo minimo', randInt(20))
print('solo maximo', randInt(max=70))
print('lod dos', randInt(min=10,max=80))
print('Error minimo mayor que maximo', randInt(min=80,max=10))
print('Maximo menor a cero', randInt(min=10,max=-20))



#BONUS II: Una función que juegue al Loto
import random
#primera balota
def loteriadecolombia():
    for i in range(0, round(random.random()*20)):
        balotanum1 = round(random.randint(0,10))
    for x in range(0, round(random.random()*10)):
        balotanum2 = round(random.randint(0,10))
    for y in range(0, round(random.random()*30)):
        balotanum3 = round(random.randint(0,10))
    return [balotanum1, balotanum2, balotanum3]

resultados=loteriadecolombia()
print('el feliz ganador es:',resultados[0],'-',resultados[1],'-',resultados[2])


