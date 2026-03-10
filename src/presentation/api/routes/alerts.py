# crie uma rota alerta para fastapi
from typing import List
from fastapi import APIRouter

router = APIRouter()

@router.post("/alerts")
async def create_alert(alert: Alert) -> Alert:
    return alert

@router.get("/alerts")
async def list_alerts() -> List[Alert]:
    return []

@router.get("/alerts/{id}")