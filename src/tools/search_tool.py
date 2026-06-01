from ddgs import DDGS


def search_web(query: str, max_results: int = 5) -> list[dict]:
    """
    Free web search tool for development.
    """

    results = []

    with DDGS() as ddgs:
        search_results = ddgs.text(
            query,
            max_results=max_results
        )

        for result in search_results:
            results.append({
                "title": result.get("title", ""),
                "url": result.get("href", ""),
                "summary": result.get("body", "")
            })

    return results


if __name__ == "__main__":
    query = "UK electric vehicle competitors 2026"

    results = search_web(query)

    for index, result in enumerate(results, start=1):
        print(f"\nResult {index}")
        print(f"Title: {result['title']}")
        print(f"URL: {result['url']}")
        print(f"Summary: {result['summary']}")