from fastapi import FastAPI
import uvicorn

# Inicializa a aplicação FastAPI
app = FastAPI()

# Endpoint de ping para verificar se a API está funcionando
@app.get("/ping")
async def ping():
    return {"message": "ping"}

# Executa o servidor se este arquivo for executado diretamente
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
