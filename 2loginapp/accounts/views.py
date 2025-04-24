from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import requests

# En accounts/views.py
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomLoginForm  # Importa tu formulario personalizado



from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
import requests

from django.contrib.auth.views import LoginView
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

import requests
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

@login_required
def profile(request):
    return render(request, "accounts/profile.html")


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario creado correctamente.")
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        captcha_response = request.POST.get('g-recaptcha-response')

        # Verificar el reCAPTCHA con Google
        payload = {
            'secret': settings.RECAPTCHA_PRIVATE_KEY,
            'response': captcha_response
        }
        verify_url = 'https://www.google.com/recaptcha/api/siteverify'
        verify_response = requests.post(verify_url, data=payload, verify=False)
        result = verify_response.json()

        # Si el reCAPTCHA no es válido, mostrar mensaje de error
        if not result.get('success'):
            messages.error(request, 'Por favor, confirma que no eres un robot.')
            return redirect('login')  # Redirige al login si el reCAPTCHA falla

        if form.is_valid():
            # Autenticación del usuario
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('profile')  # Redirige al perfil si el login es exitoso
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')

    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'accounts/login.html'
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)