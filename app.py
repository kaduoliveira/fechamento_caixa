from flask import Flask, request, render_template
from models import db, init_db

app = Flask(__name__)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app)

if __name__ == '__main__':
    app.run(debug=True)