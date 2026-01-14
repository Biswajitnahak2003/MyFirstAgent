# MyFirstAgent: AutoStream Agent

This is a conversational AI agent designed for **AutoStream**, a fictional SaaS company. It automates the process of answering product queries using RAG (Retrieval-Augmented Generation) and identifying high-intent leads to capture their contact information.

Built using **LangGraph**, **LangChain**, and **Google Gemini 2.5 Flash**.

## Features
* **Intent Detection:** Distinguishes between casual greetings, product questions, and high-intent buying signals.
* **RAG Pipeline:** Retrieves accurate pricing and policy information from a local FAISS vector database using Google Embeddings.
* **Tool Execution:** Captures lead details (Name, Email, Platform) only when all required information is collected.
* **State Management:** Retains conversation context across multiple turns using LangGraph's persistent memory.

##  Project Structure
```text
├── agent.py           # Core LangGraph logic (Nodes, Edges, State)
├── rag.py             # Vector Database setup (FAISS & Embeddings)
├── tools.py           # Tool definitions (lookup_policy, mock_lead_capture)
├── main.py            # Entry point for the CLI Chatbot
├── requirements.txt   # Project dependencies
└── .env               # API Keys (Not included in repo)
```
## Setup & Installation
1. Clone the Repository

```Bash
git clone https://github.com/Biswajitnahak2003/MyFirstAgent.git
cd INTERNSHIP_ASSIGNMENT
```
2. Create a Virtual Environment (Optional but Recommended)

```Bash
python -m venv venv
venv\Scripts\activate
```
3. Install Dependencies

```Bash
pip install -r requirements.txt
```
4. Configure Environment Variables Create a .env file in the root directory and add your Google API Key:

```Bash
GOOGLE_API_KEY=your_actual_api_key
```
5. Initialize the Knowledge Base Run this command once to build the local FAISS vector store:

```Bash
python rag.py
```
6. Run the Agent Start the interactive chat loop:

```Bash
python main.py
```

# Architecture Explanation
## Why LangGraph?
I chose LangGraph  because this project requires a cyclic workflow (Agent → Tool → Agent) rather than a linear execution also as i am familiar with LangGraph.

Reasoning Loops: LangGraph allows the agent to "think" (call a tool), "act" (execute the tool), and "observe" (read the output) in a loop until the task is complete.

Control Flow: It provides precise control over conditional edges (e.g., deciding whether to call the RAG tool or the Lead Capture tool based on user intent).

## State Management
State is managed using LangGraph's MessagesState with the "add_messages" reducer.

Persistence: I used a MemorySaver checkpointer used to persist the state.

Session Tracking: Each conversation is tracked via a unique thread_id (e.g., user_session_1). This ensures the bot remembers the user's name from the beginning of the chat when asking for their email later.

## WhatsApp Deployment
To integrate this agent with WhatsApp, I would use a Webhook architecture connecting the WhatsApp Business API to a backend API hosting the LangGraph agent.