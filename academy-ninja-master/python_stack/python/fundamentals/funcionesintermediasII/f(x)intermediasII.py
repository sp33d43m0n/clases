x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Cambia el valor 10 en x a 15. Una vez que haya terminado, x ahora debería ser [[5,2,3], [15,8,9]].
x[1][0] = 15
print(x)

# Cambia el apellido del primer alumno de 'Jordan' a 'Bryan
students[0]['last_name'] = 'Brian'
print(students)

# En el directorio sports_directory, cambia 'Messi' a 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

#Cambia el valor 20 en y a 30
z[0]['y'] = 30
print(z)

# Crea una función iterateDictionary(some_list)que, dada una lista de diccionarios, la función recorra cada diccionario de la lista e imprime cada clave y el valor asociado

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


def iterateDictionary(students):
    for i in range(len(students)):
        print('firstname -',students[i]['first_name'],',','lastname - ',students[i]['last_name'])
    
iterateDictionary(students)

# Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, la función imprima el valor almacenado en esa clave para cada diccionario

def iterateDictionary2(key_name='', some_list=students):
    if (key_name == "first_name"):
        for i in range (0,(len(some_list))):
            print(students[i]['first_name'])
                
    elif (key_name == "last_name"):
        for i in range (0,(len(some_list))):
            print(students[i]['last_name'])
            

iterateDictionary2('first_name')
iterateDictionary2('last_name')

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(dojo):
    print('#LOCATIONS',len(dojo['locations']))
    for x in dojo['locations']:
        print(x, end = "\n")

    print('#INSTRUCTORS',len(dojo['instructors']))
    for x in dojo['instructors']:
        print(x, end = "\n")
    
print(printInfo(dojo))
    
    