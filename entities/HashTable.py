import faker
from faker import Faker
from random import randint
from entities.ListaEncadeada import ListaEncadeada




class HashTable:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho

    def hashFunction(self, key):
        return key % self.tamanho

    def inserir(self, contaBancaria, nome):
        hashIndex = self.hashFunction(contaBancaria)
        aux = self.tabela[hashIndex]
        if not aux:
            self.tabela[hashIndex] = ListaEncadeada(contaBancaria, nome)
        else:
            while aux.proximo:
                aux = aux.proximo
            aux.proximo = ListaEncadeada(contaBancaria, nome)

    def mostrar(self):
        for i in range(self.tamanho):
            print(f'Index: {i}', end=" | ")
            ListaEncadeada.printLista(self.tabela[i])
            print()

    def search(self, contaBancaria):
        hashIndex = self.hashFunction(contaBancaria)
        encontrado = self.tabela[hashIndex]
        if encontrado:
            while encontrado:
                if encontrado.contaBancaria == contaBancaria:
                    return encontrado
                encontrado = encontrado.proximo

            return None
        else:
            return None

    def searchSemHash(self, contaBancaria):
        for listaEncadeada in self.tabela:
            aux = listaEncadeada
            while aux:
                if aux.contaBancaria == contaBancaria:
                    return aux
                aux = aux.proximo
        return None

    def geraDados(self):
        fake = Faker() # instanciando o faker

        # gerar 993 dados (+ 6 casos de teste = 999)
        for _ in range(993):
            self.inserir(randint(101, 9999), fake.name()) # nossos cassos de teste são abaixo de 101


