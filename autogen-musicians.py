import asyncio
import time

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.tools import AgentTool
from autogen_agentchat.ui import Console
from autogen_ext.models.ollama import OllamaChatCompletionClient

async def run(task):
    model_client = OllamaChatCompletionClient(model='qwen2.5:0.5b')

    voice_agent = AssistantAgent(
        'voice_expert',
        model_client=model_client,
        model_client_stream=True,
        system_message='You are the Singer of this music group.',
        description='A lyrics expert assistant.',
    )

    voice_agent_tool = AgentTool(
        voice_agent,
        return_value_as_last_message=True
    )

    guitar_agent = AssistantAgent(
        'guitar_expert',
        model_client=model_client,
        model_client_stream=True,
        system_message='You are the Guitarist of this music group.',
        description='A guitar expert assistant.',
    )
    
    guitar_agent_tool = AgentTool(
        guitar_agent,
        return_value_as_last_message=True
    )

    agent = AssistantAgent(
        'assistant',
        model_client=model_client,
        model_client_stream=True,
        system_message='You are a music general assistant. Use expert tools when needed.',
        tools=[voice_agent_tool, guitar_agent_tool],
        max_tool_iterations=10,
    )

    c = await Console(agent.run_stream(task=task))

    with open(f'./data/musicians-{time.time()}.md', 'a+') as file:
        for m in c.messages:
            text=f'[[{m.source}]]: {m.to_text()}\n'
            print(text)
            file.write(text)

task = input('Type your desires > ')

asyncio.run(run(task=task))
