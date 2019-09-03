from node import Node


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def getnode(self, index):
        current = self.head
        for i in range(index):
            if current:
                current = current.next
            else:
                raise IndexError("índice da lista fora de alcance")
        return current

    def __getitem__(self, index):
        current = self.getnode(index)
        if current:
            return current.data
        else:
            raise IndexError("índice da lista fora de alcance")

    def __setitem__(self, index, elem):
        current = self.getnode(index)
        if current:
            current.data = elem
        else:
            raise IndexError("índice da lista fora de alcance")

    def indexDoParaguai(self, elem):
        #retorna o índice do elemento na lista
        current = self.head
        i = 0
        while current:
            if current.data == elem:
                return i
            current = current.next
        raise ValueError("%d não está na lista." % elem)

    def append(self, data):
        if self.head is None:
            new_node = Node(data) #primeiro nó é criado no caso da lista estar vazia
            new_node.prev = None  #anterior vai ser None porque não vai ter nada antes dele
            new_node.next = None  #não tem nada depois também, ainda
            self.head = new_node  #esse novo nó se torna, então, a head da lista
            self.size = self.size + 1
        else:
            new_node = Node(data) #fazemos o nó novamente
            current = self.head   #criamos um 'atual' para andar pelos nós
            while current.next:   #"enquanto ainda tiver um próximo para o atual..."
                current = current.next #atual se transforma no próximo até chegar ao fim da lista
            current.next = new_node
            new_node.prev = current #após sair do while, o current vai ser o último.
                                    #por isso, o antecessor do novo vai ser o current.
            new_node.next = None    #agora que o novo nó é o último, ele tem que apontar para o vazio.
            self.size = self.size + 1

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)  #same shit, but the other way around
            new_node.prev = None
            self.head = new_node
            self.size = self.size + 1
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None
            self.size = self.size + 1

    def remove(self, elem):
        if self.head is None:
            print("Lista vazia.")
            pass
        elif self.head.data == elem:
            self.head = self.head.next
            self.size = self.size - 1
        else:
            ancestor = self.head
            current = self.head.next
            while current.next:
                if current.data == elem:
                    ancestor.next = current.next
                    current.next = None
                ancestor = current
                current = current.next
            self.size = self.size - 1

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

