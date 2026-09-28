from fastapi import APIRouter, Depends, HTTPException, status

from src.presentation.deps.usuario_deps import get_usuario_service

from src.application.erros.usuario_erro import CPFJaCadastradoErro, EmailJaCadastradoErro, RAJaCadastradoErro
from src.application.servico_usuario import ServicoUsuario

from src.presentation.schemas.usuario_cadastro_schema import UsuarioCadastroSchema
from src.presentation.schemas.usuario_login_schema import UsuarioLoginSchema

from src.presentation.security import create_access_token

router = APIRouter(prefix="/usuario")

@router.post("/login")
def login(
    payload: UsuarioLoginSchema,
    service: ServicoUsuario = Depends(get_usuario_service)
):
    dados_login = payload.model_dump()
    usuario = service.login(**dados_login)

    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="E-mail ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": usuario["id_elo"]})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/cadastro")
def cadastrar(
    payload: UsuarioCadastroSchema,
    service: ServicoUsuario = Depends(get_usuario_service)
):
    try:
        dados_cadastro = payload.model_dump()

        novo_usuario = service.cadastrar_usuario(**dados_cadastro)
        
        return {
            "mensagem": "usuario cadastrado com sucesso!",
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