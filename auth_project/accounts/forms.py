from django import forms
from django.contrib.auth.models import User
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re


class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput,
        help_text="La contraseña debe tener al menos 8 caracteres, incluir mayúsculas, minúsculas y caracteres especiales.",
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput,
        help_text="Repite la contraseña.",
    )
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)  # Agrega el campo captcha

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if len(username) < 5:
            raise ValidationError("El nombre de usuario debe tener al menos 5 caracteres.")
        return username

    def clean_password1(self):
        password = self.cleaned_data.get("password1")
        if len(password) < 8:
            raise ValidationError("La contraseña debe tener al menos 8 caracteres.")
        if not re.search(r"[A-Z]", password):
            raise ValidationError("La contraseña debe incluir al menos una letra mayúscula.")
        if not re.search(r"[a-z]", password):
            raise ValidationError("La contraseña debe incluir al menos una letra minúscula.")
        if not re.search(r"[0-9]", password):
            raise ValidationError("La contraseña debe incluir al menos un número.")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            raise ValidationError("La contraseña debe incluir al menos un carácter especial.")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Las contraseñas no coinciden.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])  # Encripta la contraseña
        if commit:
            user.save()
        return user


class CustomLoginForm(AuthenticationForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())