# Nuxo Bot - Assistente Financeiro via WhatsApp

## 📋 Sobre o Projeto

O **Nuxo Bot** é um assistente financeiro pessoal automatizado disponível via **WhatsApp**. Ele permite que os usuários registrem, consultem, exportem e excluam gastos, com uma interação fluida e intuitiva.

Este projeto foi desenvolvido utilizando a arquitetura Clean Architecture, com FastAPI como framework principal para a API.

## 🏗️ Arquitetura

O projeto segue os princípios da Clean Architecture, organizando o código em camadas com responsabilidades bem definidas:

```
bot_whatsapp/
│
├── main.py                        ← Entry point: inicializa bot e dependências
├── config.py                      ← Configurações do projeto (env, API keys, etc.)
│
├── app/                           ← [Clean] Casos de uso, lógica de negócio
│   ├── use_cases/                 ← [Clean] Regras de negócio (ex: registrar gasto, consultar gastos)
│   └── services/                  ← [Clean] Lógica auxiliar (ex: formatar resposta, validar mensagem)
│
├── domain/                        ← [Clean] Entidades de negócio (ex: Gasto, Usuário)
│   └── models.py                  ← Classes de domínio simples
│
├── interfaces/                    ← [MVC/Adapter] Entrada do sistema (WhatsApp Webhook, CLI, etc.)
│   └── whatsapp_webhook.py        ← Handler HTTP que recebe mensagens do WhatsApp
│
├── infrastructure/                ← [Clean] Implementações de infraestrutura externa
│   ├── whatsapp/                  ← Integração com API do WhatsApp
│   │   └── whatsapp_gateway.py    ← Envia e recebe mensagens reais
│   └── repositories/              ← Acesso a dados (banco de dados)
│       └── user_repository.py     ← Interface com persistência
│
├── tests/                         ← [Geral] Testes unitários e de integração
│   ├── test_use_cases/
│   ├── test_services/
│   └── test_interfaces/
│
└── requirements.txt               ← Dependências do projeto
```

## 🚀 Funcionalidades

O Nuxo Bot oferece as seguintes funcionalidades:

1. **Boas-vindas e Ajuda** - Introdução ao bot e lista de comandos disponíveis
2. **Registrar Gastos** - Fluxo guiado para registrar gastos fixos ou avulsos
3. **Visualizar Gastos** - Consulta de gastos com filtros por período e categoria
4. **Exportar Planilha** - Geração de planilha Excel com os gastos registrados
5. **Excluir Gastos** - Remoção de gastos específicos

## 🛠️ Tecnologias Utilizadas

- **Backend**: FastAPI (Python)
- **Servidor ASGI**: Uvicorn
- **Integração WhatsApp**: API (definir qual) do WhatsApp Business
- **Banco de Dados**: PostgreSQL (Supabase?)
- **Documentação**: Swagger UI (automática via FastAPI)

## 🔧 Instalação e Execução

### Pré-requisitos

- Python 3.8+

### Instalação

1. Clone o repositório:

```bash
git clone [URL_DO_REPOSITORIO]
cd bot_whatsapp
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o servidor:

```bash
uvicorn main:app --reload
```

4. Acesse a documentação da API:

```
http://localhost:8000/docs
```

## 📝 Endpoints da API

- **GET /ping**: Endpoint de verificação de status da API
- Outros endpoints serão implementados conforme o desenvolvimento do projeto

## 🔄 Futuras Features

- Comando de metas e alertas de orçamento
- Integração com calendário para lembrar gastos futuros e pagamentos
- Criação de interface Web
- Adição de IA para insights financeiros

## 👥 Contribuição

Instruções para contribuição serão adicionadas em breve.

---

Desenvolvido com 💜 pelo Time Nuxo - Matheus Campos e Bruno Martins
