from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from app.config import DATABASE_URL
from app.db.base import Base

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

try:
    # Test the connection by executing a simple query
    with engine.connect() as connection:
        print("Engine connection successful.")
except SQLAlchemyError as e:
    print("Engine connection failed:", e)


# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database tables if they do not exist
def init_db():
    # Import all models here to ensure they are registered
    from app.models import Lookup, User, Request
    
    # Create all tables in the database
    Base.metadata.create_all(bind=engine)

# Dependency for getting the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
