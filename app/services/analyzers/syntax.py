import spacy
from app.core.config import settings
from app.core.logger import logger

# Load language model based on configuration
def load_language_model(language: str):
    logger.info(f"Loading language model for: {language}")
    if language == "es":
        return spacy.load("es_core_news_sm")
    elif language == "en":
        return spacy.load("en_core_web_sm")
    else:
        logger.error("Unsupported language requested")
        raise ValueError("Unsupported language")

def analyze_sentence(sentence: str, language: str):
    """
    Analyzes the syntax of a given sentence and determines if it makes sense.
    """
    try:
        logger.info(f"Analyzing sentence: '{sentence}' in language: {language}")
        nlp = load_language_model(language)
        doc = nlp(sentence)
        
        # Check if the sentence contains at least one verb
        verbs = [token for token in doc if token.pos_ == "VERB"]
        if not verbs:
            logger.warning("Sentence lacks a verb, may be nonsensical.")
            return "Sentence lacks a verb, may be nonsensical."
        
        logger.info("Sentence structure appears valid.")
        return "Sentence structure appears valid."
    except Exception as e:
        logger.exception("Error analyzing sentence")
        return f"Error analyzing sentence: {str(e)}"