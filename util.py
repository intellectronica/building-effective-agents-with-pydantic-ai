import os
import random
from pprint import pformat

from dotenv import load_dotenv
import nest_asyncio


def initialize():
    load_dotenv(override=True)

    _ai_models = (
        [] + 
        (['openai:gpt-4o', 'openai:gpt-4o-mini'] if os.environ.get('OPENAI_API_KEY') else []) +
        (['gemini-1.5-pro', 'gemini-2.0-flash-exp'] if os.environ.get('GEMINI_API_KEY') else []) +
        (['claude-3-5-haiku-latest', 'claude-3-5-sonnet-latest'] if os.environ.get('ANTHROPIC_API_KEY') else [])
    )
    print(f"Available AI models:\n{pformat(_ai_models)}")

    _ai_model = (
        os.environ['AI_MODEL']
        if os.environ.get('AI_MODEL')
        else random.choice(_ai_models)
    )
    print(f"Using AI model: {_ai_model}")

    nest_asyncio.apply()

    return _ai_model