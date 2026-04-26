from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Impulso Pro API",
    description="API de gestão de treinamentos operacionais para redes de restaurantes.",
    version="0.1.0"
)

# Configuração do CORS — permite que o frontend React acesse a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Porta padrão do Vite
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Health Check"])
def root():
    return {"status": "ok", "message": "Impulso Pro API funcionando."}
