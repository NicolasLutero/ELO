from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt

from src.application.servico_usuario import ServicoUsuario
from src.infra.bd.nucleo.dao_gremio import GremioDAO
from src.infra.bd.nucleo.dao_usuario import UsuarioDAO
from src.infra.bd.connection_factory import ConnectionFactory


def get_usuario_service() -> ServicoUsuario:
    conn = ConnectionFactory.get_connection()
    dao_usuario = UsuarioDAO(conn)
    dao_gremio = GremioDAO(conn)

    return ServicoUsuario(dao_usuario=dao_usuario, dao_gremio=dao_gremio)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def obter_usuario_atual(
    token: str = Depends(oauth2_scheme),
    service: ServicoUsuario = Depends(
        get_usuario_service
    ),
):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não foi possível validar as credenciais",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        from security import ALGORITHM, SECRET_KEY

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id = payload.get("sub")

        if id is None:
            raise credential_exception
        
    except jwt.PyJWTError:
        raise credential_exception

    usuario = service.buscar_por_id(id)

    if usuario is None:
        raise credential_exception

    return usuario