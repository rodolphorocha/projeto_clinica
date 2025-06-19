from django.db import models

class Exame(models.Model):
    horario_exame = models.DateTimeField()

    def __str__(self):
        return self.horario_exame.strftime("%d/%m/%Y %H:%M")

class Consulta(models.Model):
    horario_consulta = models.DateTimeField()
    motivo_consulta = models.CharField(max_length=120)
    paciente = models.ForeignKey('Paciente', on_delete=models.PROTECT)
    medico = models.ForeignKey('Medico', on_delete=models.PROTECT, null=True, blank=True)


    def __str__(self):
        return f"Consulta {self.paciente.nome_paciente} com {self.medico.nome_medico}"

class Medico(models.Model):
    nome_medico = models.CharField(max_length=120)
    data_nascimento = models.DateField()
    cpf_medico = models.CharField(max_length=11)

    def __str__(self):
        return self.nome_medico

class Paciente(models.Model):
    cpf_paciente = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=16)

    def __str__(self):
        return self.nome_paciente

class Especialidade(models.Model):
    nome_especialidade = models.CharField(max_length=100)
    anos_experiencia = models.IntegerField()

    def __str__(self):
        return self.nome_especialidade

class Medicamento(models.Model):
    nome_medicamento = models.CharField(max_length=100)
    validade = models.DateField()

    def __str__(self):
        return self.nome_medicamento

class Receita(models.Model):
    prescricao = models.CharField(max_length=100)
    data_emissao = models.DateField()
    validade = models.DateField()
    paciente = models.ForeignKey('Paciente', on_delete=models.PROTECT)
    medico = models.ForeignKey('Medico', on_delete=models.PROTECT)
    medicamentos = models.ManyToManyField(Medicamento)

    def __str__(self):
        return f"Receita de {self.paciente.nome_paciente} emitida em {self.data_emissao.strftime('%d/%m/%Y')}"
