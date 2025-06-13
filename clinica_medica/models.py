from django.db import models

class exame(models.Model):
    dataExame = models.DateField()
    horarioExame = models.CharField(max_lenght=45)

class consulta(models.Model):
    dataConsulta = models.DateField()
    horarioConsulta = models.CharField(max_lenght=120)
    motivoConsulta  = models.