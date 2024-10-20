

SECRET_KEY = 'secret'

SQLALCHEMY_DATABASE_URI = \
      '{SGBD}://{username}:{senha}@{servido}/{database}'.format(
          SGBD = 'mysql+mysqlconnector',
          username = 'root',
          senha = 'sumimasen',
          servidor = 'localhost',
          database = 'fechamento_caixa'
      )