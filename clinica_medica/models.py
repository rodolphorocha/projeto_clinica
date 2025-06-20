from django.db import models

class Especialidade(models.Model):
    nome = models.CharField(max_length=100)
    anos_experiencia = models.IntegerField()

    def __str__(self):
        return self.nome


class Medico(models.Model):
    nome = models.CharField(max_length=120)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    especialidade = models.ForeignKey(Especialidade, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nome} ({self.especialidade})"


class Paciente(models.Model):
    nome = models.CharField(max_length=120)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=16)
    endereco = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, related_name='consultas')
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT, null=True, blank=True, related_name='consultas')
    horario = models.DateTimeField()
    motivo = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.horario.strftime('%d/%m/%Y %H:%M')} - {self.paciente.nome} com {self.medico.nome}"


class Exame(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE, related_name='exames')
    horario = models.DateTimeField()

    def __str__(self):
        return f"Exame em {self.horario.strftime('%d/%m/%Y %H:%M')}"


class Medicamento(models.Model):
    nome = models.CharField(max_length=100)
    validade = models.DateField()

    def __str__(self):
        return self.nome


class Receita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT)
    data_emissao = models.DateField()
    validade = models.DateField()

    def __str__(self):
        return f"Receita de {self.paciente.nome} em {self.data_emissao.strftime('%d/%m/%Y')}"


class ReceitaMedicamento(models.Model):
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE, related_name='itens')
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    posologia = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.quantidade}x {self.medicamento.nome} para {self.receita.paciente.nome}"
