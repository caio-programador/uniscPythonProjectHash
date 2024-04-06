from entities.TabelaHash import TabelaHash
from entities.ListaEncadeada import ListaEncadeada
from time import time


def mostraEncontrado(encontrado, tempoDeProcuraHash, tempoDeProcura):
    print("--=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=")

    if encontrado:  # se achou o encontrado printa ele e o tempo de resposta
        ListaEncadeada.printRegistro(encontrado)
    else:  # senão printa o tempo de resposta
        print("Não existe nenhuma pessoa com esta conta bancária")

    print(f"Tempo de procura com o hash: {tempoDeProcuraHash} segundo(s) ou " + "%.9f segundo(s)" % tempoDeProcuraHash)
    print(f"Tempo de procura sem o hash: {tempoDeProcura} segundo(s) ou " + "%.9f segundo(s)" % tempoDeProcura)
    print("--=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=")
    print()
    input("Pressione qualquer tecla...  ")
    print()


def main():
    tabela = TabelaHash(17)  # instanciando a hash tabela

    tabela.geraDados()

    tabela.inserirCasosTeste()
    for _ in range(6):
        tabela.mostrar()
        contaBancaria = int(input("Qual conta bancária deseja buscar? "))
        inicioHash = time()  # captura tempo no inicio
        encontrado = tabela.busca(contaBancaria)
        fimHash = time()  # captura tempo após executar funcão de busca
        tempoDeProcuraHash = fimHash - inicioHash  # calcula tempo de procura total

        inicio = time()  # captura tempo no inicio
        tabela.buscaSemHash(contaBancaria)
        fim = time()  # captura tempo após executar funcão de busca
        tempoDeProcura = fim - inicio  # calcula tempo de procura total

        print()

        mostraEncontrado(encontrado, tempoDeProcuraHash, tempoDeProcura)


main()
