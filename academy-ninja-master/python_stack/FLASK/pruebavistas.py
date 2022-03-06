from flask import Flask, render_template
app = Flask(__name__)

@app.route('/home')
def hello_world():
    # En lugar de devolver una cadena, 
    # devolvemos el resultado del metodo render_template , pasando el nombre de nuestro archivo HTML
    # return render_template('index.html')
    return render_template("index.html", phrase="hello", times=5)
    
if __name__=="__main__":
    app.run(debug=True)  