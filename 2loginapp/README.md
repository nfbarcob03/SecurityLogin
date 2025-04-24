# Seguridad en el Desarrollo - Ejercicio de Autenticación

**Autor:** Nelson Felipe Barco Benavides  
**CC:** 1040749494  
**Curso:** Seguridad en el Desarrollo

---

## 🛠️ ¿Cómo correr el programa?

1. Tener Python instalado.
2. Crear un ambiente virtual:

   ```bash
   python -m venv env
   ```

3. Activar el ambiente virtual:

   - En Windows:

     ```bash
     env\Scripts\activate
     ```

   - En Unix/Mac:

     ```bash
     source env/bin/activate
     ```

4. Instalar las librerías requeridas:

   ```bash
   pip install -r requirements.txt
   ```

5. Correr la aplicación:

   ```bash
   python manage.py runserver
   ```

6. Ingresar a la app en el navegador:

   ```
   http://127.0.0.1:8000/accounts/login
   ```

7. Crear una nueva cuenta (en el enlace **¿No tienes cuenta? Regístrate**).
8. Después de crear la cuenta, hacer login.
9. Si desea usar un usuario ya  creado puede usar el siguiente: usuario felipe3, contraseña: Barco9503*

---

## 🔍 Verificar almacenamiento seguro del usuario

1. Crear un superusuario:

   ```bash
   python manage.py createsuperuser
   ```

   Un ejemplo de usuario/contraseña válido: `felipe33` / `felipe33`

2. Ingresar al panel de administración:

   ```
   http://127.0.0.1:8000/admin/
   ```

3. Verificar que la contraseña esté correctamente encriptada y que el usuario esté guardado.

---

## ✅ ¿Qué se implementó?

### 🔐 1. Ocultar detalles en mensajes de error

- **Siempre mostrar:** `"Usuario y/o contraseña incorrectos"`.
- ✅ Evita la enumeración de usuarios.

---

### 🔄 2. Uso de métodos HTTP seguros

- **Logout se hace por POST, no por GET.**
- ✅ Previene ataques CSRF al cerrar sesión.

---

### 🚫 3. Protección contra fuerza bruta

- **Limitamos intentos de login.**
- ⚠️ Aunque desactivado en desarrollo, **se recomienda activarlo en producción** (por ejemplo, con `django-axes`).

---

### 🧪 4. Protección CSRF habilitada

- Todos los formularios usan `{% csrf_token %}`.
- ✅ Protege contra peticiones maliciosas desde otros sitios.

---

### 📦 5. Gestión segura de sesiones

- Autenticación usando sesiones protegidas por Django.
- Logout seguro (por POST).
- Uso de cookies seguras:
  - `HttpOnly`
  - `Secure`
  - `SameSite`

---

### 🤖 Integración de reCAPTCHA

- ✅ En formularios de **registro** y **login**.
- ✅ Previene la creación de cuentas por bots.

---

💡 **Este proyecto demuestra prácticas de seguridad en autenticación para aplicaciones web construidas con Django.**
