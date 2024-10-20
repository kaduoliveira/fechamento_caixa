from app import app
from models import FechamentoCaixa
from flask import render_template

@app.route('/')
def index():
    lista = FechamentoCaixa.query.order_by(FechamentoCaixa.id)
    print('Abrindo a página inicial.')
    return render_template('lista.html', fechamento = lista)