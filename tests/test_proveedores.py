from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine, get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Crear una base de datos temporal en memoria
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine_test = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)

# Reemplazar la dependencia de get_db con la de testing
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
Base.metadata.create_all(bind=engine_test)

client = TestClient(app)

def test_crear_proveedor():
    response = client.post(
        "/proveedores/",
        json={"nombre": "Proveedor Test", "contacto": "Juan", "telefono": "123456789"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["nombre"] == "Proveedor Test"


def test_listar_proveedores():
    response = client.get("/proveedores/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
