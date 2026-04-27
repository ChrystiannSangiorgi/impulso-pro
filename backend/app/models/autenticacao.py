from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class ColaboradorAutenticacao(Base):
    __tablename__ = "colaborador_autenticacao"

    ID_Colaborador = Column(Integer, ForeignKey("colaborador_usuario.ID_Colaborador"), primary_key=True)
    Senha_Hash = Column(String(255), nullable=False)
    Data_Ultima_Atualizacao = Column(DateTime)
    Tentativas_Falhas = Column(Integer, default=0)
    Conta_Bloqueada = Column(Boolean, default=False)
    Data_Bloqueio = Column(DateTime, nullable=True)

    # Relacionamento com colaborador
    colaborador = relationship("ColaboradorUsuario", back_populates="autenticacao")