import os

from dotenv import load_dotenv
from langchain_ollama import OllamaLLM
from langchain_openai import ChatOpenAI


load_dotenv()


def get_llm(model_mode: str = "openai"):
    if model_mode == "openai":
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError("OPENAI_API_KEY is missing from environment variables.")

        return ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.2,
            max_tokens=700,
            api_key=api_key,
        )

    if model_mode == "ollama":
        return OllamaLLM(model="mistral")

    raise ValueError(f"Unsupported model mode: {model_mode}")