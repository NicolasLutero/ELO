

class Usuario:
    def __init__(self, id_elo, nome, cpf, email, ra, senha, gremio_id=None):
        self.id = id_elo
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.ra = ra
        self.senha = senha
        self.gremio_id = gremio_id
