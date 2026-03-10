import asyncio
import httpx
import logging
import os  
from fastapi import FastAPI

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

ELIXIR_HUB_URL = "http://realtime-hub:4000/api/alerts"
OPENAI_KEY = os.getenv("OPENAI_API_KEY", "Chave não encontrada")
INTERVALO_BUSCA = 20 

async def worker_monitoramento():
    logger.info(f"⚙️ Configurações carregadas:")
    
    async with httpx.AsyncClient() as client:
        while True:
            try:
                msg_teste = "Just Travel Detectada: Nova rota B2B para o Caribe em 2026."
                
                response = await client.post(ELIXIR_HUB_URL, json={"message": msg_teste}, timeout=10.0)
                
                if response.status_code == 200:
                    logger.info("✅ [Worker] Hub Elixir confirmou recebimento.")
                else:
                    logger.error(f"❌ [Worker] Falha no Hub. Status: {response.status_code}")

            except Exception as e:
                logger.error(f"⚠️ [Worker] Erro na integração: {e}")

            await asyncio.sleep(INTERVALO_BUSCA)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(worker_monitoramento())

@app.get("/")
async def status():
    return {
        "status": "AI Agent Running", 
        "hub_url": ELIXIR_HUB_URL
    }