from langchain_ollama import OllamaLLM


def validate_research(summary: str) -> str:
    """
    Validator Agent:
    Checks whether the research summary is useful, balanced, and source-aware.
    """

    llm = OllamaLLM(model="mistral")

    prompt = f"""
You are a research quality validator.

Review the research summary below.

Research summary:
{summary}

Check the summary for:

1. Missing information
2. Weak or vague claims
3. Missing competitors or key players
4. Missing risks
5. Missing source references
6. Possible improvements

Return your answer in this format:

Validation Result:
PASS or NEEDS IMPROVEMENT

Issues Found:
- ...

Suggested Improvements:
- ...
"""

    validation_result = llm.invoke(prompt)

    return validation_result


if __name__ == "__main__":
    sample_summary = """
The UK electric vehicle market is growing quickly.
Main competitors include Tesla, BMW, BYD, Volkswagen, Hyundai, Kia and MG.
Challenges include charging infrastructure, battery costs and consumer confidence.
"""

    result = validate_research(sample_summary)

    print("\nVALIDATION OUTPUT:\n")
    print(result)