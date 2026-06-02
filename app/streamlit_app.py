import sys
from pathlib import Path

import streamlit as st

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
    "Cost-controlled multi-agent AI research assistant using Streamlit, LangChain, Ollama and OpenAI."
)

with st.sidebar:
    st.header("Settings")

    model_choice = st.selectbox(
        "Model Mode",
        [
            "OpenAI Cloud - Recruiter Demo",
            "Local Ollama/Mistral - Developer Mode"
        ]
    )

    if model_choice == "OpenAI Cloud - Recruiter Demo":
        model_mode = "openai"
        st.success("Production demo mode enabled.")
        st.info("Uses OpenAI API with controlled budget limits.")
    else:
        model_mode = "ollama"
        st.warning(
            "Local Ollama mode only works on your own laptop with Ollama and Mistral installed."
        )

    st.markdown("### Agent Pipeline")
    st.write("1. Research Agent")
    st.write("2. Summarizer Agent")
    st.write("3. Validator Agent")
    st.write("4. Report Writer Agent")

    st.markdown("### Project Features")
    st.write("✅ Web search")
    st.write("✅ Local + Cloud model support")
    st.write("✅ Source tracking")
    st.write("✅ Report generation")
    st.write("✅ Cost-aware design")

topic = st.text_input(
    "Enter research topic",
    value="UK electric vehicle competitors 2026"
)

run_button = st.button("Run Multi-Agent Research", type="primary")

if run_button:
    if not topic.strip():
        st.warning("Please enter a research topic.")
    else:
        try:
            with st.status("Running multi-agent pipeline...", expanded=True) as status:
                st.write("🔎 Research Agent: searching and collecting data...")
                st.write("🧠 Summarizer Agent: preparing summary...")
                st.write("🕵️ Validator Agent: checking quality...")
                st.write("📝 Report Writer Agent: creating final report...")

                result = run_research_pipeline(
                    topic=topic,
                    model_mode=model_mode
                )

                status.update(
                    label="Research completed successfully!",
                    state="complete"
                )

            metrics = result["metrics"]
            search_results = result["search_results"]
            final_report = result["final_report"]

            st.subheader("Pipeline Metrics")

            col1, col2, col3, col4, col5 = st.columns(5)

            col1.metric("Model", metrics["model_name"])
            col2.metric("Mode", metrics["model_mode"])
            col3.metric("Agents", metrics["agent_count"])
            col4.metric("API Cost", str(metrics["api_cost"]))
            col5.metric("Time", f'{metrics["execution_time_seconds"]}s')

            st.subheader("Sources Found")

            for index, source in enumerate(search_results, start=1):
                with st.expander(f"Source {index}: {source.get('title', 'No title')}"):
                    st.write(source.get("summary", "No summary"))
                    st.write(source.get("url", "No URL"))

            st.subheader("Final Report")
            st.markdown(final_report)

            st.download_button(
                label="Download Report as Markdown",
                data=final_report,
                file_name="final_report.md",
                mime="text/markdown"
            )

        except Exception as error:
            st.error("Something went wrong while running the AI pipeline.")
            st.exception(error)