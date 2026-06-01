import sys
from pathlib import Path

import streamlit as st

# Allow Streamlit to import from src/
project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

from src.main_pipeline import run_research_pipeline


st.set_page_config(
    page_title="Multi-Agent Research Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Multi-Agent Research Assistant")
st.caption(
    "Cost-controlled local AI research assistant using Ollama, Mistral, LangChain and Streamlit"
)

with st.sidebar:
    st.header("Settings")

    model_mode = st.selectbox(
        "Model Mode",
        [
            "Local - Ollama/Mistral",
            "Hybrid - Coming Soon",
            "Premium - Coming Soon"
        ]
    )

    st.info("Current mode uses local Ollama/Mistral, so API cost is £0.")

    st.markdown("### Agent Pipeline")
    st.write("1. Research Agent")
    st.write("2. Summarizer Agent")
    st.write("3. Validator Agent")
    st.write("4. Report Writer Agent")

    st.markdown("### Project Features")
    st.write("✅ Web search")
    st.write("✅ Local LLM")
    st.write("✅ Source tracking")
    st.write("✅ Report generation")
    st.write("✅ Cost tracking")

topic = st.text_input(
    "Enter research topic",
    value="UK electric vehicle competitors 2026"
)

run_button = st.button(
    "Run Multi-Agent Research",
    type="primary"
)

if run_button:
    if not topic.strip():
        st.warning("Please enter a research topic.")
    else:
        with st.status("Running multi-agent pipeline...", expanded=True) as status:
            st.write("🔎 Research Agent: searching and collecting data...")
            st.write("🧠 Summarizer Agent: preparing summary...")
            st.write("🕵️ Validator Agent: checking quality...")
            st.write("📝 Report Writer Agent: creating final report...")

            result = run_research_pipeline(topic)

            status.update(
                label="Research completed successfully!",
                state="complete"
            )

        final_report = result["final_report"]
        metrics = result["metrics"]
        search_results = result["search_results"]

        st.subheader("Pipeline Metrics")

        col1, col2, col3, col4, col5 = st.columns(5)

        col1.metric("Model", metrics["model_name"])
        col2.metric("Mode", metrics["model_mode"])
        col3.metric("Agents", metrics["agent_count"])
        col4.metric("API Cost", f"£{metrics['api_cost_gbp']}")
        col5.metric("Time", f"{metrics['execution_time_seconds']}s")

        st.subheader("Sources Found")

        for index, source in enumerate(search_results, start=1):
            with st.expander(f"Source {index}: {source['title']}"):
                st.write(source["summary"])
                st.link_button("Open Source", source["url"])

        st.subheader("Final Report")
        st.markdown(final_report)

        st.download_button(
            label="Download Report as Markdown",
            data=final_report,
            file_name="final_report.md",
            mime="text/markdown"
        )