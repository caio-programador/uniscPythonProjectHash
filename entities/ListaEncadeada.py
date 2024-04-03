
class ListaEncadeada:

    def __init__(self, contaBancaria, nome):
        self.contaBancaria = contaBancaria
        self.nome = nome
        self.proximo = None

    @staticmethod
    def printLista(lista):
        while lista:
            print(f'Conta Bancária: {lista.contaBancaria} Nome: {lista.nome}', end=" -> ")
            lista = lista.proximo

    @staticmethod
    def printNodo(nodo):
        print(f'Conta Bancária: {nodo.contaBancaria} Nome: {nodo.nome}')
