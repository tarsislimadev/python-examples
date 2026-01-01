import asyncio
import time

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.tools import AgentTool
from autogen_agentchat.ui import Console
from autogen_ext.models.ollama import OllamaChatCompletionClient

async def run(task):
    model_client = OllamaChatCompletionClient(model='qwen2.5:0.5b')

    frontend_agent = AssistantAgent(
        'frontend_expert',
        model_client=model_client,
        model_client_stream=True,
        system_message='You are Senior Front-end developer.',
        description='A React expert assistant.',
    )

    frontend_agent_tool = AgentTool(
        frontend_agent,
        return_value_as_last_message=True
    )

    backend_agent = AssistantAgent(
        'backend_expert',
        model_client=model_client,
        model_client_stream=True,
        system_message='You are Senior Back-end developer.',
        description='A Node.js expert assistant.',
    )
    
    backend_agent_tool = AgentTool(
        backend_agent,
        return_value_as_last_message=True
    )

    financial_agent = AssistantAgent(
        'financial_expert',
        model_client=model_client,
        model_client_stream=True,
        system_message='You are Binance.com expert.',
        description='A Binance.com expert assistant.',
    )
    
    financial_agent_tool = AgentTool(
        financial_agent,
        return_value_as_last_message=True
    )

    agent = AssistantAgent(
        'assistant',
        model_client=model_client,
        model_client_stream=True,
        system_message='You are Tech Lead assistant. Use expert tools when needed.',
        tools=[frontend_agent_tool, backend_agent_tool, financial_agent_tool],
        max_tool_iterations=100,
    )

    c = await Console(agent.run_stream(task=task))

    with open(f'./data/developers-{time.time()}.md', 'a+') as file:
        for m in c.messages:
            text=f'[[{m.source}]]: {m.to_text()}\n'
            print(text)
            file.write(text)

task = input('Type your desires > ')

asyncio.run(run(task=task))
