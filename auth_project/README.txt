Autor: Nelson Felipe Barco Benavides
CC: 1040749494
Curso: Seguridad en el Desarrollo


Para correr el programa:
- Tener python instalado
- Crear ambiente virtual (python -m venv nombre_ambiente)
- Activar ambiente virtual (env/Scripts/activate)
- Instalar librerias (pip install -r requierements.txt)
- Correr la app (python manage.py runserver)
- Ingresar a la app (http://127.0.0.1:8000/accounts/login)
- Crear una nueva cuenta (por la opcion de ¿No tienes cuenta? Regístrate)
- Despues de crear la cuenta hacer login
PAra verificar correcto guardado del usuario y encriptado de la contraseña:
- Crear un super usuario (python manage.py createsuperuser)
- un usuario y contraseña posible es felipe33 (ambas)
- ingresar a http://127.0.0.1:8000/admin/ con usuario y contraseña
- varificar


¿Que se implemento?

✅ 1. No revelar si el usuario o contraseña son incorrectos
🔐 Siempre mostrar el mismo mensaje de error:
"Usuario y/o contraseña incorrectos"

💡 Evita enumeración de usuarios (adivinar si un usuario existe).

✅ 2. Uso de métodos HTTP seguros
🔄 Las acciones como logout se realizan por POST, no por GET.

✅ Previene ataques tipo CSRF al cerrar sesión o modificar datos.

✅ 3. Protección contra ataques de fuerza bruta
🚫 Limitamos intentos de login (opcionalmente con django-axes).

🧱 Aunque lo desactivamos en desarrollo, en producción debe activarse.

✅ 4. Protección CSRF habilitada
🧪 Todos los formularios tienen {% csrf_token %}.

🛡 Esto protege contra peticiones maliciosas desde otros sitios.

✅ 5. Gestión segura de sesiones
🔐 Autenticación con sesiones protegidas por Django.

🚪 Cierre de sesión seguro (logout con POST).

📦 Uso de mecanismos de sesión de Django que incluyen:

Expiración de sesiones

Cookies seguras (HttpOnly, Secure, SameSite)

Integración de reCAPTCHA ✅
✔️ Evita que bots creen cuentas de forma automatizada.

🎯 Especialmente importante en formularios públicos (registro, login).