# Definition of Done (DoD) — Impulso Pro

> **Versão:** 1.0  
> **Data:** Abril de 2026  
> **Status:** Ativo  
> **Responsável:** Chrystiann Caesar Sangiorgi de Oliveira

---

## O que é a Definition of Done?

A Definition of Done (DoD) é um conjunto de critérios acordados que uma User Story precisa atender para ser considerada **verdadeiramente concluída**. Não basta o código funcionar — a entrega só está pronta quando todos os critérios abaixo são satisfeitos.

Em um time Scrum, a DoD é um contrato de qualidade. Neste projeto solo, ela serve como checklist obrigatório antes de mover qualquer tarefa para a coluna **Done** no Scrum Board.

---

## Critérios Gerais

Aplicam-se a **todas** as User Stories, independente do épico.

### Código

- [ ] O código foi escrito e está funcionando conforme os critérios de aceitação da User Story
- [ ] Não há erros ou exceções não tratadas nos fluxos cobertos pela story
- [ ] O código segue o padrão de nomenclatura definido para o projeto (snake_case para Python, camelCase para JavaScript/React)
- [ ] Não há código comentado ou debug deixado no arquivo (`print()`, `console.log()` de teste, etc.)
- [ ] Variáveis de ambiente sensíveis (credenciais, secrets) estão em `.env` e não estão commitadas

### Versionamento

- [ ] O código foi commitado em uma branch separada com nome no padrão `feature/US-XXX-descricao-curta`
- [ ] O commit segue a convenção **Conventional Commits**:
  - `feat:` nova funcionalidade
  - `fix:` correção de bug
  - `docs:` documentação
  - `refactor:` refatoração sem mudança de comportamento
  - `test:` adição ou correção de testes
- [ ] A branch foi mergeada na branch `develop` via Pull Request
- [ ] O Pull Request referencia a Issue correspondente (`Closes #XX`)

### Banco de Dados

- [ ] Alterações no schema (novas tabelas, colunas, índices) estão documentadas em um arquivo de migration versionado
- [ ] Nenhuma query utiliza `SELECT *` — apenas colunas necessárias são selecionadas
- [ ] Chaves estrangeiras e constraints estão aplicadas corretamente

### Backend (API)

- [ ] O endpoint está documentado automaticamente no Swagger (FastAPI gera isso automaticamente)
- [ ] A rota está protegida com autenticação JWT quando necessário
- [ ] A rota valida os dados de entrada (tipos, campos obrigatórios) via Pydantic
- [ ] Respostas de erro retornam HTTP status code adequado com mensagem descritiva:
  - `400` Bad Request — dados inválidos
  - `401` Unauthorized — não autenticado
  - `403` Forbidden — sem permissão
  - `404` Not Found — recurso não encontrado
  - `500` Internal Server Error — erro inesperado do servidor

### Frontend

- [ ] A interface implementada corresponde ao fluxo descrito na User Story
- [ ] Erros de API são tratados e exibidos ao usuário de forma amigável (sem mensagens técnicas expostas)
- [ ] A tela é responsiva para desktop e mobile
- [ ] Campos de formulário têm validação no lado do cliente antes de enviar à API
- [ ] Nenhum dado sensível (token JWT, senha) é exibido ou logado no console do browser

### Testes

- [ ] O fluxo principal da User Story foi testado manualmente e está funcionando
- [ ] Os fluxos alternativos (erros, campos vazios, dados inválidos) foram testados manualmente
- [ ] Para endpoints de backend: ao menos um teste automatizado cobre o caminho feliz (happy path)

---

## Critérios por Tipo de Entrega

### Quando a entrega envolve Autenticação / Segurança

- [ ] Senha nunca trafega em texto puro — apenas hash bcrypt
- [ ] Token JWT não é armazenado em localStorage (usar httpOnly cookie ou sessionStorage)
- [ ] Rotas protegidas retornam `401` quando o token está ausente ou expirado
- [ ] Consentimento LGPD é registrado com data/hora quando aplicável

### Quando a entrega envolve Relatório ou Dashboard

- [ ] Os dados exibidos correspondem ao escopo de visibilidade do perfil do usuário (Gestor de Unidade não vê dados de outras unidades)
- [ ] Filtros funcionam corretamente e não expõem dados fora do escopo
- [ ] Exportação CSV (quando aplicável) gera arquivo válido e com cabeçalho

### Quando a entrega envolve Importação de Dados

- [ ] Importação valida cada linha antes de inserir
- [ ] Relatório de importação exibe claramente o que foi importado e o que falhou
- [ ] Dados duplicados são tratados sem gerar erro crítico

### Quando a entrega envolve Log de Auditoria

- [ ] A ação realizada está sendo registrada corretamente na tabela `Log_Auditoria`
- [ ] O log contém: usuário responsável, tabela afetada, ID do registro, ação e timestamp

---

## Critérios de Documentação

- [ ] A Issue correspondente no GitHub foi atualizada com o resultado da implementação
- [ ] Se a story introduziu uma decisão técnica relevante (ex: mudança de arquitetura, novo padrão), ela foi registrada no Wiki do repositório
- [ ] O README foi atualizado se a entrega adicionou alguma funcionalidade visível ao projeto

---

## Checklist Rápido (para usar no dia a dia)

Antes de mover uma story para **Done**, confirme:

```
[ ] Critérios de aceitação da story: todos atendidos?
[ ] Código commitado na branch correta com mensagem semântica?
[ ] Pull Request aberto e mergeado em develop?
[ ] Endpoint documentado no Swagger?
[ ] Testes manuais dos fluxos principal e alternativos realizados?
[ ] Nenhum dado sensível exposto ou commitado?
[ ] Issue fechada com referência ao PR?
```

---

## O que NÃO é DoD

Para evitar confusão, os itens abaixo **não fazem parte** da DoD — eles são critérios de aceitação específicos de cada User Story e devem estar na própria Issue:

- Regras de negócio específicas (ex: "colaborador inativo não aparece em novas atribuições")
- Layouts ou comportamentos visuais específicos de uma tela
- Validações de negócio particulares de um fluxo

---

*A DoD pode ser revisada ao final de cada Sprint durante a Retrospectiva.*
