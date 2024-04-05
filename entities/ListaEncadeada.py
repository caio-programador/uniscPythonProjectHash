
class ListaEncadeada:

    def __init__(self, contaBancaria, nome):  # construtor
        self.contaBancaria = contaBancaria
        self.nome = nome
        self.proximo = None

    @staticmethod
    def printLista(lista):
        while lista:  # caminha pela lista e printa ela
            print(f'Conta Bancária: {lista.contaBancaria} Nome: {lista.nome}', end=" -> ")
            lista = lista.proximo

    @staticmethod
    def printRegistro(registro):
        print(f'Conta Bancária: {registro.contaBancaria} Nome: {registro.nome}')
