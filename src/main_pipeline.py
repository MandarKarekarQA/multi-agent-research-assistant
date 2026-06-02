import time
from pathlib import Path

from src.agents.research_agent import research_topic
from src.agents.summarizer_agent import summarize_research
from src.agents.validator_agent import validate_research
from src.agents.report_writer_agent import write_report
from src.utils.cost_tracker import CostTracker
from src.utils.format_sources import format_sources


def save_report(report: str, file_name: str = "final_report.md") -> None:
    reports_folder = Path("reports")
    reports_folder.mkdir(exist_ok=True)

    file_path = reports_folder / file_name

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(report)

    print(f"\nReport saved successfully: {file_path}")


def run_research_pipeline(
    topic: str,
    model_mode: str = "openai"
) -> dict:
    start_time = time.time()

    cost_tracker = CostTracker(
        model_name="gpt-4o-mini" if model_mode == "openai" else "mistral",
        model_mode="OpenAI Cloud" if model_mode == "openai" else "Local Ollama"
    )

    print("STEP 1: Running Research Agent...")
    research_output = research_topic(topic, model_mode=model_mode)

    raw_research = research_output["raw_research"]
    search_results = research_output["search_results"]

    sources_text = format_sources(search_results)

    print("\nSTEP 2: Running Summarizer Agent...")
    summary = summarize_research(raw_research, model_mode=model_mode)

    print("\nSTEP 3: Running Validator Agent...")
    validation_feedback = validate_research(summary, model_mode=model_mode)

    print("\nSTEP 4: Running Report Writer Agent...")
    final_report = write_report(
        summary=summary,
        validation_feedback=validation_feedback,
        sources_text=sources_text,
        model_mode=model_mode
    )

    save_report(final_report)

    execution_time = round(time.time() - start_time, 2)

    metrics = cost_tracker.get_metrics(
        agent_count=4,
        execution_time_seconds=execution_time
    )

    return {
        "topic": topic,
        "raw_research": raw_research,
        "summary": summary,
        "validation_feedback": validation_feedback,
        "final_report": final_report,
        "search_results": search_results,
        "metrics": metrics
    }


if __name__ == "__main__":
    topic = "UK electric vehicle competitors 2026"

    result = run_research_pipeline(
        topic=topic,
        model_mode="ollama"
    )

    print("\nFINAL MULTI-AGENT REPORT:\n")
    print(result["final_report"])

    print("\nMETRICS:\n")
    print(result["metrics"])