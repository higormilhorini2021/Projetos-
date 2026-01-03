# Controle de Estoque - Loja de Eletrônicos MUKIARA

## Descrição

Este é um sistema simples de controle de estoque desenvolvido em Python para uma loja de eletrônicos fictícia chamada MUKIARA. O programa permite gerenciar produtos no estoque, incluindo adicionar, atualizar, excluir e visualizar itens, além de calcular totais de quantidade e valor patrimonial.

O sistema utiliza um arquivo JSON (`estoque.json`) para persistir os dados, garantindo que as informações sejam salvas mesmo após o fechamento do programa.

## Funcionalidades

- **Adicionar Produto**: Permite cadastrar um novo produto informando nome, preço e quantidade.
- **Atualizar Produto**: Busca um produto pelo nome e permite alterar seu preço e quantidade.
- **Excluir Produto**: Remove um produto do estoque pelo nome.
- **Visualizar Estoque**: Exibe uma tabela com todos os produtos, incluindo subtotais por item e totais gerais de quantidade e valor.
- **Salvar e Sair**: Salva os dados no arquivo JSON e encerra o programa.

O programa inicia com um estoque padrão contendo 5 produtos: Teclado, Monitor, Mouse, Fone e TV 55".

## Requisitos

- Python 3.x instalado no sistema.

## Como Executar

1. Certifique-se de que o Python está instalado.
2. Navegue até a pasta do projeto: `cd Controle-de-Estoque`
3. Execute o script: `python Trabalho/Estoque.py`
4. Siga as instruções no menu interativo.

## Estrutura do Código

O código está organizado em funções principais:

- `salvar_dados()`: Salva a lista de produtos no arquivo JSON.
- `carregar_dados()`: Carrega os dados do JSON ou inicia com produtos padrão.
- Loop principal com menu para interagir com o usuário.

O programa usa cores ANSI para melhorar a visualização no terminal (negrito, vermelho, verde, azul, ciano).
