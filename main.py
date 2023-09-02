from flask import Flask, render_template
import os
import datetime as dt

BIRTH_YEAR = 1998
BIRTH_MONTH = 1
BIRTH_DAY = 31

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')


@app.route('/')
def home():
    year = dt.datetime.today().year
    age = year - BIRTH_YEAR - 1
    if dt.datetime.today().month > BIRTH_MONTH:
        age = age + 1
    return render_template('index.html', age=age, year=year)


if __name__ == "__main__":
    app.run(debug=False)