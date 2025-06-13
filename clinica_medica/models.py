from django.db import models

class exame(models.Model):
    dataExame = models.DateField()
    horarioExame = models.CharField(max_lenght=45)

class consulta(models.Model):
    dataConsulta = models.DateField()
    horarioConsulta = models.DateTimeField()
    motivoConsulta  = models.CharField(max_length=120)

class medico(models.Model):
    nomeMedico = models.CharField(max_length=120)
    dataNascimentoM = models.DateField()
    cpfMedico = models.CharField(max_length=11)

class paciente(models.Model):
    cpfPaciente = models.CharField(max_length=11)
    nomePaciente = models.CharField(max_length=120)
    dataNascimentoP = models.DateField()
    telefoneP = models.CharField(max_length=16)

class especialidade(models.Model):
    nomeEspecialidade = models.CharField(max_length=100)
    tempoexperiencia = models.DateTimeField()

class medicamento(models.Model):
    nomeMedicamento = models.CharField(max_length=100)
    validade = models.DateField()

class receita(models.Model):
    prescricao = models.CharField(max_length=100)
    dataEmissao = models.DateField()
    validade = models.DateField()