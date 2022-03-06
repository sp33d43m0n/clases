from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def encuesta():
    return render_template("index.html")

@app.route('/resultado', methods=['POST'])
def fill_form():
    print('*'*20,'Prueba exitosa')
    print(request.form)
    email_from_form = request.form['email']
    option1_from_form=request.form['option1']
    option2_from_form=request.form['option2']
    comments_from_form=request.form['comments']
    geek_from_forms=request.form['geek']
    information_from_forms=request.form['information_value']
    flex_Radio_from_form = request.form['flexRadioDefault']
    return render_template('answer.html',email_on_template=email_from_form, option1_on_form=option1_from_form, option2_on_form=option2_from_form, comments_on_form=comments_from_form, geek_on_form=geek_from_forms, information_on_forms=information_from_forms , flex_Radio_on_form=flex_Radio_from_form)
    


    
if __name__=="__main__":
    app.run(debug=True)