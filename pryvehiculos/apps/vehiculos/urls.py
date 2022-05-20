from django.urls import path
from apps.vehiculos.views import listVehiculos, vehiculoCreate, vehiculoDelete, vehiculoUpdate

app_name='vehiculos'
urlpatterns = [
    path('', listVehiculos, name= 'listVehiculos'),
    path('nuevo/', vehiculoCreate, name= 'vehiculoCreate'),
    path('delete/<int:id>', vehiculoDelete, name='vehiculoDelete'),
    path('update/<int:id>', vehiculoUpdate, name='vehiculoUpdate'),
]

