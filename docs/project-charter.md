# Project Charter — Impulso Pro

> **Versão:** 1.0  
> **Data:** Abril de 2026  
> **Status:** Ativo  
> **Autor:** Chrystiann Caesar Sangiorgi de Oliveira

---

## 1. Visão Geral do Projeto

**Impulso Pro** é uma plataforma web de gestão de treinamentos operacionais desenvolvida exclusivamente para redes de restaurantes. O sistema centraliza o registro, o acompanhamento e o monitoramento de capacitações de equipes como garçons, cozinheiros, atendentes e auxiliares, oferecendo visibilidade em tempo real para Gestores de RH e Treinadores.

O projeto nasce da evolução de um trabalho acadêmico de modelagem de banco de dados (1º semestre — Ciência da Computação), agora desenvolvido como produto independente com arquitetura full-stack, documentação formal e gestão ágil com Scrum.

---

## 2. Objetivos

| # | Objetivo |
|---|----------|
| 1 | Centralizar o registro de presença e desempenho de colaboradores por treinamento e por unidade |
| 2 | Permitir que Gestores de RH criem, editem e atribuam treinamentos obrigatórios e livres |
| 3 | Oferecer visão consolidada de desempenho por colaborador, equipe e unidade |
| 4 | Suportar redes com múltiplas unidades, incluindo treinadores que atuam em mais de uma unidade |
| 5 | Integrar-se com sistemas de RH externos via importação de colaboradores |

---

## 3. Escopo

### 3.1 Incluso

- Cadastro e gestão de treinamentos (nome, descrição, categoria, trilha)
- Atribuição de treinamentos a colaboradores ou equipes
- Registro de presença em sessões de treinamento
- Avaliação de desempenho por sessão (nota, progresso, feedback)
- Registro de resultado final por trilha (Aprovado / Reprovado)
- Relatórios de frequência e desempenho por colaborador e unidade
- Importação de colaboradores via integração com sistema de RH externo
- Suporte a dois níveis de gestão: Gestor por Unidade e Gestor da Rede
- Suporte a Treinadores que atuam em múltiplas unidades da rede
- Log de auditoria de ações no sistema
- Autenticação segura com JWT e hash de senha (bcrypt)

### 3.2 Excluso

- Aplicação dos treinamentos (o sistema gerencia, não executa)
- Gestão de folha de pagamento
- Controle de ponto dos colaboradores
- Emissão de certificados de conclusão
- Gestão de benefícios ou férias

---

## 4. Stakeholders

| Perfil | Papel no Sistema | Nível de Gestão |
|--------|-----------------|-----------------|
| Gestor de RH da Rede | Visão consolidada de todas as unidades, configuração global | Rede |
| Gestor de RH por Unidade | Gestão de treinamentos e colaboradores da sua unidade | Unidade |
| Treinador | Conduz sessões, registra desempenho, pode atuar em múltiplas unidades | Unidade(s) |
| Colaborador | Registra presença, visualiza resultados e treinamentos obrigatórios | Individual |

> **Nota:** Os perfis de acesso detalhados (permissões específicas por perfil) serão definidos como parte do backlog da Sprint 1.

---

## 5. Requisitos de Alto Nível

### Funcionais

- O sistema deve permitir que o Gestor de RH crie e atribua treinamentos a colaboradores ou equipes
- O sistema deve registrar a presença de colaboradores em sessões de treinamento
- O sistema deve calcular e exibir o desempenho de cada colaborador por sessão e por trilha
- O sistema deve suportar dois níveis hierárquicos de gestão (unidade e rede)
- O sistema deve importar colaboradores via integração com sistema externo de RH
- Um treinador pode ser vinculado a uma ou mais unidades da rede

### Não Funcionais

- Autenticação via JWT com expiração configurável
- Senhas armazenadas com hash bcrypt
- Bloqueio de conta após tentativas de login excessivas
- Conformidade com LGPD (consentimento registrado por colaborador)
- API RESTful documentada automaticamente via Swagger (FastAPI)
- Tempo de resposta das principais rotas abaixo de 500ms

---

## 6. Stack Tecnológica

| Camada | Tecnologia | Justificativa |
|--------|-----------|---------------|
| Backend | Python + FastAPI | Alinhado ao aprendizado acadêmico atual; documentação automática via Swagger |
| Banco de Dados | MySQL | Schema já modelado e validado com normalização até 3FN |
| Frontend | React + Vite | Stack familiar do desenvolvedor; componentização eficiente |
| Autenticação | JWT + bcrypt | Padrão de mercado; alinhado com o schema `Colaborador_Autenticacao` |
| Deploy | Railway (backend) + Vercel (frontend) | Gratuitos, simples e adequados para portfólio |
| Versionamento | GitHub | Documentação, Issues e Projects centralizados |

---

## 7. Restrições e Premissas

### Restrições

- Projeto desenvolvido individualmente, sem equipe
- Recursos de infraestrutura limitados ao plano gratuito das plataformas de deploy
- Sistema exclusivo para o segmento de redes de restaurantes

### Premissas

- A rede de restaurantes contratante possui um sistema de RH externo com capacidade de exportar dados de colaboradores
- A regra de um treinador poder atuar em múltiplas unidades é configurável por rede (não é padrão obrigatório)
- O sistema não gerencia a criação manual de contas — colaboradores são importados do sistema de RH

---

## 8. Riscos Iniciais

| Risco | Probabilidade | Impacto | Mitigação |
|-------|--------------|---------|-----------|
| Escopo crescer além da capacidade solo | Alta | Alto | Backlog priorizado com MoSCoW; sprints curtas de 2 semanas |
| Integração com sistema de RH externo ser complexa | Média | Alto | Implementar importação via CSV como fallback na Sprint 1 |
| Definição tardia dos perfis de acesso atrasar o desenvolvimento | Média | Médio | Mapear permissões como primeira User Story do backlog |
| Treinador multi-unidade exigir refatoração do schema atual | Alta | Médio | Revisão do schema antes da Sprint 1 de desenvolvimento |

---

## 9. Metodologia de Gestão

O projeto seguirá o framework **Scrum** adaptado para desenvolvimento solo:

- **Sprints:** 2 semanas
- **Papéis:** Chrystiann acumula Product Owner, Scrum Master e Developer
- **Cerimônias adaptadas:**
  - Sprint Planning ao início de cada sprint (definição do sprint backlog)
  - Sprint Review ao final (demo do que foi entregue)
  - Sprint Retrospective ao final (o que funcionou, o que melhorar)
- **Artefatos:**
  - Product Backlog → GitHub Issues com labels e milestones
  - Sprint Backlog → GitHub Projects (Scrum Board)
  - Definition of Done → Wiki do repositório
  - Incremento → Deploy funcional ao final de cada sprint

---

## 10. Critérios de Sucesso

| Critério | Como será medido |
|----------|-----------------|
| API funcional com as rotas principais | Todos os endpoints documentados e testados via Swagger |
| Frontend conectado ao backend | Fluxos principais navegáveis no browser |
| Sistema deployado e acessível | URL pública funcionando |
| Documentação completa no GitHub | README, Wiki e histórico de sprints preenchidos |
| Código versionado com histórico limpo | Commits semânticos, branches por feature |

---

## 11. Origem do Projeto

Este projeto é a evolução de um trabalho acadêmico desenvolvido em grupo na disciplina de Modelagem de Banco de Dados (1º semestre — Ciência da Computação, 2025). O repositório original com os artefatos de modelagem está disponível em:

🔗 [Impulso_Pro_Projeto_Banco_De_Dados](https://github.com/ChrystiannSangiorgi/Impulso_Pro_Projeto_Banco_De_Dados)

---

*Documento sujeito a revisão ao início de cada sprint.*
