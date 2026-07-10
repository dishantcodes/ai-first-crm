from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.database import Base, engine
from app.routes.ai import router as ai_router
from app.routes.hcp import router as hcp_router
from app.routes.interaction import router as interaction_router

# Import models
from app.models.hcp import HCP
from app.models.interaction import Interaction

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI First CRM",
    version="1.0.0",
    description="AI First CRM for Healthcare Professionals"
)

# CORS
# CORS
# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://ai-first-crm-sage.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(hcp_router)
app.include_router(ai_router)
app.include_router(interaction_router)


@app.get("/")
def root():
    return {
        "message": "AI First CRM Backend Running Successfully 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "Running"
    }
