# 1. TAREA: imprimir "Hola mundo"
print( "hola mundo" )
# 2. imprimir "Hola Noelle!" con el nombre en una variable
name = "Javier"
print( "hola", name )	# con una coma
print( "hola" + name )	# con un +
# 3. imprimir "Hola 42!" con un numero en una variable
number = 7
print( "mi numero favorito es", number,"!" )	# con una coma
print("mi numero favorito es" + number)
# print(  "Hola"+ name + "!")	# con un + - !Este debería darnos un error!
# 4. imprimir "Me encanta comer sushi and pizza." con los alimentos en variables
fave_food1 = "sushi"
fave_food2 = "spaguetti"
print( "Me encanta comer {} and {}".format(fave_food1, fave_food2) ) # con .format()
print( f"Me encanta comer {fave_food1} y {fave_food2}") # con una cadena f

# **************Bonus ***********
number = 7
print(  "Mi numero favorito es" + str(number) + "!")


texto = "/mi nombre es javier, mi nombres era de un cantante, me gusta mi nombre/"
print(texto.count("nombre")) # Cuantas veces se repite un elemento
print(texto.find("de")) #  posicion del string donde empieza la palabra buscada
print(texto.rfind("/")) #  ultima posicion del string donde se encuentra por ultima vez la palabra buscada
print(texto.index("nombre"))  #  posicion del string donde empieza la palabra buscada
print(texto.startswith("/")) #la frase empieza con = true de lo contrario false
print(texto.endswith("nombre/")) #la frase termina con = true de lo contrario false
print("445".isdecimal()) #solo numeros decimales
print("abc".islower()) #son minusculas = true
print("hola mundo".isspace()) #contiene espacion = true
print("CaSa BlANCA".lower()) #pasa a minusculas *importante para formularios*
print("hola mundo cruel    ".strip()) #remueven los espacion del inicio y el final del string. Existe rstip() y lstrip()
print(texto.replace("mi","ayo")) #remplaza una palabra por otra
print(texto.split()) #separador de palabras en un vector ***bastante usado***


