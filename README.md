# Building Effective Agents with Pydantic AI

Code examples for the agentic AI patterns discussed in the excellent article
[Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)
by [Erik Schluntz](https://github.com/eschluntz) and [Barry Zhang](https://github.com/ItsBarryZ)
of Anthropic, inspired, ported and adapted from the
[code samples](https://github.com/anthropics/anthropic-cookbook/tree/main/patterns/agents)
by the authors.

The examples rely on [Pydantic AI](https://ai.pydantic.dev/), an agentic AI
orchestration library that is particularly well-suited for implementing these patterns
with clarity and precision.

These examples complement the original code accompanying the article and hopefully
serve a dual purpose, demonstrating both the foundational agentic AI patterns discussed
in the article and the use of Pydantic AI.

## Notebooks

- [Basic Workflows (chain, parallelize, route)](basic_workflows.ipynb)
  [📖](https://nbsanity.com/intellectronica/building-effective-agents-with-pydantic-ai/blob/main/basic_workflows.ipynb)
- [Orchestrator and Workers](orchestrator_workers.ipynb)
  [📖](https://nbsanity.com/intellectronica/building-effective-agents-with-pydantic-ai/blob/main/orchestrator_workers.ipynb)
- [Evaluator and Optimizer](evaluator_optimizer.ipynb)
  [📖](https://nbsanity.com/intellectronica/building-effective-agents-with-pydantic-ai/blob/main/evaluator_optimizer.ipynb)

## Setup

1. Copy `dot.env` to `.env`
2. Fill in the API keys for one or more of your LLM provider(s)
3. Set `AI_MODEL` to the model you want to use
   (see https://ai.pydantic.dev/models/ for supported providers and models)

   For example:
   ```
   OPENAI_API_KEY=sk-123456789
   AI_MODEL=openai:gpt-4o
   ```
   or
   ```
   GEMINI_API_KEY=ABC-123_xyz
   AI_MODEL=gemini-1.5-pro
   ```
   or
   ```
   ANTHROPIC_API_KEY=ABC-sk-123456789
   AI_MODEL=claude-3-5-sonnet-latest
   ```
   You can also omit the `AI_MODEL` variable, which will result in a random model from all the models you have
   API keys for being chosen (you can use that to play with different models and compare).

4. You can optionally set the `LOGFIRE_TOKEN` variable to instrument Pydantic AI and follow the agent calls
   with [Pydantic Logfire](https://logfire.pydantic.dev/).