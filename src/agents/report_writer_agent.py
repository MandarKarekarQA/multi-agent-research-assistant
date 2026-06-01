from langchain_ollama import OllamaLLM

from src.utils.format_sources import format_sources


def write_report(
        summary: str,
        validation_feedback: str,
        search_results: list[dict]
) -> str:
    """
    Report Writer Agent

    Takes:
    1. Research summary
    2. Validation feedback
    3. Real search result URLs

    Produces:
    Professional final report
    """

    llm = OllamaLLM(model="mistral")

    sources = format_sources(search_results)

    prompt = f"""
You are a professional business report writer.

You will receive:

1. A research summary
2. Validation feedback
3. Real source URLs

Research Summary:
{summary}

Validation Feedback:
{validation_feedback}

Real Sources:
{sources}

Create a professional report using the following structure:

# UK Electric Vehicle Competitor Research Report

## 1. Executive Summary

Provide a short overview.

## 2. Market Overview

Describe the current UK EV market.

## 3. Key Competitors

Use a markdown table:

| Company | Market Position | Strengths | Risks |
|----------|----------|----------|----------|

## 4. Market Trends

List major market trends.

## 5. Risks and Challenges

List risks and challenges.

## 6. Recommendations

Provide recommendations.

## 7. Limitations

Mention any missing data or uncertainty.

## 8. Sources Used

Use the real URLs provided.

Important Rules:

- Keep the report professional.
- Use clear business language.
- Do not invent statistics.
- Mention when data is limited.
- Use the supplied source URLs.
- Never write "[Insert sources here]".
"""

    report = llm.invoke(prompt)

    return report


if __name__ == "__main__":

    sample_summary = """
The UK electric vehicle market is growing due to consumer interest,
government incentives, and charging infrastructure improvements.

Key competitors include Tesla, BYD, BMW, Volkswagen,
Hyundai, Kia, MG and Nissan.

Challenges include battery costs,
charging availability and consumer confidence.
"""

    sample_validation = """
Validation Result: NEEDS IMPROVEMENT

Issues Found:
- Missing specific statistics.
- Source references are limited.
- Risks could be explained in more detail.

Suggested Improvements:
- Add clearer competitor comparison.
- Mention data limitations.
- Add recommendations for businesses.
"""

    sample_sources = [
        {
            "title": "Example Source",
            "url": "https://example.com"
        }
    ]

    result = write_report(
        sample_summary,
        sample_validation,
        sample_sources
    )

    print("\nFINAL REPORT:\n")
    print(result)