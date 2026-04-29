from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class EnderecoRestaurante(Base):
    __tablename__ = "endereco_restaurante"

    ID_Endereco = Column(Integer, primary_key=True, index=True)
    Cep = Column(String(9), nullable=False)
    Estado = Column(String(2), nullable=False)
    Cidade = Column(String(100), nullable=False)
    Bairro = Column(String(100), nullable=False)
    Rua = Column(String(200), nullable=False)
    Numero_Local = Column(String(10), nullable=False)
    Complemento_Local = Column(String(100))

    restaurante = relationship("Restaurante", back_populates="endereco", uselist=False)

class Restaurante(Base):
    __tablename__ = "restaurante"

    ID_Restaurante = Column(Integer, primary_key=True, index=True)
    Nome_Restaurante = Column(String(100), nullable=False)
    ID_Endereco = Column(Integer, ForeignKey("endereco_restaurante.ID_Endereco"), nullable=False, unique=True)
    Atividade = Column(Boolean, default=True)

    endereco = relationship("EnderecoRestaurante", back_populates="restaurante")