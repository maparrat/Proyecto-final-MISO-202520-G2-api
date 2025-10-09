from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend

# ----------------------------
# Configuración de base de datos de prueba (SQLite local)
# ----------------------------
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine_test = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
Base.metadata.create_all(bind=engine_test)

# ----------------------------
# Inicialización del cache en memoria
# ----------------------------
FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache")

# ----------------------------
# Cliente de pruebas
# ----------------------------
client = TestClient(app)

# ----------------------------
# Tests
# ----------------------------
def test_crear_proveedor():
    response = client.post(
        "/proveedores/",
        json={
            "nombre": "Proveedor Test",
            "id_tax": "123456789",
            "direccion": "Calle 123",
            "telefono": "987654321",
            "correo": "proveedor@test.com",
            "contacto": "Juan",
            "estado": "activo",
            "certificado": "True"
           
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["nombre"] == "Proveedor Test"
    assert data["id_tax"] == "123456789"
    assert data["direccion"] == "Calle 123"
    assert data["telefono"] == "987654321"
    assert data["correo"] == "proveedor@test.com"
    assert data["contacto"] == "Juan"
    assert data["estado"] == "activo"
    assert data["certificado"] == "True"


def test_listar_proveedores():
    response = client.get("/proveedores/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
