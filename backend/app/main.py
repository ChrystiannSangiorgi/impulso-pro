from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, perfil, restaurante

app = FastAPI(
    title="Impulso Pro API",
    description="API de gestão de treinamentos operacionais para redes de restaurantes.",
    version="0.1.0"
)

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registra os routers
app.include_router(auth.router)
app.include_router(perfil.router)
app.include_router(restaurante.router)

@app.get("/", tags=["Health Check"])
def root():
    return {"status": "ok", "message": "Impulso Pro API funcionando."}