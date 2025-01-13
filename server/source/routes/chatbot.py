from fastapi import APIRouter, Request
from pydantic import BaseModel, Field

from source.controller.chatbotManagement import answer
router = APIRouter()

@router.post("/generative_ai")
def generative_ai(request: Request, query: str):
    return answer(query)
