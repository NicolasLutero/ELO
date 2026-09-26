from fastapi import APIRouter, Depends, HTTPException, status

from src.infra.bd.connection_factory import ConnectionFactory
from src.infra.bd.nucleo.dao_usuario import UsuarioDAO
from src.infra.bd.nucleo.dao_gremio import GremioDAO

from src.application.erros.usuario_erro import CPFJaCadastradoErro, EmailJaCadastradoErro, RAJaCadastradoErro
from src.application.servico_usuario import ServicoUsuario

from src.presentation.schemas.usuario_schema import UsuarioCadastroSchema


def get_usuario_service() -> ServicoUsuario:
    conn = ConnectionFactory.get_connection()
    dao_usuario = UsuarioDAO(conn)
    dao_gremio = GremioDAO(conn)

    return ServicoUsuario(dao_usuario=dao_usuario, dao_gremio=dao_gremio)

router = APIRouter(prefix="/usuario")

@router.get("/")
def ola():
    return {
        "msg": "oi"
    }

@router.post("/cadastrar")
def cadastrar(
    payload: UsuarioCadastroSchema,
    service: ServicoUsuario = Depends(get_usuario_service)
):
    try:
        dados_cadastro = payload.model_dump()

        novo_usuario = service.cadastrar_usuario(**dados_cadastro)
        
        return {
            "mensagem": "usuario cadastrado com sucesso!",
            "id": novo_usuario.id_elo
        }

    except CPFJaCadastradoErro:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="O CPF informado já está cadastrado no sistema."
        )
    except EmailJaCadastradoErro:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="O e-mail informado já está cadastrado no sistema."
        )
    except RAJaCadastradoErro:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="O RA informado já está cadastrado no sistema."
        )