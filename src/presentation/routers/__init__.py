# esse arquivo funciona como um centralizador de 
# todas os routers em um só

from fastapi import APIRouter
from src.presentation.routers.usuario_router import router as usuario_router

api_router = APIRouter()

api_router.include_router(usuario_router)