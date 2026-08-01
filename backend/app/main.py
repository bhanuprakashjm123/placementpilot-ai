from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routes import auth

# Creates all tables defined in models.py (like "users") if they don't exist yet
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="PlacementPilot AI",
    description="Your AI Mentor for Placements",
    version="0.1.0"
)

# CORS lets our React frontend (running on a different port, e.g. 5173)
# make requests to this backend (running on port 8000) without the
# browser blocking it for security reasons.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # our future Vite dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Plug in our authentication routes
app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": "PlacementPilot AI backend is running"}