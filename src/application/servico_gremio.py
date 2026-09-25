from src.application.erros.gremio_erro import GremioJaExisteInstEtapaErro, GremioNaoExisteErro
from src.application.erros.usuario_erro import UsuarioNaoTemRAErro, UsuarioNaoExisteErro
from src.domain.nucleo.gremio import Gremio
from src.infra.api_externa.instituicao_etapa_por_ra import InstituicaoEEtapaPorRa
from src.infra.bd.nucleo.dao_gremio import GremioDAO
from src.infra.bd.nucleo.dao_usuario import UsuarioDAO


class ServicoGremio:
    def __init__(self, dao_gremio: GremioDAO, dao_usuario: UsuarioDAO):
        self.dao_gremio = dao_gremio
        self.dao_usuario = dao_usuario

    def criar_gremio(self, criador_id, nome_gremio):
        criador = self.dao_usuario.get_by_id(criador_id)
        if criador is None:
            raise UsuarioNaoExisteErro()

        ra = criador.ra
        if ra is None:
            raise UsuarioNaoTemRAErro()

        instituicao_id, etapa = InstituicaoEEtapaPorRa.get(ra)
        if not self.dao_gremio.check_availability_inst_etapa(instituicao_id, etapa):
            raise GremioJaExisteInstEtapaErro()

        # TODO dar cargo de adm temporario ao criador

        dados_novo_gremio = self.dao_gremio.create(nome_gremio, instituicao_id, etapa)
        return Gremio(**dados_novo_gremio)

    def legitimar_gremio(self, gremio_id):
        gremio = self.dao_gremio.get_by_id(gremio_id)
        if gremio is None:
            raise GremioNaoExisteErro()

        gremio.legitimidade = True
        self.dao_gremio.update(gremio)
