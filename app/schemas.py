from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: str
    is_admin: bool
    class Config:
        orm_mode = True

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
