# Primeira aula em python
produtos = [] # listas
valores = []
finalizar = ""
while finalizar != "N":    
   
    prod = input("Digite o produto: ")

    preco = float(input("Digite o preço: "))

    produtos.append(prod)
    valores.append(preco)

    finalizar = ''
    while finalizar != 'S' and finalizar != 'N':
        finalizar = input("Deseja continuar cadastrando (S SIM || (N) Não: ").upper()

        if finalizar != 'S' and finalizar != 'N':
            print('Você só pode digitar (S) ou (N)')



for linha, nome_prod in enumerate(produtos):
    print(f"{linha + 1} - {nome_prod} - R${valores[linha]}")

    


"""
print(f"O tipo de dado da variável {prod}")
print(f"O tipo de dado da variável {preco}")
print(f"O tipo de dado da lista {produtos}")
"""