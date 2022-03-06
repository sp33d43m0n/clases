  # ejecuta la aplicación en modo depuración
from flask import Flask
# Importar Flask para que permita crear nuestra aplicacióncopy
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

# @app.route('/')          # El decorador "@" asocia la ruta con la función siguiente
# def hello_world():
#     return 'Hello XAVI!'  # Retorna la cadena 'Hello World!' como respuesta

var_url = 'usuario/prueba/perro'
@app.route('/<path:u_path>')
def validate_url(u_path):
    if u_path == var_url:
      return '*'*10+'La URL digitada es OK'+'*'*10
    else:
      return '*'*10+'La URL digitada es ERRONEA'+'*'*10

  
@app.route('/')
def hola_mundo():
    return 'Hola Mundo'

@app.route('/dojo')          # El decorador "@" asocia la ruta con la función siguiente
def hi():
    return 'Dojo'
  
@app.route('/say/<name>') 
def say(name):
    print(name)
    return "Hola, " + name
  
@app.route('/users/<username>/<id>') # para una ruta '/users/____/____', dos parámetros en la url se pasan como nombre de usuario e id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

@app.route('/repeat/<numero>/<duplicate>')
def repeat(numero,duplicate):
  for i in range(0,int(numero)):
    print(f"hola {duplicate}")
  return

# @app.route('/user/<user_id>')
# def isint(user_id):
#     if isinstance(user_id, complex):
#       print(user_id,'*'*20,'es un numero complejo')
#     elif isinstance(user_id, float):
#       print(user_id,'*'*20,'es un numero flotante')
#     elif isinstance(user_id, int):
#       print(user_id,'*'*20,'es un numero entero')
#     elif isinstance(user_id, str):
#       print(user_id,'*'*20,'es una cadena')
#     else:
#       print('*'*20,'nos rendimos no sabemos que metiste')
#     return            

@app.route('/numero/<int:user_id>')
def isint(user_id):
    print(user_id,'*'*20,'es un numero entero')
    # return '*'*20+'es un numero entero'+user_id
    return   #preguntar porque no se puede imprimir en pantalla
  

    
#     if @app.route(url_var) != 


if __name__=="__main__":   # Asegúrese de que este archivo se ejecute directamente y no desde un módulo diferente
  app.run(debug=True)    # ejecuta la aplicación en modo depurac