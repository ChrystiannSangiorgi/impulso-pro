from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Cria a conexão com o banco de dados usando a URL do .env
engine = create_engine(settings.DATABASE_URL)

# Cria uma fábrica de sessões para interagir com o banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos SQLAlchemy herdarem
Base = declarative_base()

# Dependência que fornece uma sessão do banco para cada requisição
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
