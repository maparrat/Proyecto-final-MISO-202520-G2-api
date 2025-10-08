from fastapi import FastAPI
from app.database import Base, engine
from app.routers import proveedor_router
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend
# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="MediSupply API", version="1.0.0")

# Incluir rutas
app.include_router(proveedor_router.router)

# ✅ Initialize in-memory cache
@app.on_event("startup")
async def startup_event():
    FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache")