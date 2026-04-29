from pydantic import BaseModel
from typing import Optional

class EnderecoCreate(BaseModel):
    Cep: str
    Estado: str
    Cidade: str
    Bairro: str
    Rua: str
    Numero_Local: str
    Complemento_Local: Optional[str] = None

class EnderecoResponse(BaseModel):
    ID_Endereco: int
    Cep: str
    Estado: str
    Cidade: str
    Bairro: str
    Rua: str
    Numero_Local: str
    Complemento_Local: Optional[str] = None

    class Config:
        from_attributes = True

class RestauranteCreate(BaseModel):
    Nome_Restaurante: str
    endereco: EnderecoCreate

class RestauranteUpdate(BaseModel):
    Nome_Restaurante: Optional[str] = None
    endereco: Optional[EnderecoCreate] = None

class RestauranteResponse(BaseModel):
    ID_Restaurante: int
    Nome_Restaurante: str
    Atividade: bool
    endereco: EnderecoResponse

    class Config:
        from_attributes = True