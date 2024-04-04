from entities.HashTable import HashTable
from entities.ListaEncadeada import ListaEncadeada



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

encontrado = table.search(52)

if encontrado:
    ListaEncadeada.printNodo(encontrado)


table.mostrar()

