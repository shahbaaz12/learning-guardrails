"""Optional real Groq output; root .env is read only on explicit invocation."""

from pathlib import Path


def generate_live(question, model_name="openai/gpt-oss-20b"):
    from dotenv import load_dotenv
    from langchain_groq import ChatGroq

    load_dotenv(Path(__file__).resolve().parents[2] / ".env", override=False)
    prompt = (Path(__file__).resolve().parents[1] / "prompts" / "answer.txt").read_text()
    model = ChatGroq(model=model_name, temperature=0).bind(response_format={"type": "json_object"})
    return model.invoke([("system", prompt), ("human", question)]).content
