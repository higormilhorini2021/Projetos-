import json
import os

# --- SISTEMA DE CONTROLE DE ESTOQUE COMPLETO ---
# Loja de Eletrônicos - MUKIARA

# Definição das Cores e Estilos (ANSI)
NEGRITO = '\033[1m'
VERMELHO = '\033[31m'
VERDE = '\033[32m'
AZUL = '\033[34m'
CIANO = '\033[36m'
RESET = '\033[0m'

NOME_ARQUIVO = "estoque.json"

def salvar_dados(lista):
    try:
        with open(NOME_ARQUIVO, "w", encoding="utf-8") as f:
            json.dump(lista, f, indent=4, ensure_ascii=False)
        print(f"{VERDE}Dados sincronizados com sucesso!{RESET}")
    except Exception as e:
        print(f"{VERMELHO}Erro ao salvar: {e}{RESET}")

def carregar_dados():
    if os.path.exists(NOME_ARQUIVO):
        try:
            with open(NOME_ARQUIVO, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []
    
    # Lista inicial padrão com os 5 produtos solicitados
    print(f"{AZUL}Iniciando sistema com estoque padrão...{RESET}")
    produtos_iniciais = [
        {"nome": "Teclado", "preco": 75.00, "quantidade": 25},
        {"nome": "Monitor", "preco": 450.00, "quantidade": 10},
        {"nome": "Mouse", "preco": 55.00, "quantidade": 35},
        {"nome": "Fone", "preco": 100.00, "quantidade": 20},
        {"nome": "TV 55\"", "preco": 1200.00, "quantidade": 5}
    ]
    salvar_dados(produtos_iniciais)
    return produtos_iniciais

# Inicializa o estoque
estoque = carregar_dados()

while True:
    # Menu com NEGRITO aplicado
    print(f"\n{NEGRITO}========= MENU DE CONTROLE DE ESTOQUE ========={RESET}")
    print(f"{NEGRITO}1 - Adicionar Produto{RESET}")
    print(f"{NEGRITO}2 - Atualizar Produto{RESET}")
    print(f"{NEGRITO}3 - Excluir Produto{RESET}")
    print(f"{NEGRITO}4 - Visualizar Estoque e Totais{RESET}")
    print(f"{NEGRITO}5 - Salvar e Sair{RESET}")
    print(f"{NEGRITO}==============================================={RESET}")
    
    opcao = input("Selecione uma opção: ")

    if opcao == '1':
        try:
            print(f"\n{NEGRITO}--- Cadastro de Novo Produto ---{RESET}")
            nome = input("Nome do produto: ")
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))
            estoque.append({"nome": nome, "preco": preco, "quantidade": quantidade})
            salvar_dados(estoque)
            print(f"{VERDE}Sucesso: {nome} cadastrado!{RESET}")
        except ValueError:
            print(f"{VERMELHO}Erro: Digite números válidos. Tente novamente.{RESET}")

    elif opcao == '2':
        print(f"\n{NEGRITO}--- Atualização de Dados ---{RESET}")
        busca = input("Nome do produto para atualizar: ")
        encontrado = False
        for produto in estoque:
            if produto["nome"].lower() == busca.lower():
                try:
                    produto["preco"] = float(input("Novo preço: "))
                    produto["quantidade"] = int(input("Nova quantidade: "))
                    salvar_dados(estoque)
                    print(f"{VERDE}Dados atualizados!{RESET}")
                    encontrado = True
                    break
                except ValueError:
                    print(f"{VERMELHO}Erro: Valor inválido.{RESET}")
                    encontrado = True
                    break
        if not encontrado:
            print(f"{VERMELHO}Erro: Produto não encontrado.{RESET}")

    elif opcao == '3':
        print(f"\n{NEGRITO}--- Remoção de Produto ---{RESET}")
        busca = input("Nome do produto para excluir: ")
        encontrado = False
        for i in range(len(estoque)):
            if estoque[i]["nome"].lower() == busca.lower():
                removido = estoque.pop(i)
                salvar_dados(estoque)
                print(f"{VERDE}Produto '{removido['nome']}' removido!{RESET}")
                encontrado = True
                break
        if not encontrado:
            print(f"{VERMELHO}Erro: Produto não localizado.{RESET}")

    elif opcao == '4':
        print(f"\n{NEGRITO}{AZUL}------------------ LISTA DE ESTOQUE ATUAL ------------------{RESET}")
        if not estoque:
            print(f"{VERMELHO}O estoque está vazio.{RESET}")
        else:
            total_qtd = 0
            valor_geral = 0
            # Tabela em Azul e Negrito no cabeçalho
            print(f"{NEGRITO}{AZUL}{'Nome':<15} | {'Preço':<10} | {'Qtd':<5} | {'Subtotal':<12}{RESET}")
            print(f"{AZUL}" + "-" * 55 + f"{RESET}")
            
            for p in estoque:
                subtotal = p['preco'] * p['quantidade']
                print(f"{AZUL}{p['nome']:<15} | R$ {p['preco']:>7.2f} | {p['quantidade']:>5} | R$ {subtotal:>9.2f}{RESET}")
                total_qtd += p['quantidade']
                valor_geral += subtotal
            
            print(f"{AZUL}" + "-" * 55 + f"{RESET}")
            print(f"{NEGRITO}{CIANO}RESUMO FINANCEIRO TOTAL:{RESET}")
            print(f"Quantidade total de itens: {total_qtd}")
            print(f"Patrimônio total em estoque: {VERDE}{NEGRITO}R$ {valor_geral:,.2f}{RESET}")

    elif opcao == '5':
        salvar_dados(estoque)
        print(f"{NEGRITO}Encerrando o sistema... Até logo!{RESET}")
        break
    
    else:
        print(f"{VERMELHO}Erro: Opção inválida.{RESET}")

