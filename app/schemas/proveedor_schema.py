from pydantic import BaseModel
from datetime import date
from typing import Optional

class CertificadoBase(BaseModel):
    nombre: str
    cuerpoCertificador: Optional[str] = None
    fechaCertificacion: Optional[date] = None
    fechaVencimiento: Optional[date] = None
    urlDocumento: Optional[str] = None


class CertificadoCreate(CertificadoBase):
    pass


class CertificadoOut(CertificadoBase):
    id: int

    class Config:
        from_attributes = True


class ProveedorBase(BaseModel):
    nombre: str
    id_tax: Optional[str] = None
    direccion: Optional[str] = None
    telefono: Optional[str] = None
    correo: Optional[str] = None
    contacto: Optional[str] = None
    estado: Optional[str] = None


class ProveedorCreate(ProveedorBase):
    certificado: Optional[CertificadoCreate] = None


class ProveedorOut(ProveedorBase):
    id: int
    certificado: Optional[CertificadoOut] = None

    class Config:
        from_attributes = True
