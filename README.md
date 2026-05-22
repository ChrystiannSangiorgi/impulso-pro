# Impulso Pro

> Plataforma de gestão de treinamentos operacionais para redes de restaurantes.

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-orange)
![Sprint](https://img.shields.io/badge/sprint-01-blue)
![Stack](https://img.shields.io/badge/stack-FastAPI%20%7C%20React%20%7C%20MySQL-informational)
![Licença](https://img.shields.io/badge/licen%C3%A7a-MIT-green)

---

## Sobre o Projeto

O **Impulso Pro** é uma plataforma web que centraliza o gerenciamento de treinamentos operacionais em redes de restaurantes. A ferramenta permite que Gestores de RH e Treinadores criem, atribuam e monitorem capacitações — enquanto colaboradores acompanham seus próprios resultados e obrigações de treinamento.

O sistema gerencia o **ciclo completo de treinamento**: da criação de trilhas e sessões até o registro de presença, avaliação de desempenho e geração de relatórios por unidade.

**O que o sistema faz:**
- Criação e atribuição de treinamentos obrigatórios e livres
- Registro de presença em sessões de treinamento
- Avaliação de desempenho por colaborador e sessão
- Trilhas de capacitação por cargo ou área
- Relatórios de frequência e desempenho por unidade
- Suporte a redes multi-unidade com treinadores que atuam em diferentes locais
- Importação de colaboradores via integração com sistemas de RH externos

**O que o sistema não faz:**
- Não aplica os treinamentos (gerencia, não executa)
- Não gerencia folha de pagamento ou controle de ponto
- Não emite certificados

---

## Stack Tecnológica

| Camada | Tecnologia |
|--------|-----------|
| Backend | Python 3.11+ · FastAPI · SQLAlchemy · Pydantic |
| Banco de Dados | MySQL 8.0 |
| Autenticação | JWT · bcrypt |
| Frontend | React 18 · Vite · Tailwind CSS · Axios |
| Deploy | Railway (backend) · Vercel (frontend) |
| Versionamento | GitHub · Conventional Commits |

---

## Arquitetura

```
impulso-pro/
├── backend/
│   └── app/
│       ├── main.py
│       ├── database.py
│       ├── models/          # Modelos SQLAlchemy (mapeamento das tabelas)
│       ├── schemas/         # Schemas Pydantic (validação de entrada/saída)
│       ├── routers/         # Endpoints organizados por domínio
│       ├── services/        # Regras de negócio
│       └── core/
│           ├── security.py  # JWT e bcrypt
│           └── config.py    # Variáveis de ambiente
├── frontend/
│   └── src/
│       ├── components/      # Componentes reutilizáveis
│       ├── pages/           # Páginas da aplicação
│       ├── services/        # Comunicação com a API (axios)
│       └── contexts/        # Contextos React (auth, perfil)
├── database/
│   └── impulso_pro.sql      # Schema completo do banco
└── docs/                    # Documentação do projeto
```

---

## Modelo de Dados

O banco de dados foi modelado com normalização até a **Terceira Forma Normal (3FN)** e conta com 20 tabelas cobrindo os domínios de autenticação, colaboradores, treinamentos, sessões, desempenho e auditoria.

Entidades principais: `Colaborador_Usuario`, `Restaurante`, `Treinamento`, `Trilha_Treinamento`, `Sessao_Equipe`, `Desempenho_Sessao`, `Presenca_Sessao`, `Perfil`, `Log_Auditoria`.

📄 [Ver schema SQL completo](database/impulso_pro.sql)  
📊 [Ver DER — Diagrama Entidade-Relacionamento](docs/der-impulso-pro.png)

---

## Perfis de Acesso

| Perfil | Capacidades principais |
|--------|----------------------|
| **Gestor da Rede** | Visão consolidada de todas as unidades, configuração global de perfis e permissões |
| **Gestor de Unidade** | Criação e atribuição de treinamentos, acompanhamento de colaboradores da sua unidade |
| **Treinador** | Condução de sessões, registro de desempenho, pode atuar em múltiplas unidades |
| **Colaborador** | Registro de presença, visualização de resultados e treinamentos obrigatórios |

---

## Como Rodar Localmente

### Pré-requisitos

- Python 3.11+
- Node.js 18+
- MySQL 8.0

### Backend

```bash
# Clone o repositório
git clone https://github.com/ChrystiannSangiorgi/impulso-pro.git
cd impulso-pro/backend

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente
cp .env.example .env
# Edite o .env com suas credenciais do MySQL e secret do JWT

# Suba o servidor
uvicorn app.main:app --reload
```

A documentação da API estará disponível em: `http://localhost:8000/docs`

### Banco de Dados

```bash
# No MySQL, crie o banco e execute o schema
mysql -u root -p
CREATE DATABASE impulso_pro;
USE impulso_pro;
source database/impulso_pro.sql;
```

### Frontend

```bash
cd impulso-pro/frontend

# Instale as dependências
npm install

# Configure as variáveis de ambiente
cp .env.example .env
# Edite o .env com a URL da API

# Suba o servidor de desenvolvimento
npm run dev
```

---

## Documentação do Projeto

Toda a documentação formal está disponível na [Wiki do repositório](../../wiki).

| Documento | Descrição |
|-----------|-----------|
| [Project Charter](Project‐Charter) | Visão, escopo, stakeholders e critérios de sucesso |
| [Product Backlog](../../wiki/Product-Backlog) | 29 User Stories priorizadas com MoSCoW |
| [Definition of Done](../../wiki/Definition-of-Done) | Critérios de qualidade para conclusão de stories |
| [Sprint 01 — Planejamento](../../wiki/Sprint-01-Planejamento) | Objetivo, sprint backlog e tasks detalhadas |

---

## Status do Projeto

### Progresso Geral

| Fase | Status |
|------|--------|
| Planejamento e documentação | ✅ Concluído |
| Sprint 01 — Fundação (Auth + Unidades) | 🔄 Em andamento |
| Sprint 02 — Colaboradores e Importação | ⏳ Planejada |
| Sprint 03 — Treinamentos e Trilhas | ⏳ Planejada |
| Sprint 04 — Sessões e Presença | ⏳ Planejada |
| Sprint 05 — Desempenho e Relatórios | ⏳ Planejada |
| Deploy em produção | ⏳ Planejada |

---

## Gestão do Projeto

Este projeto é desenvolvido individualmente com a metodologia **Scrum** adaptada para desenvolvimento solo:

- **Sprints** de 2 semanas
- **User Stories** como Issues do GitHub com labels e estimativas
- **Scrum Board** via GitHub Projects
- **Conventional Commits** para histórico semântico
- **Sprint Reviews e Retrospectivas** documentadas na Wiki

---

## Origem do Projeto

O Impulso Pro nasceu como trabalho acadêmico na disciplina de **Modelagem de Banco de Dados** (1º semestre, Ciência da Computação, 2025), desenvolvido em equipe com foco em análise de requisitos, modelagem conceitual, DER e normalização até 3FN.

O repositório original com todos os artefatos acadêmicos — minimundo, DER, MER, verificação de formas normais e schema SQL — está disponível em:

🔗 [Impulso_Pro_Projeto_Banco_De_Dados](https://github.com/ChrystiannSangiorgi/Impulso_Pro_Projeto_Banco_De_Dados)

Este repositório representa a **evolução do projeto** para uma aplicação full-stack real, com arquitetura de software, API REST, interface web e gestão ágil formal.

---

## Autor

**Chrystiann Caesar Sangiorgi de Oliveira**  
Estudante de Ciência da Computação · 2º Semestre

[![GitHub](https://img.shields.io/badge/GitHub-ChrystiannSangiorgi-black?logo=github)](https://github.com/ChrystiannSangiorgi)

---

*Projeto em desenvolvimento ativo. Documentação e funcionalidades são atualizadas a cada sprint.*
