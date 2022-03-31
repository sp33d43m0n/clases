contexto = {}
contexto = {'nombre': 'Javier', 'edad': 40, 'sexo': 'M'}
contexto['nombre']= 'alejandro'
print(contexto)
contexto['hobbies']=['correr', 'caminar']
print(contexto)
print(contexto['hobbies'])
print(contexto['hobbies'][0])
print(type(contexto))
print(len(contexto))

for key in contexto.keys():
    print(key)

for value in contexto.values():
    print(value)

for key, value in contexto.items():
    print(key,':',value)
    
arr = [1,3,5,7]
arr[0], arr[1] = arr[1], arr[0]
print(arr)

