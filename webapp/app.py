from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import get_functions

app = Flask(__name__)

@app.route("/")
def index():
    print(get_functions.price('BTC'))
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)