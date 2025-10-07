from fastapi import FastAPI
from app.database import Base, engine
from app.routers import proveedor_router

# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="MediSupply API", version="1.0.0")

# Incluir rutas
app.include_router(proveedor_router.router)
