# Customer Feedback Analysis Agent

This is boilerplate code for a customer feedback analysis agent.

## Setup

Install the Python dependencies.

```bash
pip install -r requirements.txt
```

## Run the agent

```bash
python -m feedback_agent.agent.feedback_analysis_agent
```

## Requirements

- Python 3.10+
- autogen
- ollama
- fix-busted-json

## Minimal Autogen Example

In the `agent/calculator_agent.py` file, there is a minimal example of how to use Autogen to create an agent that can use tools.

> [!NOTE]
> Open source LLM's need to support tool calling for this to work.
> LLama 3.1 and LLama 3.1 Instruct support tool calling.
