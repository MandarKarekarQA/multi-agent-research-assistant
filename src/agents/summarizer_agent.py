import json
from pathlib import Path

from src.utils.model_provider import get_llm


def save_json(data, file_path: str) -> None:
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def summarize_research(raw_research: str, model_mode: str = "openai") -> str:
    llm = get_llm(model_mode)

    prompt = f"""
You are a summarizer agent.

Summarize the research below into a short, clear business summary.

Research:
{raw_research}

Return:
1. Market overview
2. Main competitors
3. Key trends
4. Major risks

Keep it concise.
Do not invent exact numbers.
"""

    response = llm.invoke(prompt)

    if hasattr(response, "content"):
        response = response.content

    save_json(
        {"summary": response},
        "data/processed/summary.json"
    )

    print("Summary saved: data/processed/summary.json")

    return response


if __name__ == "__main__":
    sample_research = """
    The UK electric vehicle market is growing. Major competitors include Tesla,
    Nissan, BMW, BYD, Volkswagen, Kia, Hyundai and MG. Key challenges include
    charging infrastructure, battery costs and consumer confidence.
    """

    result = summarize_research(
        sample_research,
        model_mode="ollama"
    )

    print("\nSUMMARY:\n")
    print(result)