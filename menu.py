import os
import platform
from funcoes import adicionar_produto, atualizar_produto, excluir_produto, visualizar_estoque

# Arquivo menu.py
# Contém o menu do sistema e a lógica principal do programa

def limpar_terminal():
    """
    Limpa a tela do terminal de acordo com o sistema operacional.
    """
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def exibir_menu():
    """
    Mostra as opções disponíveis para o usuário.
    """
    print("\n--- SISTEMA DE CONTROLE DE ESTOQUE ---")
    print("1 - Adicionar produto")
    print("2 - Atualizar produto")
    print("3 - Excluir produto")
    print("4 - Visualizar estoque")
    print("0 - Sair")

def escolher_opcao(estoque):
    """
    Mostra o menu, recebe a opção do usuário e executa a ação correspondente.

    Parâmetro:
    - estoque: lista de dicionários com os produtos

    Retorna:
    - True para continuar o sistema
    - False para sair do sistema
    """
    limpar_terminal()      # Limpa a tela para mostrar o menu limpo
    exibir_menu()         # Mostra as opções

    escolha = input("Escolha uma opção: ").strip()   # Recebe a opção do usuário

    # Verifica a opção e chama a função adequada
    if escolha == "1":
        adicionar_produto(estoque)
    elif escolha == "2":
        atualizar_produto(estoque)
    elif escolha == "3":
        excluir_produto(estoque)
    elif escolha == "4":
        visualizar_estoque(estoque)
    elif escolha == "0":
        print("Saindo do sistema. Até logo!")
        return False      # Sinaliza para encerrar o loop no executar_sistema()
    else:
        print("Opção inválida. Tente novamente.")

    input("\nPressione Enter para continuar...")  # Pausa para o usuário ler a mensagem
    return True       # Continua o sistema

def executar_sistema():
    """
    Função principal que inicia o sistema, inicializa o estoque com produtos
    e mantém o loop até o usuário optar por sair.
    """
    # Estoque inicial com alguns produtos de exemplo
    estoque = [
        {"nome": "Smartphone Samsung Galaxy S21", "preço": 3200.00, "quantidade": 10},
        {"nome": "Notebook Dell Inspiron", "preço": 4500.50, "quantidade": 5},
        {"nome": "Fone de ouvido Bluetooth JBL", "preço": 350.90, "quantidade": 15},
        {"nome": "Smart TV LG 50''", "preço": 2200.00, "quantidade": 7},
        {"nome": "Caixa de som portátil Sony", "preço": 400.00, "quantidade": 12}
    ]

    continuar = True   # Controla o loop do sistema

    # Loop principal que mantém o sistema funcionando enquanto continuar for True
    while continuar:
        continuar = escolher_opcao(estoque)   # Exibe o menu e executa a ação escolhida


executar_sistema()   # Inicia o sistema quando o script for executado diretamente