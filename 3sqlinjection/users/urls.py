from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('unsafe/', views.unsafe_lookup, name='unsafe_lookup'),
    path('safe/', views.safe_lookup, name='safe_lookup'),
]
