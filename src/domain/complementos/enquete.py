

class Enquete:
    def __init__(self, idelo, titulo, descricao, data_criacao, data_encerramento, gremio_id, autor_idelo=None, cargo_adm_idelo=None):
        self.idelo = idelo
        self.titulo = titulo
        self.descricao = descricao
        self.data_criacao = data_criacao
        self.data_encerramento = data_encerramento
        self.gremio_id = gremio_id
        self.autor_idelo = autor_idelo
        self.cargo_adm_idelo = cargo_adm_idelo