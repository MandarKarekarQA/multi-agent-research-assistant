from src.utils.model_provider import get_llm


def validate_research(summary: str, model_mode: str = "openai") -> str:
    llm = get_llm(model_mode)

    prompt = f"""
You are a validator agent.

Review the research summary below.

Summary:
{summary}

Check:
1. Is it clear?
2. Is it too vague?
3. Are sources or limitations missing?
4. What should be improved?

Return:
- Validation result: PASS or NEEDS IMPROVEMENT
- Issues found
- Suggested improvements

Keep it concise.
"""

    response = llm.invoke(prompt)

    if hasattr(response, "content"):
        response = response.content

    return response


if __name__ == "__main__":
    sample_summary = """
    The UK electric vehicle market is growing. Main competitors include Tesla,
    Nissan, BMW, BYD, Volkswagen, Kia, Hyundai and MG. Challenges include
    charging infrastructure, battery costs and consumer confidence.
    """

    result = validate_research(
        sample_summary,
        model_mode="ollama"
    )

    print("\nVALIDATION OUTPUT:\n")
    print(result)