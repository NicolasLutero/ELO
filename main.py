from src.infra.bd.connection_factory import ConnectionFactory
from src.infra.bd.nucleo.dao_usuario import UsuarioDAO

from src.application.servico_usuario import ServicoUsuario


connection = ConnectionFactory().get_connection()

dao_usuario = UsuarioDAO(connection)

servico = ServicoUsuario(dao_usuario)

# servico.cadastrar_usuario("nome", "senha", "cpf4", "email4", None)
servico.registrar_ra(7, "4ab")
