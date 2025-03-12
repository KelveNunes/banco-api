from django.db import models
from abc import ABC, abstractmethod

class Transacao(models.Model):
    valor = models.FloatField()
    tipo = models.CharField(max_length=50)

    class Meta:
        abstract = True

class Deposito(Transacao):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    
    def registrar(self, conta):
        conta.saldo += self.valor
        conta.save()
    
    def __str__(self):
        return f"Depósito de {self.valor}"

class Saque(Transacao):
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def registrar(self, conta):
        if conta.saldo >= self.valor:
            conta.saldo -= self.valor
            conta.save()
    
    def __str__(self):
        return f"Saque de {self.valor}"

