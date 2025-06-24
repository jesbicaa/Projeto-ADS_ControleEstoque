# Arquivo funcoes.py
# Contém as funções para manipular o estoque (lista de produtos)

def adicionar_produto(estoque):
    """
    Adiciona um novo produto ao estoque.
    Solicita nome, preço e quantidade ao usuário.
    Verifica se o produto já existe antes de adicionar.
    """
    nome = input("Nome do produto: ").strip()
    
    # Verifica se o produto já existe pelo nome
    for produto in estoque:
        if produto["nome"].lower() == nome.lower():
            print("Produto já existe no estoque.")
            return
    
    try:
        preco = float(input("Preço do produto: R$ "))
        quantidade = int(input("Quantidade em estoque: "))
    except ValueError:
        print("Preço ou quantidade inválidos. Tente novamente.")
        return
    
    # Adiciona o produto na lista
    estoque.append({"nome": nome, "preço": preco, "quantidade": quantidade})
    print(f"Produto '{nome}' adicionado com sucesso!")

def atualizar_produto(estoque):
    """
    Atualiza preço e quantidade de um produto existente.
    Busca pelo nome do produto.
    """
    nome = input("Nome do produto para atualizar: ").strip()
    for produto in estoque:
        if produto["nome"].lower() == nome.lower():
            try:
                preco = float(input("Novo preço do produto: R$ "))
                quantidade = int(input("Nova quantidade em estoque: "))
            except ValueError:
                print("Preço ou quantidade inválidos. Tente novamente.")
                return
            produto["preço"] = preco
            produto["quantidade"] = quantidade
            print(f"Produto '{nome}' atualizado com sucesso.")
            return
    print("Produto não encontrado no estoque.")

def excluir_produto(estoque):
    """
    Exclui um produto do estoque pelo nome.
    """
    nome = input("Nome do produto para excluir: ").strip()
    for i, produto in enumerate(estoque):
        if produto["nome"].lower() == nome.lower():
            del estoque[i]
            print(f"Produto '{nome}' excluído com sucesso!")
            return
    print("Produto não encontrado no estoque.")

def visualizar_estoque(estoque):
    """
    Exibe todos os produtos do estoque.
    """
    if not estoque:
        print("Estoque vazio.")
        return
    
    print("\n======== ESTOQUE ATUAL: ========")
    print(f"{'Nome':<30} {'Preço (R$)':<12} {'Quantidade':<10}")
    print("-" * 55)
    for produto in estoque:
        print(f"{produto['nome']:<30} {produto['preço']:<12.2f} {produto['quantidade']:<10}")
    print()