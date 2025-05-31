# app/endpoints/ping.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/ping", tags=["Health Check"])
def ping():
    return {"message": "pong"}