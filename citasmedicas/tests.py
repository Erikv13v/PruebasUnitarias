import os
import sys
import django
import coverage

# Inicia la medición de cobertura
cov = coverage.Coverage(source=['citasmedicas'])  # Reemplaza 'citasmedicas' con el nombre de tu app si es diferente
cov.start()

# Configurar el entorno Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'citasmedicas_rest.settings')
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
django.setup()

# Importaciones de Django
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.reverse import reverse

# Importaciones de los modelos y componentes de la aplicación
from citasmedicas.models import Medico, Paciente
from citasmedicas.serializers import MedicoSerializer, PacienteSerializer
from citasmedicas.views import MedicoViewSet, PacienteViewSet

# Pruebas para los modelos
class MedicoViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        Medico.objects.create(nombre="Jordan", apellido="Villao", edad=21, especialidad="Doctor")

    def test_obtener_todos_los_medicos(self):
        response = self.client.get('http://127.0.0.1:8000/api/Medical/Medico/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

class PacienteViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        Paciente.objects.create(nombre="Anthony", apellido="Ramirez", edad=22, correo="anthony@gmail.com", alergia="Dolor de la vista")

    def test_obtener_todos_los_pacientes(self):
        response = self.client.get('http://127.0.0.1:8000/api/Medical/Paciente/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

# Pruebas para serializers
class SerializerTestCase(TestCase):
    def test_medico_serializer(self):
        medico = Medico.objects.create(nombre="Test", apellido="Doctor", edad=30, especialidad="Cardiología")
        serializer = MedicoSerializer(medico)
        self.assertEqual(serializer.data['nombre'], "Test")
        self.assertEqual(serializer.data['apellido'], "Doctor")

    def test_paciente_serializer(self):
        paciente = Paciente.objects.create(nombre="Test", apellido="Paciente", edad=25, correo="test@correo.com", alergia="Ninguna")
        serializer = PacienteSerializer(paciente)
        self.assertEqual(serializer.data['nombre'], "Test")
        self.assertEqual(serializer.data['apellido'], "Paciente")

# Pruebas para las URLs
class URLTestCase(TestCase):
    def test_medico_list_url(self):
        url = reverse('medico-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_paciente_list_url(self):
        url = reverse('paciente-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

# Detener la medición de cobertura y mostrar el informe
cov.stop()
cov.save()

# Mostrar el reporte de cobertura en la terminal
cov.report()

# Verificar que la cobertura sea al menos del 60%
cov_fail_under = 60.0
coverage_percentage = cov.report()
if coverage_percentage < cov_fail_under:
    sys.exit("ERROR: La cobertura de código es inferior al 60%.")
