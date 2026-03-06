# IPUB — Ambiente de Estudo para Residência Médica

Agente de estudo que analisa questões de prova, registra padrões de erro e mantém resumos clínicos organizados. Portável para qualquer LLM via workflows.

## Estrutura

```
IPUB/
├── ESTADO.md              ← fonte de verdade (ler primeiro)
├── CLAUDE.md              ← pointer para Claude Code
├── caderno_erros.md       ← banco de erros (36 entradas)
├── progresso.md           ← visão consolidada
│
├── .agents/workflows/     ← workflows portáveis
│   ├── criar-resumo.md
│   ├── analisar-questoes.md
│   └── registrar-sessao.md
│
├── referencia/            ← specs e padrões
│   └── estilo-resumo.md
│
├── Temas/                 ← resumos por área/subespecialidade
│   ├── Cirurgia/
│   ├── Clínica Médica/
│   ├── GO/
│   ├── Pediatria/
│   └── Preventiva/
│
├── Tools/                 ← scripts e protocolos
├── Fichas/                ← PDFs de fichas de prova
├── Memorex/               ← PDFs de revisão rápida
├── Extracted/             ← textos extraídos (regeneráveis)
└── history/               ← session logs por sessão
```

## Para começar

1. Leia `ESTADO.md`
2. Use o workflow apropriado em `.agents/workflows/`
