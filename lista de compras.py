"""
LISTA DE COMPRAS

Desenvolvido em Python
Autor: Natan Mauricio Santos
Data: 07/2025
"""

opcoes = [
    "Adicionar item à lista",
    "Remover item da lista",
    "Exibir lista de compras",
    "Sair"
]

# Exibe o menu com as opções
def menu():
    print("=" * 100)
    print(" " * 42 + "LISTA DE COMPRAS")
    print("=" * 100 + "\n")
    
    print("Opções:")
    for indice, opcao in enumerate(opcoes):
        print(f"  {indice + 1}. {opcao}")
    print("-" * 100 + "\n")

# Capta a escolha do usuário
def escolher():
    escolha = 0
    while (escolha < 1) or (escolha > 4): 
        try:
            escolha = int(input("Insira a opção que deseja (1 - 4): "))
            if (escolha < 1) or (escolha > 4):
                print("Digite um valor numérico válido!")
        except ValueError:
            print("Digite um valor numérico válido!")
    print("=" * 100 + "\n")
    return escolha

# Adiciona um item no final da lista
def adicionar_item():
    item = input("Digite o nome do item a ser adicionado: ")
    return item.upper()

# Adiciona a quantidade que deve ser comprada
def adicionar_qtd():
    qtd = input("Digite a quantidade e a medida (Ex.: 4 kg): ")
    return qtd.upper()

# Remove um item da lista
def remove(lista, qtd):
    item = input("Digite o nome do item a ser removido: ")
    item = item.upper()
    
    if item in lista:
        indice = lista.index(item)
        lista.pop(indice)
        qtd.pop(indice)
        print(f"Item '{item}' removido com sucesso!")
    else:
        print(f"O item '{item}' não está na lista.")
    return lista, qtd

# Imprime a lista completa
def imprimir(lista, qtd):
    if not lista:
        print("A lista de compras está vazia.\n")
    else:
        print("Itens na lista de compras:\n")
        for i in range(len(lista)):
            print(f"- {qtd[i]} de {lista[i]}")
    print()

# Programa principal
lista_compras = []
quantidade = []
escolha = 0
while escolha != 4:
    menu()
    escolha = escolher()

    if escolha == 1:
        lista_compras.append(adicionar_item())
        quantidade.append(adicionar_qtd())
    elif escolha == 2:
        lista_compras, quantidade = remove(lista_compras, quantidade)
    elif escolha == 3:
        imprimir(lista_compras, quantidade)
    else:
        print("Muito Obrigado!")
