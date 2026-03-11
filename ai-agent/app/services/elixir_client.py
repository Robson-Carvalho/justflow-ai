import httpx
from app.core.config import settings

class ElixirClient:
    def __init__(self):
        self.url = settings.HUB_URL

    async def send_alert(self, message: str):
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(self.url, json={"message": message}, timeout=10.0)
                return response.status_code == 200
            except Exception as e:
                print(f"❌ Erro ao conectar com Elixir: {e}")
                return False