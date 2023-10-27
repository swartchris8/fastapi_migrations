from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from pathlib import Path
import os


repo_root = Path(__file__).parent.parent.parent

load_dotenv(str(repo_root / ".env"))

sqlalchemy_database_url = os.getenv("DATABASE_URL")

engine = create_engine(sqlalchemy_database_url, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
