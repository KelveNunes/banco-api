from django.db import models
from cliente.models import Cliente

class Conta(models.Model):
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    numero = models.IntegerField(unique=True)
    agencia = models.CharField(max_length=20)
    cliente = models.ForeignKey(Cliente, related_name='contas', on_delete=models.CASCADE)
    
    def saldo_atual(self):
        return self.saldo

    def nova_conta(cls, cliente, numero):
        return cls.objects.create(cliente=cliente, numero=numero)

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.save()

    def depositar(self, valor):
        self.saldo += valor
        self.save()

    def __str__(self):
        return f"Conta {self.numero} - {self.agencia}"
    
class ContaCorrente(Conta):
    limite = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    limite_saques = models.IntegerField(default=3)

    def __str__(self):
        return f"Conta Corrente {self.numero} - Limite: {self.limite}"


