from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'b1tc0mp0w3r'
# nuestra ruta de indice se encargara de representar nuestro formulario

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/users', methods=['POST'])
def create_user():
    print("*"*20,"Vamos a pasar info")
    print(request.form)
    print(f"el valor de name es {request.form['name']},el valor email es {request.form['email']}")
    # name_from_form = request.form['name']
    # email_from_form = request.form['email']
    session['username'] = request.form['name']
    session['usermail'] = request.form['email']
    # return render_template("show.html", name_on_template=name_from_form, email_on_template=email_from_form)
    return redirect('/show')

@app.route("/show")
def show_user():
    return render_template("show.html")
    # return render_template("show.html", name_on_template=session['username'], email_on_template=session['usermail'])

if __name__ == "__main__":
    app.run(debug=True)
