from django.urls import path, include
from . import views

urlpatterns = [
    # CRUD
    # acceso por defecto
    path('', views.inicio, name="inicio"), 
    path('process_money', views.process_money), 
]

