from entities.HashTable import HashTable
from entities.ListaEncadeada import ListaEncadeada
from time import time, sleep



table = HashTable(17) # instanciando a hash table

# -------------- CASOS DE TESTE --------------
table.inserir(52, "Prendon")
table.inserir(29, "Gaio")
table.inserir(26, "Staubo")
table.inserir(100, "Luigi")
table.inserir(7, "Kaua")
table.inserir(13, "Andréi")
# ---------------------------------------------

table.geraDados()

inicio = time() # captura tempo no inicio
encontrado = table.search(52)
fim = time() # captura tempo após executar funcão de busca
tempoDeProcura = fim - inicio # calcula tempo de procura total


if encontrado:
    print("--=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=")
    ListaEncadeada.printNodo(encontrado)
    print(f"Tempo de procura: {tempoDeProcura}")
    print("--=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=")


table.mostrar()


