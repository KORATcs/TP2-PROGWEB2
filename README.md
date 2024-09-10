<img src="https://github.com/KORATcs/TP2-PROGWEB2/blob/4ddaea7b3f32fed94e34cc6ffd80dbec3f5344f7/Presentaci%C3%B3n%20Proyecto%20libreta%20Creativo%20Doodle%20Rosa.png" alt="logo">

# Proyecto Django: Mensajes  

Bienvenido al proyecto **Mensajes**, una aplicación web construida con Django que permite enviar y recibir mensajes de manera sencilla y eficiente.  
[Descargar Informe](https://github.com/KORATcs/TP2-PROGWEB2/blob/8a00b39265409583ac8d1e2dd787587db6d52440/TP%202%20-%20PWII%20(1).pdf)  
[Acceder a la Aplicación](http://127.0.0.1:8000)   

---

## Tabla de Contenidos

- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Uso](#uso)

---

## Características

- Envío y recepción de mensajes.
- Interfaz de usuario amigable y moderna.
- Eliminación de mensajes.
- Visualización de mensajes por remitente y destinatario.

---

## Requisitos

Antes de comenzar, asegúrate de tener instalados los siguientes requisitos:

- Python 3.8 o superior
- Django 5.1.1
- pip (gestor de paquetes de Python)

---

## Instalación

Sigue estos pasos para instalar el proyecto:

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/tu_usuario/mensajes.git
   cd mensajes

2. Crea un entorno virtual:
bash
python -m venv venv

3. Activa el entorno virtual:
En Windows:
bash
venv\Scripts\activate

En macOS y Linux:
bash
source venv/bin/activate

4. Instala las dependencias:
bash
pip install -r requirements.txt

## Configuración
1. Configura la base de datos:  
Abre settings.py y ajusta la configuración de la base de datos según tus necesidades. Por defecto, se utiliza SQLite.  
2. Realiza las migraciones:  
bash  
python manage.py migrate  

## Uso  
1. Inicia el servidor de desarrollo:  
bash  
python manage.py runserver  

2. Accede a la aplicación:  
Abre tu navegador y ve a http://127.0.0.1:8000/.  

4. Explora las características:
Envía y recibe mensajes.
Visualiza tus mensajes.
Elimina mensajes si es necesario.
