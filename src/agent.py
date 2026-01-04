import os
from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv

load_dotenv()

class AgentState(TypedDict):
    company: str
    research_notes: str
    final_pitch: str

# Node 1: Research (Stays the same)
def research_node(state: AgentState):
    search = TavilySearchResults(max_results=2)
    query = f"recent business news and growth of {state['company']} 2026"
    results = search.invoke(query)
    return {"research_notes": str(results)}

# Node 2: Writer (Updated for Gemini Free Tier)
def writer_node(state: AgentState):
    # We use Gemini 2.5 Flash which is highly capable and free
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.7,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )
    
    prompt = f"""
    You are a Senior Sales VP. Using these research notes: {state['research_notes']},
    Write a highly personalized 2-sentence sales pitch to {state['company']}.
    """
    response = llm.invoke(prompt)
    return {"final_pitch": response.content}

# Build the Graph (Stays the same)
builder = StateGraph(AgentState)
builder.add_node("researcher", research_node)
builder.add_node("writer", writer_node)
builder.set_entry_point("researcher")
builder.add_edge("researcher", "writer")
builder.add_edge("writer", END)

agent_workflow = builder.compile()