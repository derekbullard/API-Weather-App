from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/weather", methods=['POST'])
def weather_app():
    zipcode = request.form['zip']
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid=9489c2ed687f284eabf8f3adea48557b')
    json_object = r.json()
    tempk = float(json_object['main']['temp'])
    tempf = round((tempk - 273.15) * 1.8 + 32)

    return render_template('tempf.html', temp=tempf)
    #return render_template("guide.html")

@app.route("/")
def index():
    return render_template('boot.html')


if __name__ == "__main__":
    app.run(debug=True)
