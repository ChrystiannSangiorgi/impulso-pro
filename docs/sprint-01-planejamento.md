# Sprint 1 — Planejamento

> **Sprint:** 01  
> **Início:** A definir  
> **Término:** A definir (2 semanas após o início)  
> **Capacidade:** 12 Story Points  
> **Status:** Planejada

---

## Objetivo da Sprint

> *"Ao final desta sprint, é possível fazer login no sistema com perfil de acesso definido e gerenciar as unidades da rede — estabelecendo a fundação de segurança e estrutura sobre a qual todo o restante do sistema será construído."*

Esta sprint não entrega funcionalidades visíveis para o usuário final, mas é a mais crítica do projeto: sem autenticação e sem perfis de acesso, nenhuma outra feature pode ser desenvolvida com segurança. Sem unidades cadastradas, colaboradores e treinamentos não têm onde se ancorar.

---

## Sprint Backlog

| ID | User Story | Épico | Points | Prioridade |
|----|-----------|-------|--------|------------|
| US-001 | Como usuário, quero fazer login com e-mail e senha | EP-01 Autenticação | 3 | 🔴 M |
| US-002 | Como usuário autenticado, quero fazer logout | EP-01 Autenticação | 1 | 🔴 M |
| US-003 | Como Gestor da Rede, quero definir perfis e permissões | EP-01 Autenticação | 5 | 🔴 M |
| US-027 | Como Gestor da Rede, quero cadastrar e gerenciar unidades | EP-09 Administração | 3 | 🔴 M |
| **Total** | | | **12** | |

---

## Tarefas Técnicas (Tasks)

Além das User Stories, esta sprint inclui tarefas de setup que não são stories mas são pré-requisito para tudo.

### TASK-001 — Setup do Projeto

**Descrição:** Criar a estrutura inicial do repositório e configurar os ambientes de desenvolvimento.

**Subtarefas:**
- [ ] Criar novo repositório `impulso-pro` no GitHub
- [ ] Criar estrutura de pastas: `backend/`, `frontend/`, `database/`, `docs/`
- [ ] Configurar `.gitignore` para Python e Node
- [ ] Criar branch `develop` como branch principal de desenvolvimento
- [ ] Subir documentação inicial (Project Charter, Backlog, DoD, Sprint 1) na Wiki
- [ ] Configurar GitHub Projects com colunas: **Backlog → Sprint Backlog → In Progress → In Review → Done**
- [ ] Criar Milestones no GitHub para cada Sprint

---

### TASK-002 — Setup do Backend (FastAPI)

**Descrição:** Inicializar o projeto Python com FastAPI e configurar a conexão com o banco de dados.

**Subtarefas:**
- [ ] Criar ambiente virtual Python (`venv`)
- [ ] Instalar dependências iniciais: `fastapi`, `uvicorn`, `sqlalchemy`, `pymysql`, `python-jose`, `passlib`, `pydantic`, `python-dotenv`
- [ ] Criar arquivo `requirements.txt`
- [ ] Configurar estrutura de pastas do backend:
  ```
  backend/
  ├── app/
  │   ├── main.py
  │   ├── database.py
  │   ├── models/
  │   ├── schemas/
  │   ├── routers/
  │   ├── services/
  │   └── core/
  │       ├── security.py
  │       └── config.py
  ├── requirements.txt
  └── .env.example
  ```
- [ ] Configurar conexão com MySQL via SQLAlchemy
- [ ] Rodar o SQL do schema existente no banco local e confirmar que todas as tabelas foram criadas
- [ ] Confirmar que o servidor FastAPI sobe sem erros (`uvicorn app.main:app --reload`)

---

### TASK-003 — Setup do Frontend (React + Vite)

**Descrição:** Inicializar o projeto React com Vite e configurar a comunicação com a API.

**Subtarefas:**
- [ ] Criar projeto com `npm create vite@latest frontend -- --template react`
- [ ] Instalar dependências iniciais: `axios`, `react-router-dom`, `tailwindcss`
- [ ] Configurar Tailwind CSS
- [ ] Criar estrutura de pastas do frontend:
  ```
  frontend/
  ├── src/
  │   ├── components/
  │   ├── pages/
  │   ├── services/
  │   │   └── api.js
  │   ├── contexts/
  │   └── App.jsx
  ├── .env.example
  └── package.json
  ```
- [ ] Configurar `axios` com a base URL da API via variável de ambiente
- [ ] Confirmar que o servidor de desenvolvimento sobe sem erros

---

## Detalhamento das User Stories

### US-001 — Login

**Como** qualquer usuário do sistema,  
**quero** fazer login com e-mail e senha,  
**para** acessar as funcionalidades do meu perfil de forma segura.

**Critérios de Aceitação:**
- [ ] Login com e-mail e senha válidos retorna token JWT
- [ ] Senha incorreta incrementa contador de tentativas falhas
- [ ] Após 5 tentativas falhas, a conta é bloqueada
- [ ] Token JWT expira em 8 horas
- [ ] Senha armazenada com hash bcrypt

**Tasks de implementação:**
- [ ] `backend` — Criar rota `POST /auth/login` com validação de credenciais
- [ ] `backend` — Implementar geração de token JWT em `core/security.py`
- [ ] `backend` — Implementar hash bcrypt para verificação de senha
- [ ] `backend` — Implementar lógica de bloqueio de conta após 5 tentativas
- [ ] `frontend` — Criar página de Login com campos e-mail e senha
- [ ] `frontend` — Armazenar token JWT retornado em sessionStorage
- [ ] `frontend` — Redirecionar para dashboard após login bem-sucedido
- [ ] `frontend` — Exibir mensagem de erro em caso de credenciais inválidas

---

### US-002 — Logout

**Como** qualquer usuário autenticado,  
**quero** fazer logout do sistema,  
**para** encerrar minha sessão com segurança.

**Critérios de Aceitação:**
- [ ] Token é removido ao fazer logout
- [ ] Usuário é redirecionado para a tela de login

**Tasks de implementação:**
- [ ] `frontend` — Criar botão de logout no layout principal
- [ ] `frontend` — Remover token do sessionStorage ao clicar em logout
- [ ] `frontend` — Redirecionar para `/login` após logout
- [ ] `frontend` — Criar guard de rota que redireciona para `/login` se não houver token

---

### US-003 — Perfis e Permissões

**Como** Gestor de RH da Rede,  
**quero** definir os perfis de acesso e suas permissões,  
**para** controlar o que cada tipo de usuário pode visualizar e executar no sistema.

**Critérios de Aceitação:**
- [ ] Perfis disponíveis: Colaborador, Treinador, Gestor de Unidade, Gestor da Rede
- [ ] Cada perfil tem um conjunto de permissões associadas
- [ ] Permissões podem ser visualizadas por perfil
- [ ] Um colaborador pode ter apenas um perfil ativo

**Tasks de implementação:**
- [ ] `database` — Popular tabelas `Perfil` e `Permissao` com dados iniciais (seed)
- [ ] `backend` — Criar rota `GET /perfis` para listar perfis com suas permissões
- [ ] `backend` — Criar middleware de autorização que valida o perfil do token JWT
- [ ] `backend` — Criar decorator/dependência para proteger rotas por perfil
- [ ] `frontend` — Criar tela de listagem de perfis e permissões (somente Gestor da Rede)
- [ ] `frontend` — Adaptar layout e menu de navegação conforme o perfil do usuário logado

---

### US-027 — Cadastro de Unidades

**Como** Gestor de RH da Rede,  
**quero** cadastrar e gerenciar as unidades (restaurantes) da rede,  
**para** organizar colaboradores e treinamentos por unidade.

**Critérios de Aceitação:**
- [ ] Cadastro com nome, endereço completo e status (ativo/inativo)
- [ ] Unidade inativa não aparece em novas atribuições
- [ ] Histórico de treinamentos da unidade é preservado ao inativar

**Tasks de implementação:**
- [ ] `backend` — Criar rota `POST /restaurantes` para cadastrar nova unidade
- [ ] `backend` — Criar rota `GET /restaurantes` para listar unidades (com filtro ativo/inativo)
- [ ] `backend` — Criar rota `PUT /restaurantes/{id}` para editar unidade
- [ ] `backend` — Criar rota `PATCH /restaurantes/{id}/status` para ativar/inativar
- [ ] `frontend` — Criar tela de listagem de unidades com status visual
- [ ] `frontend` — Criar formulário de cadastro e edição de unidade
- [ ] `frontend` — Implementar ação de ativar/inativar com confirmação

---

## Decisões Técnicas desta Sprint

| Decisão | Justificativa |
|---------|--------------|
| Token JWT armazenado em `sessionStorage` | Mais seguro que `localStorage` contra ataques XSS; expira ao fechar o browser |
| Perfis e permissões populados via seed | Perfis são fixos no sistema — não faz sentido criar via CRUD livre |
| SQLAlchemy como ORM | Abstrai queries SQL, reduz risco de SQL injection, integra bem com FastAPI |
| Pydantic para validação de entrada | Nativo do FastAPI; garante tipagem e validação automática nos endpoints |

---

## Riscos desta Sprint

| Risco | Mitigação |
|-------|-----------|
| Configuração do ambiente Python ser demorada | Reservar a primeira sessão só para setup, sem pressão de feature |
| Lógica de permissões por perfil ser mais complexa que o estimado | Simplificar para permissões fixas por perfil nesta sprint; CRUD de permissões pode entrar numa sprint futura |

---

## Definição de Pronto desta Sprint

Além da DoD geral do projeto, esta sprint está concluída quando:

- [ ] É possível fazer login e logout no sistema funcionando localmente
- [ ] O perfil do usuário logado é identificado e reflete no menu de navegação
- [ ] Gestor da Rede consegue cadastrar, editar e inativar unidades
- [ ] Toda a documentação desta sprint está publicada no GitHub (Wiki + Issues)
- [ ] O repositório `impulso-pro` está criado e com a estrutura de pastas commitada

---

## Sprint Review (a preencher ao final)

**Data da Review:** _______________

**O que foi entregue:**

**O que não foi entregue e por quê:**

**Demo:**

---

## Sprint Retrospectiva (a preencher ao final)

**O que funcionou bem:**

**O que pode melhorar:**

**Ação para a próxima sprint:**
