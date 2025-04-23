from flask import render_template, request, redirect, url_for
from .models import consulta_prod

# Datos de usuarios (simulados para el ejemplo)
USUARIOS = {
    'usuario1': 'u1',
    'usuario2': 'u2'
}

def registrar_rutas(app):
    #----------------------------------------
    # Página de registro al sistema
    #----------------------------------------
    @app.route('/', methods=['GET', 'POST'])
    @app.route('/login', methods=['GET', 'POST'])
    def login_home():
        error = None
        if request.method == 'POST':
            username = request.form['usuario']
            password = request.form['contrasena']
            if username in USUARIOS and USUARIOS[username] == password:
                # Iniciar sesión exitosa, redirigir a otra página
                return redirect(url_for('inicio_home'))
            else:
                # Credenciales incorrectas, mostrar mensaje de error
                #return 'Credenciales incorrectas. <a href="/login">Intenta de nuevo</a>'
                msj= 'Credenciales incorrectas'
                return  render_template('login.html', error = msj), 401
        else:
            return render_template('login.html')
        


    #----------------------------------------    
    # Página  del menu principal
    #----------------------------------------
    @app.route('/inicio', methods=['GET', 'POST']) 
    def inicio_home():
            return render_template('inicio.html')


    #----------------------------------------
    # Página de la consulta de productos
    #----------------------------------------
    @app.route('/consulta_productos', methods=['GET', 'POST'])
    def consulta_productos():
            resultados = consulta_prod()
            return render_template("consulta.html", datos=resultados)
