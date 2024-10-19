from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import false

app = Flask(__name__)

@app.route('calcular', methods=['GET', 'POST'])
def calcular():
    if request.method == 'POST':
        data = request.form.get('data')

        caixa1 = request.form.get('caixa1')
        caixa2 = request.form.get('caixa2')
        caixa3 = request.form.get('caixa3')
        caixa4 = request.form.get('caixa4')
        caixa_total = request.form.get('caixa_total')
        
        dinheiro1 = request.form.get('dinheiro1')
        dinheiro2 = request.form.get('dinheiro2')
        dinheiro3 = request.form.get('dinheiro3')
        dinheiro4 = request.form.get('dinheiro4')
        dinheiro_total = request.form.get('dinheiro_total')
        
        cartao_cred1 = request.form.get('cartao_cred1')
        cartao_cred2 = request.form.get('cartao_cred2')
        cartao_cred3 = request.form.get('cartao_cred3')
        cartao_cred4 = request.form.get('cartao_cred4')
        cartao_cred_total = request.form.get('cartao_cred_total')

        cartao_deb1 = request.form.get('cartao_deb1')
        cartao_deb2 = request.form.get('cartao_deb2')
        cartao_deb3 = request.form.get('cartao_deb3')
        cartao_deb4 = request.form.get('cartao_deb4')
        cartao_deb_total = cartao_deb1 + cartao_deb2 + cartao_deb3 + cartao_deb4
        
        pix1 = request.form.get('pix1')
        pix2 = request.form.get('pix2')
        pix3 = request.form.get('pix3')
        pix4 = request.form.get('pix4')
        pix_total = pix1 + pix2 + pix3 + pix4

        cheque1 = request.form.get('cheque1')
        cheque2 = request.form.get('cheque2')
        cheque3 = request.form.get('cheque3')
        cheque4 = request.form.get('cheque4')
        cheque_total = request.form.get('cheque_total')

        total1 = dinheiro1 + cartao_cred1 + cartao_deb1 + pix1 + cheque1
        total2 = dinheiro2 + cartao_cred2 + cartao_deb2 + pix2 + cheque2
        total3 = dinheiro3 + cartao_cred3 + cartao_deb3 + pix3 + cheque3
        total4 = dinheiro4 + cartao_cred4 + cartao_deb4 + pix4 + cheque4
        total_total = total1 + total2 + total3 + total4

        malote1 = request.form.get('malote1')
        malote2 = request.form.get('malote2')
        malote3 = request.form.get('malote3')
        malote4 = request.form.get('malote4')
        malote_total = request.form.get('malote_total')

        