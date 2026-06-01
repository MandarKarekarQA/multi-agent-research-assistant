import json
from pathlib import Path
from datetime import datetime

from langchain_ollama import OllamaLLM

from src.tools.search_tool import search_web


def save_search_results(search_results: list[dict]) -> None:
    raw_folder = Path("data/raw")
    raw_folder.mkdir(parents=True, exist_ok=True)

    file_path = raw_folder / "search_results.json"

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(search_results, file, indent=4)

    print(f"Search results saved: {file_path}")


def create_research_context(search_results: list[dict]) -> str:
    context = ""

    for index, result in enumerate(search_results, start=1):
        context += f"""
Source {index}
Title: {result["title"]}
URL: {result["url"]}
Summary: {result["summary"]}
"""

    return context


def research_topic(topic: str) -> dict:
    print("Searching the web...")

    search_results = search_web(topic, max_results=5)

    save_search_results(search_results)

    print("Creating research context...")

    research_context = create_research_context(search_results)

    print("Sending research context to local AI model...")

    llm = OllamaLLM(model="mistral")

    prompt = f"""
You are a research assistant.

User topic:
{topic}

Use the search results below to create a clear research summary.

Search results:
{research_context}

Write:
1. Short overview
2. Key competitors or key players
3. Important trends
4. Risks or challenges
5. Sources used

Important:
- Use only the information from the search results.
- Mention source names when possible.
- Do not invent exact statistics if they are not provided.

Keep the answer simple and structured.
"""

    response = llm.invoke(prompt)

    return {
        "topic": topic,
        "timestamp": datetime.now().isoformat(),
        "raw_research": response,
        "search_results": search_results
    }


if __name__ == "__main__":
    topic = "UK electric vehicle competitors 2026"

    research_output = research_topic(topic)

    print("\nFinal Research Summary:\n")
    print(research_output["raw_research"])