from django.contrib import admin

from .models import Cita
from .models import Medicamento
from .models import Paciente
from .models import Medico
from .models import Admin1

# Register your models here.



admin.site.register(Admin1)
admin.site.register(Cita)
admin.site.register(Medicamento)
admin.site.register(Paciente)
admin.site.register(Medico)