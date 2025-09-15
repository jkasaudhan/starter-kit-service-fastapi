from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import api_router
from app.core.config import settings
from app.models.database import create_db_and_tables

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="A simple Todo API built with FastAPI",
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

# CORS middleware
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Include API router
app.include_router(api_router, prefix=settings.API_V1_STR)

# Create database tables on startup
@app.on_event("startup")
def on_startup():
    create_db_and_tables()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)