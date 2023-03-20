import sqlite3
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap = Bootstrap(app)
connection = sqlite3.connect('kursverwaltung.db')

@app.route("/")

@app.route("/index", methods=['POST'])
def index():
    if request.method == 'POST':
        kurs = request.form['kurs']
        art = request.form['art']
        schiene = request.form['schiene']
        lehrer = request.form['lehrer']
        anmerkungen = request.form['anmerkungen']
    return render_template('index.html', title= 'Verwaltung')

@app.route("/gespeichert", methods=["POST"])
def gespeichert():
    return render_template('index.html', title= 'Verwaltung')


@app.route("/reset")
def reset():
    return render_template('index.html', title= 'Verwaltung')

@app.route("/konto")
def konto():
    return render_template('konto.html', title= 'Verwaltung')

if __name__ == '__main__':
    app.run(debug=True)
    
connection.execute()
connection.commit()
connection.close()