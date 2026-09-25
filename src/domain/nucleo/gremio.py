

class Gremio:
    def __init__(self, id_elo, nome, instituicao, etapa_ensino, legitimado=False, cargo_adm_id_elo=None):
        self.id_elo = id_elo
        self.nome = nome
        self.instituicao = instituicao
        self.etapa_ensino = etapa_ensino
        self.legitimado = legitimado
        self.cargo_adm_id_elo = cargo_adm_id_elo
