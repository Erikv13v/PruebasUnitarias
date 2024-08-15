from rest_framework import viewsets

from .serializer import CitaSerializer
from .serializer import MedicamentoSerializer
from .serializer import MedicoSerializer
from .serializer import PacienteSerializer
from .serializer import AdminSerializer



from .models import Cita
from .models import Medicamento
from .models import Paciente
from .models import Medico
from .models import Admin1

# Create your views here.

class AdminViewSet(viewsets.ModelViewSet):
    queryset= Admin1.objects.all()
    serializer_class= AdminSerializer

class CitaViewSet(viewsets.ModelViewSet):
    queryset= Cita.objects.all()
    serializer_class= CitaSerializer
    

class MedicoViewSet(viewsets.ModelViewSet):
    queryset= Medico.objects.all()
    serializer_class= MedicoSerializer
   
class PacienteViewSet(viewsets.ModelViewSet):
    queryset= Paciente.objects.all()
    serializer_class=PacienteSerializer

class MedicamentosViewSet(viewsets.ModelViewSet):
    queryset=Medicamento.objects.all()
    serializer_class= MedicamentoSerializer
