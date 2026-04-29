from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.restaurante import Restaurante, EnderecoRestaurante
from app.schemas.restaurante import RestauranteCreate, RestauranteUpdate, RestauranteResponse
from app.core.security import decode_access_token
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

router = APIRouter(prefix="/restaurantes", tags=["Restaurantes"])
security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado."
        )
    return payload

@router.post("/", response_model=RestauranteResponse, status_code=status.HTTP_201_CREATED)
def criar_restaurante(
    dados: RestauranteCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    endereco = EnderecoRestaurante(**dados.endereco.model_dump())
    db.add(endereco)
    db.flush()

    restaurante = Restaurante(
        Nome_Restaurante=dados.Nome_Restaurante,
        ID_Endereco=endereco.ID_Endereco
    )
    db.add(restaurante)
    db.commit()
    db.refresh(restaurante)
    return restaurante

@router.get("/", response_model=list[RestauranteResponse])
def listar_restaurantes(
    ativo: bool = None,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    query = db.query(Restaurante)
    if ativo is not None:
        query = query.filter(Restaurante.Atividade == ativo)
    return query.all()

@router.get("/{id}", response_model=RestauranteResponse)
def buscar_restaurante(
    id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    restaurante = db.query(Restaurante).filter(Restaurante.ID_Restaurante == id).first()
    if not restaurante:
        raise HTTPException(status_code=404, detail="Restaurante não encontrado.")
    return restaurante

@router.put("/{id}", response_model=RestauranteResponse)
def atualizar_restaurante(
    id: int,
    dados: RestauranteUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    restaurante = db.query(Restaurante).filter(Restaurante.ID_Restaurante == id).first()
    if not restaurante:
        raise HTTPException(status_code=404, detail="Restaurante não encontrado.")

    if dados.Nome_Restaurante:
        restaurante.Nome_Restaurante = dados.Nome_Restaurante

    if dados.endereco:
        for campo, valor in dados.endereco.model_dump(exclude_none=True).items():
            setattr(restaurante.endereco, campo, valor)

    db.commit()
    db.refresh(restaurante)
    return restaurante

@router.patch("/{id}/status", response_model=RestauranteResponse)
def alterar_status(
    id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    restaurante = db.query(Restaurante).filter(Restaurante.ID_Restaurante == id).first()
    if not restaurante:
        raise HTTPException(status_code=404, detail="Restaurante não encontrado.")

    restaurante.Atividade = not restaurante.Atividade
    db.commit()
    db.refresh(restaurante)
    return restaurante