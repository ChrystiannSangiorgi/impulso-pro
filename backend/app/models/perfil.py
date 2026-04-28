from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Perfil(Base):
    __tablename__ = "perfil"

    ID_Perfil = Column(Integer, primary_key=True, index=True)
    Nome_Perfil = Column(String(50), nullable=False)
    Descricao_perfil = Column(String(200), nullable=False)

    permissoes = relationship("Permissao", secondary="perfil_permissoes", back_populates="perfis")

class Permissao(Base):
    __tablename__ = "permissao"

    ID_Permissao = Column(Integer, primary_key=True, index=True)
    Nome_Permissao = Column(String(100), nullable=False)
    Descricao_Permissao = Column(String(200), nullable=False)

    perfis = relationship("Perfil", secondary="perfil_permissoes", back_populates="permissoes")

class PerfilPermissoes(Base):
    __tablename__ = "perfil_permissoes"

    ID_Perfil = Column(Integer, ForeignKey("perfil.ID_Perfil"), primary_key=True)
    ID_Permissao = Column(Integer, ForeignKey("permissao.ID_Permissao"), primary_key=True)

class ColaboradorPerfil(Base):
    __tablename__ = "colaborador_perfil"

    ID_Perfil = Column(Integer, ForeignKey("perfil.ID_Perfil"), primary_key=True)
    ID_Colaborador = Column(Integer, ForeignKey("colaborador_usuario.ID_Colaborador"), primary_key=True)