
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        # self é a referência que sabe onde encontrar o objeto em memória.
        #
        # Ao se preceder o nome de um atributo com dois underlines (__) o Python torna o atributo
        # pseudo privado. É pseudo porque o que o Python faz é mudar a forma de acessar o atributo.
        # Por exemplo: sem o __ o atributo saldo pode ser acesso através de conta.saldo ao passo que, com
        # o __ o acesso passa ser feito através de conta.__Conta__saldo.
        # O grande problema é que ainda assim o valor de um atributo poderia ser modificado diretamente.
        # Basicamente a forma na mudança de acesso ao atributo serve apenas para um alerta do desenvolvedor
        # pois, com a sintaxe conta.__Conta__saldo fica claro que o atributo não deveria ser acessado
        # diretamente.
        #
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

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
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def extrato(self):
        print("O saldo da conta do titulo {} é {}".format(self.__titular, self.__saldo))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, valor):
        self.__limite = valor
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