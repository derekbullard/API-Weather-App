from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/<name>')
def index(name):
    
    return render_template('derek.html',name=name)

@app.route('/add/<int:num1>/<int:num2>')
def add(num1,num2):
    return render_template("derp.html", num1=num1, num2=num2,)


app.run(debug=True,)
