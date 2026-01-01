import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.tools import AgentTool
from autogen_agentchat.ui import Console
from autogen_ext.models.ollama import OllamaChatCompletionClient

async def run():
    model_client = OllamaChatCompletionClient(model='qwen2.5:0.5b')

    math_agent = AssistantAgent(
        'math_expert',
        model_client=model_client,
        model_client_stream=True,
        system_message='You are a math expert.',
        description='A math expert assistant.',
    )

    math_agent_tool = AgentTool(
        math_agent,
        return_value_as_last_message=True
    )

    chemistry_agent = AssistantAgent(
        'chemistry_expert',
        model_client=model_client,
        model_client_stream=True,
        system_message='You are a chemistry expert.',
        description='A chemistry expert assistant.',
    )
    
    chemistry_agent_tool = AgentTool(
        chemistry_agent,
        return_value_as_last_message=True
    )

    agent = AssistantAgent(
        'assistant',
        model_client=model_client,
        model_client_stream=True,
        system_message='You are a general assistant. Use expert tools when needed.',
        tools=[math_agent_tool, chemistry_agent_tool],
        max_tool_iterations=10,
    )

    await Console(agent.run_stream(task='How much is 2 plus 3?'))

asyncio.run(run())
