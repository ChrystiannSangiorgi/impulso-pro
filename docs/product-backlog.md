# Product Backlog — Impulso Pro

> **Versão:** 1.0  
> **Data:** Abril de 2026  
> **Status:** Ativo  
> **Responsável:** Chrystiann Caesar Sangiorgi de Oliveira

---

## Legenda

### Prioridade (MoSCoW)
| Sigla | Significado |
|-------|-------------|
| 🔴 M | **Must Have** — Essencial. O sistema não funciona sem isso. |
| 🟠 S | **Should Have** — Importante, mas não bloqueia o lançamento. |
| 🟡 C | **Could Have** — Desejável. Entra se houver tempo. |
| ⚪ W | **Won't Have** — Fora do escopo desta versão. |

### Esforço (Story Points — Fibonacci)
`1` Trivial · `2` Simples · `3` Médio · `5` Complexo · `8` Muito complexo · `13` Épico

---

## Épicos

| ID | Épico |
|----|-------|
| EP-01 | Autenticação e Controle de Acesso |
| EP-02 | Gestão de Colaboradores |
| EP-03 | Gestão de Treinamentos |
| EP-04 | Sessões de Treinamento |
| EP-05 | Presença e Desempenho |
| EP-06 | Trilhas de Treinamento |
| EP-07 | Relatórios e Dashboards |
| EP-08 | Integração com Sistema de RH |
| EP-09 | Administração da Rede |

---

## EP-01 — Autenticação e Controle de Acesso

### US-001
**Como** qualquer usuário do sistema,  
**quero** fazer login com e-mail e senha,  
**para** acessar as funcionalidades do meu perfil de forma segura.

**Critérios de Aceitação:**
- Login com e-mail e senha válidos retorna token JWT
- Senha incorreta incrementa contador de tentativas falhas
- Após 5 tentativas falhas, a conta é bloqueada
- Token JWT expira em 8 horas
- Senha armazenada com hash bcrypt

**Prioridade:** 🔴 M | **Esforço:** 3

---

### US-002
**Como** qualquer usuário autenticado,  
**quero** fazer logout do sistema,  
**para** encerrar minha sessão com segurança.

**Critérios de Aceitação:**
- Token é invalidado ao fazer logout
- Usuário é redirecionado para a tela de login

**Prioridade:** 🔴 M | **Esforço:** 1

---

### US-003
**Como** Gestor de RH da Rede,  
**quero** definir os perfis de acesso e suas permissões,  
**para** controlar o que cada tipo de usuário pode visualizar e executar no sistema.

**Critérios de Aceitação:**
- Perfis disponíveis: Colaborador, Treinador, Gestor de Unidade, Gestor da Rede
- Cada perfil tem um conjunto de permissões associadas
- Permissões podem ser visualizadas por perfil
- Um colaborador pode ter apenas um perfil ativo

**Prioridade:** 🔴 M | **Esforço:** 5

---

### US-004
**Como** qualquer usuário,  
**quero** redefinir minha senha em caso de esquecimento,  
**para** recuperar o acesso à minha conta.

**Critérios de Aceitação:**
- Usuário informa e-mail cadastrado
- Sistema envia link de redefinição com expiração de 1 hora
- Nova senha deve ser diferente das últimas 3 senhas utilizadas

**Prioridade:** 🟠 S | **Esforço:** 3

---

## EP-02 — Gestão de Colaboradores

### US-005
**Como** Gestor de RH (Unidade ou Rede),  
**quero** visualizar a lista de colaboradores da(s) minha(s) unidade(s),  
**para** ter visão completa do quadro de pessoal.

**Critérios de Aceitação:**
- Lista exibe nome, cargo, departamento e status (ativo/inativo)
- Gestor de Unidade vê apenas colaboradores da sua unidade
- Gestor da Rede vê colaboradores de todas as unidades, com filtro por unidade
- Lista é paginada e pesquisável por nome ou cargo

**Prioridade:** 🔴 M | **Esforço:** 3

---

### US-006
**Como** Gestor de RH da Rede,  
**quero** importar colaboradores a partir de um sistema de RH externo,  
**para** evitar o cadastro manual e manter os dados sincronizados.

**Critérios de Aceitação:**
- Sistema aceita importação via arquivo CSV como mecanismo inicial
- Campos obrigatórios: nome, e-mail, cargo, departamento, unidade
- Importação exibe relatório de sucesso e erros por linha
- Colaboradores duplicados (mesmo e-mail) são ignorados com aviso

**Prioridade:** 🔴 M | **Esforço:** 5

---

### US-007
**Como** Gestor de RH (Unidade ou Rede),  
**quero** ativar ou desativar um colaborador no sistema,  
**para** gerenciar entradas e saídas sem excluir o histórico de treinamentos.

**Critérios de Aceitação:**
- Colaborador inativo não aparece em novas atribuições de treinamento
- Histórico de treinamentos do colaborador inativo é preservado
- Ação fica registrada no Log de Auditoria

**Prioridade:** 🔴 M | **Esforço:** 2

---

### US-008
**Como** Colaborador,  
**quero** visualizar meu perfil com dados pessoais e profissionais,  
**para** verificar se minhas informações estão corretas no sistema.

**Critérios de Aceitação:**
- Exibe: nome, e-mail, telefone, cargo, departamento e unidade
- Colaborador não pode editar cargo, departamento ou unidade
- Colaborador pode solicitar correção de dados via sistema

**Prioridade:** 🟠 S | **Esforço:** 2

---

## EP-03 — Gestão de Treinamentos

### US-009
**Como** Gestor de RH (Unidade ou Rede),  
**quero** criar um novo treinamento com nome, descrição e categoria,  
**para** ampliar o catálogo de capacitações disponíveis.

**Critérios de Aceitação:**
- Campos obrigatórios: nome, descrição, categoria e trilha vinculada
- Categoria define se o treinamento é obrigatório ou livre
- Treinamento criado fica disponível no catálogo da rede

**Prioridade:** 🔴 M | **Esforço:** 3

---

### US-010
**Como** Gestor de RH (Unidade ou Rede),  
**quero** editar as informações de um treinamento existente,  
**para** manter o catálogo atualizado.

**Critérios de Aceitação:**
- Possível editar nome, descrição e categoria
- Edição não afeta registros históricos de sessões já realizadas
- Alteração registrada no Log de Auditoria

**Prioridade:** 🟠 S | **Esforço:** 2

---

### US-011
**Como** Gestor de RH (Unidade ou Rede),  
**quero** atribuir um treinamento a um colaborador específico ou a uma equipe,  
**para** garantir que as capacitações certas cheguem às pessoas certas.

**Critérios de Aceitação:**
- Atribuição pode ser feita para um colaborador individual ou para um cargo/departamento inteiro
- Colaboradores atribuídos recebem notificação no sistema
- Treinamentos obrigatórios são destacados visualmente

**Prioridade:** 🔴 M | **Esforço:** 5

---

### US-012
**Como** Colaborador,  
**quero** visualizar os treinamentos que me foram atribuídos,  
**para** saber quais capacitações preciso realizar e quais são obrigatórias.

**Critérios de Aceitação:**
- Lista separada entre treinamentos obrigatórios e livres
- Exibe status de cada treinamento: Pendente, Em andamento, Concluído
- Treinamentos obrigatórios não concluídos são destacados com alerta

**Prioridade:** 🔴 M | **Esforço:** 3

---

## EP-04 — Sessões de Treinamento

### US-013
**Como** Gestor de RH ou Treinador,  
**quero** criar uma sessão de treinamento com data, horário e local,  
**para** agendar a realização de um treinamento para uma equipe.

**Critérios de Aceitação:**
- Campos obrigatórios: treinamento vinculado, data, horário e local
- Treinador responsável pela sessão deve ser selecionado
- Colaboradores participantes são associados à sessão no momento da criação

**Prioridade:** 🔴 M | **Esforço:** 5

---

### US-014
**Como** Treinador,  
**quero** visualizar todas as sessões sob minha responsabilidade,  
**para** me organizar e me preparar para os treinamentos que vou conduzir.

**Critérios de Aceitação:**
- Lista exibe sessões futuras e passadas com filtro por período
- Treinador multi-unidade visualiza sessões de todas as unidades em que atua
- Cada sessão exibe: treinamento, data, horário, local e lista de participantes

**Prioridade:** 🔴 M | **Esforço:** 3

---

### US-015
**Como** Gestor de RH ou Treinador,  
**quero** editar ou cancelar uma sessão de treinamento,  
**para** adaptar a agenda a mudanças operacionais.

**Critérios de Aceitação:**
- Possível editar data, horário e local antes da realização
- Cancelamento notifica os participantes
- Sessões já realizadas não podem ser editadas

**Prioridade:** 🟠 S | **Esforço:** 3

---

## EP-05 — Presença e Desempenho

### US-016
**Como** Colaborador,  
**quero** registrar minha presença em uma sessão de treinamento após sua conclusão,  
**para** confirmar minha participação no sistema.

**Critérios de Aceitação:**
- Registro de presença disponível apenas após o horário de início da sessão
- Colaborador só pode registrar presença em sessões às quais foi atribuído
- Presença registrada não pode ser desfeita pelo colaborador

**Prioridade:** 🔴 M | **Esforço:** 3

---

### US-017
**Como** Treinador,  
**quero** registrar a nota de avaliação e o feedback de cada colaborador em uma sessão,  
**para** documentar o desempenho individual de forma contextualizada.

**Critérios de Aceitação:**
- Campos disponíveis: nota (0 a 10), progresso (0% a 100%), feedback textual e resultado (Aprovado/Reprovado)
- Preenchimento disponível apenas para colaboradores com presença registrada
- Registro salvo no histórico de desempenho do colaborador

**Prioridade:** 🔴 M | **Esforço:** 5

---

### US-018
**Como** Colaborador,  
**quero** visualizar meus resultados de avaliações anteriores,  
**para** acompanhar meu próprio desenvolvimento.

**Critérios de Aceitação:**
- Exibe histórico de sessões com nota, progresso e resultado
- Inclui feedback do treinador quando disponível
- Ordenado da sessão mais recente para a mais antiga

**Prioridade:** 🟠 S | **Esforço:** 2

---

### US-019
**Como** Treinador,  
**quero** visualizar o desempenho de todos os colaboradores das sessões que conduzi,  
**para** identificar quem precisa de reforço ou atenção especial.

**Critérios de Aceitação:**
- Visão consolidada por sessão com todos os participantes
- Destaque visual para colaboradores com resultado Reprovado
- Exportação básica dos dados da sessão (CSV)

**Prioridade:** 🟠 S | **Esforço:** 3

---

## EP-06 — Trilhas de Treinamento

### US-020
**Como** Gestor de RH da Rede,  
**quero** criar trilhas de treinamento agrupando múltiplos treinamentos,  
**para** estruturar a capacitação por função ou área.

**Critérios de Aceitação:**
- Trilha tem nome e conteúdo teórico associado
- Uma trilha pode conter múltiplos treinamentos
- Trilha pode ser vinculada a um cargo específico

**Prioridade:** 🔴 M | **Esforço:** 3

---

### US-021
**Como** Colaborador,  
**quero** visualizar meu progresso em uma trilha de treinamento,  
**para** saber quantos treinamentos já concluí e o que ainda falta.

**Critérios de Aceitação:**
- Exibe percentual de conclusão da trilha
- Lista os treinamentos da trilha com status individual
- Resultado final da trilha exibido quando todos os treinamentos são concluídos

**Prioridade:** 🟠 S | **Esforço:** 3

---

## EP-07 — Relatórios e Dashboards

### US-022
**Como** Gestor de RH (Unidade ou Rede),  
**quero** visualizar um dashboard com indicadores gerais da minha unidade ou rede,  
**para** ter visão rápida da saúde dos treinamentos.

**Critérios de Aceitação:**
- Indicadores: total de colaboradores, % com treinamentos obrigatórios em dia, sessões realizadas no mês
- Gestor de Unidade vê dados da sua unidade
- Gestor da Rede vê dados consolidados com possibilidade de filtrar por unidade

**Prioridade:** 🟠 S | **Esforço:** 5

---

### US-023
**Como** Gestor de RH (Unidade ou Rede),  
**quero** gerar um relatório de frequência por período e por treinamento,  
**para** monitorar a adesão dos colaboradores.

**Critérios de Aceitação:**
- Filtros: período (data inicial e final), treinamento e unidade
- Relatório exibe: colaborador, sessão, data e status de presença
- Exportação em CSV

**Prioridade:** 🟠 S | **Esforço:** 5

---

### US-024
**Como** Gestor de RH ou Treinador,  
**quero** gerar um relatório de desempenho por colaborador,  
**para** identificar necessidade de novos treinamentos ou reforços.

**Critérios de Aceitação:**
- Filtros: colaborador, período e trilha
- Relatório exibe: sessões, notas, progresso e resultados
- Média geral calculada automaticamente

**Prioridade:** 🟠 S | **Esforço:** 5

---

## EP-08 — Integração com Sistema de RH

### US-025
**Como** Gestor de RH da Rede,  
**quero** importar colaboradores via arquivo CSV,  
**para** cadastrar múltiplos colaboradores de forma rápida sem depender de integração direta.

**Critérios de Aceitação:**
- Template CSV disponível para download no sistema
- Campos: nome, e-mail, telefone, cargo, departamento, unidade
- Relatório de importação com linhas com erro e linhas importadas com sucesso
- E-mails duplicados são ignorados com aviso

**Prioridade:** 🔴 M | **Esforço:** 5

---

### US-026
**Como** Gestor de RH da Rede,  
**quero** que o sistema suporte integração via API com sistemas de RH externos,  
**para** automatizar a sincronização de colaboradores sem intervenção manual.

**Critérios de Aceitação:**
- Endpoint de recebimento de dados de colaboradores via POST autenticado
- Atualiza dados de colaboradores existentes e cria novos
- Log de cada sincronização disponível para auditoria

**Prioridade:** 🟡 C | **Esforço:** 8

---

## EP-09 — Administração da Rede

### US-027
**Como** Gestor de RH da Rede,  
**quero** cadastrar e gerenciar as unidades (restaurantes) da rede,  
**para** organizar colaboradores e treinamentos por unidade.

**Critérios de Aceitação:**
- Cadastro com nome, endereço completo e status (ativo/inativo)
- Unidade inativa não aparece em novas atribuições
- Histórico de treinamentos da unidade é preservado ao inativar

**Prioridade:** 🔴 M | **Esforço:** 3

---

### US-028
**Como** Gestor de RH da Rede,  
**quero** vincular um Treinador a uma ou mais unidades da rede,  
**para** permitir que ele conduza sessões em diferentes locais.

**Critérios de Aceitação:**
- Treinador pode ser vinculado a N unidades
- Vínculo pode ser adicionado ou removido sem afetar histórico de sessões
- Treinador visualiza apenas as sessões das unidades às quais está vinculado

**Prioridade:** 🔴 M | **Esforço:** 3

---

### US-029
**Como** Gestor de RH da Rede,  
**quero** visualizar o Log de Auditoria das ações realizadas no sistema,  
**para** rastrear alterações e garantir a integridade dos dados.

**Critérios de Aceitação:**
- Exibe: data/hora, usuário responsável, tabela afetada, ação realizada e detalhes
- Filtros por período, usuário e tipo de ação
- Log é somente leitura — não pode ser editado ou excluído

**Prioridade:** 🟡 C | **Esforço:** 3

---

## Resumo do Backlog

| Épico | Total de US | 🔴 Must | 🟠 Should | 🟡 Could |
|-------|------------|--------|----------|---------|
| EP-01 Autenticação | 4 | 2 | 1 | 1 |
| EP-02 Colaboradores | 4 | 3 | 1 | 0 |
| EP-03 Treinamentos | 4 | 3 | 1 | 0 |
| EP-04 Sessões | 3 | 2 | 1 | 0 |
| EP-05 Presença e Desempenho | 4 | 2 | 2 | 0 |
| EP-06 Trilhas | 2 | 1 | 1 | 0 |
| EP-07 Relatórios | 3 | 0 | 3 | 0 |
| EP-08 Integração RH | 2 | 1 | 0 | 1 |
| EP-09 Administração | 3 | 2 | 0 | 1 |
| **Total** | **29** | **16** | **10** | **3** |

---

*Backlog sujeito a revisão e repriorização ao início de cada Sprint.*
