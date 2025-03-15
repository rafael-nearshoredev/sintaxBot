from fastapi import APIRouter
from pydantic import BaseModel
from app.services.syntax_analyzer import analizar_frase

router = APIRouter()

class SentenceInput(BaseModel):
    sentence: str
    language: str

class SentenceOutput(BaseModel):
    sentence: str
    language: str
    result: str

@router.get("/analyze/", response_model=SentenceOutput, tags=["Syntax Analysis"], summary="Analyze a sentence")
def analyze(input_data: SentenceInput):
    """
    Analyzes the syntax of a sentence and determines if it is valid or nonsensical.
    
    **Parameters:**
    - sentence (str): The sentence to analyze.
    - language (str): The language of the sentence (e.g., "es" for Spanish, "en" for English).

    **Response:**
    - JSON containing the sentence, language, and analysis result.
    """
    result = analizar_frase(input_data.sentence)  # Language handling needs implementation
    return SentenceOutput(sentence=input_data.sentence, language=input_data.language, result=result)