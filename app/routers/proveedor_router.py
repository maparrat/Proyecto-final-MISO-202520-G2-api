
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.proveedor import Proveedor
from app.schemas.proveedor_schema import ProveedorCreate, ProveedorOut
from fastapi_cache.decorator import cache

router = APIRouter(prefix="/proveedores", tags=["Proveedores"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ProveedorOut)
def crear_proveedor(proveedor: ProveedorCreate, db: Session = Depends(get_db)):
    nuevo_proveedor = Proveedor(
        nombre=proveedor.nombre,
        contacto=proveedor.contacto,
        telefono=proveedor.telefono
    )
    db.add(nuevo_proveedor)
    db.commit()
    db.refresh(nuevo_proveedor)
    return nuevo_proveedor

@router.get("/", response_model=list[ProveedorOut])
@cache(expire=60)  # cache for 60 seconds
def listar_proveedores(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Proveedor).offset(skip).limit(limit).all()
