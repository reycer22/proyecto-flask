from flask import Flask, render_template, request, redirect, url_for
from clases import Usuario, Anuncio, Sistema

app = Flask(__name__)

# Crear sistema y algunos datos de prueba
sistema = Sistema()
sistema.registrar_usuario(Usuario("admin", "1234"))
sistema.agregar_anuncio(Anuncio(1, "Lana del Rey"))
sistema.agregar_anuncio(Anuncio(2, "Queen"))

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nombre = request.form['nombre']
        contraseña = request.form['contraseña']

        for usuario in sistema.usuarios:
            if usuario.nombre == nombre and usuario.contraseña == contraseña:
                return redirect(url_for('portal'))
        return render_template('login.html', error="Usuario o contraseña incorrectos")
    return render_template('login.html')

@app.route('/portal')
def portal():
    return render_template('portal.html', anuncios=sistema.anuncios)

@app.route('/click/<int:id>')
def click(id):
    for anuncio in sistema.anuncios:
        if anuncio.id == id:
            anuncio.registrar_click()
    return redirect(url_for('acceso'))

@app.route('/acceso')
def acceso():
    return render_template('acceso.html')

if __name__ == '__main__':
    app.run(debug=True)
