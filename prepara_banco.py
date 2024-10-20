import mysql.connector
from mysql.connector import errorcode

print("Connecting to MySQL...")

# conectando com o Banco de Dados
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sumimasen",
    )
    print("Conectado!!!")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Usuário ou senha inválidos.")
    else:
        print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS fechamento_caixa;")
cursor.execute("CREATE DATABASE fechamento_caixa;")
cursor.execute("USE fechamento_caixa;")

# CRIANDO TABELAS
cursor.execute('''
        CREATE TABLE fechamento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data DATE,
    caixa1 INT,
    caixa2 INT,
    caixa3 INT,
    caixa4 INT,
    dinheiro1 DECIMAL(10, 2),
    dinheiro2 DECIMAL(10, 2),
    dinheiro3 DECIMAL(10, 2),
    dinheiro4 DECIMAL(10, 2),
    dinheiro_total DECIMAL(10, 2),
    cartao_cred1 DECIMAL(10, 2),
    cartao_cred2 DECIMAL(10, 2),
    cartao_cred3 DECIMAL(10, 2),
    cartao_cred4 DECIMAL(10, 2),
    cartao_cred_total DECIMAL(10, 2),
    cartao_deb1 DECIMAL(10, 2),
    cartao_deb2 DECIMAL(10, 2),
    cartao_deb3 DECIMAL(10, 2),
    cartao_deb4 DECIMAL(10, 2),
    cartao_deb_total DECIMAL(10, 2),
    pix1 DECIMAL(10, 2),
    pix2 DECIMAL(10, 2),
    pix3 DECIMAL(10, 2),
    pix4 DECIMAL(10, 2),
    pix_total DECIMAL(10, 2),
    cheque1 DECIMAL(10, 2),
    cheque2 DECIMAL(10, 2),
    cheque3 DECIMAL(10, 2),
    cheque4 DECIMAL(10, 2),
    cheque_total DECIMAL(10, 2),
    total1 DECIMAL(10, 2),
    total2 DECIMAL(10, 2),
    total3 DECIMAL(10, 2),
    total4 DECIMAL(10, 2),
    total_total DECIMAL(10, 2),
    malote1 DECIMAL(10, 2),
    malote2 DECIMAL(10, 2),
    malote3 DECIMAL(10, 2),
    malote4 DECIMAL(10, 2),
    malote_total DECIMAL(10, 2),
    despesa1 DECIMAL(10, 2),
    despesa2 DECIMAL(10, 2),
    despesa3 DECIMAL(10, 2),
    despesa4 DECIMAL(10, 2),
    despesa_total DECIMAL(10, 2),
    resultado1 DECIMAL(10, 2),
    resultado2 DECIMAL(10, 2),
    resultado3 DECIMAL(10, 2),
    resultado4 DECIMAL(10, 2),
    resultado_total DECIMAL(10, 2),
    qtd_vendas INT,
    tkt_medio DECIMAL(10, 2),
    servicos1 DECIMAL(10, 2),
    servicos2 DECIMAL(10, 2),
    servicos3 DECIMAL(10, 2),
    servicos4 DECIMAL(10, 2),
    servicos5 DECIMAL(10, 2)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
''')
cursor.execute("INSERT INTO fechamento (data, qtd_vendas, tkt_medio) VALUES ('2024-10-20', 35, 32.1)")
cursor.execute("select * from fechamento_caixa.fechamento;")
cursor.fetchall()

# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()
