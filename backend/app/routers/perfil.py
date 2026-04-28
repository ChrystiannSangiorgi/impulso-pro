from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.perfil import Perfil
from app.schemas.perfil import PerfilResponse
from app.core.security import decode_access_token
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

router = APIRouter(prefix="/perfis", tags=["Perfis"])
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

@router.get("/", response_model=list[PerfilResponse])
def listar_perfis(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    perfis = db.query(Perfil).all()
    return perfis