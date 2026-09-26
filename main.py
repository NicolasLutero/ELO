from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.presentation.routers import api_router

app = FastAPI(
    title="ELO API",
    description="Backend do sistema ELO integrado com React",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

@app.get("/", tags=["Health Check"])
def health_check():
    return {"status": "ok", "mensagem": "API ELO rodando com sucesso!"}