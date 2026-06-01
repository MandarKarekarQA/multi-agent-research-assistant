from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="mistral")

response = llm.invoke(
    "Explain the UK EV market in simple words"
)

print(response)