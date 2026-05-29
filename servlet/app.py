from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime
from functools import wraps

app = Flask(__name__)
app.secret_key = 'tu-clave-secreta-cambia-esto-12345'

# Decorador para proteger rutas
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Validación simple (después puedes conectar a BD)
        if email == "usuario@ejemplo.com" and password == "123456":
            session['usuario'] = {
                'nombre': email.split('@')[0],
                'email': email,
                'login_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Credenciales incorrectas")
    
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    usuario = session['usuario']
    return render_template('dashboard.html',
        nombre=usuario['nombre'],
        email=usuario['email'],
        fecha=usuario['login_time'],
        ip=request.remote_addr
    )

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=8080)