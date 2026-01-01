import asyncio
import time

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.tools import AgentTool
from autogen_agentchat.ui import Console
from autogen_ext.models.ollama import OllamaChatCompletionClient

backend_system_message = """"
# Programador de sistemas de informação

## Descrição Sumária

Desenvolvem sistemas e aplicações, determinando interface gráfica, critérios ergonômicosde navegação, montagem da estrutura de banco de dados e codificação de programas;projetam, implantam e realizam manutenção de sistemas e aplicações; selecionam recur sos de trabalho, tais como metodologias de desenvolvimento de sistemas, linguagem deprogramação e ferramentas de desenvolvimento. planejam etapas e ações de trabalho.

## Formação e Experiência

Para o exercício dessas ocupações requer-se ensino técnico de nível médio de informáticaou superior incompleto em áreas como ciências exatas, informática, engenharia. a atuali zação profissional permanente é condição para o seu exercício. o desempenho pleno dasatividades do programador de máquinas-ferramentas com comando numérico requer detrês a quatro anos de experiência. as demais ocupações, de um a dois anos.

## Condições Gerais de Exercício

Trabalham em atividades de informática e conexas, presentes em todas as atividades eco nômicas. o programador de máquinas-ferramentas com controle númérico se faz presen te na indústria. o programador de sistema de informação e o prgramador de maquinas ferramentas com controle numérico são, predominantemente, empregados com carteiraassinada, ao passo que o programador de multimídia trabalha também como autônomo.as atividades são realizadas no horário diurno, exceto o programador de sistemas deinformação, que realiza suas atividades no horário noturno, e o programador de internet,que trabalha em horários irregulares. todas as atividades se desenvolvem em ambientefechado. trabalham individualmente e com supervisão ocasional, exceto o programadorde internet, o programador de multimídia e o programador de sistemas de informação,que podem, eventualmente, trabalhar em equipe. em algumas ocupações, é possível otrabalho a distância. no exercício das atividades, podem permanecer em posições.
"""

async def run(task):
    model_client = OllamaChatCompletionClient(model='qwen2.5:0.5b')

    frontend_agent = AssistantAgent(
        'frontend_expert',
        model_client=model_client,
        model_client_stream=True,
        system_message='Você é um Desenvolvedor Front-end Senior.',
        description='Um assistente especialista em React.',
    )

    frontend_agent_tool = AgentTool(
        frontend_agent,
        return_value_as_last_message=True
    )

    backend_agent = AssistantAgent(
        'backend_expert',
        model_client=model_client,
        model_client_stream=True,
        system_message=backend_system_message,
        description='Um assistente especialista em Node.js.',
    )
    
    backend_agent_tool = AgentTool(
        backend_agent,
        return_value_as_last_message=True
    )

    agent = AssistantAgent(
        'assistant',
        model_client=model_client,
        model_client_stream=True,
        system_message='Você é o assistent Tech Lead. Use as ferramentas expert quando precisar.',
        tools=[frontend_agent_tool, backend_agent_tool],
        max_tool_iterations=100,
    )

    c = await Console(agent.run_stream(task=task))

    with open(f'./data/developers2-{time.time()}.md', 'a+') as file:
        for m in c.messages:
            text=f'[[{m.source}]]: {m.to_text()}\n'
            print(text)
            file.write(text)

task = input('Diz aí > ')

asyncio.run(run(task=task))
