from django.db import models
from conta.models import Conta
from transacao.models import Deposito, Saque 

class Historico(models.Model):

    transacoes_deposito = models.ManyToManyField(Deposito, through='TransacaoHistorico', blank=True)
    transacoes_saque = models.ManyToManyField(Saque, through='TransacaoHistorico', blank=True)
    conta = models.OneToOneField(Conta, on_delete=models.CASCADE)

    def adicionar_transacao(self, transacao):
        if isinstance(transacao, Deposito):
            self.transacoes_deposito.add(transacao)
        elif isinstance(transacao, Saque):
            self.transacoes_saque.add(transacao)
    
    def __str__(self):
        return f"Histórico de {self.conta.numero}"

class TransacaoHistorico(models.Model):
    historico = models.ForeignKey(Historico, on_delete=models.CASCADE)
    transacao_deposito = models.ForeignKey(Deposito, null=True, blank=True, on_delete=models.CASCADE)
    transacao_saque = models.ForeignKey(Saque, null=True, blank=True, on_delete=models.CASCADE)
    data_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transação histórica registrada em {self.data_registro}"

