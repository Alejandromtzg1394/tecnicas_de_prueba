import pytest
from app_web.sistema import create_app
from app_web.extension  import pgdb

#carga los metodos de las vistas

@pytest.fixture(scope="session")
def app_flask():
    # Setup de la aplicación 
    app = create_app()
    
    app.config.update({
        "TESTING": True,
    })

    # Inicialización de la base de datos
    print("...inicializando entorno de TESTING...")
    pgdb.init_app(app)
    # pgdb.create_all_tables()
 
    yield app
    # apartir de aquí se pone el código para liberar los recursos 

    # teardown limpiar/ reinicializar


@pytest.fixture(scope="session")
def client(app_flask):
    print("creando cliente...")
    return app_flask.test_client()


#--------------------------------------------------
# Test de las transacciones de la aplicación
#--------------------------------------------------

def test_login(app_flask, client):
    with client:
        usuario = 'usuario1'
        password = 'u1'
        response = client.post("/login", data={"usuario":  usuario , "contrasena": password}, follow_redirects=True)
        data = response.get_data().decode('utf-8')
        print(data)
        assert "<h1>Menú</h1>" in data
        # assert response.status_code == 200 


def test_login_failed(app_flask, client):

    with client:
        # Si las credenciales fallaron la página retorna un codigo 401
        usuario = 'usuario1'
        password = 'u'
        response = client.post("/login", data={"usuario":  usuario , "contrasena": password}, follow_redirects=True)
        data = response.get_data().decode('utf-8')
        print(data)
        assert "<strong>Error:</strong> Credenciales incorrectas" in data
        # assert response.status_code == 401


def test_consulta_producto(app_flask, client):
    with client:
        response = client.post("/consulta_productos", data={},  follow_redirects=True)
        data = response.get_data().decode('utf-8')
        print(data)        
        assert "Lista de Datos" in data
        # assert response.status_code == 200



#===========================================================================
# Ejecución de los test.
#===========================================================================
# Desde la terminal ejecutar
#
#
# pytest -v test_sistema.py
#
#---------------------------------------------------------------------------
# Para visualizar las impresiones en consola usar el parámetro -s
#---------------------------------------------------------------------------
#
# pytest -vs test_sistema.py
#
#---------------------------------------------------------------------------



#===========================================================================
# Ejercicio
#===========================================================================
# De las páginas creadas para la tabla Empleado agregar los tests 
# correspondientes.
#
# 1. Agregar los tests para consulta de empleados
# 2. Agregar los tests para agregar empleado
#===========================================================================