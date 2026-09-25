from src.infra.bd.nucleo.dao_usuario import UsuarioDAO
from src.domain.nucleo.usuario import Usuario

from src.application.erros.usuario_ja_existe_erro import CPFJaCadastradoErro, EmailJaCadastradoErro, RAJaCadastradoErro
from src.application.erros.usuario_nao_existe_erro import UsuarioNaoExisteErro

from src.infra.api_externa.gremio_por_ra import GremioPorRa


class ServicoUsuario:
    def __init__(self, dao_usuario: UsuarioDAO):
        self.dao_usuario = dao_usuario

    def cadastrar_usuario(self, nome, senha, cpf, email, ra):
        if not self.dao_usuario.check_availability_cpf(cpf):
            raise CPFJaCadastradoErro()
        if not self.dao_usuario.check_availability_email(email):
            raise EmailJaCadastradoErro()
        if ra is not None and not self.dao_usuario.check_availability_ra(ra):
            raise RAJaCadastradoErro()

        gremio_id = GremioPorRa.get(ra)
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
        usuario.gremio_id = GremioPorRa.get(ra)
        self.dao_usuario.update(usuario)
