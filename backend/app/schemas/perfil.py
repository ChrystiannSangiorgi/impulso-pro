from pydantic import BaseModel

class PermissaoResponse(BaseModel):
    ID_Permissao: int
    Nome_Permissao: str
    Descricao_Permissao: str

    class Config:
        from_attributes = True

class PerfilResponse(BaseModel):
    ID_Perfil: int
    Nome_Perfil: str
    Descricao_perfil: str
    permissoes: list[PermissaoResponse] = []

    class Config:
        from_attributes = True