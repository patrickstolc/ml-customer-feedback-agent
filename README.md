# Evaluating AI Agents

This repository contains a "minimal" AI agent that can fetch customer feedback data and perform some basic analysis on it.

The purpose of this repository is to provide a starting point for evaluating AI agents.

> [!NOTE]
> The agent instructions are based on [ReAct prompting strategy](https://microsoft.github.io/autogen/0.2/docs/topics/prompting-and-reasoning/react).

> [!NOTE]
> The LLM used in this example is [Llama 3.1 8B](https://ollama.com/library/llama3.1:8b). Other models might not perform as well.

---

## Setup

Install the Python dependencies.

```bash
pip install -r requirements.txt
```

---

## Dependencies

- Python 3.10+
- autogen
- ollama
- fix-busted-json

---

## Run the agent

```bash
python -m feedback_agent.agent.feedback_analysis_agent
```

---

## Run the tests

### Final response

```bash
python -m tests.test_final_response
```

### Single step

```bash
python -m tests.test_single_step
```
