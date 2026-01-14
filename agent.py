from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import ALL_TOOLS

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0)
llm_with_tools = llm.bind_tools(ALL_TOOLS)

class State(TypedDict):
    messages: Annotated[list, add_messages]

def chatbot(state: State):
    sys_msg = SystemMessage(content="""
    You are a helpful sales assistant for AutoStream.
    
    GOALS:
    1. If user asks about product/pricing, use 'lookup_policy'.
    2. If user shows high intent (wants to buy/try), ask for Name, Email, and Platform.
    3. Once you have ALL 3 details, use 'mock_lead_capture'.
    """)
    return {"messages": [llm_with_tools.invoke([sys_msg] + state["messages"])]}

builder = StateGraph(State)

builder.add_node("chatbot", chatbot)
builder.add_node("tools", ToolNode(ALL_TOOLS))

builder.add_edge(START, "chatbot")
builder.add_conditional_edges("chatbot", tools_condition)
builder.add_edge("tools", "chatbot")

memory = MemorySaver()
graph = builder.compile(checkpointer=memory)