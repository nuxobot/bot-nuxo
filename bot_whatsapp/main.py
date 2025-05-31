from fastapi import FastAPI
import uvicorn
from config import APP_NAME, DEBUG, PORT
from app.endpoints.ping import router as ping_router

# Inicializa a aplicação FastAPI
app = FastAPI(
    title=APP_NAME,
    description="API do Nuxo Bot - Assistente Financeiro via WhatsApp",
    version="1.0.0",
    debug=DEBUG
)

# Endpoint raiz
@app.api_route("/", methods=["GET", "HEAD"])
async def root():
    return {
        "message": "Bem-vindo à API do Nuxo Bot",
        "status": "online",
        "endpoints": {
            "root": "/",
            "ping": "/ping",
            "docs": "/docs"
        }
    }

# Inclui o router do endpoint /ping
app.include_router(ping_router)

# Executa o servidor se este arquivo for executado diretamente
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=PORT,
        reload=DEBUG,
        workers=1
    )
