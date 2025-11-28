# app/main.py
from fastapi import FastAPI
from app.database import engine, Base
from app.api import auth, verbs, practice, admin

Base.metadata.create_all(bind=engine)

app = FastAPI(title="French Verbs Trainer")

app.include_router(auth.router)
app.include_router(verbs.router)
app.include_router(practice.router)
app.include_router(admin.router)

@app.get("/")
def root():
    return {"message": "¡Bienvenido al Entrenador de Verbos en Francés! 🇫🇷"}