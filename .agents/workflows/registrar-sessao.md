---
description: Registrar sessão no history ao final do trabalho
---

# Workflow: Registrar Sessão

## Quando usar
Ao final de qualquer sessão de trabalho significativa (criação de resumo, análise de questões, refatoração).

## Passos

### 1. Identificar o próximo número
Verificar `history/` e usar o próximo número sequencial: `session_NNN.md`.

### 2. Criar o session log
Criar `history/session_NNN.md` com o seguinte formato:

```markdown
# Session NNN — [Título descritivo]
**Data:** YYYY-MM-DD
**Ferramenta:** [Antigravity / Claude Code / Gemini / etc.]
**Continuidade:** Sessão NNN-1 (se aplicável)

---

## O que foi feito
- [Lista de ações realizadas]

## Artefatos criados/modificados
- [Lista de arquivos com paths relativos]

## Decisões tomadas
- [Decisões importantes para contexto futuro]

## Próximos passos (se houver)
- [O que ficou pendente]
```

### 3. Atualizar ESTADO.md
Adicionar entrada na seção "Últimas sessões" do `ESTADO.md` com resumo de uma linha.
