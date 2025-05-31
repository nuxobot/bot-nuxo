from fastapi import FastAPI
import uvicorn
from config import APP_NAME, DEBUG, PORT

# Inicializa a aplicação FastAPI
app = FastAPI(
    title=APP_NAME,
    description="API do Nuxo Bot - Assistente Financeiro via WhatsApp",
    version="1.0.0",
    debug=DEBUG
)

# Endpoint de ping para verificar se a API está funcionando
@app.get("/ping")
async def ping():
    return {"message": "pong", "status": "online"}

# Executa o servidor se este arquivo for executado diretamente
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=PORT,
        reload=DEBUG,
        workers=1
    )
