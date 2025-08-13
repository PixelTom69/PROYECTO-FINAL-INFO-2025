from django.urls import path
from . import views

app_name = 'contacto'

urlpatterns = [
    path('', views.contacto_view, name='contacto'),
    path('listar/', views.listar_contactos, name='listar'),
]