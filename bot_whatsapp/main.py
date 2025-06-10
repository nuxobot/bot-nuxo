from fastapi import FastAPI
import uvicorn
from .infrastructure.whatsapp.webhook import router

app = FastAPI()

app.include_router(router)

@app.get("/ping")
async def ping():
    return {"message": "ping"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
