import os
from app import app
from flask_wtf import FlaskForm
from wtforms import DateField, FloatField, IntegerField

class FormCaixa(FlaskForm):
    data = DateField('Data')
    
    caixa1 = IntegerField('Caixa 1')
    caixa2 = IntegerField('Caixa 2')
    caixa3 = IntegerField('Caixa 3')
    caixa4 = IntegerField('Caixa 4')

    dinheiro1 = FloatField('Dinheiro 1')
    dinheiro2 = FloatField('Dinheiro 2')
    dinheiro3 = FloatField('Dinheiro 3')
    dinheiro4 = FloatField('Dinheiro 4')
    