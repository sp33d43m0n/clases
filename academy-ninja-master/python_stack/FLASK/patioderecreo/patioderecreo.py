from flask import Flask, render_template
app = Flask(__name__)

@app.route('/root')
def hello_world():
    return render_template("index.html", nickname="Xavi")
    
if __name__=="__main__":
    app.run(debug=True)