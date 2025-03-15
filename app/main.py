from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import os
from app.api.routes import router
from app.core.logger import logger

app = FastAPI(title="FastAPI Syntax Analyzer", version="1.0.0")

# Include routes
app.include_router(router)

@app.on_event("startup")
def startup_event():
    logger.info("Starting FastAPI application...")

@app.on_event("shutdown")
def shutdown_event():
    logger.info("Shutting down FastAPI application...")

@app.get("/", include_in_schema=False)
def root():
    if os.getenv("ACTIVE_SWAGGER", "false").lower() == "true":
        return RedirectResponse(url="/docs")
    return {"message": "FastAPI Syntax Analyzer is running"}
