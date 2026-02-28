from pydantic import BaseModel

class ApplicationCreate(BaseModel):
    name: str
    email: str
    phone: str
    course: str