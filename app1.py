from flask import Flask, render_template, request
from converter1 import convert_units

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        result = convert_units(value, from_unit, to_unit)
    except ValueError:
        result = "Invalid input. Please enter a numerical value."
    return render_template('index1.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
