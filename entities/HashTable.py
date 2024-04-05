import faker
from faker import Faker
from random import randint
from entities.ListaEncadeada import ListaEncadeada




class HashTable:
    def __init__(self, tamanho):  # construtor
        self.tamanho = tamanho
        self.tabela = [None] * tamanho # cria uma tabela com tudo none

    def hashFunction(self, key): # função hash faz o mod do tamanho da lista
        return key % self.tamanho

    def inserir(self, contaBancaria, nome):  # função responsável por inserir na tabela
        hashIndex = self.hashFunction(contaBancaria)  # pega o index onde será inserido
        aux = self.tabela[hashIndex] # pega o local na tabela com o index
        if not aux: # se estiver vazio então insere no início da lista
            self.tabela[hashIndex] = ListaEncadeada(contaBancaria, nome) # cria o nodo na lista
        else:  # senão, insere no fim da lista
            while aux.proximo:
                aux = aux.proximo
            aux.proximo = ListaEncadeada(contaBancaria, nome) # cria o nodo na lista

    def mostrar(self):  # função responsável por mostrar a tabela
        for i in range(self.tamanho):  # percorre de acordo com o tamanho
            print(f'Index: {i}', end=" | ")
            ListaEncadeada.printLista(self.tabela[i])  # printa a lista
            print()

    def search(self, contaBancaria):  # função de busca utilizando hash
        hashIndex = self.hashFunction(contaBancaria)  # pega o index
        encontrado = self.tabela[hashIndex]  # pega o local na tabela com o index
        if encontrado:  # se achou então percorre a lista para procurar pela conta bancária desejada
            while encontrado:
                if encontrado.contaBancaria == contaBancaria:
                    return encontrado
                encontrado = encontrado.proximo

            return None
        else:
            return None  # retorna nada se não achou

    def searchSemHash(self, contaBancaria):  # função de busca que não usa hash
        for listaEncadeada in self.tabela:
            aux = listaEncadeada
            while aux:
                if aux.contaBancaria == contaBancaria:
                    return aux
                aux = aux.proximo
        return None

    def geraDados(self):  # função responsável por preencher nossa base de dados
        fake = Faker() # instanciando o faker

        # gerar 993 dados
        for _ in range(993):
            self.inserir(randint(101, 9999), fake.name()) # nossos casos de teste são abaixo de 101

    def inserirCasosTeste(self):
        # -------------- CASOS DE TESTE --------------
        self.inserir(52, "Prendon")
        self.inserir(29, "Gaio")
        self.inserir(26, "Staubo")

        self.inserir(7, "Kaua")
        self.inserir(13, "Andréi")
        # ---------------------------------------------


