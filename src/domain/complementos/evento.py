

class Evento:
    def __init__(self, idelo, nome, descricao, data_evento, local, gremio_id, organizador_idelo=None, cargo_adm_idelo=None):
        self.idelo = idelo
        self.nome = nome
        self.descricao = descricao
        self.data_evento = data_evento
        self.local = local
        self.gremio_id = gremio_id
        self.organizador_idelo = organizador_idelo
        self.cargo_adm_idelo = cargo_adm_idelo
