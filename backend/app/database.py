from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Load variables from .env into the environment
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# The engine manages the actual connection pool to PostgreSQL
engine = create_engine(DATABASE_URL)

# SessionLocal is a factory that creates new database sessions.
# Each request in FastAPI will get its own session, used, then closed.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base is what our model classes (like User) will inherit from,
# so SQLAlchemy knows to treat them as database tables.
Base = declarative_base()


def get_db():
    """
    Dependency function used by FastAPI routes.
    Opens a database session, hands it to the route,
    then guarantees it's closed afterward — even if an error occurs.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()