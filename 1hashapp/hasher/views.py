from django.shortcuts import render
from .forms import HashForm
import hashlib
from django.contrib.auth.hashers import make_password

def hash_view(request):
    hash_result = None

    if request.method == "POST":
        form = HashForm(request.POST)
        if form.is_valid():
            palabra = form.cleaned_data["palabra"]
            algoritmo = form.cleaned_data["algoritmo"]

            if algoritmo == "sha256":
                hash_result = hashlib.sha256(palabra.encode()).hexdigest()
            elif algoritmo == "argon2":
                hash_result = make_password(palabra)  # Django usa Argon2 por defecto

    else:
        form = HashForm()

    return render(request, "hasher/hash_form.html", {"form": form, "hash_result": hash_result})
