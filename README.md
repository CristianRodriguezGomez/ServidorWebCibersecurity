# 🛡️ Flask Security Application

## 📌 Descripción  
Este proyecto es una aplicación web desarrollada con **Flask**, enfocada en la **seguridad** y en la protección contra ataques comunes como **CSRF**, **fuerza bruta** y **clickjacking**.  
Además, utiliza **Redis** para el almacenamiento de restricciones de acceso y mantiene un registro detallado de todas las solicitudes en archivos de log.  

---

## 🚀 Características  
✔️ **Protección CSRF** con `Flask-WTF`  
✔️ **Encabezados HTTP seguros** con `Flask-Talisman`  
✔️ **Limitación de accesos** con `Flask-Limiter` y Redis  
✔️ **Registro de accesos** en un archivo de logs (`access.log`)  
✔️ **Despliegue con ngrok** para exponer el servidor públicamente  

---

## 📦 Instalación  

### 🔹 Requisitos previos  
Antes de comenzar, asegúrate de tener los siguientes requisitos:  

- 🛠️ **Python 3.8+** instalado  
- 🛠️ **Redis** ejecutándose en `localhost:6379`  

### 🔹 Pasos de instalación  
1. **Clona este repositorio** en tu máquina local:  
   ```sh
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio
2. **Crea un entorno virtual e instala las dependencias:**
   -python -m venv venv
   -source venv/bin/activate  # En Windows usa: venv\Scripts\activate
   -pip install -r requirements.txt
3. **Configura las variables de entorno copiando el archivo de ejemplo:**
   cp .env.example .env

   Luego, edita el archivo **.env** y define tu **FLASK_SECRET_KEY**


##🚀 Uso
###🔹 Ejecutar la aplicación
Para iniciar el servidor Flask, usa el siguiente comando:
python app.py
Luego, accede a la aplicación en:
📍 http://localhost:5000

###🔹 Inspeccionar tráfico con ngrok
Para exponer tu servidor Flask a internet con ngrok, usa:

ngrok http 5000
Después, accede al dashboard de monitoreo en:
📍 http://localhost:4040/inspect/http

##🔐 Seguridad Implementada
🔒 Protección CSRF: Previene ataques de falsificación de solicitudes.
🔒 Encabezados HTTP seguros: Evita ataques como clickjacking y XSS.
🔒 Limitación de accesos: Previene ataques de fuerza bruta restringiendo el número de solicitudes.

##📝 Autor
👨‍💻 Nombre: Cris
