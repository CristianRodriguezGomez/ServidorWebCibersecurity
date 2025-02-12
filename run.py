import os
import logging
from flask import Flask, render_template, request
from dotenv import load_dotenv
from flask_wtf.csrf import CSRFProtect
from flask_talisman import Talisman
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from redis import Redis
from datetime import datetime

# Cargar variables de entorno
load_dotenv()

# Crear la aplicación Flask
app = Flask(__name__, template_folder="app/templates", static_folder="app/static")
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'clave_super_segura')

# Seguridad CSRF
csrf = CSRFProtect(app)

# Seguridad en encabezados HTTP
Talisman(app)

# Conexión a Redis
redis = Redis(host='localhost', port=6379, db=0)

# Protección contra ataques de fuerza bruta
limiter = Limiter(
    get_remote_address,
    app=app,
    storage_uri="redis://localhost:6379"  # Usando Redis para almacenar las restricciones de velocidad
)

# Configuración del registro de accesos
logging.basicConfig(
    filename="access.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

@app.before_request
def log_acceso():
    """Registra cada solicitud con IP, ruta, método y User-Agent."""
    ip_usuario = request.remote_addr
    ruta = request.path
    metodo = request.method
    agente = request.headers.get("User-Agent", "Desconocido")
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Registrar el intento de acceso
    logging.info(f"Acceso desde {ip_usuario} | Ruta: {ruta} | Método: {metodo} | Agente: {agente} | Fecha: {fecha}")

@app.route('/')
@limiter.limit("10 per minute")  # Limita a 10 peticiones por minuto
def home():
    return render_template("index.html")  # Muestra la página HTML

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)





"""import os
from flask import Flask
from dotenv import load_dotenv
from flask_wtf.csrf import CSRFProtect
from flask_talisman import Talisman
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Cargar variables de entorno
load_dotenv()

# Crear la aplicación
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'clave_super_segura')

# Seguridad contra CSRF
csrf = CSRFProtect(app)

# Seguridad en encabezados HTTP
Talisman(app)

# Protección contra ataques de fuerza bruta
limiter = Limiter(get_remote_address, app=app, default_limits=["100 per hour"])

@app.route('/')
@limiter.limit("10 per minute")  # Limita a 10 peticiones por minuto
def home():
    return "Bienvenido a la página segura de Ciberseguridad"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

"""

#ngrok http 5000
#http://localhost:4040/inspect/http