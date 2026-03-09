<h1 align="center"> JustFlow AI 🚀 </h1>

<div  align="center">

**Real-time AI Agent for Travel Market Intelligence**

![Python](https://img.shields.io/badge/python-3670A0?style=flat-square&logo=python&logoColor=ffdd54)
![Elixir](https://img.shields.io/badge/elixir-%234B275F.svg?style=flat-square&logo=elixir&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat-square&logo=fastapi)
![Phoenix](https://img.shields.io/badge/phoenix-%23FD4F00.svg?style=flat-square&logo=phoenix&logoColor=white)
![Next.js](https://img.shields.io/badge/next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat-square&logo=docker&logoColor=white)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

O **JustFlow AI** é uma solução de inteligência de mercado desenvolvida para o setor de turismo (B2B). O sistema utiliza **Agentes de IA** para monitorar tendências globais e distribui insights acionáveis em tempo real para agências de viagens parceiras através de uma arquitetura orientada a eventos.

---

## 🎯 O Problema & A Solução

No mercado de turismo, a velocidade da informação é crucial. Agências parceiras de uma **Travel Tech** precisam reagir rapidamente a mudanças de mercado (vistos, novas atrações, variações cambiais).

O JustFlow resolve a latência de informação ao:

1.  **Monitorar:** Um agente (LangGraph) filtra notícias e dados relevantes.
2.  **Analisar:** Transforma dados brutos em "Insights de Venda" (B2B).
3.  **Notificar:** Distribui o insight instantaneamente via WebSockets para o dashboard do cliente.

---

## 🏗️ Arquitetura do Sistema

O projeto é dividido em três microserviços orquestrados via **Docker**:

1.  **`ai-agent` (Python/FastAPI):** O "cérebro". Orquestra o fluxo de pesquisa e análise usando **LangGraph**.
2.  **`realtime-hub` (Elixir/Phoenix):** O distribuidor de alta performance. Gerencia conexões persistentes (WebSockets) para entrega de mensagens em tempo real.
3.  **`dashboard` (Next.js/React):** A interface do usuário final, conectada ao Hub para atualizações sem refresh.

---

## 🛠 Tech Stack

- **Backend IA:** Python 3.11, FastAPI, LangGraph, LangChain.
- **Backend Real-time:** Elixir 1.15, Phoenix Framework (Channels).
- **Frontend:** Next.js 14, Tailwind CSS, Phoenix.js (Socket client).
- **Infra:** Docker, Docker Compose.

---

## 🚀 Como Executar

Certifique-se de ter o **Docker** e o **Docker Compose** instalados.

1. Clone o repositório:
   ```bash
   git clone [https://github.com/Robson-Carvalho/justflow-ai.git](https://github.com/Robson-Carvalho/justflow-ai.git)
   cd justflow-ai
   ```
2. Configure as variáveis de ambiente (API Keys de IA) no arquivo `.env`.

3. Suba o ambiente:
    ```bash
    docker-compose up --build
    ```
4. Acesse:
    - Dashboard: http://localhost:3000

    - API IA: http://localhost:8000/docs

    - Hub Elixir: http://localhost:4000

## ⚡ PBL Mindset

Este projeto foi desenvolvido aplicando a metodologia Problem-Based Learning, focando na agilidade de aprendizado de novas stacks (Elixir/Phoenix) para resolver um desafio técnico real de escalabilidade e entrega de valor no setor de Travel Tech.
