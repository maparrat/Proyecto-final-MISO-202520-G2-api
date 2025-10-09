from sqlalchemy import Column, Integer, String
from app.database import Base

class Proveedor(Base):
    __tablename__ = "proveedores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    id_tax = Column(String)
    direccion = Column(String)
    telefono = Column(String)
    correo = Column(String)
    contacto = Column(String)
    estado = Column(String)
    certificado = Column(String)
