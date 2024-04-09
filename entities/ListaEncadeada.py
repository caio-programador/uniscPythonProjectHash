
class ListaEncadeada:

    def __init__(self, contaBancaria, nome):  # construtor
        self.contaBancaria = contaBancaria
        self.nome = nome
        self.proximo = None

    @staticmethod
    def printLista(lista):
        while lista:  # caminha pela lista e printa cada elemento dela
            print(f'Conta Bancária: {lista.contaBancaria} Nome: {lista.nome}', end=" -> ")
            lista = lista.proximo

    @staticmethod
    def printRegistro(registro):  # função de printar um elemento da lista
        print(f'Conta Bancária: {registro.contaBancaria} Nome: {registro.nome}')
