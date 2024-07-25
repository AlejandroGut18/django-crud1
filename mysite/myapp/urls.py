from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarMoto/', views.registrarMoto),
    path('eliminarMoto/<int:moto_id>', views.eliminarMoto),
    path('edicionMoto/<int:moto_id>', views.edicionMoto),
    path('editMoto/<int:moto_id>', views.editMoto),
    
]
