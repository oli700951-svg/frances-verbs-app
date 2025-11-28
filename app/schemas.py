# app/schemas.py
from pydantic import BaseModel
from typing import List, Optional

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class VerbResponse(BaseModel):
    id: int
    spanish: str
    infinitive: str
    presente: List[str]
    passe_compose: str

    class Config:
        from_attributes = True

class PresenteAnswer(BaseModel):
    je: str
    tu: str
    il: str
    nous: str
    vous: str
    ils: str

class PasseAnswer(BaseModel):
    je: str

class IndividualPracticeRequest(BaseModel):
    verb_id: int
    presente: PresenteAnswer
    passe: PasseAnswer

class ExamQuestion(BaseModel):
    question: str
    answer: str
    verb_id: int
    type: str  # "presente" or "passe"

class ExamSubmission(BaseModel):
    answers: List[str]
    questions: List[ExamQuestion]