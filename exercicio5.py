"""5) Implemente a estrutura Conjunto Inteiros através de uma lista duplamente encadeada cujos nós armazenam
inteiros e com as operações típicas de união, interseção, diferença e soma. """

from doublylinkedlist import DoublyLinkedList

CI1 = DoublyLinkedList()
CI2 = DoublyLinkedList()


def addConjunto1():
    op2 = int(input("Prefere adicionar ao início ou ao fim da lista?"
                    "\nInício = 1"
                    "\nFim = 2"))
    if op2 is 1:
        try:
            CI1.prepend(int(input("Digite o número a ser inserido no início da lista:")))
        except ValueError:
            print("Valor inválido. Só valores inteiros são aceitos.")
    if op2 is 2:
        try:
            CI1.append(int(input("Digite o número a ser inserido no fim da lista:")))
        except ValueError:
            print("Valor inválido. Só valores inteiros são aceitos.")


def addConjunto2():
    op2 = int(input("Prefere adicionar ao início, ou ao fim da lista?"
                    "\nInício = 1"
                    "\nFim = 2"))
    if op2 is 1:
        try:
            CI2.prepend(int(input("Digite o número a ser inserido no início da lista:")))
        except ValueError:
            print("Valor inválido. Só valores inteiros são aceitos.")
    if op2 is 2:
        try:
            CI2.append(int(input("Digite o número a ser inserido no fim da lista:")))
        except ValueError:
            print("Valor inválido. Só valores inteiros são aceitos.")


def uniao():
    for i in range(CI1.__len__()):
        print("Valor número %d da união dos dois conjuntos: %d" % (i, CI1.__getitem__(i)))
    for i in range(CI2.__len__()):
        print("Valor número %d da união dos dois conjuntos: %d" % (i+CI1.__len__(), CI2.__getitem__(i)))


def intersecao():
    batata = 0
    CIU = DoublyLinkedList()
    while batata < (CI1.__len__() + CI2.__len__()):
        if CI1.__getitem__(batata) == CI2.__getitem__(batata):
            CIU.append(CI1.__getitem__(batata))
            CIU.size = CIU.size + 1
        elif CI1.__getitem__(batata-1) == CI2.__getitem__(batata):
            CIU.append(CI1.__getitem__(batata))
            CIU.size = CIU.size + 1
        elif CI1.__getitem__(batata) == CI2.__getitem__(batata-1):
            CIU.append(CI2.__getitem__(batata))
            CIU.size = CIU.size + 1
    for i in range(CIU.__len__()):
        print("Valor número %d da união dos dois conjuntos: %d" % (i, CIU.__getitem__(i)))


def diferenca():
    batata = 0
    while batata < (CI1.__len__() + CI2.__len__()):
        if CI1
    pass


def menu():
    print("MENU:"
          "\n1) União"
          "\n2) Interseção"
          "\n3) Diferença"
          "\n4) Sair")
    try:
        op = int(input("Digite a opção desejada:"))
    except ValueError:
        print("Valor inválido.")

    if op is 1:
        uniao()
    elif op is 2:
        intersecao()
    elif op is 3:
        diferenca()
    elif op is 4:
        exit()


while True:
    while True:
        try:
            arroz = int(input("Defina quantos números adicionarás a ambos os conjuntos:"))
        except ValueError:
            print("Valor inválido.")

    for i in range(arroz):
        addConjunto1()
    for i in range(arroz):
        addConjunto2()

    menu()
