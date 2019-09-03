"""2) Escreva uma TAD de lista de inteiros ordenada simplesmente encadeada com as seguintes operações:
a)	Verificar se um número pertence lista;
b)	Inserir um novo elemento na lista mantendo a ordem;
c)	Remover um elemento da lista;
d)	Imprimir os valores da lista;
e)	Copiar uma lista l1 para uma lista l2;
f)	Concatenar uma lista l1 com uma lista l2;
g)	Intercalar l1 e l2;
"""

from linkedlist import LinkedList

onze = LinkedList()
doze = LinkedList()


def a():
    batatinha = False
    if onze.__len__() == 0:
        print("A lista está vazia!")
        pass
    else:
        numero = int(input("Digite o número pelo qual queres procurar:"))
        for i in range(onze.__len__()):
            if onze[i] == numero:
                print("Número %d encontrado com sucesso na posição %d." % (numero, i))
                batatinha = True
    if batatinha == False:
        print("O número %d não foi encontrado na lista." % numero)


def b():
    while True:
        try:
            onze.appendDoParaguai(int(input("Digite o número a ser inserido ao fim da lista:")))
        except ValueError:
            print("Valor inválido. Só valores inteiros são aceitos.")
        break


def c():
    if onze.__len__() == 0:
        print("A lista está vazia!")
        pass
    while True:
        try:
            numero_remocao = int(input("Digite o número a ser removido da lista:"))
            for i in range(onze.__len__()):
                if onze[i] == numero_remocao:
                    onze.remove(onze[i])
                    onze.size -= 1
                    print("Número %d removido com sucesso da lista." % numero_remocao)
                    break
        except ValueError:
            print("Valor inválido. Só valores inteiros são aceitos.")


def d():
    if onze.__len__() == 0:
        print("A lista está vazia!")
        pass
    for i in range(onze.__len__()):
        print("Valor número %d: %d" % (i, onze[i]))


def e():
    if onze.__len__() == 0:
        print("A lista está vazia!")
        pass
    for i in range(onze.__len__()):
        doze.appendDoParaguai(onze[i])
    print("Lista 11 copiada para a lista 12 com sucesso.")


def f():
    if onze.__len__() == 0:
        print("A lista está vazia!")
        pass
    if onze.__len__() != doze.__len__():
        e()
    print("Concatenação das listas 11 e 12:\n")
    for i in range(onze.__len__()):
        print("Valor número %d: %d" % (i, onze[i]))
    for i in range(doze.__len__()):
        print("Valor número %d: %d" % (i+onze.__len__(), doze[i]))


def g():
    if onze.__len__() == 0:
        print("A lista está vazia!")
        pass
    treze = LinkedList()
    if onze.__len__() != doze.__len__():
        e()
    for i in range((onze.__len__())*2):
        if i % 2 != 0:
            treze.appendDoParaguai(onze[i])
        if i % 2 == 0:
            treze.appendDoParaguai(doze[i])
    for i in range(treze.__len__()):
        print("Valor número %d: %d\n" % (i, treze[i]))


def menu():
    print("MENU DE OPÇÕES:\n"
          "a) Verificar se um número pertence à lista\n"
          "b) Inserir um novo elemento mantendo a ordem\n"
          "c) Remover um elemento da lista\n"
          "d) Imprimir os valores da lista\n"
          "e) Copiar uma lista 11 para uma lista 12\n"
          "f) Concatenar uma lista 11 com uma lista 12\n"
          "g) Intercalar 11 e 12\n"
          "h) Sair")
    while True:
        op = input("\nEscolha a opção desejada:\n").upper()
        if op == "A":
            a()
        elif op == "B":
            b()
        elif op == "C":
            c()
        elif op == "D":
            d()
        elif op == "E":
            e()
        elif op == "F":
            f()
        elif op == "G":
            g()
        elif op == "H":
            exit()
        else:
            print("Opção inexistente. Tente novamente.")


while True:
    menu()
