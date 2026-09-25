
class UsuarioNaoExisteErro(Exception):
    def __init__(self, mensagem="Usuário não existe."):
        super().__init__(mensagem)
