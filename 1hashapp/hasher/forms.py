from django import forms

class HashForm(forms.Form):
    palabra = forms.CharField(label="Ingrese una palabra", max_length=100)
    algoritmo = forms.ChoiceField(
        label="Seleccione algoritmo",
        choices=[("sha256", "SHA-256"), ("argon2", "Argon2")]
    )