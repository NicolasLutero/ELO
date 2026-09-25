from src.application.servico_gremio import ServicoGremio
from src.infra.bd.connection_factory import ConnectionFactory
from src.infra.bd.nucleo.dao_cargo import CargoDAO
from src.infra.bd.nucleo.dao_gremio import GremioDAO
from src.infra.bd.nucleo.dao_permissao import PermissaoDAO
from src.infra.bd.nucleo.dao_usuario import UsuarioDAO
from src.infra.bd.nucleo.dao_validade import ValidadeDAO

from src.application.servico_usuario import ServicoUsuario

connection = ConnectionFactory().get_connection()

dao_usuario = UsuarioDAO(connection)
dao_gremio = GremioDAO(connection)
dao_cargo = CargoDAO(connection)
dao_permissao = PermissaoDAO(connection)
dao_validade = ValidadeDAO(connection)

servico_usuario = ServicoUsuario(dao_usuario, dao_gremio)
servico_gremio = ServicoGremio(dao_gremio, dao_usuario, dao_cargo, dao_permissao, dao_validade)

usuario = dao_usuario.get_by_id(1)
servico_gremio.criar_gremio(usuario, "Novo Gremio")
