from fastapi import APIRouter, Request
from pydantic import BaseModel, Field

from source.controller.chatbotManagement import answer
router = APIRouter()

class Message(BaseModel):
    messages: str = Field(..., description="The query of the user")

@router.post("/generative_ai")
def generative_ai(request: Request, messages: Message):
    print(messages)
    return answer(messages.messages)
