# Proyecto de Seguridad: Prevención de SQL Injection con Django

## Contextualización del Proyecto

Este proyecto es una aplicación web desarrollada con Django cuyo objetivo es **exponer la vulnerabilidad de SQL Injection** y mostrar **buenas prácticas de desarrollo seguro** para evitarla. A través de dos formularios (uno vulnerable y otro protegido), se ejemplifica cómo un sistema puede ser comprometido si no se siguen principios de seguridad fundamentales, especialmente aquellos definidos por **OWASP SQL Injection Cheat Sheet**.

---

## Instrucciones para Iniciar el Proyecto

Sigue estos pasos para ejecutar el proyecto en tu entorno local:

### 1. Clona el repositorio (si aplica)

```bash
git clone <url-del-repo>
cd <nombre-del-proyecto>
```

### 2. Crea un entorno virtual

```bash
python -m venv env
```

### 3. Activa el entorno virtual

- En Windows:
  ```bash
  env\Scripts\activate
  ```

- En macOS/Linux:
  ```bash
  source env/bin/activate
  ```

### 4. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 5. Ejecuta las migraciones y carga los datos

```bash
python manage.py makemigrations
python manage.py migrate
```


### 6. Crea un superusuario (opcional para acceder al admin)

```bash
python manage.py createsuperuser
```

### 7. Ejecuta el servidor

```bash
python manage.py runserver
```

---

## Estructura del Proyecto y Pantallas

La aplicación tiene dos rutas principales:

- `http://127.0.0.1:8000/unsafe/` → **Pantalla vulnerable (Unsafe)**
- `http://127.0.0.1:8000/safe/` → **Pantalla segura (Safe)**

### Pantalla Unsafe

- Recibe un `user_id` desde un formulario HTML.
- Realiza una consulta SQL sin parametrización.
- **Vulnerable a ataques de SQL Injection.**
- Si se envia por ejemplo "1 OR 1=1" se muestran todos los usuarios

### Pantalla Safe

- También recibe un `user_id` desde un formulario HTML.
- Utiliza consultas SQL parametrizadas correctamente.
- **No es vulnerable a ataques de inyección SQL.**

---

## Cómo Explotar la Vulnerabilidad en la Pantalla Unsafe

Accede a `http://127.0.0.1:8000/unsafe/` y prueba los siguientes casos en el campo del formulario:

### 1. Obtener todos los usuarios (bypass lógico)

```sql
1 OR 1=1
```

Esto devolverá todos los registros de la base de datos, eludiendo la validación del ID.

### 2. Eliminar la tabla de usuarios (ataque destructivo)

```sql
1; DROP TABLE users_user
```

Este ataque intenta ejecutar dos instrucciones: obtener un usuario y luego eliminar toda la tabla `users_user`.

> ⚠️ **Este tipo de ataque demuestra por qué no se deben construir consultas SQL concatenando directamente el input del usuario.**

---

## Buenas Prácticas Implementadas en la Pantalla Safe

La pantalla segura implementa varias buenas prácticas basadas en la [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html):

1. **Uso de consultas parametrizadas** (`cursor.execute(sql, [params])`)
2. **Separación de datos y comandos SQL**
3. **Validación de entrada estricta (solo se acepta ID numérico)**
4. **No uso de concatenación de cadenas para construir consultas**
5. **Principio de menor privilegio aplicado (no hay comandos peligrosos permitidos)**
6. **Uso de meotod POST y no GET**

---

## Recursos

- 🛡️ OWASP SQL Injection Cheat Sheet:  
  https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html
- 📚 Documentación de Django sobre seguridad:  
  https://docs.djangoproject.com/en/stable/topics/security/

---

## Autor

**Nelson Felipe Barco**  
Curso: Seguridad en el Desarrollo