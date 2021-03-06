
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
        if(self.saque_permitido(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} ultrapassa seu limite disponível para saque".format(valor))

    def extrato(self):
        print("O saldo da conta do titulo {} é {}".format(self.__titular, self.__saldo))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    #
    # Assim como ocorre com atributos, ao se preceder o nome de um método dois sinais de underline (__)
    # o Python passa a definir o nome do método como sendo _Classe__nome_do_metodo. No exemplo abaixo
    # o método passa a ser referenciado por _Conta__saque_permitido. E também como acontece com atributos,
    # isso não impede que o método seja acessado externamente à classe. A nova referência ao método serve
    # apenas como um alerta para o desenvolvedor, indicando a ele que trata-se de um método privado.
    #
    def __saque_permitido(self, valor_a_sacar):
        saldo_disponivel_para_saque = self.saldo + self.limite
        return valor_a_sacar <= saldo_disponivel_para_saque

    #
    # Vide observações na classe Cliente para compreender o papel das anotações @property e @atributo.setter
    #
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    #
    # A anotação para definir um método como estático é @staticmethod
    #
    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {"BB": "001", "Caixa": "104", "Bradesco": "237"}
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