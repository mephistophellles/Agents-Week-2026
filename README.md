# Agents Week 2026

Материалы курса **Agents Week 2026** — интенсив по AI-агентам на базе LLM.

## Структура репозитория

```
Agents-Week-2026/
├── Лекции/
│   ├── Lecture 1.1/   — Intro to AI Agents & LLM
│   ├── Lecture 1.2/   — Tools & MCP
│   ├── Lecture 2/     — Memory and Guardrails
│   ├── Lecture 3/     — AI Agent Workflow, Multi-Agent Systems
│   ├── Lecture 4/     — Agent Evaluation: From Metrics to Managed Quality
│   └── Lecture 5/     — (продвинутые темы)
├── Отборочный контест/
│   ├── Task 1/
│   ├── Task 2/
│   ├── Task 3/
│   └── Task 4/
└── README.md
```

## Лекции

| # | Тема | Спикер | Материалы |
|---|------|--------|-----------|
| 1.1 | [Intro to AI Agents & LLM](Лекции/Lecture%201.1/) | Zaytseva Alena, AI Lead @ Yandex Lavka | Конспект, 2 Jupyter-ноутбука |
| 1.2 | [Tools & MCP](Лекции/Lecture%201.2/) | Zaytseva Alena, AI Lead @ Yandex Lavka | Конспект, Jupyter-ноутбук |
| 2 | [Memory and Guardrails](Лекции/Lecture%202/) | Kirill Mishchenko, Yandex Browser ML Team Lead | Конспект, Jupyter-ноутбук |
| 3 | [AI Agent Workflow & Multi-Agent Systems](Лекции/Lecture%203/) | — | Конспект, практический ноутбук |
| 4 | [Agent Evaluation](Лекции/Lecture%204/) | — | Конспект, практический ноутбук |
| 5 | [Продвинутые темы](Лекции/Lecture%205/) | — | Видео лекций |

## Краткое содержание курса

### Лекция 1.1 — Intro to AI Agents & LLM
Введение в AI-агентов: применение, эволюция взаимодействия с LLM (от prompting до multi-agent systems), определение агента (`Agent = runtime(AI model + prompts + tools + memory + guardrails + planning skills)`), основы LLM — токенизация, авторегрессия, стратегии выбора токенов, этапы обучения (Pre-training → SFT → RLHF).

### Лекция 1.2 — Tools & MCP
Инструменты для LLM: зачем нужны, как работает вызов, принципы проектирования (идемпотентность, обработка сбоев, структурированный вывод). Model Context Protocol (MCP) — открытый стандарт Anthropic для соединения AI-моделей с внешними системами. Архитектура Host/Server/Client.

### Лекция 2 — Memory and Guardrails
**Memory:** типы памяти (Short-Term, Long-Term, Context, Entity), RAG (пайплайн, трансформации запросов: Query Rewriting, Decomposition, HyDE), двухфазный поиск, обучение vs RAG.
**Guardrails:** модель угроз (Prompt Injection, Jailbreaking, Hallucinations), контентные фильтры, ограничители действий, спектр инструментов (Regex → ML → BERT → LLM), мониторинг.

### Лекция 3 — Multi-Agent Systems
Практический семинар: построение MAS для клиентского сервиса авиакомпании. Single Agent (ReAct/TAO loop) → Hierarchical MAS (Coordinator + специализированные агенты) → MAS + Critic (Reflexion pattern). Benchmark: Single Agent 6.0/10, MAS 9.3/10, MAS+Critic 10.0/10.

### Лекция 4 — Agent Evaluation
Полный цикл eval-системы: корзина задач, три грейдера (state_grader, policy_grader, LLM-as-Judge), Iron User (симулированный пользователь для multi-turn оценки), человеческая разметка, итеративное улучшение LLM-судьи (v1→v5). Prompt engineering > model scaling.

## Отборочный контест

Задания отборочного контеста для участия в курсе:
- **Task 1** — Python-задача
- **Task 2** — Работа с данными (CSV)
- **Task 3** — Python-задача
- **Task 4** — Python-задача

## Технологии

- **LLM:** OpenAI GPT-4o-mini, GPT-4.1-nano
- **Фреймворки:** LangChain, LangGraph, OpenAI Agents SDK
- **Протоколы:** Model Context Protocol (MCP)
- **Инструменты:** Pydantic, Python

## Ссылки

- [OpenAI Agents SDK](https://www.youtube.com/watch?v=joHR2pmxDQE)
- [Lilian Weng — LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/)
- [Andrej Karpathy — Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro)
- [Anthropic MCP Announcement](https://www.anthropic.com/news/model-context-protocol)
- [LangChain Tools](https://docs.langchain.com/oss/python/integrations/tools)
- [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers)
- [τ-bench](https://github.com/sierra-research/tau-bench)
- [GPT Week (ШАД)](https://shad.yandex.ru/gptweek)
