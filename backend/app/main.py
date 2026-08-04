from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routes import auth, roles

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="PlacementPilot AI",
    description="Your AI Mentor for Placements",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(roles.router)


@app.get("/")
def root():
    return {"message": "PlacementPilot AI backend is running"}