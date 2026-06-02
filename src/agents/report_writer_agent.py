from src.utils.model_provider import get_llm


def write_report(
    summary: str,
    validation_feedback: str,
    sources_text: str = "",
    model_mode: str = "openai"
) -> str:
    llm = get_llm(model_mode)

    prompt = f"""
You are a professional business report writer.

Create a concise professional markdown report.

Research Summary:
{summary}

Validation Feedback:
{validation_feedback}

Sources:
{sources_text}

Report structure:

# UK Electric Vehicle Competitor Research Report

## 1. Executive Summary
## 2. Market Overview
## 3. Key Competitors
Use a markdown table:
Company | Market Position | Strengths | Risks

## 4. Market Trends
## 5. Risks and Challenges
## 6. Recommendations
## 7. Limitations
## 8. Sources Used

Rules:
- Keep it concise.
- Do not invent exact statistics.
- Use only information provided.
- Mention limitations clearly.
"""

    response = llm.invoke(prompt)

    if hasattr(response, "content"):
        response = response.content

    return response


if __name__ == "__main__":
    sample_summary = """
    UK EV market is growing. Key competitors include Tesla, Nissan, BMW, BYD,
    Volkswagen, Kia, Hyundai and MG.
    """

    sample_validation = """
    Validation Result: NEEDS IMPROVEMENT
    Add sources, limitations and clearer competitor comparison.
    """

    sample_sources = """
    1. Example EV source - https://example.com
    """

    result = write_report(
        sample_summary,
        sample_validation,
        sample_sources,
        model_mode="ollama"
    )

    print("\nFINAL REPORT:\n")
    print(result)