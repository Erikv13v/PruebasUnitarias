from rest_framework import serializers

from .models import Cita
from .models import Medicamento
from .models import Paciente
from .models import Medico
from .models import Admin1



class AdminSerializer (serializers.ModelSerializer):
    class Meta:
        model = Admin1
        fields = ('usuario','correo','contraseña')
        
        
class CitaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = ('paciente','medico','fecha','hora')
        
    
        
        
class MedicamentoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = ('nombre','marca','costo')
        
        
class PacienteSerializer (serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ('nombre','apellido','edad','correo','alergia')
        
        
class MedicoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ('nombre','apellido','edad','especialidad')