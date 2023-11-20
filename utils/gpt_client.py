import openai

from config import (
    OPENAI_AI_API_KEY,
    OPEN_AI_GPT_4,
    OPEN_AI_GPT_35_TURBO,
    OPEN_AI_GPT_4_TURBO
)


openai.api_key = OPENAI_AI_API_KEY

def GetResponseFromLLM(model : str, prompt : str):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt},
        ],
        max_tokens=700,
        temperature=0.5,
    )

    return response["choices"][0]["message"]["content"]




