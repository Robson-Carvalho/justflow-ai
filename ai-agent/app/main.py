import asyncio
import random
from fastapi import FastAPI
from app.agent.graph import app_graph
from app.services.elixir_client import ElixirClient
from app.core.config import settings

app = FastAPI(title="JustFlow AI Agent")
elixir = ElixirClient()

TEMAS_TURISMO = [
    "promoções passagens aéreas B2B brasil 2026",
    "mudanças visto estados unidos para brasileiros 2026",
    "novas regras visto europa ETIAS 2026",
    "destinos tendência para influenciadores viagem 2026",
    "novas taxas turísticas veneza e europa 2026",
    "tendências hotelaria tecnologia B2B brasil",
    "seguro viagem regras internacionais 2026"
]

async def worker_monitoramento():
    print("🤖 Agente JustFlow IA Ativo com LangGraph!")
    
    while True:
        try:
            tema_atual = random.choice(TEMAS_TURISMO)
            
            print(f"\n--- 🚀 INICIANDO NOVO CICLO: {tema_atual} EM 10 SEGUNDOS---")
            
            await asyncio.sleep(10)
            
            inputs = {
                "query": tema_atual,
                "context": "", 
                "insight": "", 
                "relevant": False, 
                "retry_count": 0
            }
            
            # Executa o grafo (Search -> Analyst -> Checker)
            final_state = await asyncio.to_thread(app_graph.invoke, inputs)
            
            insight = final_state.get("insight")
            is_relevant = final_state.get("relevant")

            if is_relevant and insight:
                print(f"✅ Insight Aprovado: {insight}")
                print("📢 Disparando para o Hub Elixir...")
                await elixir.send_alert(insight)
            else:
                print("⚠️ Insight descartado ou irrelevante para este ciclo.")
                
        except Exception as e:
            print(f"⚠️ Erro no ciclo: {e}")
            
        print(f"😴 Aguardando {settings.AGENT_INTERVAL} segundos para o próximo ciclo...")
        await asyncio.sleep(settings.AGENT_INTERVAL)

@app.on_event("startup")
async def startup():
    asyncio.create_task(worker_monitoramento())