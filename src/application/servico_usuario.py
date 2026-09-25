from src.infra.api_externa.instituicao_etapa_por_ra import InstituicaoEEtapaPorRa
from src.infra.bd.nucleo.dao_usuario import UsuarioDAO
from src.infra.bd.nucleo.dao_gremio import GremioDAO

from src.domain.nucleo.usuario import Usuario
from src.domain.nucleo.gremio import Gremio

from src.application.erros.usuario_erro import CPFJaCadastradoErro, EmailJaCadastradoErro, RAJaCadastradoErro, \
    UsuarioNaoExisteErro


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

        gremio_id = self._id_gremio_dado_ra(ra)

        dados_novo_usuario = self.dao_usuario.create(nome, cpf, email, ra, senha, gremio_id)
        return Usuario(**dados_novo_usuario)

    def registrar_ra(self, usuario_id, ra):
        if not self.dao_usuario.check_availability_ra(ra):
            raise RAJaCadastradoErro()

        dados_usuario = self.dao_usuario.get_by_id(usuario_id)
        if dados_usuario is None:
            raise UsuarioNaoExisteErro()

        usuario = Usuario(**dados_usuario)
        usuario.ra = ra
        usuario.gremio_id = self._id_gremio_dado_ra(ra)
        self.dao_usuario.update(usuario)

    def _id_gremio_dado_ra(self, ra):
        instituicao_id, etapa = InstituicaoEEtapaPorRa.get(ra)
        gremio = Gremio(**self.dao_gremio.get_by_inst_etapa(instituicao_id, etapa))
        if gremio is None:
            return None
        else:
            return gremio.id_elo
