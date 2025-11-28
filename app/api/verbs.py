# app/api/verbs.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database

router = APIRouter(prefix="/verbs", tags=["verbs"])

@router.get("/", response_model=list[schemas.VerbResponse])
def get_verbs(db: Session = Depends(database.get_db)):
    verbs = db.query(models.Verb).all()
    result = []
    for v in verbs:
        result.append(schemas.VerbResponse(
            id=v.id,
            spanish=v.spanish,
            infinitive=v.infinitive,
            presente=[v.presente_je, v.presente_tu, v.presente_il, v.presente_nous, v.presente_vous, v.presente_ils],
            passe_compose=v.passe_compose
        ))
    return result