from fastapi import FastAPI
from app.endpoints import ping

app = FastAPI(
    title="Nuxo Bot API",
    description="API do Assistente Financeiro via WhatsApp",
    version="1.0.0"
)

# Endpoint raiz ("/") para checagem básica de status
@app.api_route("/", methods=["GET", "HEAD"])
def root():
    return {"message": "Nuxo Bot API online 🚀"}

# Inclui os endpoints adicionais
app.include_router(ping.router)
