import json
from datetime import datetime
from pathlib import Path

from src.tools.search_tool import search_web
from src.utils.model_provider import get_llm


def save_json(data, file_path: str) -> None:
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def create_research_context(search_results: list[dict]) -> str:
    context = ""

    for index, result in enumerate(search_results, start=1):
        context += f"""
Source {index}
Title: {result.get("title", "")}
URL: {result.get("url", "")}
Summary: {result.get("summary", "")}
"""

    return context


def research_topic(topic: str, model_mode: str = "openai") -> dict:
    print("Searching the web...")

    search_results = search_web(topic, max_results=5)

    save_json(search_results, "data/raw/search_results.json")

    print("Creating research context...")

    research_context = create_research_context(search_results)

    print(f"Sending research context to AI model: {model_mode}")

    llm = get_llm(model_mode)

    prompt = f"""
You are a research assistant.

Research topic:
{topic}

Use ONLY the search results below.

Search results:
{research_context}

Create a simple structured research summary with:
1. Short overview
2. Key competitors or key players
3. Important trends
4. Risks or challenges
5. Sources used

Keep it concise.
Do not invent exact statistics.
"""

    response = llm.invoke(prompt)

    if hasattr(response, "content"):
        response = response.content

    return {
        "topic": topic,
        "timestamp": datetime.now().isoformat(),
        "raw_research": response,
        "search_results": search_results,
    }


if __name__ == "__main__":
    output = research_topic(
        topic="UK electric vehicle competitors 2026",
        model_mode="ollama"
    )

    print("\nFinal Research Summary:\n")
    print(output["raw_research"])