from tavily import TavilyClient
from langchain_openai import ChatOpenAI
from app.core.config import settings
from .state import AgentState

tavily = TavilyClient(api_key=settings.TAVILY_API_KEY)
llm = ChatOpenAI(
        openai_api_key=settings.OPENAI_API_KEY, 
        base_url="https://api.groq.com/openai/v1", 
        model="llama-3.3-70b-versatile"
    )

def search_node(state: AgentState):
    print(f"--- 🔍 BUSCANDO NO TAVILY (Tentativa {state['retry_count'] + 1}) ---")
    search_result = tavily.search(query=state["query"], search_depth="advanced", max_results=3)
    context = "\n".join([r['content'] for r in search_result['results']])
    return {"context": context}

def analyst_node(state: AgentState):
    print("--- 🧠 GERANDO INSIGHT PARA VENDAS ---")
    
    prompt = f"""
    Contexto: {state['context']}
    
    Você é o assistente de crescimento de uma Travel Tech. 
    Seu objetivo é gerar um alerta para Agências de Viagem e Influenciadores.
    
    Foque em:
    1. Oportunidades de lucro (ex: queda de preço em vistos ou taxas).
    2. Alertas de urgência (ex: mudança de regra amanhã).
    3. Dicas de marketing para influenciadores (ex: 'Destino X está bombando').
    
    Regra: Máximo 140 caracteres. Seja persuasivo.
    """
    res = llm.invoke(prompt)
    return {"insight": res.content}

def check_relevance_node(state: AgentState):
    prompt = f"""
    O insight: '{state['insight']}' ajuda uma agência a vender mais ou um influenciador a criar conteúdo relevante?
    Responda apenas SIM ou NAO.
    """
    res = llm.invoke(prompt)
    is_relevant = "SIM" in res.content.upper()
    return {"relevant": is_relevant, "retry_count": state["retry_count"] + 1}