
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        # self é a referência que sabe onde encontrar o objeto em memória.
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    # A assinatura dos métodos obrigatoriamente terão como primeiro argumento self que nada mais é do que o
    # this do Python. Entretanto, esse parâmetro não é passado explicitamente quando o método é chamado.
    # Por exemplo: para se chamar o método deposita em uma instância chamada conta, deve se fazer:
    #
    # conta.deposita(100.0)
    #
    # Somente o valor a ser depositado é passado. O Python infere o 'self' como sendo a instância através da
    # qual o método está sendo chamado que, no exemplo acima, é 'conta'.
    #
    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor

    def extrato(self):
        print("O saldo da conta do titulo {} é {}".format(self.titular, self.saldo))

#
# Classe do desafio opcional
#
class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        print("{}/{}/{}".format(self.dia, self.mes, self.ano))