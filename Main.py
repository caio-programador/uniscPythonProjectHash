from entities.HashTable import HashTable
from entities.ListaEncadeada import ListaEncadeada

table = HashTable(17)

table.inserir(27, "Ruan")

table.inserir(53, "Neymar")

table.inserir(28, "Pedro")

table.inserir(54, "Joao")

table.inserir(29, "Gaio")

table.inserir(52, "Prendon")

table.inserir(30, "Luigi")

table.inserir(7, "Kaua")

table.inserir(234, "Andréi")

table.inserir(26, "Staubo")


encontrado = table.search(234)

if encontrado:
    ListaEncadeada.printNodo(encontrado)


table.mostrar()

