from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class ColaboradorUsuario(Base):
    __tablename__ = "colaborador_usuario"

    ID_Colaborador = Column(Integer, primary_key=True, index=True)
    Nome_Colaborador = Column(String(200), nullable=False)
    Data_Nascimento = Column(Date, nullable=False)
    Email = Column(String(200), unique=True, nullable=False)
    Telefone = Column(String(15))
    Atividade = Column(Boolean, default=True)
    Consentimento_LGPD = Column(Boolean, default=False)
    Data_Aceite_LGPD = Column(DateTime, nullable=True)
    ID_Restaurante = Column(Integer, ForeignKey("restaurante.ID_Restaurante"), nullable=False)
    ID_Cargo = Column(Integer, ForeignKey("cargo.ID_Cargo"), nullable=False)

    # Relacionamento com autenticação
    autenticacao = relationship("ColaboradorAutenticacao", back_populates="colaborador", uselist=False)