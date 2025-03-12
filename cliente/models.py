from django.db import models

class Cliente(models.Model):
    endereco = models.CharField(max_length=255)
    
    def __str__(self):
        return f"Cliente: {self.id} - {self.endereco}"

class PessoaFisica(Cliente):
    cpf = models.CharField(max_length=11, unique=True)
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()

    def __str__(self):
        return f"Pessoa Física: {self.nome} - CPF: {self.cpf}"

