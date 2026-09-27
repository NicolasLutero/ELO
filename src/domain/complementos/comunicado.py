

class Comunicado:
    def __init__(self, idelo, titulo, conteudo, data_publicacao, gremio_idelo, autor_idelo=None, cargo_adm_idelo=None):
        self.idelo = idelo
        self.titulo = titulo
        self.conteudo = conteudo
        self.data_publicacao = data_publicacao
        self.gremio_idelo = gremio_idelo
        self.autor_idelo = autor_idelo
        self.cargo_adm_idelo = cargo_adm_idelo
