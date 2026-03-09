from openai import OpenAI
import os

model="openai/gpt-oss-20b"

input="Explain the importance of fast language models"

client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

response = client.responses.create(model=model, input=input)

print(response.output_text)
