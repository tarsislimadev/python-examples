# pip install autogen autogen_ext "autogen-ext[ollama]" --break-system-packages

from autogen_ext.models.ollama import OllamaChatCompletionClient
from autogen_core.models import UserMessage
import asyncio

ollama_client=OllamaChatCompletionClient(model='qwen2.5:0.5b')

message=UserMessage(content='What is the capital of France?', source='user')

async def run():
  result=await ollama_client.create([message])
  print(result.content)

asyncio.run(run())
