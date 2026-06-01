def format_sources(search_results: list[dict]) -> str:
    """
    Convert search results into a clean source list.
    """

    sources_text = ""

    for index, result in enumerate(search_results, start=1):
        title = result.get("title", "No title")
        url = result.get("url", "No URL")

        sources_text += f"{index}. {title}\n   URL: {url}\n\n"

    return sources_text