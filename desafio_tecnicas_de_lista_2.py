def produto_mais_vendido(produtos):
    print(produtos)
    contagem = {}
    
    for produto in produtos:
        if produto in contagem:
            contagem[produto] += 1
        else:
            contagem[produto] = 1
        print(produto, contagem)    
        
    
    max_produto = None
    max_count = 0
    
    for produto, count in contagem.items():
        # TODO: Encontre o produto com a maior contagem
        if count > max_count:
            max_count = count
            max_produto = produto
    
    return max_produto

def obter_entrada_produtos():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    # TODO: Converta a entrada em uma lista de strings, removendo espaços extras:
    mascara1 = entrada.split(',')
    produtos = []
    for item in mascara1:
        produtos.append(item.strip())
    return produtos

produtos = obter_entrada_produtos()
print(produto_mais_vendido(produtos))