from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/calc', methods=['GET', 'POST'])
def temp_calc():
    if request.method == 'GET':
        return render_template('temp.html')
    else:
        conv = request.form.get('convertionType')
        degrees = float(request.form.get("degrees"))
        if conv == "celcToFahr":
            result = (9/5) * degrees + 32

        elif conv == "FahrToCelc":
            result = (5/9) * (degrees - 32)

        return render_template('temp.html', result=round(result))


if __name__ == '__main__':
    app.run(debug=True)
