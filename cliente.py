class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    #
    # A anotação @property abaixo define uma forma especial de método getter. Sem a anotação, para chamar o método
    # nome seria necessário escrever cliente.nome(). Com @property o método nome pode ser chamado com a sintaxe
    # cliente.nome.
    #
    @property
    def nome(self):
        return self.__nome.title()

    #
    # Com relação a métodos setter, a sintaxe é um pouco diferente. A anotação deve conter o nome do atributo
    # que será modificado pelo método seguido de .setter. Porém, o funcionamento é o mesmo: para alterar
    # o valor de um atributo anotado com @setter, basta referenciá-lo diretamente com .nomeatributo. Por exemplo:
    # cliente.nome = 'John Armless'.
    #
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
