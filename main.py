import os
import getpass
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from agent import graph

load_dotenv()

def run_chat():
    print("--- AutoStream AI Agent (with FAISS RAG) ---")
    print("Type 'q' to quit.\n")
    
    config = {"configurable": {"thread_id": "user_session_1"}}
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["q", "quit"]:
            break
            
        events = graph.stream(
            {"messages": [HumanMessage(content=user_input)]}, 
            config, 
            stream_mode="values"
        )
        
        for event in events:
            if "messages" in event:
                last_msg = event["messages"][-1]
                
                if last_msg.type == "ai" and last_msg.content:
                    print(f"Agent: {last_msg.content}")
                
                elif last_msg.type == "ai" and last_msg.tool_calls:
                    print(f"Agent: (Thinking... Calling tool: {last_msg.tool_calls[0]['name']})")

if __name__ == "__main__":
    run_chat()