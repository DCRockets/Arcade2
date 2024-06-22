# app1.py (update)
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

# Update index1.html to display errors clearly
<p>{{ result }}</p>
