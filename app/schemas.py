from pydantic import BaseModel

# Auth
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

# Verbos
class VerbCreate(BaseModel):
    spanish: str
    infinitive: str
    presente_je: str
    presente_tu: str
    presente_il: str
    presente_nous: str
    presente_vous: str
    presente_ils: str
    passe_compose: str

class VerbOut(BaseModel):
    id: int
    spanish: str
    infinitive: str
    class Config:
        orm_mode = True

# Progreso de usuario
class UserProgressCreate(BaseModel):
    user_id: int
    verb_id: int
    total_attempts: int
    correct_attempts: int

class UserProgressOut(BaseModel):
    id: int
    user_id: int
    verb_id: int
    total_attempts: int
    correct_attempts: int
    class Config:
        orm_mode = True

# Resultado de examen
class ExamResultCreate(BaseModel):
    user_id: int
    score: int
    total: int

class ExamResultOut(BaseModel):
    id: int
    user_id: int
    score: int
    total: int
    timestamp: str
    class Config:
        orm_mode = True
