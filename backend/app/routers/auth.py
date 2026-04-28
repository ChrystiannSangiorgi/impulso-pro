from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.colaborador import ColaboradorUsuario
from app.models.autenticacao import ColaboradorAutenticacao
from app.models.perfil import ColaboradorPerfil, Perfil
from app.schemas.auth import LoginRequest, TokenResponse
from app.core.security import verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Autenticação"])

@router.post("/login", response_model=TokenResponse)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    # Busca o colaborador pelo e-mail
    colaborador = db.query(ColaboradorUsuario).filter(
        ColaboradorUsuario.Email == request.email
    ).first()

    # Verifica se o colaborador existe e está ativo
    if not colaborador or not colaborador.Atividade:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas."
        )

    # Busca os dados de autenticação
    autenticacao = db.query(ColaboradorAutenticacao).filter(
        ColaboradorAutenticacao.ID_Colaborador == colaborador.ID_Colaborador
    ).first()

    if not autenticacao:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas."
        )

    # Verifica se a conta está bloqueada
    if autenticacao.Conta_Bloqueada:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Conta bloqueada. Entre em contato com o administrador."
        )

    # Verifica a senha
    if not verify_password(request.senha, autenticacao.Senha_Hash):
        # Incrementa tentativas falhas
        autenticacao.Tentativas_Falhas += 1
        if autenticacao.Tentativas_Falhas >= 5:
            autenticacao.Conta_Bloqueada = True
        db.commit()
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas."
        )

    # Login bem sucedido — zera tentativas falhas
    autenticacao.Tentativas_Falhas = 0
    db.commit()
    # Busca o perfil do colaborador
    colaborador_perfil = db.query(ColaboradorPerfil).filter(
        ColaboradorPerfil.ID_Colaborador == colaborador.ID_Colaborador
    ).first()

    nome_perfil = None
    if colaborador_perfil:
        perfil = db.query(Perfil).filter(
            Perfil.ID_Perfil == colaborador_perfil.ID_Perfil
        ).first()
        nome_perfil = perfil.Nome_Perfil if perfil else None

    # Gera o token JWT com perfil incluído
    token = create_access_token(data={
        "sub": str(colaborador.ID_Colaborador),
        "email": colaborador.Email,
        "perfil": nome_perfil,
        "nome": colaborador.Nome_Colaborador
    })

    return TokenResponse(access_token=token)