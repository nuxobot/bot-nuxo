from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class MessageKey(BaseModel):
    remoteJid: str
    fromMe: bool  # adiciona o campo fromMe aqui

class MessageContent(BaseModel):
    conversation: Optional[str] = None

class MessageData(BaseModel):
    key: MessageKey
    message: MessageContent

class WebhookPayload(BaseModel):
    instance: str
    data: MessageData
    sender: str

@router.post("/webhook")
async def receive_webhook(payload: WebhookPayload):
    instance = payload.instance
    message = payload.data.message.conversation
    raw_contato = payload.data.key.remoteJid
    from_me = payload.data.key.fromMe  # pega o campo fromMe

    # Limpa o contato para conter apenas os números
    contato = raw_contato.split('@')[0]

    print(f"Instância: {instance}")
    print(f"Mensagem: {message}")
    print(f"Contato: {contato}")
    print(f"Mensagem enviada por mim? {from_me}")

    return {
        "instancia": instance,
        "mensagem": message,
        "contato": contato,
        "enviada_por_mim": from_me
    }
