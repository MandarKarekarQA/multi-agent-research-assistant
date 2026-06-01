from pathlib import Path

from src.agents.research_agent import research_topic
from src.agents.summarizer_agent import summarize_research
from src.agents.validator_agent import validate_research
from src.agents.report_writer_agent import write_report
from src.utils.cost_tracker import CostTracker


def save_report(report: str, file_name: str = "final_report.md") -> None:
    """
    Save the final report into the reports folder.
    """

    reports_folder = Path("reports")
    reports_folder.mkdir(exist_ok=True)

    file_path = reports_folder / file_name

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(report)

    print(f"\nReport saved successfully: {file_path}")


def run_research_pipeline(topic: str) -> dict:
    """
    Main multi-agent pipeline.

    Flow:
    1. Research Agent
    2. Summarizer Agent
    3. Validator Agent
    4. Report Writer Agent

    Returns:
    Final report + pipeline metrics
    """

    tracker = CostTracker()
    tracker.start()

    print("STEP 1: Running Research Agent...")
    research_output = research_topic(topic)

    raw_research = research_output["raw_research"]
    search_results = research_output["search_results"]

    print("\nSTEP 2: Running Summarizer Agent...")
    summary = summarize_research(research_output)

    print("\nSTEP 3: Running Validator Agent...")
    validation_feedback = validate_research(summary)

    print("\nSTEP 4: Running Report Writer Agent...")
    final_report = write_report(
        summary,
        validation_feedback,
        search_results
    )

    save_report(final_report)

    tracker.stop()
    metrics = tracker.get_metrics()

    print("\nPIPELINE METRICS:")
    print(metrics)

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

    result = run_research_pipeline(topic)

    print("\nFINAL MULTI-AGENT REPORT:\n")
    print(result["final_report"])

    print("\nMETRICS:\n")
    print(result["metrics"])