# main.py

from fastapi import FastAPI
from app.endpoints import ping

app = FastAPI(
    title="Nuxo Bot API",
    description="API do Assistente Financeiro via WhatsApp",
    version="1.0.0"
)

# Inclui os endpoints
app.include_router(ping.router)
