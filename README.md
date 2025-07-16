# Agenda de Contatos

Um sistema simples de gerenciamento de contatos desenvolvido em Python com interface de linha de comando.

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+** - Linguagem de programação principal
- **Bibliotecas padrão do Python** - Não requer dependências externas

## 🏗️ Arquitetura do Projeto

O projeto segue uma estrutura simples e organizada:

```
adress-book/
├── main.py           # Ponto de entrada da aplicação
├── src/
│   └── contact.py    # Classe Contact com lógica de negócio
└── README.md         # Documentação do projeto
```

### Padrões de Design Utilizados

- **Singleton Pattern**: Instância única da classe `Contact` para gerenciar todos os contatos
- **Encapsulamento**: Separação clara entre interface do usuário (`main.py`) e lógica de negócio (`contact.py`)
- **Type Hints**: Utilização de anotações de tipo para melhor legibilidade do código

## 🚀 Como Executar

### Pré-requisitos

- Python 3.8 ou superior instalado
- Terminal/Prompt de comando

### Instalação e Execução

1. Clone ou baixe o projeto:

```bash
git clone <url-do-repositorio>
cd adress-book
```

2. Execute o programa:

```bash
python main.py
```

## 📋 Funcionalidades

- ✅ Adicionar novos contatos
- ✅ Listar todos os contatos
- ✅ Visualizar detalhes de um contato específico
- ✅ Editar informações de contatos existentes
- ✅ Marcar/desmarcar contatos como favoritos
- ✅ Visualizar lista de contatos favoritos
- ✅ Remover contatos

## 📝 Estrutura de Dados

Cada contato contém:

- ID único (gerado automaticamente)
- Nome
- Telefone
- Email
- Status de favorito (booleano)

## 🔧 Melhorias Futuras

- Persistência de dados (arquivo JSON/CSV ou banco de dados)
- Validação de email e telefone
- Busca por nome/email
- Interface gráfica
- Testes unitários
