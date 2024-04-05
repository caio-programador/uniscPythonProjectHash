from entities.HashTable import HashTable
from entities.ListaEncadeada import ListaEncadeada
from time import time



table = HashTable(17) # instanciando a hash table

# -------------- CASOS DE TESTE --------------
table.inserir(52, "Prendon")
table.inserir(29, "Gaio")
table.inserir(26, "Staubo")

table.inserir(7, "Kaua")
table.inserir(13, "Andréi")
# ---------------------------------------------

table.geraDados()

table.inserir(100, "Luigi")

inicioHash = time() # captura tempo no inicio
encontrado = table.search(100)
fimHash = time() # captura tempo após executar funcão de busca
tempoDeProcuraHash = fimHash - inicioHash # calcula tempo de procura total

inicio = time() # captura tempo no inicio
table.searchSemHash(100)
fim = time() # captura tempo após executar funcão de busca
tempoDeProcura = fim - inicio # calcula tempo de procura total



if encontrado:
    print("--=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=")
    ListaEncadeada.printNodo(encontrado)
    print(f"Tempo de procura com o hash: {tempoDeProcuraHash}")
    print(f"Tempo de procura sem o hash: {tempoDeProcura}")
    print("--=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=")


table.mostrar()


