from pydantic import BaseModel
from datetime import date
from typing import Optional

class CertificadoBase(BaseModel):
    nombre: str
    cuerpoCertificador: str| None = None
    fechaCertificacion: date| None = None
    fechaVencimiento: date| None = None
    urlDocumento: str| None = None


class CertificadoCreate(CertificadoBase):
    pass


class CertificadoOut(CertificadoBase):
    id: int

    class Config:
        from_attributes = True


class ProveedorBase(BaseModel):
    nombre: str
    id_tax: str | None = None
    direccion: str | None = None
    telefono: str | None = None
    correo: str | None = None
    contacto: str | None = None
    estado: str | None = None


class ProveedorCreate(ProveedorBase):
    certificado: Optional[CertificadoOut] = None


class ProveedorOut(ProveedorBase):
    id: int
    certificado: Optional[CertificadoOut] = None

    class Config:
        from_attributes = True
