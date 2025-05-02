from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse

from .models import User
import re

def index(request):
    return render(request, 'index.html')

def unsafe_lookup(request):
    rows = None
    error = None

    if request.method == 'GET':
        # Obtén el parámetro 'query' de la solicitud
        user_input = request.GET.get('query', '')

        # Construye una consulta SQL insegura
        query = f"SELECT * FROM users_user WHERE id = {user_input}"

        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
        except Exception as e:
            error = str(e)

        # Renderiza el HTML con los resultados o el error
        return render(request, 'unsafe.html', {'results': rows, 'error': error})
    
def safe_lookup(request):
    result = None
    error = None
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        
        # Validar que el ID es un número
        if not re.match(r'^\d+$', user_id):
            error = "El ID proporcionado no es un número válido."
        else:
            # Consulta parametrizada, segura
            with connection.cursor() as cursor:
                cursor.execute("SELECT first_name, last_name FROM users_user WHERE id = %s", [user_id])
                result = cursor.fetchone()
    
    return render(request, 'safe.html', {'result': result, 'error': error})
