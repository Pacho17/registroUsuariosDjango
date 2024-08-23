from django.urls import path
from .views import registerUser,listarUsuario

urlpatterns = [
    path("registrar/", registerUser, name='RegisterUser'),
    path('listarUsuario/',listarUsuario,name='listarUsuario')
]
