"""Optional real provider call. Importing this file never loads credentials."""

from pathlib import Path


def classify_live(question, schema, model_name="openai/gpt-oss-20b"):
    from dotenv import load_dotenv
    from langchain_groq import ChatGroq

    load_dotenv(Path(__file__).resolve().parents[2] / ".env", override=False)
    model = ChatGroq(model=model_name, temperature=0)
    structured = model.with_structured_output(schema, method="json_mode")
    prompt = (Path(__file__).resolve().parents[1] / "prompts" / "classify.txt").read_text()
    return structured.invoke([("system", prompt), ("human", question)])
