# app/api/admin.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database

router = APIRouter(prefix="/admin", tags=["admin"])

@router.post("/verbs")
def create_verb(
    verb: schemas.VerbResponse,
    db: Session = Depends(database.get_db)
):
    db_verb = models.Verb(
        spanish=verb.spanish,
        infinitive=verb.infinitive,
        presente_je=verb.presente[0],
        presente_tu=verb.presente[1],
        presente_il=verb.presente[2],
        presente_nous=verb.presente[3],
        presente_vous=verb.presente[4],
        presente_ils=verb.presente[5],
        passe_compose=verb.passe_compose
    )
    db.add(db_verb)
    db.commit()
    db.refresh(db_verb)
    return db_verb