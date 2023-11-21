import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# OpenAI
OPENAI_AI_API_KEY = os.getenv("OPENAI_AI_API_KEY", "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")
OPEN_AI_EMBEDDING_MODEL_ADA_002 = os.getenv("OPEN_AI_EMBEDDING_MODEL_ADA", "text-embedding-ada-002")
OPEN_AI_GPT_4 = os.getenv("OPEN_AI_GPT_4", "gpt-4-0613")
OPEN_AI_GPT_35_TURBO = os.getenv("OPEN_AI_GPT_35_TURBO", "gpt-3.5-turbo-1106")
OPEN_AI_GPT_4_TURBO = os.getenv("OPEN_AI_GPT_4_TURBO", "gpt-4-1106-preview ")
