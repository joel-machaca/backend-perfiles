from fastapi import FastAPI
from routers import profiles, auth
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from database.db import Base,engine
import os


app = FastAPI()

Base.metadata.create_all(bind=engine)

load_dotenv()

FRONTEND_URL=os.getenv("FRONTEND_URL","http://localhost:5173")

origins=[FRONTEND_URL]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      
    allow_credentials=True,
    allow_methods=["*"],       
    allow_headers=["*"]
)

app.include_router(profiles.router)
app.include_router(auth.router)


@app.get("/")
def read_root():
    return {"message": "Bienvenido a mi API"}
