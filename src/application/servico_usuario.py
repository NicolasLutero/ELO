from src.infra.api_externa.instituicao_etapa_por_ra import InstituicaoEEtapaPorRa
from src.infra.bd.nucleo.dao_usuario import UsuarioDAO
from src.infra.bd.nucleo.dao_gremio import GremioDAO

from src.domain.nucleo.usuario import Usuario
from src.domain.nucleo.gremio import Gremio

from src.application.erros.usuario_erro import CPFJaCadastradoErro, EmailJaCadastradoErro, RAJaCadastradoErro, \
    UsuarioNaoExisteErro, CredenciaisInvalidasErro


class ServicoUsuario:
    def __init__(self, dao_usuario: UsuarioDAO, dao_gremio: GremioDAO):
        self.dao_usuario = dao_usuario
        self.dao_gremio = dao_gremio

    def cadastrar_usuario(self, nome, senha, cpf, email, ra):
        if not self.dao_usuario.check_availability_cpf(cpf):
            raise CPFJaCadastradoErro()
        if not self.dao_usuario.check_availability_email(email):
            raise EmailJaCadastradoErro()
        if ra is not None and not self.dao_usuario.check_availability_ra(ra):
            raise RAJaCadastradoErro()

        gremio_idelo = self._idelo_gremio_dado_ra(ra)
        dados_novo_usuario = self.dao_usuario.create(nome, cpf, email, ra, senha, gremio_idelo)

        return Usuario(**dados_novo_usuario)

    def registrar_ra(self, usuario_idelo, ra):
        if not self.dao_usuario.check_availability_ra(ra):
            raise RAJaCadastradoErro()

        dados_usuario = self.dao_usuario.get_by_idelo(usuario_idelo)
        if dados_usuario is None:
            raise UsuarioNaoExisteErro()

        usuario = Usuario(**dados_usuario)
        usuario.ra = ra
        usuario.gremio_idelo = self._idelo_gremio_dado_ra(ra)
        self.dao_usuario.update(usuario)

    def _idelo_gremio_dado_ra(self, ra):
        instituicao_idelo, etapa = InstituicaoEEtapaPorRa.get(ra)
        dados_gremio = self.dao_gremio.get_by_inst_etapa(instituicao_idelo, etapa)
        if dados_gremio is None:
            return None
        else:
            gremio = Gremio(**dados_gremio)
            return gremio.idelo

    def login(self, email, senha):
        usuario = self.dao_usuario.get_by_email_senha(email, senha)
        if usuario is None:
            raise CredenciaisInvalidasErro()
        del usuario["senha"]
        return usuario

    def get_by_idelo(self, idelo):
        usuario = self.dao_usuario.get_by_idelo(idelo)
        if usuario is None:
            raise UsuarioNaoExisteErro()
        del usuario["senha"]
        return usuario
