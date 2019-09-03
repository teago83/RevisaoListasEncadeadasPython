from node import Node

class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def appendDoParaguai(self, elem):
        # ignora a joça caso já tenham elementos na lista
        if self.head:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(elem)
            # cria o nó mermão
        else:
            self.head = Node(elem)
        self.size = self.size + 1
    #retorna o tamanho pow

    def __len__(self):
        return self.size

    def getnode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("índice da lista fora de alcance")
        return pointer
    def set(self, index, elem):
        pass

    def __getitem__(self, index):
        pointer = self.getnode(index)
        if pointer:
            return pointer.data
        else:
            raise IndexError("índice da lista fora de alcance")

    def __setitem__(self, index, elem):
        pointer = self.getnode(index)
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("índice da lista fora de alcance")

    def indexDoParaguai(self, elem):
        #retorna o índice do elemento na lista
        pointer = self.head
        i = 0
        while pointer:
            if pointer.data == elem:
                return i
            pointer = pointer.next
        raise ValueError("%d não está na lista." % elem)

    def insert(self, index, elem):
        """essa joça funciona assim:
        tu manda o raparigo digitar o índice onde ele quer tacar a joça
        manda ele dizer o elemento pra tacar nesse índice
        GG"""
        node = Node(elem)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self.getnode(index-1)
            node = Node(elem)
            node.next = pointer.next
            pointer.next = node
        self.size = self.size + 1

    def remove(self, elem):
        if self.head is None:
            raise ValueError("Lista vazia!")
        elif self.head.data == elem:
            self.head = self.head.next
            self.size = self.size - 1
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while pointer:
                if pointer.data == elem:
                    ancestor.next = pointer.next
                    pointer.next = None
                ancestor = pointer
                pointer = pointer.next
            self.size = self.size - 1
            return True
        raise ValueError("Elemento %.2f não foi encontrado na lista." % (elem))

    def __repr__(self):
        r = ""
        pointer = self.head
        while pointer:
            r = r + str(pointer.data) + "->"
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()

