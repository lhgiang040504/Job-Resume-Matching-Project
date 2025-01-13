from fastapi import UploadFile, File, Request, Body
from fastapi.responses import JSONResponse
import os
import logging
import random

from dotenv import dotenv_values
config = dotenv_values("../../.env")

from source.services.RAG.db_connection import get_mongo_client
from source.services.RAG.vector_search import vector_search
from source.services.RAG.utils import message_prompt
from source.services.RAG.llm_model import get_response_completion


def answer(query: str):
    # Lưu vào database
    client = get_mongo_client('mongodb+srv://admin:admin@cluster0.gsgut.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
    database = client['HR_MANAGER']
    collection = database["course"]

    get_knowledges = vector_search(query, collection)

    message = message_prompt(query, get_knowledges)

    response = get_response_completion(message)

    random_choice = random.choice(response.choices)

    return JSONResponse(
        status_code=200,
        content={
            "status": 200,
            "success": True,
            "message": "Successfull",
            "data": random_choice.message.content
        }
    )