from flask import Flask, render_template, request


app = Flask(__name__)

# Ruta para la página de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para la página de portafolio
@app.route('/portafolio')
def Portafolio():
    return render_template('portafolio.html')

# Ruta para la página "Acerca de mí"
@app.route('/Acercademi')
def Acercademi():
    return render_template('Acercademi.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

# Ruta para la página de contacto
@app.route('/mensaje', methods=['POST'])
def mensaje():
    if request.method == 'POST':
        nombres = (request.form['Nombres'])
        correo = (request.form['Correo'])
        mensaje = (request.form['Mensaje'])
        return render_template('mensaje.html', nombres=nombres, correo=correo, mensaje=mensaje)


if __name__ == '__main__':
    app.run(debug=True)