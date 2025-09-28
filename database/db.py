from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker ,declarative_base
from dotenv import load_dotenv
import os

# DB_USER='joel'
# DB_PASS='password'
# DB_HOST='localhost'
# DB_PORT='5432'
# DB_NAME='mydbjoel'
load_dotenv()

DB_URL=os.environ.get("DATABASE_URL")


engine=create_engine(DB_URL,echo=True)

SessionLocal=sessionmaker(bind=engine ,autocommit=False)

Base=declarative_base()


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
