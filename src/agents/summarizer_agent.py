import json
from pathlib import Path
from datetime import datetime

from langchain_ollama import OllamaLLM


def save_summary(summary: str) -> None:
    processed_folder = Path("data/processed")
    processed_folder.mkdir(parents=True, exist_ok=True)

    file_path = processed_folder / "summary.json"

    summary_data = {
        "timestamp": datetime.now().isoformat(),
        "summary": summary
    }

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(summary_data, file, indent=4)

    print(f"Summary saved: {file_path}")


def summarize_research(research_data: dict) -> str:
    """
    Summarizer Agent:
    Takes raw research data and creates a clean summary.
    """

    raw_research = research_data["raw_research"]

    llm = OllamaLLM(model="mistral")

    prompt = f"""
You are a professional AI research summarizer.

Your task:
Convert the research into a short structured business summary.

Research:
{raw_research}

Create:
1. Market overview
2. Main competitors
3. Key trends
4. Major risks

Keep the answer concise and professional.
"""

    summary = llm.invoke(prompt)

    save_summary(summary)

    return summary


if __name__ == "__main__":

    sample_research = {
        "raw_research": """
The UK EV market is growing rapidly.
Major competitors include Tesla, BYD, BMW and Volkswagen.
Challenges include charging infrastructure and battery costs.
"""
    }

    result = summarize_research(sample_research)

    print("\nSUMMARY:\n")
    print(result)