from dotenv import load_dotenv
import os

from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langchain_core.runnables import RunnableLambda
from todoist_api_python.api import TodoistAPI


load_dotenv()

todoist_api_key = os.getenv("TODOIST_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")

todoist = TodoistAPI(todoist_api_key)

@tool
def add_task(task: str, desc: str = None) -> str:
    """
    Add a new task to the user's task list. 
    Use this when the user wants to add or create a task
    """
    print(f"Adding task: {task}")
    todoist.add_task(content=task, description=desc)
    return f"Task '{task}' added. {desc}"

@tool
def show_tasks() -> str:
    """
    Show all tasks from Todoist. Use this tool when the user wants to see their tasks. 
    """
    result_paginator = todoist.get_tasks()
    tasks = []
    for task_list in result_paginator:
        for task in task_list:
            tasks.append(task.content)
    return tasks

def run_tools(message):
    if message.tool_calls:
        tool_call = message.tool_calls[0]
        if tool_call["name"] == "add_task":
            return add_task.invoke(tool_call["args"])
        elif tool_call["name"] == "show_tasks":
            return show_tasks.invoke(tool_call["args"])
    return message.content



tools = [add_task, show_tasks]

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    google_api_key=gemini_api_key,
    temperature=0.3
)

system_prompt = """You are a helpful assistant. 
You will help the user add tasks.
You will help the user show existing tasks.
Show them in a bullet list format."""


prompt = ChatPromptTemplate([
    ("system", system_prompt),
    ("human", "{input}"),
    ("placeholder", "{history}")
    
])

chain = (
    prompt
    | llm.bind_tools(tools)
    | RunnableLambda(run_tools)
)

history = []
while True:
    user_input = input("You: ")
    response = chain.invoke({"input": user_input, "history": history})
    print(response)
    history.append(HumanMessage(content=user_input))
    history.append(AIMessage(content=response))