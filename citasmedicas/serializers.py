# citasmedicas/serializers.py

from rest_framework import serializers
from .models import Medico, Paciente

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ['nombre', 'apellido', 'edad', 'especialidad']

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'edad', 'correo', 'alergia']
