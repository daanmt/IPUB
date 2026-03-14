# Product Roadmap: Sistema de Estudos IPUB

> **Visão de Produto:** Um ecossistema de aprendizado ativo para residência médica que transforma passividade (ler) em hiper-retenção (testes, espaçamento e análise metacognitiva de erros). 
> **Foco Core:** Automação do trabalho braçal de criar materiais, permitindo ao usuário focar exclusivamento no estudo e na resolução clínica.

---

## 📍 Fase 1: MVP - Fundação de Conhecimento (Status: Concluído / Em uso)
*A infraestrutura básica para curadoria de conhecimento médico e diagnóstico de erros de prova.*

**Entregas Atuais:**
- [x] **Agente LLM Integrado (Antigravity):** Atua como co-piloto na IDE para processamento rápido baseando-se em `AGENTE.md` e `ESTADO.md`.
- [x] **Caderno de Erros Centralizado (`caderno_erros.md`):** Taxonomia robusta baseada em Habilidades Sequenciais e Metacognição (Diagnóstico do tipo de erro).
- [x] **Base de Conhecimento (`Temas/`):** Geração e formatação padronizada de resumos clínicos otimizados, alimentados diretamente pelos erros das questões.
- [x] **Motor de Extração de Texto:** Script local (`extract_pdfs.py`) para consumir grandes volumes de PDFs e apostilas sem poluir o repositório.
- [x] **Workflows Standard Operating Procedures (SOPs):** `.agents/workflows/` (Ex: Analisar questões médicas complexas garantindo o mesmo output sempre).

---

## 🚀 Fase 2: Motor de Retenção e Espaçamento (Status: Próximo Passo)
*Transformar o texto estático dos cadernos de erros e resumos em flashcards e algoritmos de repetição espaçada.*

**Objetivos:**
- [ ] **Conversão Automatizada para Flashcards:** 
  - Criar um script/workflow onde o Agente lê o `caderno_erros.md` e gera pares de *Front/Back* (Ex. Pergunta/Resposta) baseados no "Elo Quebrado" e na "Regra/Armadilha".
- [ ] **Exportação Universal (Anki / Texto):** 
  - Gerar arquivos `.csv` ou `.txt` formatados para importação num clique no Anki, ou para consumo futuro do nosso próprio Frontend.
- [ ] **Flashcards de Resumos (Cloze Deletion):**
  - Mapear os resumos na pasta `Temas/` e, através do Agente, extrair os tópicos marcados com `🔴` e `⭐` gerando flashcards de preenchimento de lacunas e de alta retenção.

---

## 🖥️ Fase 3: Interface do Usuário (UI) & Banco de Dados (Em Planejamento)
*Sair da interface da IDE (Markdown) para uma aplicação Web (Streamlit), democratizando o acesso e facilitando a interação diária.*

**Objetivos:**
- [ ] **Migração de Arquivos para Banco de Dados Relacional:**
  - Substituir/Espelhar os `.md` por um banco leve (SQLite ou PostgreSQL), estruturando as tabelas: `usuarios`, `questoes_resolvidas`, `flashcards`, `resumos_teoricos`.
- [ ] **App Web IPUB UI (Streamlit):**
  - **Módulo 1 - Input de Questões:** Área de texto simples onde o usuário cola a questão que errou. O backend (LLM) processa em background com o mesmo prompt de `comando de analise de questao.md` e salva no DB.
  - **Módulo 2 - Painel de Flashcards:** Interface estilo Tinder (Swipe Right/Left, Hard/Good/Easy) para o usuário revisar seus flashcards gerados dinamicamente na Fase 2 direto pelo navegador.
  - **Módulo 3 - Wiki Médica / Resumos:** Leitor estruturado dos resumos de `Temas/` em formato HTML bonitos.
- [ ] **Dashboard de Progressão:** 
  - Gráficos visuais importando os dados numéricos hoje presentes em `progresso.md` (distribuição de erros por área, taxa de sucesso).

---

## 🧠 Fase 4: O Workflow Fechado — Simulados e Analytics Ativo (Visão de Futuro)
*O sistema não apenas armazena, mas coordena ativamente as revisões do aluno.*

**Objetivos:**
- [ ] **Gerador de Simulados Personalizados:** 
  - O sistema "puxa" do Banco de Dados questões e temas que o aluno tem alta taxa de erro (ex: Trauma Pediátrico) e monta um arquivo de 50 questões "Cirúrgicas" personalizadas focadas nas fraquezas (Weakness-based testing).
- [ ] **Rotinas de Revisão Automática D-7 / D-30:**
  - O Agente notifica o aluno no frontend: *"Hoje você tem 15 flashcards de Clínica Médica que completaram 7 dias e 3 conceitos de Ginecologia para revisar"*.
- [ ] **Ataque Antecipado de Armadilhas:**
  - Relatório semanal automatizado: *"Nos últimos 7 dias, 40% dos seus erros foram por desatenção a limiares numéricos, especialmente na área de Pediatria."* (Insights que um humano só perceberia meses depois).

---

## 📝 Próximos Passos (Action Items para o Usuário e Agente)

1. **Definir o padrão de Flashcards:** (Agente + Usuário) Precisamos criar um prompt/script modelo para converter o formato atual das entradas do Caderno de Erros em algo como `[Frente] Qual o limiar de VDRL para reinfecção? | [Verso] Aumento de duas diluições.`
2. **Iniciar Banco de Dados Local SQLite:** O Markdown baterá no teto de performance logo logo com 500+ questões. Precisamos escrever um script Python que leia as pastas atuais e popule um `.db`.
3. **Hello World em Streamlit:** Criar o esqueleto básico do app local para o usuário já conseguir testar a visualização dos dados.
