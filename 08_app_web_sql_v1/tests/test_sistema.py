import pytest
from app_web.sistema import create_app
from app_web.extension  import pgdb

#carga los metodos de las vistas

@pytest.fixture(scope="session")
def app():
    # Setup de la aplicación 
    app = create_app()
    
    app.config.update({
        "TESTING": True,
    })

    # Inicialización de la base de datos
    print("...inicializando entorno de TESTING...")
    pgdb.init_app(app)
    #pgdb.create_all_tables()

    yield app
    # apartir de aquí se pone el código para liberar los recursos 

    # teardown limpiar/ reinicializar


@pytest.fixture(scope="session")
def client(app):
    print("creando cliente...")
    return app.test_client()


#--------------------------------------------------
# Test de las transacciones de la aplicación
#--------------------------------------------------

def test_login(app, client):
    with client:
        usuario = 'usuario1'
        password = 'u1'
        response = client.post("/login", data={"usuario":  usuario , "contrasena": password}, follow_redirects=True)
        assert response.status_code == 200 


def test_login_failed(app, client):

    with client:
        # Si las credenciales fallaron la página retorna un codigo 401
        usuario = 'usuario1'
        password = 'u'
        response = client.post("/login", data={"usuario":  usuario , "contrasena": password}, follow_redirects=True)
        assert response.status_code == 401


def test_inicio_home(app, client):
    with client:
        response = client.get("/inicio", follow_redirects=True)
        assert response.status_code == 200 


def test_consulta_producto(app, client):
    res = client.get("/consulta_productos", follow_redirects=True)
    assert res.status_code == 200
