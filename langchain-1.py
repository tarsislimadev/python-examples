# python -m pip install langchain langchain-openai langchain-community langchain-core  python-dotenv
# python -m pip install langchain==1.0.5 langchain-community==0.4.1

from langchain_core.output_parsers import XMLOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# Define the parser
parser = XMLOutputParser()

# Prompt with MusicXML schema guidance
prompt = PromptTemplate(
  template="""
You are a music notation assistant.
Generate a short MusicXML snippet for a melody in C major, 4/4 time, with quarter notes C-D-E-F.

Output must be valid MusicXML inside <score-partwise> tags.
{format_instructions}
""",
  input_variables=[],
  partial_variables={"format_instructions": parser.get_format_instructions()},
)

# Initialize LLM
llm = ChatOpenAI(
  model='meta-llama/Llama-3.1-8B-Instruct',
  temperature=0,
  base_url="https://router.huggingface.co/v1",
  api_key=os.getenv("HF_TOKEN")
)

# Chain
chain = prompt | llm | parser

# Run
result = chain.invoke({})
print(result)
