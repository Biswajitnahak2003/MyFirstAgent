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

## Setup & Installation
1. Clone the Repository

```Bash
git clone [https://github.com/your-username/autostream-agent-assignment.git](https://github.com/your-username/autostream-agent-assignment.git)
cd autostream-agent-assignment

2. Create a Virtual Environment (Optional but Recommended)

```Bash
python -m venv venv
# Windows:
venv\Scripts\activate

3. Install Dependencies

```Bash
pip install -r requirements.txt

4. Configure Environment Variables Create a .env file in the root directory and add your Google API Key:

```Bash
GOOGLE_API_KEY=your_actual_api_key_here

5. Initialize the Knowledge Base Run this command once to build the local FAISS vector store:

```Bash
python rag.py

6. Run the Agent Start the interactive chat loop:

```Bash
python main.py