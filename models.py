from app import db
from datetime import datetime

class FechamentoCaixa(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data = db.Column(db.Date, nullable=False)
    
    caixa1 = db.Column(db.String(10))
    caixa2 = db.Column(db.String(10))
    caixa3 = db.Column(db.String(10))
    caixa4 = db.Column(db.String(10))
    
    dinheiro1 = db.Column(db.Numeric(10, 2), default=0.0)
    dinheiro2 = db.Column(db.Numeric(10, 2), default=0.0)
    dinheiro3 = db.Column(db.Numeric(10, 2), default=0.0)
    dinheiro4 = db.Column(db.Numeric(10, 2), default=0.0)
    dinheiro_total = db.Column(db.Numeric(10, 2), default=0.0)
    
    cartao_cred1 = db.Column(db.Numeric(10, 2), default=0.0)
    cartao_cred2 = db.Column(db.Numeric(10, 2), default=0.0)
    cartao_cred3 = db.Column(db.Numeric(10, 2), default=0.0)
    cartao_cred4 = db.Column(db.Numeric(10, 2), default=0.0)
    cartao_cred_total = db.Column(db.Numeric(10, 2), default=0.0)
    
    cartao_deb1 = db.Column(db.Numeric(10, 2), default=0.0)
    cartao_deb2 = db.Column(db.Numeric(10, 2), default=0.0)
    cartao_deb3 = db.Column(db.Numeric(10, 2), default=0.0)
    cartao_deb4 = db.Column(db.Numeric(10, 2), default=0.0)
    cartao_deb_total = db.Column(db.Numeric(10, 2), default=0.0)
    
    pix1 = db.Column(db.Numeric(10, 2), default=0.0)
    pix2 = db.Column(db.Numeric(10, 2), default=0.0)
    pix3 = db.Column(db.Numeric(10, 2), default=0.0)
    pix4 = db.Column(db.Numeric(10, 2), default=0.0)
    pix_total = db.Column(db.Numeric(10, 2), default=0.0)
    
    cheque1 = db.Column(db.Numeric(10, 2), default=0.0)
    cheque2 = db.Column(db.Numeric(10, 2), default=0.0)
    cheque3 = db.Column(db.Numeric(10, 2), default=0.0)
    cheque4 = db.Column(db.Numeric(10, 2), default=0.0)
    cheque_total = db.Column(db.Numeric(10, 2), default=0.0)
    
    total1 = db.Column(db.Numeric(10, 2), default=0.0)
    total2 = db.Column(db.Numeric(10, 2), default=0.0)
    total3 = db.Column(db.Numeric(10, 2), default=0.0)
    total4 = db.Column(db.Numeric(10, 2), default=0.0)
    total_total = db.Column(db.Numeric(10, 2), default=0.0)
    
    malote1 = db.Column(db.Numeric(10, 2), default=0.0)
    malote2 = db.Column(db.Numeric(10, 2), default=0.0)
    malote3 = db.Column(db.Numeric(10, 2), default=0.0)
    malote4 = db.Column(db.Numeric(10, 2), default=0.0)
    malote_total = db.Column(db.Numeric(10, 2), default=0.0)
    
    despesa1 = db.Column(db.Numeric(10, 2), default=0.0)
    despesa2 = db.Column(db.Numeric(10, 2), default=0.0)
    despesa3 = db.Column(db.Numeric(10, 2), default=0.0)
    despesa4 = db.Column(db.Numeric(10, 2), default=0.0)
    despesa_total = db.Column(db.Numeric(10, 2), default=0.0)

    serviço1 = db.Column(db.Numeric(10, 2), default=0.0)
    serviço2 = db.Column(db.Numeric(10, 2), default=0.0)
    serviço3 = db.Column(db.Numeric(10, 2), default=0.0)
    serviço4 = db.Column(db.Numeric(10, 2), default=0.0)
    serviço5 = db.Column(db.Numeric(10, 2), default=0.0)

    qtd_vendas = db.Column(db.Integer, default=0)
    tkt_medio = db.Column(db.Numeric(10, 2), default=0.0)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<FechamentoCaixa {self.data}>'
