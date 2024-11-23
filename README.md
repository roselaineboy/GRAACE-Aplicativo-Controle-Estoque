# GRAACE-Aplicativo-Controle-Estoque
GRAACE - Aplicativo de Controle de Estoque - Pós FACENS

# 📦 Aplicativo de Controle de Estoque

Este projeto é um **Aplicativo de Controle de Estoque** que permite gerenciar produtos e seus respectivos estoques, facilitando o controle de entradas e saídas de mercadorias do estoque de uma pequena loja on-line. 
O objetivo é oferecer uma solução simples para registrar e consultar produtos, além de monitorar quantidades mínimas de estoque apresentando uma listagem dos produtos que necessitam de reposição.

## ✨ Funcionalidades

- **CRUD Completo para Produtos:**
  - Inserção, edição, exclusão e consulta de produtos.
- **Gestão de Estoque:**
  - Registro de quantidade mínima de estoque para cada produto.
  - Inclusão de quantidades em estoque (entrada de produtos).
  - Retirada de quantidades do estoque (saída de produtos).
- **Alerta de Estoque Mínimo:**
  - Ao iniciar o aplicativo, exibe uma lista de produtos que estão com a quantidade igual ou abaixo do estoque mínimo cadastrado.
- **Armazenamento de Dados:**
  - Os dados são salvos em dois arquivos para persistência no formato JSON.
  - Também será armazenado um log de eventos e erros no formato .txt.

## 🛠️ Tecnologias Utilizadas

- Linguagem: Python
- Armazenamento: JSon e txt
- Dependencias: Pandas, tabulate

## 📂 Estrutura do Projeto

```plaintext
├── classes/
│   ├── log.py
│   ├── menu.py
│   ├── movimentacao_estoque.py
│   ├── produto.py
│   └── relatorio.py
├── configuracoes/
│   └── config.py
├── dados/
│   ├── log.txt
│   ├── movimentacoes.json
│   └── produtos.json
├── definicoes_de_tabelas/
│   ├── def_produto.py
│   └── def_estoque.py
│   └── def_log.py
├── utils/
│   └── bib.py
├── main.py
└── README.md

