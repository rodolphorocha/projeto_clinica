from django.contrib import admin
from .models import Exame, Consulta, Medico, Paciente, Especialidade, Medicamento, Receita, ReceitaMedicamento


admin.site.register(Exame)
admin.site.register(Consulta)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Especialidade)
admin.site.register(Medicamento)
admin.site.register(Receita)
admin.site.register(ReceitaMedicamento)