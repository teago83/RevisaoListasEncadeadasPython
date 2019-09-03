"""3) Considere uma coleção de nomes de sites da web e seus respectivos links na Internet
armazenados através de uma lista simplesmente encadeada. Escreva a respectiva estrutura e um
método que, dado o nome de um site, busque o seu link correspondente na lista e ao mesmo tempo
mova o nó que contém o nome buscado para o início da lista, de forma que ele possa ser encontrado
mais rapidamente na próxima vez que for buscado. """

sitesz = []
pastel = 0


class Sites:
    def __init__(self):
        self.nome = str
        self.endereco = str

    def adicionarSites(self):
        auxiliar = []
        while True:
            self.nome = input("\nDigite o nome do site:")
            auxiliar.append(self.nome)
            self.endereco = input("Digite o endereço do site:")
            auxiliar.append(self.endereco)
            break
        sitesz.append(auxiliar[:])


def buscarSites():
    batata = False
    nome_busca = input("\nDigite o nome do site pelo qual buscas:")
    for i in range(pastel):
        if nome_busca == sitesz[i][0]:
            batata = True
            print("Site encontrado com sucesso!")
    if batata == False:
        print("Site não encontrado.")


sites = Sites()

pastel = int(input("Digite o número de sites que irás registrar:"))
for i in range(pastel):
    sites.adicionarSites()

buscarSites()
