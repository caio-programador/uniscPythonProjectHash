from entities.HashTable import HashTable
from entities.ListaEncadeada import ListaEncadeada
from time import time


def mostraEncontrado(encontrado, tempoDeProcuraHash, tempoDeProcura):
    if encontrado:  # se achou o encontrado printa ele e o tempo de resposta
        print("--=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=")
        ListaEncadeada.printRegistro(encontrado)
        print(f"Tempo de procura com o hash: {tempoDeProcuraHash}")
        print(f"Tempo de procura sem o hash: {tempoDeProcura}")
        print("--=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=")
    else:  # senão printa o tempo de resposta
        print("--=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=")
        print("Não existe nenhuma pessoa com esta conta bancária")
        print(f"Tempo de procura com o hash: {tempoDeProcuraHash}")
        print(f"Tempo de procura sem o hash: {tempoDeProcura}")
        print("--=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=")


def main():
    table = HashTable(17)  # instanciando a hash table

    table.geraDados()

    table.inserirCasosTeste()
    for _ in range(6):
        table.mostrar()

        inicioHash = time()  # captura tempo no inicio
        fimHash = time()  # captura tempo após executar funcão de busca
        encontrado = table.search(int(input("Qual conta bancária deseja encontrar? ")))
        tempoDeProcuraHash = fimHash - inicioHash  # calcula tempo de procura total

        inicio = time()  # captura tempo no inicio
        table.searchSemHash(26)
        fim = time()  # captura tempo após executar funcão de busca
        tempoDeProcura = fim - inicio  # calcula tempo de procura total

        print()

        mostraEncontrado(encontrado, tempoDeProcuraHash, tempoDeProcura)


main()
