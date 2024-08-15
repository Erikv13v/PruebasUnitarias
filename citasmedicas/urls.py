from django.urls import path,include
from rest_framework import routers
from citasmedicas import views

router= routers.DefaultRouter()
router.register(r'Admin',views.AdminViewSet)
router.register(r'Medico',views.MedicoViewSet)
router.register(r'Cita',views.CitaViewSet)
router.register(r'Paciente',views.PacienteViewSet)
router.register(r'Medicamento',views.MedicamentosViewSet)




urlpatterns = [
    path('', include(router.urls))
]

