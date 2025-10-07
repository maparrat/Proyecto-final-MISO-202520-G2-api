from pydantic import BaseModel

class ProveedorCreate(BaseModel):
    nombre: str
    contacto: str | None = None
    telefono: str | None = None
    correo: str | None = None


class ProveedorOut(BaseModel):
    id: int
    nombre: str
    id_tax: str | None = None
    direccion: str | None = None
    telefono: str | None = None
    correo: str | None = None
    contacto: str | None = None
    estado: str | None = None
    certificado: str | None = None

    class Config:
        from_attributes = True  # reemplaza orm_mode en Pydantic v2
 