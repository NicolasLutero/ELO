

class Usuario:
    def __init__(self, idelo, nome, cpf, email, ra, senha, gremio_idelo=None):
        self.idelo = idelo
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.ra = ra
        self.senha = senha
        self.gremio_idelo = gremio_idelo
