from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap = Bootstrap(app)

@app.route("/")

@app.route("/index")
def index():
    return render_template('index.html', title= 'Verwaltung')

if __name__ == '__main__':
    app.run(debug=True)
    