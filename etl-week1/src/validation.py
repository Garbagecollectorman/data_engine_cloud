from pydantic import BaseModel, ValidationError, field_validator
from typing import Optional

class DataRow(BaseModel):
    id: int
    name: str
    email: str
    age: Optional[int]

    @field_validator('email')
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email address')
        return v
